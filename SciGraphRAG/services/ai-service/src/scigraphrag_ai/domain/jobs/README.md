# AI domain: jobs

Trạng thái: STRUCTURE_ONLY. Owner: AI / jobs. AIJob runtime và TaskExecution trong Neo4j; product ai_jobs và credit settlement thuộc Core.

Trách nhiệm: Giữ model, state, value object và invariant thuần cho nhóm jobs.

Dependency hợp lệ: Python standard library và common value types thuần; không import FastAPI, Pydantic transport, Neo4j driver, AMQP hoặc provider.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt retry/recovery/cancel/progress (D13); PROCESSING không đồng nghĩa completed; ack sau terminal commit + Outbox. Chưa có source hoặc behavior thực thi.
