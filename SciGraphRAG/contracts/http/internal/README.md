# Internal HTTP contracts

Trạng thái: STRUCTURE_ONLY. Owner: Core và AI API; private network.

Trách nhiệm: Core → AI API bounded query-preview/runtime status; AI API → Core authorization check. Authorization không gọi ngược AI để tránh recursion.

TODO: Chốt service identity, timeout, minimal verified user context và fail-closed behavior. Authorization response dự kiến allowed/subject/resource/scope/reason/expiry; chưa có OpenAPI (D06, D12).
