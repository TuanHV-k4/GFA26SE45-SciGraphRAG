# AI domain: retrieval

Trạng thái: STRUCTURE_ONLY. Owner: AI / retrieval. Evidence/path invariants trên dữ liệu AI; không tạo wallet/account state.

Trách nhiệm: Giữ model, state, value object và invariant thuần cho nhóm retrieval.

Dependency hợp lệ: Python standard library và common value types thuần; không import FastAPI, Pydantic transport, Neo4j driver, AMQP hoặc provider.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt server-side depth/node/edge limits, Project/build scope và retrieval ports. Thiếu evidence trả INSUFFICIENT_EVIDENCE/NO_GROUNDED_PATH. Chưa có source hoặc behavior thực thi.
