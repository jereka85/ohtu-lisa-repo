*** Settings ***
Resource  resource.robot
#Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Input Login Command
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Login Command
    Run Keyword And Expect Error  *User with username kalle already exists*  Create User  kalle  moimoimoimoi1

Register With Too Short Username And Valid Password
    Run Keyword And Expect Error  *Username incorrect. There should be at least 3 char.*  Create User  fu  kalle123

Register With Enough Long But Invalid Username And Valid Password
    Run Keyword And Expect Error  *Username incorrect. There should be at least 3 char.*  Create User  2828177##¤  kalle123

Register With Valid Username And Too Short Password
    Run Keyword And Expect Error  *Too weak password! There should be at least 8 char and 1 special char.*  Create User  kalle  hj24

Register With Valid Username And Long Enough Password Containing Only Letters
    Run Keyword And Expect Error  *Too weak password! There should be at least 8 char and 1 special char.*  Create User  kalle  moikkamoionhyvasalasana
