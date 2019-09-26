import random
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


brower = webdriver.Firefox()
brower.implicitly_wait(5)

# 打开网页
brower.get("https://magicube.moredian.com/#/login")

# 个人中心
def personCenter():
    # 跳转个人中心
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/i[2]').click()
    brower.find_element_by_xpath('/html/body/div[3]/ul/li[1]').click()

    # 跳转回魔蓝
    # brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div').click()

    # 跳转账号设置-修改资料
    # brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]').click()
    brower.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div[3]/div').click()
    #
    # 修改人脸
    # flag = brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/img')
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/span/input')
    filepath = r'D:\picture\沈晨菲.jpg'
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/span/input').send_keys(
        filepath)

    # 修改姓名
    sleep(2)
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/input').click()
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/div/i').click()
    sleep(2)
    name = str("管理员") + str(random.randint(10000, 99999))
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/input').click()
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/input').send_keys(name)

    # 切换性别
    brower.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[4]/div/div[2]/span[1]').click()
    brower.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[4]/div/div[2]/span[2]').click()

    # 选择出生日期为当天
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/div[2]/div/div[2]/input').click()
    brower.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[3]/div/span').click()

    # 跳转更换手机号码
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[2]/a').click()


    # 跳转重置登录密码
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div[3]/a').click()

# 搜索机构
def selectOrg():
    sleep(2)
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/i[2]').click()  # 点击下拉框
    # brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()  # 点击跳转按钮
    brower.find_element_by_xpath('/html/body/div[4]/ul/li[3]').click()  # 点击跳转按钮(个人中心)
    # print("跳转我的机构成功")
    # 搜索机构
    brower.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').click()  # 聚焦光标
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').send_keys(
        "+——-=")  # 输入搜索内容
    brower.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/i').click()  # 点击搜索按钮
    brower.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/span[2]')  # 确认 无相关记录 的提示
    print("无相关记录提示 确认")
    brower.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/i').click()  # 清除搜索内容
    print("清除搜索记录成功")
    # brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[1]/td[5]/div/div[3]').click()

    # 前往机构
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[2]/td[5]/div/div[3]').click()

# 切换主机构
def orgList():
    # 跳转机构列表页
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/i[2]').click()  # 点击下拉框
    brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()  # 点击跳转按钮
    print("跳转我的机构成功")

    #切换主机构
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[1]/td[5]/div/div[1]').click()  # 设立第一个机构为主机构
    sleep(2)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[2]/td[5]/div/div[1]').click()  # 设立第二个机构为主机构
    print("切换主机构机构成功")

# 创建新机构
def creatOrg():
    sleep(2)
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/i[2]').click()  # 点击下拉框
    # brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()  # 点击跳转按钮
    try:
        element = WebDriverWait(brower, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/ul/li[3]')))  # 等待直到搜索元素显示
    finally:
        brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()  # 点击某一元素
    # brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()  # 点击跳转按钮(个人中心)
    # print("跳转我的机构成功")

    # 确认是否满机构
    try:
        # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[15]/td[1]/div').click()
        brower.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[15]/td[1]/div')  # 点击第15个机构
        print("15个机构已满")

    except selenium.common.exceptions.NoSuchElementException:
        # 新增机构
        print("跳转新增机构")
        brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]').click()  # 点击新增机构
        brower.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').click()  # 聚焦光标在机构名称输入框
        brower.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').send_keys(
            random.randint(100000, 999999))  # 机构名称为随机100000~999999 的数字串
        brower.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/span').click()  # 点击跳转选择机构所在地址
        brower.find_element_by_xpath('//*[@id="search-input"]').click()  # 聚焦光标在地址输入框
        brower.find_element_by_xpath('//*[@id="search-input"]').send_keys("北京")  # 地址输入框输入地址
        try:
            element = WebDriverWait(brower, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="amap-sug1"]')))  # 等待直到搜索元素显示
        finally:
            brower.find_element_by_xpath('//*[@id="amap-sug1"]').click()  # 点击某一元素
        sleep(2)
        brower.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/ul/li[1]/div[1]').click()  # 点击某一选项地址
        brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]').click()  # 保存地址
        sleep(2)
        # brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]').click() # 创建机构
        brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]').click()  # 取消操作
    except Exception as e:
        print(e)

# 魔点门禁-设备配置
def deviceConfig():
    # 选择第一个设备
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/i').click()

    # 修改设备名
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').click()
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').send_keys(
        str(random.randint(10000, 99999)))

    # 跳转权限组列表页
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[4]/div/div[2]/div/div[2]/i').click()
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/table/tr/th[1]/div/div/i').click()
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div[1]').click()

    # 音量设置
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div/span[3]/i[1]').click()  # 下拉框
    brower.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[2]').click()  # 低音模式
    sleep(1)
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[5]/div/div[2]/div/div/span[3]/i[1]').click()  # 下拉框
    brower.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[3]').click()  # 静音模式

    # 重新设置开门延时
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[7]/div[1]/div[2]/div/div/i').click()
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[7]/div[1]/div[2]/div/input').click()
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[7]/div[1]/div[2]/div/input').send_keys("3")

    # 切换极速模式
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[9]/div/div[2]/div[2]/i').click()  # 开启
    brower.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[9]/div/div[2]/div[1]/i').click()  # 关闭

    # 设置
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[3]/div[2]').click()  # 取消
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[3]/div[1]').click()    # 保存

# 创建带 Selenium 的权限组
def creatGroup():   # Selenium12345
    # 新增权限组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[2]/a').click()
    sleep(0.5)
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

# 编辑全员组
def editGroup():
    # 切换权限组界面
    sleep(3)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[2]/a').click()  # 跳转权限组界面
    sleep(1)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').click()  # 聚焦搜索框
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').send_keys("全员组")  # 输入搜索关键字：全员组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/i').click()  # 开始搜索
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/table/tr[1]/td[6]/div/div[1]').click()   # 编辑默认组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').click()
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').send_keys(random.randint(10000,99999))
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/i').click()    # 选择全员
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/i').click()    # 选择指定范围
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/i').click() # 点击选人组件
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div').click()  # 清空当前选择
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').click()
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/input').send_keys("第一个")
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/i').click()  # 搜索名字
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/div[2]/div/i').click()  # 选中该人
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div/span[2]/i').click() # 删除该人
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[1]/div[3]/div[1]/div/div[2]/div/i').click()  # 再次选中该人
    # # brower.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]').click() # 保存设置
    # brower.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[2]').click() # 取消
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
    brower.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]').click() # 确认
    # brower.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[2]').click() # 取消
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

# 删除带 Selenium 的权限组
def deleteGroup():
    sleep(0.5)
    # 删除普通组
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').click()  # 聚焦搜索框
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/input').send_keys("Selenium")  # 输入搜索关键字：Selenium
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/i').click()  # 开始搜索
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/table/tr/td[6]/div/div[2]').click()  # 尝试删除普通组
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[2]').click() # 取消删除
    sleep(0.5)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/table/tr/td[6]/div/div[2]').click()  # 再次删除普通组
    sleep(0.5)
    brower.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[1]').click() # 确认删除
    sleep(3)
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div') # 确认"创建权限组"按钮

    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/i').click()    # 清除搜索内容
    sleep(1)
    try:
        brower.find_element_by_xpath("//*[contains(text(),'全员组')]")
        print("全员组存在！")
    except:
        print("全员组不存在！")




# 登陆
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click() # 聚焦手机号码输入框
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()  # 点击登陆
print("1、登陆成功")

personCenter() # 跳转个人中心
orgList()
creatOrg()
selectOrg()

# 选择机构
sleep(2)
brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div/div/span[3]/i[1]').click()
brower.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[7]').click()

# 进入魔点门禁
# brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[10]/td[5]/div/div[1]').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()

# 修改设备配置
deviceConfig()

creatGroup()
editGroup()
deleteGroup()















#退出账号
sleep(2)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]').click()
try:                                                                                    #/html/body/div[3]/ul/li[4] (工作台)
    element = WebDriverWait(brower, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/ul/li[4]')))  # 等待直到搜索元素显示
finally:
    brower.find_element_by_xpath('/html/body/div[3]/ul/li[4]').click()





# brower.close()
