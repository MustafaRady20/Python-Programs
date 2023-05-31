# Reminds  you to take a break after an hour of hard work...!

import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title ="Alert!!",
            message = "Take a short break, It has been an hour",
            timeout=10 
        )
        time.sleep(3600)
