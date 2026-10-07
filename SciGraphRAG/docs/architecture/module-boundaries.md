# Ranh giới module và chiều phụ thuộc

Trạng thái: Core Service và AI API đã có skeleton 3-layer; service boundary và ownership là BASELINE.

Core Service: `controller → service → repository`. Controller chỉ xử lý HTTP và DTO; service điều phối use case, transaction và business rule; repository cô lập truy cập PostgreSQL/JPA. Dependency không được import ngược lên layer trên.

Các nhóm nghiệp vụ identity, workspace, billing, credits, jobs, curation, audit, integration và administration khi triển khai phải nằm trong ba layer trên. DTO, entity và mapper là cấu trúc hỗ trợ, không được dùng để bỏ qua service layer.

Nhóm nghiệp vụ gọi service của nhóm khác; controller không gọi repository trực tiếp và repository không phụ thuộc controller/service. Integration dispatch event tới jobs/credits/curation và phối hợp local transaction cần thiết. Workspace sở hữu Paper metadata/status, jobs điều phối product AI job.

AI API: `controllers → services → repositories`. Controller chỉ xử lý HTTP/schema, service điều phối use case và repository cô lập truy cập dữ liệu/runtime. `models` giữ kiểu nội bộ, `schemas` giữ transport contract, `core` giữ cấu hình/cross-cutting concerns. Dependency không được import ngược lên layer trên.

Các nhóm documents, graph, retrieval, curation và jobs khi triển khai phải được đặt theo cùng ba layer. Neo4j/object storage/RabbitMQ được bọc bởi repository; controller không được import concrete client hoặc repository trực tiếp.

Gateway chỉ routing/security/filter/config/observability. Scientific pipeline/PathRAG thuộc AI hoặc research adapter. Common chỉ giữ helper/value/error nhỏ, không chứa policy billing/owner/wallet/graph.

AI API hiện có source và health endpoint tối thiểu. Các use case khoa học, worker và integration contracts vẫn cần triển khai; không dùng shared Java/Python entity library tại contracts.
