# <insert cool project name here>
AI Project Submission for Bootcamp 2 - MSA 2021

## IDEA
### What is the problem?
It is difficult for game producers to make a prediction on the number of people that will be playing their game once it is released, which is an indicator of the success of the game. It is particularly more of an issue for multiplayer games, which necessitate the hosting of dedicated server which may not be easily provisioned. To address this problem, a machine learning solution that can predict the number of concurrent players for a game can be created.

### Why is AI helpful for this?
There is a large amount of data on the performance of past released games, which can be leveraged by AI and the computing power of the cloud to predict the number of players for a game based on known information such as the title, the genre, the publisher etc.

## APPROACH
### What does the ML model look like?
3 Kaggle datasets on past and current games on Steam, one of the largest digital game distributors, have been used to generate a dataset to train the model. The features used in the model include the title of the game (how common it is based on its words), the developer and publisher (how many games they have been involved with in the past), the tags and genres of the games (how common they are), whether the game is multiplayer and the number of platforms that the game supports. The model will use a regression model to predict the average number of concurrent players in a month for the game.

### What does the setup look like (ideally)?
* 1 ML model deployed to an endpoint
* 1 deployed flask web app that uses the endpoint

### What about the machine learning cycle?
* Planning: problem and solution identification
* Data: data sourcing, data processing, feature identification
* Model: model training, model evaluation and selection, model deployment
* Production: (initially planned to log user feedback about prediction but ran out of time)

### How to go further?
* Allow user to log feedback about prediction
* Periodic retraining of models with new data (statically sourced for now, but can be scraped from Steam API directly)

## IMPLEMENTATION
### What has been done?
* Processed the data and created the final aggregated dataset
* Created and evaluated a regression model with okay result (R2 value close to 0)
* Model is deployed as an endpoint on Azure
* Webapp that uses the endpoint is created, working on deployment

### Anything else to note?
Data sources:
* https://www.kaggle.com/michau96/popularity-of-games-on-steam
* https://www.kaggle.com/trolukovich/steam-games-complete-dataset
* https://www.kaggle.com/jesneuman/pc-games