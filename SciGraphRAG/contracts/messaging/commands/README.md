# AI commands

Trạng thái: STRUCTURE_ONLY. Owner: Core publish qua Core Outbox → RabbitMQ → AI Worker.

Trách nhiệm: Baseline task types: PROCESS_PAPER, REPROCESS_PAPER, BUILD_GRAPH, REBUILD_GRAPH, GENERATE_EMBEDDINGS, RUN_COMMUNITY_DETECTION. RUN_GROUNDED_QA, EXPLAIN_GROUNDED_PATH, APPLY_CURATION là SCAFFOLD.

TODO: Chốt data.jobId/taskId/projectId/requestedBy, paperId/source.objectKey/checksum hoặc build/config/snapshot theo task. Curation giữ reviewTaskId/actionId/expected build/revision. requestedBy chỉ phục vụ audit, không thay authorization.
