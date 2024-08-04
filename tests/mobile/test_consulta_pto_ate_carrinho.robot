# This sample code supports Appium Robot client >=2
# pip install robotframework-appiumlibrary
# Then you can paste this into a file and simply run with Robot
#
# Find keywords at: http://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html
#
# If your tests fails saying 'did not match any elements' consider using 'wait activity' or
# 'wait until page contains element' before a click command

*** Settings ***
Library           AppiumLibrary
Test Teardown     Close Application

*** Variables ***
${SAUCE_USERNAME}    karklose  
${REMOTE_URL}    https://${SAUCE_USERNAME}:5c1fd24c-1340-40fb-92b7-9915dd2fdc98@ondemand.us-west-1.saucelabs.com:443/wd/hub


*** Test Cases ***
Test Case Name
    Open Application    http://ondemand.us-west-1.saucelabs.com:80/wd/hub    
    ...    platformName=Android    appium:platformVersion=9.0    
    ...    appium:deviceName=Samsung Galaxy S9 FHD GoogleAPI Emulator    
    ...    appium:deviceOrientation=portrait    
    ...    appium:app=storage:filename=Giuliana Flores_2.0.56_APKPure.apk    
    ...    appium:appPackage=br.com.giulianaflores.android    
    ...    appium:appActivity=br.com.giulianaflores.android.MainActivity    
    ...    browserName=undefined    
    ...    appium:ensureWebviewsHavePages=${True}    
    ...    appium:nativeWebScreenshot=${True}    
    ...    sauce:options=[object Object]    
    ...    appium:newCommandTimeout=${3600}    
    ...    appium:connectHardwareKeyboard=${True}
    
    Swipe    ${568}    ${504}    ${378}    ${1442}
    ${el1} =    Set Variable     xpath=//android.widget.TextView[@text="Pular"]
    Click Element    ${el1}
    ${el2} =    Set Variable     accessibility_id=Entrar
    Click Element    ${el2}
    ${el3} =    Set Variable     xpath=//android.widget.EditText[@text="   Digite seu e-mail ou CPF"]
    Input Text    ${el3}    amanda_dacosta@structureesquadrias.com.br
    ${el4} =    Set Variable     xpath=//android.widget.EditText[@text="Digite sua senha"]
    Input Text    ${el4}    Choco@2024
    ${el5} =    Set Variable     accessibility_id=Entrar
    Click Element    ${el5}
    Swipe    ${576}    ${351}    ${488}    ${1141}
    ${el6} =    Set Variable     xpath=//android.widget.TextView[@text="NÃO, OBRIGADO"]
    Click Element    ${el6}
    @{finger} =    Create List    ${88}    ${1213}
    @{positions} =    Create List    ${finger}
    Tap With Positions    ${100}    ${positions}
    ${el7} =    Set Variable     xpath=//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]
    Click Element    ${el7}
    ${el8} =    Set Variable     xpath=//android.widget.TextView[@text=""]
    Click Element    ${el8}
    ${el9} =    Set Variable     xpath=//android.widget.TextView[@text="Cestas"]
    Click Element    ${el9}
    ${el10} =    Set Variable     xpath=//android.widget.TextView[@text="Cestas Românticas"]
    Click Element    ${el10}
    ${el11} =    Set Variable     xpath=//android.widget.TextView[@text="Cesta Café Com Pelúcia"]
    Click Element    ${el11}
    ${el12} =    Set Variable     xpath=(//android.widget.TextView[@text="Cesta Café Com Pelúcia"])[2]
    Click Element    ${el12}
    ${el13} =    Set Variable     xpath=//android.widget.TextView[@text=" R$ 299,90"]
    Click Element    ${el13}
    ${el14} =    Set Variable     xpath=//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup
    Click Element    ${el14}
    ${el15} =    Set Variable     xpath=//android.widget.TextView[@text="30"]
    Click Element    ${el15}
    ${el16} =    Set Variable     xpath=//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup
    Click Element    ${el16}
    Swipe    ${626}    ${423}    ${572}    ${942}
    ${el17} =    Set Variable     xpath=//android.widget.TextView[@text="Sacola de Compras"]
    Click Element    ${el17}
    ${el18} =    Set Variable     xpath=//android.widget.TextView[@text="Cesta Café Com Pelúcia"]
    Click Element    ${el18}
    ${el19} =    Set Variable     xpath=(//android.widget.TextView[@text="R$ 299,90"])[1]
    Click Element    ${el19}
