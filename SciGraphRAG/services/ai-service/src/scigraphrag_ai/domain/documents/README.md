# AI domain: documents

Trạng thái: STRUCTURE_ONLY. Owner: AI / documents. PaperRef, Chunk và provenance khoa học trong Neo4j; Core vẫn sở hữu Paper metadata.

Trách nhiệm: Giữ model, state, value object và invariant thuần cho nhóm documents.

Dependency hợp lệ: Python standard library và common value types thuần; không import FastAPI, Pydantic transport, Neo4j driver, AMQP hoặc provider.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt parser, chunking, schema/evidence và idempotent paper processing (D04, D10). Chưa có source hoặc behavior thực thi.
