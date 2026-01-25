import schedule
import time


def information():
    print("Hello this is information")


schedule.every(5).seconds.do(information)
schedule.every(1).minute.do(information)
schedule.every().day.do(information)
schedule.every().hours.do(information)
schedule.every().monday.do(information)
schedule.every().friday.do(information)

while True:
    schedule.run_pending()
    time.sleep(1)