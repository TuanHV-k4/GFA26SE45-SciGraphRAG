# Backend workflows

Trạng thái: STRUCTURE_ONLY. Owner: Core điều phối product state; AI thực thi scientific operations.

Trách nhiệm: Tham chiếu phần 12, 13 và 16.2 của tài liệu nguồn cho WF01–WF10: auth, payment, credit, ingestion, graph, exploration/QA, discovery, curation, subscription và reconciliation.

TODO: Viết state/transaction/sequence chi tiết khi implement; giữ Core Outbox → Worker và AI Outbox → Core Inbox, ack-after-commit và scope guards.
