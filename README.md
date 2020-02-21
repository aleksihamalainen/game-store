# Project plan
Team Members
Paavo Kaijala 608952
Aleksi Hämäläinen 655109
Markus Mantila 596815


## Features
The goal of this project is to implement a web store for JavaScript games. The project will include all the mandatory features (Authentication, player and developer -user functionalities, game/service-interaction), as well as RESTful API, mobile friendliness, social media sharing and, if we have time, 3rd party login. We aren’t planning on implementing any unlisted features.
For non-functional requirements we are planning to do the documentation, demo and project management as well as possible.


## Models and views
Authentication Users (players and developers) are able to login, logout and register to the service. We will use Django’s models to implement user authentication and email validation. Users, both players and developers, are defined with user objects. The primary attributes of the default user are username, password, email, first_name and last_name. Developers and players will have special attributes that will differentiate them from each. These attributes let developers to add games to their inventory and see list of the games and players to buy games, play games, see game high scores and record their score to it. Registration will happen by using create_user() function. Logging in will happen by using authenticate() and login() functions. Authenticate() will return None if the username-password pair is not correct. Logging out will happen simply by using logout() function.
### Player functionalities
Players will be able to purchase games using the course’s mockup payment system provided in https://tilkkutakki.cs.aalto.fi/payments/. The seller needs to get a secret key in order to use the service. The payment requests are made as HTTP POST requests to URL https://tilkkutakki.cs.aalto.fi/payments/pay. The user can either cancel or continue the payment and it will result to either success_url or cancel_url. The user should be able to get a game to his inventory and “money” would be transferred. Players should only be able to play games they have bought. The website will include a simple search functionality to search for games.
### Developer functionalities
Developers will be able to add games, set a price and remove or modify them. Games can be added by providing a URL to an HTML file and removed by removing that reference. Developers will only be able to add games to their own inventory, and add/remove their own games. This will be implemented by using primary keys which will add a developer attribute to a game. This attribute will be checked before any actions would be done. Developers should also have a basic game inventory and have access to sales statistics. This could be done for example by saving data to SQL tables.
### Game/service interaction
When a player presses submit score, the game sends a postMessage to the parent window containing the current score. This score will be recorded to the player’s scores and to the global high score list for that game. Communication will happen with window.postMessage and the message must contain “score” attribute. The score attribute will be compared with the player’s scores and the global high scores and only the best ones will be saved. Other messages to be implemented are save, load_request and setting from the game to the service and load and error from the service to the game. The messages will be in JSON format. Error messages will contain information about what went wrong.
### Quality of Work
We will maintain good quality of code, and use informative comments and commit messages. We will use “Don’t-Repeat-Yourself principle” and “Model-View-Template separation of concerns” as our frameworks.
### Mobile Friendliness
We will implement our online game store to be usable on computers and mobile devices. The important things in this implementation are taking into account the varying screen width and how the game store will work in touch based devices. We will use the bootstrap framework for styling.
### RESTful API
Users will be able to freely fetch open information about available games, highscores, etc. in JSON format. With authentication, developers and players will be able to fetch information about their game inventories. Developers will also be able to add, remove or modify games, as well as fetch information, eg. sales statistics.
### Working on project
During the project we will meet whenever necessary. Due to the small size of the team, we will not use any project management tools. For communication we will use Telegram.
## Models
We will use django.contrib.auth.models.Group models to categorize users and give different permissions to developers and players. The correct group would be chosen during registration. Game-models will include information about eg. developers of games, prices, etc. One way to implement the list of the games and game inventory is with models. The structure we could use in this are List Fields.


## Timetable
There will be 6 weeks of time for doing this project. The division of workload between the weeks will be approximately as presented below.
1. Planning how to start the project and familiarizing ourselves with the libraries we will use.
2. Implementing the basics of the website
3. Authentication, basic player functionalities
4. Basic developer functionalities, game/service interaction
5. Begin work on additional features
6. Continuing the additional features, security, finishing the project


# Final submission
https://blooming-falls-61222.herokuapp.com/


## Implemented Features
We have implemented all mandatory features and some extra features. Extra features are mobile friendliness, save/load and resolution. Everything we have done was not too hard.
### Authentication
We have done only minimum requirements so we would give 100 points. Email validation was too time consuming.
### Basic player functionalities
300 points, because every functionality was done properly.
### Basic developer functionalities
200 points, because every functionality was done properly.
### Game/service interaction
200 points, because every functionality was done properly.
### Quality of work
100 points, because every criterion was done properly.
### Save/load and resolution feature
100 points, no problems with this.
### Mobile Friendly
50 points, bootstrap was used.


## Dividing work
Paavo and Aleksi focused more on django and Markus more on HTML.


## Using application
First you register to the service as player or developer. Then everything is pretty self explanatory as there is the navbar with options to choose from. You can edit games from owned games in profile view. Buy games from browsing by clicking the game you want.

Example users on heroku:

(username - password)

testdev1 - jcKQrVCu

testdev2 - Y63UEXIeh

admin - xgLT0qqZ