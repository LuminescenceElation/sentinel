# Sentinel

Self-healing monitoring platform (DevOps/SRE portfolio project)

---

## Overview

Sentinel is a lightweight self-healing monitoring platform designed to demonstrate practical DevOps and Site Reliability Engineering (SRE) practices using containerized services.

It monitors services, detects failures, and automatically recovers them using Docker health checks, restart policies, and a custom monitoring agent.

This project is a work in progress and evolves as new reliability features are added.

---

## Current Capabilities

- Containerized FastAPI demo service with health endpoint
- Docker health checks for automated service validation
- Self-healing via container restart policies
- Cross-container monitoring service
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

## Running the Project

### Prerequisites
- Docker Desktop
- Git
- VS Code (recommended)

### Start services
    cd deploy
    docker compose up --build

### View monitor logs
    cd deploy
    docker compose logs -f monitor

### Stop services
    cd deploy
    docker compose down

### Example output
    🔎 Sentinel monitor started
    ❌ demo-service unreachable: connection refused
    ✅ demo-service is healthy

This demonstrates startup ordering and automatic recovery.

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

---

## Author

Built as part of my transition into DevOps / Cloud Engineering.

GitHub: https://github.com/LuminescenceElation