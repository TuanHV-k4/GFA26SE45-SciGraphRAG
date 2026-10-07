# AI application: graph

Trạng thái: STRUCTURE_ONLY. Owner: AI / graph. Entity, GraphBuild, Community và scientific assertions/evidence trong Neo4j.

Trách nhiệm: Extraction, resolution, representation, embedding, build/rebuild, community và quality gates.

Dependency hợp lệ: Domain và application ports; không import concrete drivers, routers hoặc consumer entry point. Concrete adapter được bootstrap wire.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt canonical identity/versioned representation, model dimension và activation guards (D04, D05, D09). Build lỗi giữ active graph cũ. Chưa có source hoặc behavior thực thi.
