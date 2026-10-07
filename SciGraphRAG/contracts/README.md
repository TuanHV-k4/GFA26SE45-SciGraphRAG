# Contracts Backend

Trạng thái: STRUCTURE_ONLY. Owner: Core và AI cùng sở hữu wire contract tại boundary, mỗi service tự map sang domain.

Trách nhiệm: HTTP và RabbitMQ neutral versioned JSON; không chứa shared entity library/database model. Schemas/examples sẽ được tạo và validate sau khi payload được chốt.

TODO: Pin versioning, identity, authorization scope, outcome/usage units và compatibility trước OpenAPI/JSON Schema. Không tạo fake 200/success hoặc allow-all.
