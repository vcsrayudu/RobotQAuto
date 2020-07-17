*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${Browser}  Chrome
${Url}  Http://Amazon.Com
*** Test Cases ***
Login With Valid User And Password
	Open Browser  ${URL}  ${Browser}
	Input Text  xpath=User  Subbu
	Input Text  xpath=Password  Password
	Click Element  xpath=Login
	Close Browser
Login With Invalid User And Valid Password
	Open Browser  ${URL}  ${Browser}
	Input Text  xpath=User  Invalid
	Input Text  xpath=Password  Password
	Click Element  xpath=Login
	Close Browser
Login With Valid User And Invalid Password
	Open Browser  ${URL}  ${Browser}
	Input Text  xpath=User  Valid
	Input Text  xpath=Password  Invalid
	Click Element  xpath=Login
	Close Browser
Login With Invalid User And Invalid Password
	Open Browser  ${URL}  ${Browser}
	Input Text  xpath=User  Invalid
	Input Text  xpath=Password  Invalid
	Click Element  xpath=Login
	Close Browser