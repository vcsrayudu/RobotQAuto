*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${Browser}  Chrome
${URL}  http://amazon.com

*** Test Cases ***
Search Test1
   Open Browser  ${URL}  ${Browser}
   Input Text  xpath=//*[@id='twotabsearchtextbox']  subbu
   Click Element  xpath=//input[@value='Go']
   #Click Element
   Close Browser
Search Test2
   Open Browser  ${URL}  ${Browser}
   Input Text  xpath=//*[@id='twotabsearchtextbox']  subbu
   Click Element  xpath=//input[@value='Go']
   #Click Element
   Close Browser