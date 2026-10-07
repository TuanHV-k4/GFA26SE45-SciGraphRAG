# AI domain: graph

Trạng thái: STRUCTURE_ONLY. Owner: AI / graph. Entity, GraphBuild, Community và scientific assertions/evidence trong Neo4j.

Trách nhiệm: Giữ model, state, value object và invariant thuần cho nhóm graph.

Dependency hợp lệ: Python standard library và common value types thuần; không import FastAPI, Pydantic transport, Neo4j driver, AMQP hoặc provider.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt canonical identity/versioned representation, model dimension và activation guards (D04, D05, D09). Build lỗi giữ active graph cũ. Chưa có source hoặc behavior thực thi.
