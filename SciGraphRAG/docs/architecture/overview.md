# Tổng quan Backend

Trạng thái: STRUCTURE_ONLY. Nguồn: [SCIGRAPHRAG_ARCHITECTURE_CODEX.md](../../SCIGRAPHRAG_ARCHITECTURE_CODEX.md). Chỉ tài liệu tổng hợp này có sẵn lúc dựng cấu trúc; bốn tài liệu gốc được liệt kê trong đó chưa có trong workspace để đối chiếu độc lập.

**BASELINE**: hai business service Core và AI; Gateway là public API entry point. AI API và AI Worker dùng chung một codebase, chạy và scale riêng.

```text
Client → Gateway → Core → PostgreSQL
                 → AI API → Neo4j
Core → AI API                         (Internal REST đồng bộ)
Core Outbox → RabbitMQ → AI Worker    (heavy task)
AI Outbox → RabbitMQ → Core Inbox     (result)
Core / AI Worker → S3-compatible storage
```

Core authorize owner/task scope, entitlement, quota và credit trước khi tạo job. Metered operations mặc định đi async qua Core; bounded read không dùng model có thể qua AI API. Core không giữ transaction mở trong pipeline/external call. Worker không expose HTTP hoặc xác thực end-user JWT trong task.

Gateway/Core/AI API xác minh JWT; resource authorization là bước độc lập. AI API dự kiến gọi AuthorizationPort tới Core và fail closed. Một Project có một owner, Curator chỉ được truy cập assigned target/evidence scope.

PostgreSQL chỉ thuộc Core; Neo4j chỉ thuộc AI; không dùng database credential chéo, shared database hay cross-database FK. PDF/artifact lớn ở object storage; message chỉ chứa reference/checksum. Broker dùng RabbitMQ và neutral versioned JSON.

Claim khoa học phải truy về evidence/build. Curation chỉ RESOLVED sau graph apply confirmation. Inbox/Outbox, settlement và graph mutation chịu duplicate delivery; không hứa exactly-once delivery.

**SCAFFOLD**: đường dẫn service/package/module, Maven/uv, outbound ports và route/command names đề xuất. Backend được dựng trực tiếp tại root hiện có; phần Web chưa thuộc phạm vi lần này.

**TO PIN**: dependency/image/model versions, schemas, auth/service identity, retry/lease và các policy còn mở trong [D01–D16](open-decisions.md). Không có runtime, migration, API/schema hay triển khai nghiệp vụ trong scaffold hiện tại.
