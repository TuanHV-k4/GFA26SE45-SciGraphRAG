# SciGraphRAG Core Service

Core Service owns platform business workflows and PostgreSQL-backed state.

## Structure

The service follows a three-layer dependency direction:

```text
controller -> service -> repository
```

- `controller`: HTTP request handling and DTO validation.
- `service`: business use cases and transaction coordination.
- `repository`: persistence access through Spring Data JPA.
- `dto`: request and response contracts.
- `entity`: persistence entities.
- `mapper`: conversion between DTOs and entities.
- `config`: service configuration.
- `exception`: centralized domain and HTTP errors.

Application entry point:
`src/main/java/com/scigraphrag/core/CoreApplication.java`.

## PostgreSQL

Start the development database:

```powershell
docker compose up -d postgres
docker compose ps
```

Open `psql` inside the container:

```powershell
docker compose exec postgres psql -U scigraphrag -d scigraphrag
```

The default development connection is
`jdbc:postgresql://localhost:5432/scigraphrag`. Override credentials with
the environment variables documented in `.env.example`.

## Run checks

On Windows:

```powershell
.\mvnw.cmd test
```
