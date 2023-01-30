from threading import Timer
from time import sleep


def hello(text):
    print(text)

t = None
def debouncer(func):
    global t
    if t is not None:
        t.cancel()
    t = Timer(0.5, func)
    t.start()
    
total = ""
for i in "aminsedi":
    total += i
    debouncer(lambda: hello(total))
    sleep(0.2)
else:
    print("Done", total)
    sleep(1)
    total = ""
    
