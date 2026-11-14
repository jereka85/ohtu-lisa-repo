*** Settings ***
Resource  resource.robot

*** Test Cases ***
Reset Counter After One Incerment
    Counter Value Should Be  0
    Increase Counter
    Counter Value Should Be  1
    Increase Counter
    Counter Value Should Be  2

Reset Counter After Several Incerments
    Counter Value Should Be  0
    Increment Counter By  5
    Counter Value Should Be  5
    Reset Counter
    Counter Value Should Be  0
