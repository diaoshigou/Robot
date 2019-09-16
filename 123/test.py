from selenium import webdriver
import time

brower = webdriver.Firefox()

# 打开网页
brower.get("https://magicube.moredian.com/#/login")
time.sleep(2)#等待网页加载
# 登陆
# brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()
print("1、登陆成功")
time.sleep(2)


# 跳转个人中心
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]').click()
brower.find_element_by_xpath('/html/body/div[3]/ul/li[1]').click()
time.sleep(2)

# 跳转回魔蓝
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div').click()
time.sleep(2)

# 跳转账号设置-修改资料
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]').click()
brower.find_element_by_xpath('/html/body/div[3]/ul/li[2]').click()
time.sleep(2)

# 跳转更换手机号码
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/a').click()
time.sleep(1)

# 跳转重置登录密码
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[3]/a').click()
time.sleep(1)


# 跳转我的机构
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]').click()
brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()
time.sleep(2)

# 搜索机构
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').send_keys("+——-=")
time.sleep(1)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/i').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/span[2]')    #无相关记录
time.sleep(1)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/i').click()    #清除搜索内容
time.sleep(1)
# brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[1]/td[5]/div/div[3]').click()

# 确认是否满机构
if brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[15]/td[1]/div'):
    print("机构已满")
else:# 机构未满跳转新增机构
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]').click()











#退出账号
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]').click()
brower.find_element_by_xpath('/html/body/div[3]/ul/li[4]').click()





# brower.close()
