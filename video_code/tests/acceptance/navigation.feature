Feature: test navigation between pages

Scenario: Homepage can go to blog
    Given: I am on the homepage
    When: I click on the link with id "blog-link"
    Then: I am on the blog page.

Scenario: Blog can go to homepage
    Given: I am on the blogpage
    When: I click on the link with id "home-link"
    Then: I am on the home page.