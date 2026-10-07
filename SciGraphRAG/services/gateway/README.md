# API Gateway

Trạng thái: STRUCTURE_ONLY. Owner: thành phần hạ tầng Gateway; không sở hữu dữ liệu nghiệp vụ.

Trách nhiệm: public routing tới Core/AI API, xác minh JWT lớp đầu, CORS, size/rate limit, correlation ID, timeout và TLS theo môi trường. Các package `config`, `security`, `filters`, `routing`, `errors`, `observability` chỉ giữ trách nhiệm kỹ thuật.

Dependency hợp lệ: Core/AI API qua HTTP và public JWKS; không truy cập PostgreSQL/Neo4j, không tính credit hoặc kiểm tra owner bằng business rule. Không route Worker hoặc public `/internal/**`. Core/AI API vẫn xác minh JWT và resource scope.

Entry point dự kiến: `src/main/java/com/scigraphrag/gateway/GatewayApplication.java`. Java 21 và Spring Cloud Gateway là baseline tài liệu; Maven là SCAFFOLD. Chưa có source, manifest, cấu hình hoặc lệnh chạy đã kiểm chứng.

TODO: pin Spring Cloud flavor/BOM và Spring Boot compatibility (D01); chốt JWT, CORS, TLS, limits và timeout; kiểm soát header identity giả mạo, health/readiness (D11, D12, D15). Tham khảo [open decisions](../../docs/architecture/open-decisions.md).
