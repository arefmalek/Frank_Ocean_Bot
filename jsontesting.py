from datetime import datetime
from time import sleep

now = datetime.now()
current_time = now.strftime("%H:%M")
if ("23:11" <= current_time <= "23:12"):
    print("poggers")
    sleep(1)
    print("back")
    