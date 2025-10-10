import requests
import time
import threading
import uuid

start_time = time.time()

class ImageDownloader(threading.Thread):
    def __init__(self, image_url):
        threading.Thread.__init__(self)
        self.image_url = image_url
        # self.save_path = save_path

    def run(self):
        print(f"Starting download from {self.image_url}")
        image = requests.get(self.image_url)
        image_name = f"Images/{str(uuid.uuid4())}.jpg"
        with open(image_name, 'wb') as file:
            file.write(image.content)
        time.sleep(1)  # Simulate download time
        print(f"Finished downloading {self.image_url} to {image_name}")

if __name__ == "__main__":
    image_urls = [
        "https://images.pexels.com/photos/1583582/pexels-photo-1583582.jpeg",
        "https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg",
        "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
        "https://images.pexels.com/photos/1563356/pexels-photo-1563356.jpeg",
        "https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg"
    ]
   
    threads = []
    for url in image_urls:
        thread = ImageDownloader(url)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"All downloads completed in time: {time.time() - start_time: .2f} seconds")