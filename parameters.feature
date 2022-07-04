Feature: Learning how to pass parameters

    Scenario: Login to intra.42 with valid parameters
        Given I launch Chrome browser
        When I open the intra.42 homepage
        And I enter username "proche-c" and I pass a valid password ""
        And click on login button
        Then The user will see the profile page "https://profile.intra.42.fr/"
        And will see the profile picture
