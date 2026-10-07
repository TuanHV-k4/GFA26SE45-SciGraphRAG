# Object storage

Trạng thái: STRUCTURE_ONLY. Owner: Core workspace quản lý upload/reference/quyền; AI Worker đọc/ghi artifact theo policy.

Trách nhiệm: S3-compatible storage cho PDF/parsed output; database giữ metadata/checksum. Object key không là bằng chứng quyền.

TODO: Chốt bucket/prefix grants, scoped credentials, lifecycle/readiness; giữ private management endpoint. Không commit PDF/dữ liệu người dùng hoặc volume.
