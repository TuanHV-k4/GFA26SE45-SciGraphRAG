# AI domain: curation

Trạng thái: STRUCTURE_ONLY. Owner: AI / curation. Scientific graph mutation/provenance thuộc AI; assignment/decision history thuộc Core.

Trách nhiệm: Giữ model, state, value object và invariant thuần cho nhóm curation.

Dependency hợp lệ: Python standard library và common value types thuần; không import FastAPI, Pydantic transport, Neo4j driver, AMQP hoặc provider.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt APPLY_CURATION payload, stale/duplicate checks và terminal events (D08). Chỉ báo thành công sau commit graph mutation + Outbox. Chưa có source hoặc behavior thực thi.
