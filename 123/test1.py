import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


brower = webdriver.Firefox()
brower.implicitly_wait(3)

# 打开网页
brower.get("https://magicube.moredian.com/#/login")

# 登陆
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()
print("1、登陆成功")

# 选择机构
sleep(2)
brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div/div/span[3]/i[1]').click()
brower.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[7]').click()

# 进入魔点门禁
# brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[10]/td[5]/div/div[1]').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()

def editGroup():
    # 切换权限组界面
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[2]/a').click()  # 跳转权限组界面
    sleep(1)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').click()  # 聚焦搜索框
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').send_keys("全员组")  # 输入搜索关键字：全员组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/i').click()  # 开始搜索
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/table/tr[1]/td[6]/div/div[1]').click()   # 编辑默认组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').click()
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').send_keys(random.randint(10000,99999))
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/i').click()    # 选择全员
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/i').click()    # 选择指定范围
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/i').click() # 点击选人组件
    brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div').click()  # 清空当前选择
    brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').click()
    brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').send_keys("第一个")
    brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/i').click()  # 搜索名字
    brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/div[2]/div/i').click()  # 选中该人
    brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/span[2]/i').click() # 删除该人
    brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/div[2]/div/i').click()  # 再次选中该人
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]').click() # 保存设置
    brower.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[2]').click() # 取消
    sleep(1)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[6]/div/div[2]/div[1]/i').click() # 开放时间选择永久
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div[2]/i').click() # 开放时间选择指定时间
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[5]/div[1]/div[2]/div/div[1]/div[2]/input').click() # 点击开始时间
    brower.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[1]/ul/li[16]').click() # 开始时间选择15时
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[5]/div[2]/button[2]').click() # 确定

    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[5]/div[1]/div[2]/div/div[3]/div[2]/input').click() # 点击结束时间
    brower.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[1]/ul/li[19]').click() # 结束时间选择18时
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[6]/div[2]/button[2]').click() # 确定结束时间
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[6]/div/div[2]/div[1]/i').click() # 开放周期选择永久
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[6]/div/div[2]/div[2]/i').click() # 开放时间选择指定周期
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[8]/div[1]/div[2]/div/div[1]/div[2]/input').click() # 点击开始日期
    brower.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[2]/table[1]/tbody/tr[7]/td[1]').click() # 开始日期选择29号
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[8]/div[1]/div[2]/div/div[3]/div[2]/input').click() # 点击结束日期
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[8]/div[1]/div/div[2]/table[1]/tbody/tr[7]/td[2]').click() # 结束时间选择30号
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[9]/div/div[2]/div/div[4]/i').click() # 取消周四
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[11]/div/div[2]/div/div[2]/i').click() # 打开选择设备界面
    sleep(1)
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div[1]/div/span').click() # 清空设备选择
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').click() # 聚焦筛选输入框

    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').click() # 聚焦筛选输入框
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').send_keys("1") # 筛选带'门禁机'的设备名称
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/i').click() # 开始筛选
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/span[2]/i[1]').click() # 选择第一个设备
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span[2]/i').click() # 删除选择设备
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/span[2]/i[1]').click() # 再次选择第一个设备
    # brower.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]').click() # 确认
    brower.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[2]').click() # 取消
    sleep(0.5)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[12]/div/div[2]/div/i').click() # 设为默认组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[3]/div[1]').click() # 保存权限组编辑后配置
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[3]/div[2]').click() # 取消权限组编辑


    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/table/tr[1]/td[6]/div/div[2]').click() # 点击删除默认组
    try:
        brower.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div')  # 确认是否有"我知道了"弹窗按钮
        brower.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div').click()  # 如果有，则点击
    except:
        print("默认组被删除！！！！")

# editGroup()

def creatGroup():   # Selenium12345
    # 新增权限组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[2]/a').click()
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[1]').click()

    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').click()
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').send_keys(str("Selenium")+str(random.randint(10000, 99999)))
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/i').click()  # 选择全员
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/i').click()  # 选择指定范围
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/i').click()  # 点击选人组件
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div').click()  # 清空当前选择
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').click()
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').send_keys("第一个")
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/i').click()  # 搜索名字
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/div[2]/div/i').click()  # 选中该人
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/span[2]/i').click()  # 删除该人
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/div[2]/div/i').click()  # 再次选中该人
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]').click()  # 保存设置
    # # brower.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[2]').click() # 取消
    sleep(0.5)
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[6]/div/div[2]/div[1]/i').click()  # 开放时间选择永久
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div[2]/i').click()  # 开放时间选择指定时间
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[5]/div[1]/div[2]/div/div[1]/div[2]/input').click()  # 点击开始时间
    brower.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[1]/ul/li[16]').click()  # 开始时间选择15时
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[5]/div[2]/button[2]').click()  # 确定

    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[5]/div[1]/div[2]/div/div[3]/div[2]/input').click()  # 点击结束时间
    brower.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[1]/ul/li[19]').click()  # 结束时间选择18时
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[6]/div[2]/button[2]').click()  # 确定结束时间
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[6]/div/div[2]/div[1]/i').click()  # 开放周期选择永久
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[6]/div/div[2]/div[2]/i').click()  # 开放时间选择指定周期
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[8]/div[1]/div[2]/div/div[1]/div[2]/input').click()  # 点击开始日期
    brower.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[2]/table[1]/tbody/tr[7]/td[1]').click()  # 开始日期选择29号
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[8]/div[1]/div[2]/div/div[3]/div[2]/input').click()  # 点击结束日期
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[8]/div[1]/div/div[2]/table[1]/tbody/tr[7]/td[2]').click()  # 结束时间选择30号
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[9]/div/div[2]/div/div[4]/i').click()  # 取消周四
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[11]/div/div[2]/div/div[2]/i').click()  # 打开选择设备界面
    sleep(1)
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div[1]/div/span').click()  # 清空设备选择
    brower.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').click()  # 聚焦筛选输入框

    brower.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').click()  # 聚焦筛选输入框
    brower.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').send_keys(
        "1")  # 筛选带'门禁机'的设备名称
    brower.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/i').click()  # 开始筛选
    sleep(0.5)
    brower.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/span[2]/i[1]').click()  # 选择第一个设备
    brower.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span[2]/i').click()  # 删除选择设备
    brower.find_element_by_xpath(
        '/html/body/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/span[2]/i[1]').click()  # 再次选择第一个设备
    brower.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]').click()  # 确认
    # brower.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[2]').click() # 取消
    sleep(0.5)
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[12]/div/div[2]/div/i').click()  # 设为默认组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[3]/div[1]').click()  # 保存权限组编辑后配置
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[3]/div[2]').click() # 取消权限组编辑## #

# creatGroup()

def deleteGroup():
    sleep(0.5)
    # 删除普通组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').click()  # 聚焦搜索框
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').send_keys("Selenium")  # 输入搜索关键字：Selenium
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/i').click()  # 开始搜索
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/table/tr/td[6]/div/div[2]').click()  # 尝试删除普通组
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[2]').click() # 取消删除
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/table/tr/td[6]/div/div[2]').click()  # 再次删除普通组
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[1]').click() # 确认删除
    sleep(1)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div').click() # 确认"创建权限组"按钮

    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/i').click()    # 清除搜索内容
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()


brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[2]/a').click()  # 跳转权限组界面
sleep(1)
brower.find_element_by_xpath("//*[contains(text(),'第四组')]")
