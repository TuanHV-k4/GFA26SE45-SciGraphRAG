# Trạng thái scaffold Backend

Ngày tạo: 01/10/2026. Mode: **STRUCTURE_ONLY**. Phạm vi: Backend theo yêu cầu người dùng.

Đường dẫn giữ theo phần 5.3 của [tài liệu mẫu](../../SCIGRAPHRAG_ARCHITECTURE_CODEX.md), dựng trực tiếp tại root hiện tại. File mẫu được giữ nguyên. Lúc bắt đầu chỉ có file mẫu; không có source/manifest hoặc AGENTS.md áp dụng.

- Đã tạo Gateway scaffold; Core Spring Boot và AI FastAPI build/test được theo cấu trúc 3-layer; AI Worker vẫn là runtime dự kiến.
- Core runtime nằm ở `services/core-service`, package `com.scigraphrag.core`, theo `controller → service → repository`. Các nhóm nghiệp vụ sẽ được bổ sung trong ba layer khi implementation cần.
- AI runtime nằm ở `services/ai-service/app` với `controllers → services → repositories`; scaffold cũ dưới `src/scigraphrag_ai` chỉ còn là tài liệu tham khảo.
- Đã tạo contracts, infra, docs, scripts, tests và research support theo các cây 5.1, 11.1, 15.2. README ghi owner/trách nhiệm/TODO; thư mục lá còn rỗng dùng .gitkeep.
- Đã ghi catalog 22 bảng, ownership, dependency rules và D01–D16. BASELINE/SCAFFOLD/TO PIN giữ theo tài liệu; chưa tự pin version hoặc quyết định nghiệp vụ.

Phần chưa tạo:

- `apps/web` và các nhánh frontend: ngoài yêu cầu Backend lần này, là điều chỉnh phạm vi duy nhất đối với cây bắt buộc 5.3.
- Core chưa có controller/service/repository nghiệp vụ hoặc cấu hình PostgreSQL production; các thư mục layer hiện là placeholder được giữ bằng `.gitkeep`.
- AI đã có source entry point, manifest, application config và OpenAPI sinh từ FastAPI. Dockerfiles, SQL/Cypher migration thực thi, Compose/RabbitMQ definitions, AI Worker và research runners/results vẫn thuộc implementation tiếp theo.
- Core và AI đã có lệnh build/test được kiểm chứng; chưa có test nghiệp vụ, external call, deployment hay production data.

Entry point hiện tại được liệt kê trong [README gốc](../../README.md) và README từng service. Các .env.example chỉ minh họa; các bước cần chốt trước implementation nằm ở [open-decisions](open-decisions.md).

## Verification

Scaffold tree bên dưới là snapshot lịch sử trước khi AI API và Core Service được chuyển sang 3-layer. Trạng thái runtime hiện tại được mô tả trong README của từng service và được kiểm tra bằng pytest/Maven.

Created 174 directories and 145 files; retained the original architecture file. Current tree includes 146 files: 56 README files, 79 .gitkeep files, 4 .env.example files, .gitignore, 5 architecture documents and the original source.

## Actual tree

```text
SciGraphRAG/
├── contracts/
│   ├── examples/
│   │   ├── http/
│   │   │   └── README.md
│   │   └── messaging/
│   │       └── README.md
│   ├── http/
│   │   ├── internal/
│   │   │   └── README.md
│   │   └── public/
│   │       └── README.md
│   ├── messaging/
│   │   ├── commands/
│   │   │   └── README.md
│   │   ├── envelope/
│   │   │   └── README.md
│   │   └── events/
│   │       └── README.md
│   └── README.md
├── docs/
│   ├── adr/
│   │   └── README.md
│   ├── architecture/
│   │   ├── data-ownership.md
│   │   ├── module-boundaries.md
│   │   ├── open-decisions.md
│   │   ├── overview.md
│   │   └── scaffold-status.md
│   ├── database/
│   │   └── README.md
│   ├── runbooks/
│   │   └── README.md
│   ├── source/
│   │   └── README.md
│   └── workflows/
│       └── README.md
├── infra/
│   ├── compose/
│   │   └── README.md
│   ├── minio/
│   │   └── README.md
│   ├── neo4j/
│   │   └── README.md
│   ├── observability/
│   │   └── README.md
│   ├── postgres/
│   │   └── README.md
│   ├── rabbitmq/
│   │   └── README.md
│   └── README.md
├── research/
│   ├── adapters/
│   │   └── README.md
│   ├── baseline/
│   │   └── README.md
│   ├── configs/
│   │   └── README.md
│   ├── datasets/
│   │   └── README.md
│   ├── evaluation/
│   │   └── README.md
│   ├── experiments/
│   │   └── README.md
│   ├── results/
│   │   └── .gitkeep
│   └── README.md
├── scripts/
│   ├── checks/
│   │   └── .gitkeep
│   ├── dev/
│   │   └── .gitkeep
│   └── README.md
├── services/
│   ├── ai-service/
│   │   ├── migrations/
│   │   │   └── neo4j/
│   │   │       └── README.md
│   │   ├── resources/
│   │   │   ├── pipeline_configs/
│   │   │   │   └── .gitkeep
│   │   │   └── prompts/
│   │   │       └── .gitkeep
│   │   ├── src/
│   │   │   └── scigraphrag_ai/
│   │   │       ├── api/
│   │   │       │   ├── dependencies/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── errors/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── middleware/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── routers/
│   │   │       │   │   └── .gitkeep
│   │   │       │   └── schemas/
│   │   │       │       └── .gitkeep
│   │   │       ├── application/
│   │   │       │   ├── curation/
│   │   │       │   │   └── README.md
│   │   │       │   ├── documents/
│   │   │       │   │   └── README.md
│   │   │       │   ├── graph/
│   │   │       │   │   └── README.md
│   │   │       │   ├── jobs/
│   │   │       │   │   └── README.md
│   │   │       │   ├── ports/
│   │   │       │   │   └── README.md
│   │   │       │   └── retrieval/
│   │   │       │       └── README.md
│   │   │       ├── bootstrap/
│   │   │       │   └── .gitkeep
│   │   │       ├── common/
│   │   │       │   └── .gitkeep
│   │   │       ├── domain/
│   │   │       │   ├── curation/
│   │   │       │   │   └── README.md
│   │   │       │   ├── documents/
│   │   │       │   │   └── README.md
│   │   │       │   ├── graph/
│   │   │       │   │   └── README.md
│   │   │       │   ├── integration/
│   │   │       │   │   └── README.md
│   │   │       │   ├── jobs/
│   │   │       │   │   └── README.md
│   │   │       │   └── retrieval/
│   │   │       │       └── README.md
│   │   │       ├── infrastructure/
│   │   │       │   ├── authorization/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── community_detection/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── embeddings/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── entity_resolution/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── extraction/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── model_providers/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── neo4j/
│   │   │       │   │   ├── queries/
│   │   │       │   │   │   └── .gitkeep
│   │   │       │   │   └── repositories/
│   │   │       │   │       └── .gitkeep
│   │   │       │   ├── object_storage/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── observability/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── pathrag/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── pdf_parsing/
│   │   │       │   │   └── .gitkeep
│   │   │       │   ├── rabbitmq/
│   │   │       │   │   └── .gitkeep
│   │   │       │   └── representation/
│   │   │       │       └── .gitkeep
│   │   │       └── workers/
│   │   │           └── handlers/
│   │   │               └── .gitkeep
│   │   ├── tests/
│   │   │   ├── fixtures/
│   │   │   │   └── .gitkeep
│   │   │   ├── integration/
│   │   │   │   └── .gitkeep
│   │   │   └── unit/
│   │   │       └── .gitkeep
│   │   ├── .env.example
│   │   └── README.md
│   ├── core-service/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── scigraphrag/
│   │   │   │   │           └── core/
│   │   │   │   │               ├── common/
│   │   │   │   │               │   └── .gitkeep
│   │   │   │   │               ├── config/
│   │   │   │   │               │   └── .gitkeep
│   │   │   │   │               ├── modules/
│   │   │   │   │               │   ├── administration/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   ├── audit/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── domain/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── infrastructure/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   ├── billing/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── domain/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── infrastructure/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   ├── credits/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── domain/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── infrastructure/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   ├── curation/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── domain/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── infrastructure/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   ├── identity/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── domain/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── infrastructure/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   ├── integration/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── domain/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── infrastructure/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   ├── jobs/
│   │   │   │   │               │   │   ├── application/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── domain/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── infrastructure/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   ├── presentation/
│   │   │   │   │               │   │   │   └── .gitkeep
│   │   │   │   │               │   │   └── README.md
│   │   │   │   │               │   └── workspace/
│   │   │   │   │               │       ├── application/
│   │   │   │   │               │       │   └── .gitkeep
│   │   │   │   │               │       ├── domain/
│   │   │   │   │               │       │   └── .gitkeep
│   │   │   │   │               │       ├── infrastructure/
│   │   │   │   │               │       │   └── .gitkeep
│   │   │   │   │               │       ├── presentation/
│   │   │   │   │               │       │   └── .gitkeep
│   │   │   │   │               │       └── README.md
│   │   │   │   │               └── security/
│   │   │   │   │                   └── .gitkeep
│   │   │   │   └── resources/
│   │   │   │       └── db/
│   │   │   │           └── migration/
│   │   │   │               └── README.md
│   │   │   └── test/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── scigraphrag/
│   │   │       │           └── core/
│   │   │       │               └── .gitkeep
│   │   │       └── resources/
│   │   │           └── .gitkeep
│   │   ├── .env.example
│   │   └── README.md
│   └── gateway/
│       ├── src/
│       │   ├── main/
│       │   │   ├── java/
│       │   │   │   └── com/
│       │   │   │       └── scigraphrag/
│       │   │   │           └── gateway/
│       │   │   │               ├── config/
│       │   │   │               │   └── .gitkeep
│       │   │   │               ├── errors/
│       │   │   │               │   └── .gitkeep
│       │   │   │               ├── filters/
│       │   │   │               │   └── .gitkeep
│       │   │   │               ├── observability/
│       │   │   │               │   └── .gitkeep
│       │   │   │               ├── routing/
│       │   │   │               │   └── .gitkeep
│       │   │   │               └── security/
│       │   │   │                   └── .gitkeep
│       │   │   └── resources/
│       │   │       └── .gitkeep
│       │   └── test/
│       │       └── java/
│       │           └── com/
│       │               └── scigraphrag/
│       │                   └── gateway/
│       │                       └── .gitkeep
│       ├── .env.example
│       └── README.md
├── tests/
│   ├── contracts/
│   │   └── .gitkeep
│   ├── end-to-end/
│   │   └── .gitkeep
│   └── README.md
├── .env.example
├── .gitignore
├── README.md
└── SCIGRAPHRAG_ARCHITECTURE_CODEX.md
```
