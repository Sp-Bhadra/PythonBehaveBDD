Feature: OrangeHRM Login
  Scenario: login to orange hrm with valid parameters
    Given I launch chrome browser
    When I open orangeHRM homepage
    And I enter username "Admin" and password "admin123"
    And I clicked on submit button
    Then then user must successfully logged into dashboard page
