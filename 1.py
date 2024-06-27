from selenium import webdriver
from selenium.webdriver.common.by import By
import time  

browser = webdriver.Chrome()
browser.get('http://saa.tju.edu.cn/eams/quality/stdEvaluate!innerIndex.action?projectId=1')  

# 输入用户名密码
un = browser.find_element(by=By.ID,value='un')
un.send_keys('用户名')
pd = browser.find_element(by=By.ID,value='pd')
pd.send_keys('密码')

# 空余时间手动输入验证码，可以自己调整
time.sleep(10)

while True:
	# 选一个需要评教的课
	eval = browser.find_element(by=By.CLASS_NAME,value='eval')
	eval.click()
	time.sleep(1)

	# 把所有评分按钮点一遍
	list=browser.find_elements(by=By.CLASS_NAME,value='option-radio')
	for element in list:
		element.click()

	# 向文本框输入一些东西
	list=browser.find_elements(by=By.CLASS_NAME,value='answer-textarea')
	for element in list:
		element.send_keys('非常好')

	# 点击提交
	sub=browser.find_element(by=By.ID,value='sub')
	sub.click()

	# 点击弹窗确认 
	time.sleep(1) 
	alert = browser.switch_to.alert
	print(alert.text)
	alert.accept()

	time.sleep(1)