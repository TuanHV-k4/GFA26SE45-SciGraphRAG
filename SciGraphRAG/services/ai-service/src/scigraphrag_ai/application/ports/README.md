# AI application ports

Trạng thái: STRUCTURE_ONLY. Owner: AI application; không sở hữu thêm dữ liệu.

Trách nhiệm dự kiến: abstractions cho Neo4j UoW/repository, storage, model, parser, extraction, entity resolution, representation/embedding, PathRAG, authorization và integration.

Dependency: domain/value types và application contract; không lộ concrete driver result, FastAPI Request hoặc AMQP message. Infrastructure implement ports, bootstrap wire theo runtime.

TODO: định nghĩa interface khi triển khai. AuthorizationPort kiểm tra owner/assigned task scope tại Core, fail closed; model usage cần Core orchestration/reserve/settle. Chưa có adapter allow-all hoặc stub success.
