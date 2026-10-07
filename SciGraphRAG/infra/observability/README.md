# Observability

Trạng thái: STRUCTURE_ONLY. Owner: Từng runtime phát telemetry; backend monitoring còn TO PIN.

Trách nhiệm: Correlation xuyên HTTP/message/job/audit; structured logs, HTTP health/readiness, Worker heartbeat; metrics latency/error, queue/DLQ, worker duration, inbox duplicate và outbox delay.

TODO: Chốt backend/rate-limit store (D15). Prometheus/Grafana/OTLP/OpenTelemetry là đề xuất, chưa là dependency bắt buộc; không log token/OTP/password/provider secrets.
