# AI Neo4j migrations

Trạng thái: STRUCTURE_ONLY. Owner: AI. Vị trí migration scientific graph/vector và AI runtime records.

TODO: chốt Neo4j version/edition, node/assertion uniqueness, Project/build membership, versioned representation, full-text/vector indexes và model dimension (D03, D05, D09). Index thường không thay uniqueness guard. Không chọn embedding dimension tùy đoán.

Chưa có Cypher hoặc migration runner. Chỉ AI/deployment task được chỉ định chạy migration với concurrency guard; Core không truy cập Neo4j.
