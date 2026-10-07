# Message envelope

Trạng thái: STRUCTURE_ONLY. Owner: Core/AI boundary; wire format độc lập Java/Python.

Trách nhiệm: Fields baseline: messageId, messageType, schemaVersion, occurredAt, producer, correlationId, causationId, aggregateId, idempotencyKey, data. Retry delivery giữ messageId/taskId/business identity.

TODO: Chốt schema, timestamp/UUID/checksum validation và mapping Core event_id/AI eventId ↔ wire messageId. Cùng ID khác payload hash phải quarantine. Không JWT/OTP/password/refresh token/signed URL/binary PDF trong message.
