import requests
import time

def fetch_data(url):
    response = requests.get(url)
    print(f"Fetched {len(response.text)} characters from {url}")

def main():
    urls = [f'https://jsonplaceholder.typicode.com/posts/{i}' for i in range(1, 100)]

    start_time = time.time()

    for url in urls:
        fetch_data(url)

    end_time = time.time()
    print(f"Time taken with synchronous execution: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
