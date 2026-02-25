import time
import requests


SERVICE_URL = "http://demo-service:8080/health"
INTERVAL_S = 5
TIMEOUT_S = 2


def now_s() -> int:
    return int(time.time())


def log(**fields):
    # key=value structured logs (easy to grep, feels very “ops”)
    line = " ".join([f"{k}={v}" for k, v in fields.items()])
    print(line, flush=True)


def check_service() -> tuple[bool, int | None, str | None]:
    try:
        r = requests.get(SERVICE_URL, timeout=TIMEOUT_S)
        return (r.status_code == 200, r.status_code, None)
    except Exception as e:
        return (False, None, str(e))


if __name__ == "__main__":
    log(service="demo-service", monitor="sentinel", event="start", interval_s=INTERVAL_S)

    failures_total = 0
    consecutive_failures = 0
    recoveries_total = 0

    last_state = None  # None | "up" | "down"
    down_since = None  # unix timestamp when we first observed down

    while True:
        ok, status_code, err = check_service()
        ts = now_s()

        if ok:
            # state transition: down -> up (recovery)
            if last_state != "up":
                if down_since is not None:
                    downtime_s = ts - down_since
                else:
                    downtime_s = 0

                if last_state == "down":
                    recoveries_total += 1

                log(
                    ts=ts,
                    service="demo-service",
                    status="up",
                    status_code=status_code,
                    recoveries_total=recoveries_total,
                    failures_total=failures_total,
                    consecutive_failures=0,
                    downtime_s=downtime_s,
                    event="recovered" if last_state == "down" else "healthy",
                )

            else:
                # steady state up
                log(
                    ts=ts,
                    service="demo-service",
                    status="up",
                    status_code=status_code,
                    recoveries_total=recoveries_total,
                    failures_total=failures_total,
                    consecutive_failures=0,
                    event="healthy",
                )

            last_state = "up"
            consecutive_failures = 0
            down_since = None

        else:
            failures_total += 1
            consecutive_failures += 1

            # first time we notice down
            if last_state != "down":
                down_since = ts

            log(
                ts=ts,
                service="demo-service",
                status="down",
                status_code=status_code if status_code is not None else "na",
                recoveries_total=recoveries_total,
                failures_total=failures_total,
                consecutive_failures=consecutive_failures,
                error=err if err is not None else "non_200",
                event="unreachable" if err is not None else "unhealthy",
            )

            last_state = "down"

        time.sleep(INTERVAL_S)