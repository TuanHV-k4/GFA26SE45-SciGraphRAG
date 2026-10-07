# AI result events

Trạng thái: STRUCTURE_ONLY. Owner: AI Outbox → RabbitMQ → Core Inbox.

Trách nhiệm: Event names đề xuất: PAPER_PROCESSED, GRAPH_BUILT, AI_JOB_SUCCEEDED, AI_JOB_FAILED, CURATION_APPLIED, CURATION_APPLY_FAILED. Outcome và graph apply chỉ xác nhận sau commit.

TODO: Chốt jobId/taskId/projectId/paperId/buildId, outcome, actualUsage, result/artifact reference, error code. Dedup message và business settlement key; nhiều event không được settle nhiều lần. Timeout/DLQ không là terminal outcome.
