Feature: Design and Build a Ruby on Rails web app using Behaviour Driven Development (BDD)
In order to reduce rework and produce a web app at low cost and high speed
A developer 
Should employ a BDD methodology and agile tools

Scenario: Cucumber should be installed and configured
  Given I have installed the gem named "rails"
  When I run "rails g cucumber"
  Then I should create the directory features
