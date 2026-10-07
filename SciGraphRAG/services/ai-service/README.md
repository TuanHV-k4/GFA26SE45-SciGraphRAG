# AI Service

Trạng thái: **BUILDABLE_3_LAYER**. FastAPI chạy trên Python 3.12 với entry point `app.main:app`.

## Kiến trúc

Runtime chính dùng cấu trúc ba layer và dependency một chiều:

```text
controllers → services → repositories
      │            │            │
   schemas       models       models
```

- `app/controllers`: khai báo HTTP route, dependency injection và chuyển domain model sang response schema.
- `app/services`: điều phối use case và định nghĩa repository protocol cần dùng.
- `app/repositories`: đọc/ghi dữ liệu hoặc trạng thái runtime; không phụ thuộc controller/service.
- `app/models`: model nội bộ, không phụ thuộc FastAPI hoặc Pydantic transport.
- `app/schemas`: Pydantic request/response schema.
- `app/core`: cấu hình và cross-cutting concerns.

Các thư mục `src/scigraphrag_ai` là scaffold kiến trúc cũ, được giữ lại làm tài liệu tham khảo và không nằm trên runtime import path. Mã mới không được import ngược từ `app` vào scaffold này.

## Cài đặt

Từ `services/ai-service`:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Dependency runtime được pin trong `requirements.txt`; dependency test nằm trong `requirements-dev.txt`.

## Chạy service

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

- Health: <http://127.0.0.1:8000/health>
- Swagger UI: <http://127.0.0.1:8000/docs>
- OpenAPI: <http://127.0.0.1:8000/openapi.json>

## Kiểm tra

```powershell
.\.venv\Scripts\python.exe -m compileall app
.\.venv\Scripts\python.exe -c "from app.main import app"
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest
```

`tests/unit/test_layer_boundaries.py` bảo vệ dependency direction của ba layer.

