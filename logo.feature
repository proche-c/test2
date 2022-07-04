Feature: Logo intra.42.fr

Scenario: Logo presence on intra.42.fr home page
    Given we launch chrome browser
    When we open intra.42.fr homepage
    Then verify that the logo is present onthe page
    And close browser