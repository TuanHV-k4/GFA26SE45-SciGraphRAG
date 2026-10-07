# Quyền sở hữu dữ liệu Backend

Trạng thái: STRUCTURE_ONLY. Catalog dưới đây giữ nguyên nội dung phần 10 của [tài liệu nguồn](../../SCIGRAPHRAG_ARCHITECTURE_CODEX.md); đây là logical model, chưa có schema/migration thực thi.

BASELINE: Core độc quyền PostgreSQL (22 bảng); AI độc quyền Neo4j graph/vector/runtime state. Gateway và administration không có bảng riêng. Không shared database, credential chéo hoặc cross-database FK. Core workspace quản lý object metadata/quyền; AI Worker truy cập file qua policy riêng.

## 10. Kiến trúc dữ liệu

### 10.1 Relational catalog

Baseline có đúng **22 bảng**. Danh sách dưới đây là logical model, chưa là DDL hoàn chỉnh. PK là primary key, FK là foreign key trong PostgreSQL của Core, UQ là uniqueness cần thể hiện phù hợp trong physical schema.

| Bảng | Owner module | Các trường/constraint chính từ nguồn |
|---|---|---|
| `users` | identity | `id`, email UQ, full_name, role, status, token_version, timestamps |
| `auth_identities` | identity | `id`, user_id FK, provider, subject, password_hash; UQ(provider, subject) |
| `auth_sessions` | identity | `id`, user_id FK, refresh_token_hash UQ, expires_at, revoked_at, device_info |
| `email_verification_otps` | identity | `id`, email, otp_hash, purpose, status, expires_at, attempt_count, resend_count |
| `projects` | workspace | `id`, owner_user_id FK, name, field, status, active_corpus_id, timestamps |
| `corpora` | workspace | `id`, project_id FK, name, version, status, created_at |
| `papers` | workspace | `id`, project_id FK, corpus_id FK, doi, arxiv_id, checksum, object_key, status |
| `features` | billing | `id`, code UQ, name, metered, active |
| `plans` | billing | `id`, code UQ, price, billing_period, included_credits, status, effective_at |
| `plan_features` | billing | PK(plan_id, feature_id), enabled, quota, credit_cost |
| `subscriptions` | billing | `id`, user_id FK, plan_id FK, status, period_start/end, scheduled_change |
| `payment_transactions` | billing | `id`, user_id FK, order_code UQ, provider_reference UQ, amount, status, idempotency_key UQ |
| `webhook_events` | billing | `id`, provider, provider_event_id UQ, payload_hash, signature_valid, status, received_at |
| `credit_wallets` | credits | `id`, user_id UQ, balance, reserved_balance, version, updated_at |
| `credit_ledger` | credits | `id`, wallet_id FK, entry_type, amount, balance_after, reference, idempotency_key UQ |
| `usage_events` | credits | `id`, user_id FK, project_id FK, job_id UQ, feature_code, estimated, actual, status |
| `ai_jobs` | jobs | `id`, project_id FK, paper_id FK nullable, task_type, status, correlation_id, requested_by, timestamps |
| `review_tasks` | curation | `id`, project_id FK, target_type, target_id, assertion_id, assignee_user_id, status, priority |
| `curation_actions` | curation | `id`, task_id FK, action_type, before_json, after_json, reason, status, idempotency_key UQ |
| `audit_events` | audit | `id`, actor_id, action, target_type, target_id, correlation_id, created_at |
| `outbox_events` | integration | `id`, event_id UQ, aggregate_type/id, event_type, payload_json, status, attempts, next_attempt_at |
| `inbox_events` | integration | event_id PK, event_type, producer, payload_hash, status, processed_at, error_message |

Ràng buộc nghiệp vụ:

- User 1–N AuthIdentity/AuthSession/Project; một wallet/User.
- Project 1–N Corpus; Corpus 1–N Paper. Paper.project_id phải khớp Corpus.project_id.
- Plan N–M Feature qua plan_features; User có nhiều Subscription lịch sử nhưng chỉ một current subscription theo policy.
- Project 1–N AIJob; job có tối đa một usage record theo unique job_id, operation có metering phải có usage record.
- Project 1–N ReviewTask; ReviewTask 1–N CurationAction.
- Duplicate paper bị chặn theo Project + DOI/arXiv ID/checksum khi các giá trị hiện diện.
- Một OPEN/IN_REVIEW review cho cùng target/build theo nguồn; physical uniqueness và state guard còn TO PIN.
- Wallet mutation phải đi kèm ledger; reserve/consume/release idempotent, dùng locking/version phù hợp.

Nguồn chưa liệt kê đủ physical fields cho review build/evidence scope, immutable corpus snapshot, Plan version/history, payment currency và job result/artifact. Ghi TO PIN trong database docs; không tự sinh bảng bổ sung để lấp chỗ trống hoặc tuyên bố migration đầy đủ chỉ từ bảng trên.

### 10.2 Graph node catalog

| Label | Khóa | Dữ liệu |
|---|---|---|
| `ProjectRef` | projectId UQ | Reference tối thiểu tới Project, không là nguồn quyền |
| `PaperRef` | paperId UQ, projectId | Paper reference và provenance root |
| `Chunk` | chunkId UQ, paperId | Text, section/page/span, checksum, embedding |
| `Author` | authorId UQ | Tác giả chuẩn hóa |
| `Entity` | entityId UQ, projectId, type | Canonical entity, aliases, representationType/Version/Text, embedding |
| `GraphBuild` | buildId UQ, jobId UQ | Corpus snapshot, pipeline/config version, quality, active flag |
| `Community` | communityId UQ, buildId | Cluster/rank, summary reference và representative evidence |
| `AIJob` | jobId UQ | Runtime state, taskType, projectId/paperId, correlationId |
| `TaskExecution` | taskId UQ, messageId UQ | Claim, attempt, lease, status, startedAt/finishedAt |
| `IntegrationInbox` | messageId UQ | Dedup, payloadHash, receivedAt/processedAt, status |
| `IntegrationOutbox` | eventId UQ | Event payload, aggregateId, attempts, nextAttemptAt, status |

### 10.3 Graph relationship catalog

| Relationship | Hướng | Thuộc tính/quy tắc |
|---|---|---|
| `HAS_PAPER` | ProjectRef → PaperRef | Project nhất quán |
| `HAS_CHUNK` | PaperRef → Chunk | Chunk order, section/page |
| `AUTHORED_BY` | PaperRef → Author | Author order/role khi có |
| `MENTIONS` | Chunk → Entity | mentionId, span, confidence, buildId |
| `USES_METHOD` | Entity → Entity | assertionId UQ, evidenceChunkIds, confidence, status, buildId |
| `EVALUATES_ON` | Entity → Entity | assertionId UQ, evidenceChunkIds, confidence, status, buildId |
| `ACHIEVES_RESULT` | Entity → Entity | assertionId UQ, evidenceChunkIds, confidence, status, buildId |
| `HAS_BUILD` | ProjectRef → GraphBuild | Một active build/Project |
| `HAS_COMMUNITY` | GraphBuild → Community | Algorithm/config version |
| `CONTAINS` | Community → Entity | Membership score/rank |
| `HAS_EXECUTION` | AIJob → TaskExecution | Runtime executions/attempts |

Mỗi scientific assertion dùng cho retrieval có assertionId, buildId và Chunk evidence hợp lệ. Relation excerpt chỉ là bản sao tiện dụng; Chunk là evidence source.

Assertion identity phải không nhập nhằng khi resolve evidence hoặc curation target. Nguồn yêu cầu assertionId UQ; cách enforce uniqueness trên các relationship type và build scope phụ thuộc physical schema/Neo4j edition còn TO PIN. Index tìm kiếm thông thường không thay uniqueness guard.

Neo4j migrations giữ uniqueness/full-text/vector indexes phù hợp với phiên bản/edition đã pin. Embedding dimension và similarity metric phải thống nhất với model. Không sinh vector index với dimension tùy đoán.

TO PIN về versioning: canonical Entity có entityId UQ trong nguồn, nhưng representation/embedding cần so sánh nhiều build/variant. Chốt cách giữ identity so với versioned representation trước physical schema; không overwrite representation đang dùng bởi active build. Các query phải chứng minh membership ở đúng Project/build, không chỉ lọc một ID do client gửi.

### 10.4 File và shared identifiers

```text
PDF gốc:       projects/{projectId}/papers/{paperId}/source.pdf
Parsed output: jobs/{jobId}/parsed.json
Export/report: projects/{projectId}/exports/{exportId}
```

Export/report là convention nguồn cho feature được triển khai sau; skeleton không cần thêm export table/service. Metadata chứa object key, checksum, mime type và size theo physical design đã chốt.

| Identifier | Owner/ý nghĩa |
|---|---|
| `userId` | Core identity; message chỉ giữ audit identity tối thiểu |
| `projectId`, `paperId` | Core workspace; AI giữ reference cùng UUID |
| `jobId` | Core product job; AI runtime job dùng cùng ID |
| `taskId` | Định danh execution command, không là ReviewTask ID |
| `buildId` | AI graph version; Core/request/message tham chiếu khi cần |
| `assertionId` | Scientific relationship được truy evidence/curation |
| `reviewTaskId` | Review assignment của Core; tránh nhập nhằng với taskId của Worker |
| `actionId` | Core curation action; AI dùng chống apply lặp |
| `messageId`, `eventId` | Message/event identity ổn định khi retry publish/delivery |

SQL dùng snake_case; JSON contract dùng camelCase; Python có thể dùng snake_case nội bộ với mapping rõ. Không đổi identity khi chuyển ngôn ngữ.

