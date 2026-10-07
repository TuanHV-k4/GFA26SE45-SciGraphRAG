# AI application: retrieval

Trạng thái: STRUCTURE_ONLY. Owner: AI / retrieval. Evidence/path invariants trên dữ liệu AI; không tạo wallet/account state.

Trách nhiệm: Bounded explore, evidence, grounded QA, multi-hop discovery và community analysis.

Dependency hợp lệ: Domain và application ports; không import concrete drivers, routers hoặc consumer entry point. Concrete adapter được bootstrap wire.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt server-side depth/node/edge limits, Project/build scope và retrieval ports. Thiếu evidence trả INSUFFICIENT_EVIDENCE/NO_GROUNDED_PATH. Chưa có source hoặc behavior thực thi.
