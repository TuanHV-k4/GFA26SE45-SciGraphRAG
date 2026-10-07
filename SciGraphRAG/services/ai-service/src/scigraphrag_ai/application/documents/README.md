# AI application: documents

Trạng thái: STRUCTURE_ONLY. Owner: AI / documents. PaperRef, Chunk và provenance khoa học trong Neo4j; Core vẫn sở hữu Paper metadata.

Trách nhiệm: Parse/chunk, checksum và provenance section/page/span; publish paper outcome.

Dependency hợp lệ: Domain và application ports; không import concrete drivers, routers hoặc consumer entry point. Concrete adapter được bootstrap wire.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt parser, chunking, schema/evidence và idempotent paper processing (D04, D10). Chưa có source hoặc behavior thực thi.
