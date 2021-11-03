Feature: test navigation between pages

Scenario: Homepage can go to blog
    Given: I am on the homepage
    When: I click on the "Go to Blog' link"
    Then: I am on the blog page.

Scenario: Blog can go to homepage
    Given: I am on the blogpage
    When: I click on the "Go to Blog' link"
    Then: I am on the home page.