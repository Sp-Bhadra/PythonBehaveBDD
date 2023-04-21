Feature: OrangeHRM Logo
  Scenario: Logo presence on orangeHRM home page
    Given launch chrome browser
    When open orangeHRM homepage
    Then verify logo present on orangeHRM homepage
    And close browser