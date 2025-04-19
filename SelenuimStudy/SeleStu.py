from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--windows-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.implicitly_wait(10)

    driver.get("https://cn.bing.com/")
    print("已打开", driver.title)

    search_input = driver.find_element(By.ID, "sb_form_q")
    search_input.send_keys("OnceAgain")
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)

    search_results = driver.find_elements(By.CLASS_NAME, "b_algo")
    print(f"\n已搜索到 {len(search_results)} 条结果\n")

    for index, result in enumerate(search_results, 1):
        try:
            title_element = result.find_element(By.CSS_SELECTOR, "h2 a")
            title = title_element.text
            link = title_element.get_attribute("href")

            print(f"序号: {index}:")
            print(f"标题：{title}")
            print(f"链接：{link}")

        except Exception as e:
            print(f"无法获取第{index}条标题或链接,错误信息:{str(e)}")
            continue

finally:
    time.sleep(3)
    driver.quit()
