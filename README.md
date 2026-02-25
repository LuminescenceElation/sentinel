# Sentinel
Self-healing monitoring platform demonstrating automated recovery, health checks, and service observability (DevOps/SRE portfolio project)

---

## Overview

Sentinel is a lightweight self-healing monitoring platform designed to demonstrate practical DevOps and Site Reliability Engineering (SRE) practices using containerized services.

It monitors services, detects failures, and automatically recovers them using Docker health checks, restart policies, and a custom monitoring agent.

This project demonstrates real-world reliability patterns such as health checks, automatic recovery, and service observability.

It is designed to evolve as additional reliability features are implemented.

---

## Current Capabilities

- Containerized FastAPI demo service with health endpoint
- Docker health checks for automated service validation
- Self-healing via container restart policies
- Cross-container monitoring agent
- Service-to-service networking via Docker Compose
- Real-time health logging from monitor agent

---

**Components**

- **demo-service** — FastAPI application exposing `/health`
- **monitor** — Python monitoring agent polling service health
- **Docker Compose** — Orchestrates services and networking
- **Docker health checks** — Provide container health status
- **Restart policies** — Enable automatic recovery

---

## How It Works

1. Docker Compose starts both services.
2. The demo service exposes a `/health` endpoint.
3. Docker health checks validate the service inside the container.
4. The monitor container polls the service over the Docker network.
5. If the service fails, Docker restart policies automatically recover it.
6. The monitor logs service status in real time.

---

### Example output (startup sequence)

```text
🔎 Sentinel monitor started
❌ demo-service unreachable: connection refused
✅ demo-service is healthy
```

This demonstrates startup ordering and automatic recovery.

## Demo: Failure Detection & Recovery

Sentinel continuously checks the `demo-service` health endpoint and logs state changes.

### What you’ll see
- ✅ Normal healthy checks
- ❌ A brief “unreachable” period after a simulated failure
- ✅ Recovery confirmed once the service returns (and the container restarts)

### Example output (real run)

```bash
monitor-1 | service=demo-service status=down status_code=na event=unreachable
monitor-1 | service=demo-service status=up status_code=200 recoveries_total=1 event=healthy
```

This demonstrates startup ordering, failure detection, and automatic recovery.

---

## Running the Project

### Start services
```bash
cd deploy
docker compose up --build
```

### View monitor logs
```bash
cd deploy
docker compose logs -f monitor
```

### Stop services
```bash
cd deploy
docker compose down
```

---

## Project Structure

    sentinel/
    ├─ demo-service/          # FastAPI demo service
    ├─ monitor/               # Monitoring agent
    └─ deploy/                # Docker Compose configuration

## Architecture

    monitor (Sentinel agent)  -- polls /health -->  demo-service (FastAPI)
              |
              +-- logs health status to standard output

## Roadmap

### Planned enhancements

- Metrics collection (Prometheus)
- Visual dashboards (Grafana)
- Alerting (Slack/email/webhooks)
- Failure simulation scenarios
- Kubernetes deployment version

---

## Why This Project

This project showcases production-style reliability engineering concepts in a simple, elegant portfolio piece:

- Observability fundamentals  
- Automated recovery  
- Container orchestration  
- Service health monitoring  
- Infrastructure as code mindset
- Demonstrates production-minded thinking in a minimal, reproducible environment

---

## Author

Built by Luminescence Elation as part of a DevOps learning portfolio.