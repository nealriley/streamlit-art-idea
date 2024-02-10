import time
from content.generate import generate, content

while True:
    content(generate())
    time.sleep(10)