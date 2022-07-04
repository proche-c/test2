Feature: Learning how to work with scenario outlines

    Scenario Outline: Login to intra.42 with valid parameters
        Given I launch Chrome browser
        When I open the intra.42 homepage
        And I enter username "proche-c" and I pass a valid password ""
        And click on login button
        And I type in the nickname of a student: "<username>" on the search button
        And I press enter
        Then I will see the profile picture: "<picture>"

    Examples:
    |   username   |        picture                                |
    |   dnunez-m   |    /html/body/div[4]/div[2]/div/div[2]/div/a  |
    |   cayferna   |    /html/body/div[4]/div[2]/div/div[1]/div/a  |    
    |   mogonzal   |    /html/body/div[4]/div[2]/div/div[2]/div/a  |