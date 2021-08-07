## FINDINGS
### Data analysis
There were not many missing data but the data on number of players for a released game (prediction target) is relatively small (1.2k) compared to general data on released games (40k). This caused the final dataset to be relatively small which might have reduced the prediction accurary of the model due to the small pool of games with player number data. Data on number of players were taken from a dataset on the popularity of games, which may suggest bias towards games with high popularity (very well known with high media coverage). This means the model may not perform so well against games without such factors.

### Model selection & performance
Due to time constraints, only the Linear Regression model was attempted. It achieved a R2 score of 0.00017 which is sufficient to be used (the closer it is to 0, the more accurate the model is).

## CONCLUSION
There were plans to attempt different models with the dataset, compare results and select the best model from a list of criteria. Due to constraints, this was not accomplished within the duration of the bootcamp but it is planned for further research and experimentation. A deeper analysis of feature significance would also be a good area for additional study, in order to further understand the impact of varying factors on the performance of a released games.
