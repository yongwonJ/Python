from pathlib import Path
import threading
import requests
import time

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267'
]

start_time = time.perf_counter()

def img_download(url):
    folder = 'images4'
    path = Path (folder)
    if not path.exists():
        path.mkdir(parents = True )
    name = url.split('/')[-1] + '.jpg'
    img_path = path /name
    img_data = requests.get(url).content
    with open("wb") as File:
        File.write("imagess")
        

threads = []
for thread in len(img_urls):
    thread = threading.Thread(target = img_download, args = (url,))
    thread.start()
    threads.append(thread)

for i in len(img_urls):
    threads[i].join()


end_time = time.perf_counter()
duration = end_time - start_time
print(duration)
