# Created by ferro at 18/11/2022
Feature: Search Stories
  Search at least five Stories

  Scenario:Search at least five stories
    Given the search stories begins
    When the search returns status should be 200
    Then returns five records
    Then returns records titles