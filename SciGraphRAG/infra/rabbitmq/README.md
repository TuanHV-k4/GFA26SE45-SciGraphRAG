# RabbitMQ

Trạng thái: STRUCTURE_ONLY. Owner: Core/AI integration vận hành messaging.

Trách nhiệm: Core publish ai.tasks.exchange → Worker; Worker publish ai.events.exchange → core.ai.events; platform.dlx là DLX ví dụ trong nguồn.

TODO: Chốt queue type/bindings, confirms, manual ack, bounded retry/backoff, TTL, prefetch, DLQ/redrive và credential/vhost scopes (D13). Chưa có definitions.json; không Redis broker/Celery protocol.
