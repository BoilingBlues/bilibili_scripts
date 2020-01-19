from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

driver.get("https://www.bilibili.com/blackboard/xianxing2020bnj.html?bsource=2020bnjbt&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.38&anchor=top")

while(1):
    try:
        add = driver.find_element_by_xpath("//*[@id='app']/article/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]")
    except:
        print("加载中")
    else:
        break

add.click()
time.sleep(2)

while(1):
    try:
        add.click()
    except:
        print("登录中")
    else:
        break

while(1):
    try:
        time.sleep(0.1)
        add.click()
    except:
        try:
            driver.find_element_by_xpath("/html/body/div[10]/div/div/div/div[2]").click()
            print("触发一次菜品")
            continue
        except:
            print("10,失败")
        try:
            driver.find_element_by_xpath("/html/body/div[9]/div/div/div/div[2]").click() 
            print("触发一次菜品")
            continue
        except:
            print("9,失败") 
        print("关闭失败")
        break
driver.close()