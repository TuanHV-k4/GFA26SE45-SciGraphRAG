# PostgreSQL infrastructure

Trạng thái: STRUCTURE_ONLY. Owner: Core độc quyền dữ liệu platform.

Trách nhiệm: Provision/backup/connection configuration; migrations ở services/core-service/src/main/resources/db/migration/.

TODO: Pin image/digest/version, least-privilege credential và volume/readiness. Không cấp Core database credential cho AI; không commit volume.
