import time
import requests

SERVICE_URL = "http://demo-service:8080/health"

def check_service():
    try:
        response = requests.get(SERVICE_URL, timeout=2)
        if response.status_code == 200:
            print("✅ demo-service is healthy")
        else:
            print(f"⚠️ demo-service returned {response.status_code}")
    except Exception as e:
        print(f"❌ demo-service unreachable: {e}")

if __name__ == "__main__":
    print("🔎 Sentinel monitor started")
    while True:
        check_service()
        time.sleep(5)