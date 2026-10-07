# AI domain: integration

Trạng thái: STRUCTURE_ONLY. Owner: AI; IntegrationInbox/IntegrationOutbox và dedup records trong Neo4j.

Trách nhiệm: identity, state và payload hash invariants của Inbox/Outbox; giữ messageId/eventId ổn định khi retry. Cùng ID khác payload hash phải audit/quarantine.

Dependency: domain thuần, không driver/transport. Persistence ở infrastructure/neo4j, broker adapter ở infrastructure/rabbitmq, consumer/publisher loops ở workers. Không có integration runtime hoặc database riêng.

TODO: chốt ID mapping, states, dedup/lease/retry, atomic outcome + Outbox và publisher confirms (D13). Ack input sau commit; không dùng Inbox PROCESSING làm bằng chứng thành công.
