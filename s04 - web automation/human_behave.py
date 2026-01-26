import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class HumanBehavior:
    def __init__(self, driver):
        self.driver = driver

    def random_scroll(self):
        """اسکرول تصادفی"""
        scroll_amount = random.randint(200, 800)
        self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(1, 2))

    def human_click(self, element):
        """کلیک انسانی"""
        # حرکت به سمت عنصر
        actions = ActionChains(self.driver)

        # کمی لرزش قبل از کلیک
        for _ in range(random.randint(1, 3)):
            actions.move_by_offset(
                random.randint(-5, 5),
                random.randint(-5, 5)
            )

        # مکث قبل از کلیک
        actions.pause(random.uniform(0.2, 0.5))

        # کلیک
        actions.click(element)
        actions.perform()

        # مکث بعد از کلیک
        time.sleep(random.uniform(0.5, 1.5))

    def browsing_pattern(self):
        """الگوی مرور طبیعی"""
        # اسکرول پایین
        self.random_scroll()

        # کمی بالا برگرد
        self.driver.execute_script("window.scrollBy(0, -100);")
        time.sleep(random.uniform(0.5, 1))

        # دوباره پایین برو
        self.random_scroll()


# استفاده
driver = webdriver.Chrome()
human = HumanBehavior(driver)

# باز کردن سایت
driver.get("https://example.com")
time.sleep(random.uniform(2, 4))  # منتظر لود شدن

# رفتار انسانی
human.browsing_pattern()