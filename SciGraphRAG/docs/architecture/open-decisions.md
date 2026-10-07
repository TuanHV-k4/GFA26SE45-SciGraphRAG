# Quyết định còn mở

Trạng thái: STRUCTURE_ONLY, chưa có quyết định nào dưới đây được coi là đã triển khai. Giữ nguyên D01–D16 từ [tài liệu nguồn](../../SCIGRAPHRAG_ARCHITECTURE_CODEX.md). Frontend trong D02 ngoài phạm vi lần này; Python/build tools và các mục Backend vẫn cần chốt khi triển khai.

Chỉ file tổng hợp kiến trúc có sẵn khi scaffold; bốn nguồn gốc nêu ở phần 2 chưa có để kiểm chứng độc lập. Khi bổ sung nguồn, ghi mâu thuẫn tại đây và tạo ADR nếu có quyết định thay đổi.

## 18. Các quyết định còn mở

Ghi các mục sau vào `docs/architecture/open-decisions.md`; khi giải quyết thì thêm ADR và cập nhật status. Không đặt version tùy đoán để làm skeleton có vẻ hoàn chỉnh.

| ID | Quyết định | Mức hiện tại | Hướng xử lý khi scaffold |
|---|---|---|---|
| D01 | Spring Boot exact patch, Spring Cloud flavor/BOM, Gateway compatibility | TO PIN | Giữ Java 21 và family nguồn; xác minh official compatibility trước runnable build |
| D02 | Frontend/Python package versions và build tools | SCAFFOLD/TO PIN | Npm/Maven/uv đề xuất; một lockfile/app sau smoke test |
| D03 | PostgreSQL/Neo4j/RabbitMQ/MinIO image tag/digest/edition | TO PIN | Không gọi latest là locked; pin sau compatibility/resource review |
| D04 | Extraction/parser/entity resolution method | TO FREEZE | Ports/adapters trước; pilot rồi freeze, không ép SciBERT/LLM |
| D05 | LLM/embedding model snapshot, dimensions, price/usage unit | TO FREEZE | Config/model ports; chưa có model thì operation model usage chưa runnable |
| D06 | AI API ownership/task authorization | SCAFFOLD | AuthorizationPort → internal Core check, fail closed; chốt identity/cache/revocation |
| D07 | Metered synchronous request settlement | TO PIN | Async cho metered use case mặc định; reserve/settle/reconcile trước khi mở sync |
| D08 | Curation message schema và graph revision policy | SCAFFOLD/TO PIN | APPLY_CURATION + terminal events, actionId và expected build/revision guard |
| D09 | Canonical Entity và versioned representation/embedding | TO PIN | Giữ representation type/version; tránh overwrite active graph và experiment variants |
| D10 | Physical schema review scope/corpus snapshot/Plan version/payment currency/job result | TO PIN | Baseline 22 bảng; mô tả field constraints còn thiếu trước migration đầy đủ |
| D11 | JWT algorithm/key rotation/account lock/token_version/refresh transport | TO PIN | Core signing owner; no secret; no allow-all fallback |
| D12 | Service identity cho Internal REST | TO PIN | Port/config placeholder; không tin client-supplied service header |
| D13 | Retry/prefetch/lease/DLQ/progress/cancellation contract | TO PIN | Không ack trước commit; không tự coi timeout/DLQ là terminal outcome |
| D14 | Credit estimate/actual-over-reserve/failure/rounding policy | TO PIN | Idempotent ledger và reconciliation; không invent giá/charge policy |
| D15 | Distributed rate-limit store và observability backend | UNCONFIRMED/PROPOSED | Không thêm Redis broker hoặc stack monitoring bắt buộc |
| D16 | Research fork/dataset/metrics/full protocol | TO PIN | README/manifest TODO; không tự chọn nguồn hoặc invent result |

Các TO PIN không cản trở tạo folder/README/interface. Chúng cản trở tuyên bố implementation tương ứng đã hoàn chỉnh hoặc runnable. Nếu cần lựa chọn để làm code chạy, xác minh và ghi quyết định thay vì suy diễn từ tên folder.

