# Sentinel

Self-healing monitoring platform (DevOps/SRE portfolio project)

---

## Overview

Sentinel is a lightweight self-healing monitoring platform designed to demonstrate modern DevOps and Site Reliability Engineering (SRE) practices.

It monitors services, detects failures, and automatically recovers them using container orchestration and health checks.

This project is a work in progress and evolves as new reliability features are added.

---

## Current Capabilities

- Containerised service with health endpoint
- Docker health checks for automated health monitoring
- Self-healing via container restart policies
- Cross-container monitoring service
- Service-to-service networking via Docker Compose
- Real-time health logging

---

## Architecture

+-------------------+ health check +-------------------+
| monitor service | ─────────────────────────▶ | demo-service |
| (Sentinel) | | FastAPI app |
+-------------------+ +-------------------+
│ │
│ logs health status │
▼ ▼
Detects failure /health endpoint
Detects recovery Docker healthcheck


---

## Project Structure

sentinel/
├── demo-service/ # Example service being monitored
│ ├── Dockerfile
│ ├── main.py
│ └── requirements.txt
│
├── monitor/ # Sentinel monitoring service
│ ├── Dockerfile
│ ├── main.py
│ └── requirements.txt
│
├── deploy/
│ └── docker-compose.yml
│
└── README.md

---

## How It Works

### 1. Demo Service
- Runs a FastAPI application
- Exposes `/health` endpoint
- Docker healthcheck probes this endpoint

### 2. Docker Healthcheck
Docker automatically checks:
http://localhost:8080/health


If the service fails:
- container becomes **unhealthy**
- restart policy restarts it automatically

### 3. Sentinel Monitor
The monitor container:
- polls the service via Docker network
- logs health status
- detects outages and recovery

---

## Running the Project

From the `deploy` directory:

```bash
docker compose up --build

Check container status:
docker compose ps

View monitor logs:
docker compose logs -f monitor

Example Output
🔎 Sentinel monitor started
❌ demo-service unreachable
✅ demo-service is healthy

**What This Demonstrates
This project showcases production-style reliability patterns:
- Health checks & liveness probes
- Self-healing infrastructure
- Service discovery via container DNS
- Observability through structured logging
- Multi-service orchestration

Roadmap (Planned Features)
- Health state transition detection (failure → recovery)
- Metrics export (Prometheus)
- Alerting (Slack/webhooks)
- Web dashboard for service status
- Failure simulation endpoints
- Kubernetes deployment

Goal
Showcase production-style reliability engineering in a simple, elegant portfolio project.

Author
Built as part of a DevOps/SRE learning journey and portfolio.
