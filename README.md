****# mum_foood_rest
 
![Logo](https://www.logolynx.com/images/logolynx/f8/f8ae7fb438b097af3292f88f44e922fc.png)
# Code Test Exercise

We value your time, so please only take an hour or two on this exercise. Do as much as you can, show us what you can do. 
It is supposed to be challenging and give us things to talk about in the next interview. Just try your best!

## Goal

`Mum Food` is fictional startup looking to provide the best recipes in the market.

The goal of this exercise is to expose recipes data with an API using Django Rest Framework.


## Guidelines

* You don't need to reinvent the wheel.
* Let us now how you did and what you found challenging or interesting in a THOUGHTS.md file.


## The task

We want to expose recipes data in the back-end to display the data in an possible frontend. Based on the user stories described below, please design your API to cover all the cases in the best possible manner.

### User stories

A registered user is just a user with an account in the system that has a token to make authenticated requests.

1. As an anonymous user I want to see a list of recipes, ordered by popularity (amount of likes).
1. As an anonymous user I want to be able to see if a recipe is good for vegans. Is understood that a recipe is good for vegans if all the ingrements are compatible for vegan people.
1. As an anonymous user I want to be able to filter the recipes by ingredients and if they are vegan or not.
1. As an anonymous user I want to be able to like a recipe.
1. As an anonymous user I can check a recipe to see the ingredients for it.
1. As a registered user I want to be able to create a ingrement.
1. As a registered user I want to be able to create a recipe.

## Next steps

Build a Docker image that we can pull and run easily to check the API.

When building the image, please make sure to include inside the .sqlite3 database that you have been using. With some data and a user with a token so we can see and create some data when running the image.

Next, upload it to Docker Hub, making sure that the source repository points to the git repository so we can check out also the code. Write down the token in the description along with indication of how to use it to make an authenticated request.****