# SciGraphRAG Backend

Trạng thái: AI Service và Core Service đã có cấu trúc 3-layer build/test được; Gateway vẫn ở mức scaffold.

Cấu trúc được dựng tại root hiện tại theo [tài liệu kiến trúc](SCIGRAPHRAG_ARCHITECTURE_CODEX.md), phần 5.3, 7–15 và 17–20. Phạm vi lần này là Backend: Gateway, Core, AI và các nhánh hỗ trợ; `apps/web` chưa tạo theo yêu cầu người dùng.

```text
SciGraphRAG/
├── services/
│   ├── gateway/
│   ├── core-service/
│   └── ai-service/
├── contracts/
├── infra/
├── docs/
├── scripts/
├── tests/
└── research/
```

| Thành phần | Trách nhiệm | Entry point |
|---|---|---|
| [Gateway](services/gateway/README.md) | Public routing, JWT, filter, giới hạn request | `services/gateway/src/main/java/com/scigraphrag/gateway/GatewayApplication.java` |
| [Core](services/core-service/README.md) | Platform, PostgreSQL, billing/credits, product jobs, curation | `services/core-service/src/main/java/com/scigraphrag/core/CoreApplication.java` |
| [AI API](services/ai-service/README.md) | FastAPI theo `controllers → services → repositories` | `services/ai-service/app/main.py` |
| AI Worker | RabbitMQ, scientific pipeline, AI outcome/outbox | Chưa triển khai |

Core và AI là hai business service; Gateway là hạ tầng. Core Service và AI API hiện đã buildable; AI Worker vẫn là runtime dự kiến.

Luồng task: Core Outbox → RabbitMQ → AI Worker. Luồng result: AI Outbox → RabbitMQ → Core Inbox. Core → AI API Internal REST là kênh đồng bộ độc lập.

Chạy AI API từ `services/ai-service` bằng `.\.venv\Scripts\python.exe -m uvicorn app.main:app`. Dependency runtime và test được pin lần lượt trong `requirements.txt` và `requirements-dev.txt`.

- [Tổng quan](docs/architecture/overview.md), [ranh giới module](docs/architecture/module-boundaries.md), [ownership dữ liệu](docs/architecture/data-ownership.md).
- [Cây thư mục thực tế và trạng thái scaffold](docs/architecture/scaffold-status.md).
- [Quyết định còn mở D01–D16](docs/architecture/open-decisions.md): dependency/image/model versions, authorization, contracts, physical schema, reliability và research protocol.
- [Contracts](contracts/README.md), [hạ tầng](infra/README.md), [research](research/README.md).

AI API tự load cấu hình `AI_SERVICE_*` từ environment hoặc `services/ai-service/.env`; `.env` được loại khỏi Git. Các scaffold chưa triển khai vẫn dùng `.gitkeep`.
