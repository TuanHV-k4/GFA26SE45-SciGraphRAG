# Public HTTP contracts

Trạng thái: STRUCTURE_ONLY. Owner: Core sở hữu auth/workspace/billing/credits/jobs/curation/admin; AI sở hữu bounded graph/evidence.

Trách nhiệm: Client truy cập qua Gateway; JWT và resource authorization tại service. Metered AI operations mặc định tạo Core job.

TODO: Chốt request/response/error/status, projectId/buildId/task scope, pagination và limits; dự kiến core.openapi.yaml và ai.openapi.yaml, chưa tạo.
