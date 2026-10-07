# AI application: jobs

Trạng thái: STRUCTURE_ONLY. Owner: AI / jobs. AIJob runtime và TaskExecution trong Neo4j; product ai_jobs và credit settlement thuộc Core.

Trách nhiệm: Claim/lease, attempts, progress, runtime orchestration và terminal outcome.

Dependency hợp lệ: Domain và application ports; không import concrete drivers, routers hoặc consumer entry point. Concrete adapter được bootstrap wire.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt retry/recovery/cancel/progress (D13); PROCESSING không đồng nghĩa completed; ack sau terminal commit + Outbox. Chưa có source hoặc behavior thực thi.
