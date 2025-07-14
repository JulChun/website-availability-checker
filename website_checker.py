import requests
import time

def check_website(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()

        status = response.status_code
        elapsed = round(end_time - start_time, 3)

        print(f"\n✅ Website: {url}")
        print(f"Status Code: {status}")
        print(f"Response Time: {elapsed} seconds")

        if status == 200:
            print("Website is UP ✅")
        else:
            print("Website returned a non-OK status ⚠️")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error accessing {url}: {e}")
        print("Website may be DOWN ⛔")

if __name__ == "__main__":
    url = input("Enter website URL (e.g. https://openai.com): ")
    check_website(url)
