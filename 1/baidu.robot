
*** Settings ***
Library           Selenium2Library


*** Test Cases ***
test01
    [Documentation]    登陆
    Open Browser    https://magicube.moredian.com/#/login    chrome
    Sleep    1
    Click Element    xpath=//*[@id="app"]/div[1]/div/div[2]/div[5]
#    Click Element    xpath=//*[@id="app"]/div[1]/div/div[2]/div[2]/div/span[@title = "账号不能为空"]
    Click Element    xpath=//*[@id="app"]/div[1]/div/div[2]/div[2]/div/span[text() = "账号不能为空"]

    Sleep    1
    Click Element    xpath=//*[@id="app"]/div[1]/div/div[2]/div[3]/div/div[2]/div/input
    Input Text    xpath=//*[@id="app"]/div[1]/div/div[2]/div[3]/div/div[2]/div/input    18368387155
    Click Element    xpath=//*[@placeholder="请输入登录密码"]
    Input Text    xpath=//*[@id="app"]/div[1]/div/div[2]/div[4]/div/div[2]/div/input    Md123456
    ${title_1}    Get Title
    Click Element    xpath=//*[@id="app"]/div[1]/div/div[2]/div[5]
    Sleep     2
    ${title_2}    Get Title
    Close browser
12313132132