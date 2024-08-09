import threading
import requests
import time

def fetch_data(url):
    response = requests.get(url)
    print(f"Fetched {len(response.text)} characters from {url}")

def main():
    urls = [f'https://jsonplaceholder.typicode.com/posts/{i}' for i in range(1, 100)]
    threads = []

    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=fetch_data, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken with threading: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
