# AI application: curation

Trạng thái: STRUCTURE_ONLY. Owner: AI / curation. Scientific graph mutation/provenance thuộc AI; assignment/decision history thuộc Core.

Trách nhiệm: Apply approve/reject/edit/merge/split với action/build/revision guards.

Dependency hợp lệ: Domain và application ports; không import concrete drivers, routers hoặc consumer entry point. Concrete adapter được bootstrap wire.

Entry point: không có runtime riêng; dùng chung bởi AI API/Worker khi triển khai.

TODO: Chốt APPLY_CURATION payload, stale/duplicate checks và terminal events (D08). Chỉ báo thành công sau commit graph mutation + Outbox. Chưa có source hoặc behavior thực thi.
