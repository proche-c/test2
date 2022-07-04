Feature: Learning how to work with scenario outlines

    Background: common steps
        Given I launch Chrome browser
        When I open the intra.42 homepage
        And I enter username "proche-c" and I pass a valid password ""
        And click on login button
    
    Scenario Outline: See user profile picture
        And I type in the nickname of a student: "<username>" on the search button
        And I press enter
        Then I will see the profile picture: "<picture>"

    Examples:
    |   username   |        picture                                |
    |   dnunez-m   |    /html/body/div[4]/div[2]/div/div[2]/div/a  |
    |   cayferna   |    /html/body/div[4]/div[2]/div/div[2]/div/a  |    
    |   mogonzal   |    /html/body/div[4]/div[2]/div/div[2]/div/a  |


    Scenario Outline: See the menu 
        And I click on the icon "<menu_element>"
        Then I will see that "<menu_page>"
        And the title will be "<title>"

    Examples:
    |   menu_element       |        menu_page                   |   title                   |
    |   icon-user-2        |    https://profile.intra.42.fr/     |   Intra Profile Home      |
    |   icon-network-2-1   |    https://projects.intra.42.fr/    |   Intra Projects Home     |
    |   icon-movie-play-1  |    https://elearning.intra.42.fr/   |   Intra Elearning Home    |