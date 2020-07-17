*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${Browser}  Chrome
${Url}  Http://Amazon.Com
*** Test Cases ***
Login Test
	Open Browser  ${URL}  ${Browser}
	Input Text  xpath=//*[@id='twotabsearchtextbox']  Subbu
	Click Element  xpath=//input[@value='Go']
	Close Browser