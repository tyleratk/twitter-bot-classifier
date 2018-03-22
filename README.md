# Twitter Bot Classifier

This is a small project to expand the work I did on [Twitter Sentiment](https://github.com/tyleratk/twitter-sentiment). In the src folder, you will find a model.py that creates a Random Forest Classifier to predict if a Twitter user is a bot or not. Doing a test train split on the data will give you ~90% accuracy with this model. You will also find a get_user.py that will ask for a Twitter user handle and predict whether or not they are a bot along with the probability.

## Examples

| User Handle         | Output     |
| :-----------------: | :--------: |
| @RealDonaldTrump    | 100.0% chance that @realdonaldtrump is not a bot   |
| @dog_rates          | 97.0% chance that @dog_rates is not a bot          |
| @dogrates           | 72.0% chance that @dogrates is a bot!              |
| @kanyejordan        | 97.0% chance that @kanyejordan is a bot!           |