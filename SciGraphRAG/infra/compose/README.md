# Local Compose

Trạng thái: STRUCTURE_ONLY. Owner: Deployment; một Gateway, một Core và hai AI process dùng chung source.

Trách nhiệm: Đích Backend: gateway, core-service, ai-api, ai-worker, postgres, neo4j, rabbitmq, minio. Web trong mẫu nằm ngoài scaffold Backend lần này.

TODO: Pin images/build/config, private networking, volumes, readiness/retry/shutdown. Worker không inbound HTTP. Chưa có compose.yaml/Dockerfile, chưa có lệnh startup.
