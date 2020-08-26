# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: West Nile Virus Prediction

**by: Anastasiya Ivanova, Bryan Ho, Roshan Khemlani, Junyuan Lin | SG-DSI-14**

## Introduction

The objective is to build a classification model to predict the presence of West Nile Virus.

## Problem Statement

To create a model to predict the presence of West Nile Virus(WNV) based on geospatial and weather information and identify the most important influencing features in Chicago, Illinois.

## Target Audience and Evaluation Metrics

This model is targeted at Chicago City health officials, as it will help them identify hotspots where carriers of the West Nile Virus may see a spike in populations, or even take preventive or preemptive actions to curb the growth of WNV carriers.



For this problem, we would prefer to have higher sensitivity/recall due to the negative impact of False Negatives. The main metric is the AUC ROC score.

 ## Conclusions and Recommendations

|   Approach | Private Kaggle Score | Public Kaggle Score |
| ---------: | -------------------: | ------------------: |
| Approach A |              0.57147 |             0.61725 |
| Approach B |              0.57810 |             0.60837 |
| Approach C |              0.65931 |             0.65337 |
| Approach D |              0.62076 |             0.61955 |

Based on the summary of the Kaggle results, Approach C performs the best overall in predicting the presence of West Nile Virus. It selected the Voting Classifier, consisting of a few models: K-Nearest Neighbours, AdaBoosted Decision Trees, Bagging Classifier, Random Forest Classifier and Gradient Boosting Classifier, to perform the prediction and has an excellent ROC AUC score of 0.955 on train data. Therefore, our team has selected this model to be the prediction model for our problem statement.

From this model, we were able to extract the more important features that predict the presence of West Nile Virus. They are, in order of importance:

```
1) Location (trap, block)
2) time (sunset, month)
3) weather (cool, avgspeed, tavg).
```

**Recommendations**

For our modeling, we found a few disparity between the train and test datasets. The train dataset has only 10506 entries, compared to the test dataset which has 116293 entries. It will be better for our modeling if we can acquire more data for the training dataset.

Based on our EDA, `nummosquito` information appears to be helpful for our prediction. However, we are unable to use it as the test dataset did not have the `nummosquito` information.

Finally, none of the traps in the test dataset is affected by spraying activity. This makes it difficult to ascertain the impact of spraying on predicting West Nile Virus.

In addition, we see that the location is a strong predictor. Additional geospatial information like human density or city zoning information may help us understand better why certain WNV carrying mosquitos species tend to breed at certain parts of the city and what might be contributing to the favorable environment.

Lastly, further study can be conducted on the methodology of spraying. Based on our EDA, the impact of spraying on mosquito population in the locality is inconclusive. Further studies on the frequency of spraying or how city workers perform the spraying, i.e. walking a circle around a block or a team approaching the block from multiple directions, can help improve the effectiveness of spraying and curb mosquito population, and by extension, West Nile Virus transmission during the summer months.

### File Navigation

---

```
Project_4_West_Nile_Virus_Suppression
|__ datasets
|   |__ train.csv
|   |__ test.csv
|   |__ weather.csv
|   |__ spray.csv
|   |__ mapdata_copyright_openstreetmap_contributors.rds
|   |__ noaa_weather_qclcd_documentation.pdf
|   |__ df_train_bydate_trap.csv
|   |__ main_df.csv
|   |__ main_df_test.csv
|   |__ submission_a.csv
|   |__ submission_b.csv
|   |__ submission_c1.csv
|   |__ submission_c2.csv
|   |__ submission_d1.csv
|   |__ submission_d2.csv
|   |__ submission_d3.csv
|__ code
|   |__ Project_4_West_Nile_Virus_Prediction.ipynb
|   |__ myfunctions.py
|__ README.md
```

### Data Dictionary

| Feature                    | Type       | Dataset | Description                                                  |
| -------------------------- | ---------- | ------- | ------------------------------------------------------------ |
| **station**                | *int*      | main_df | Station 1: CHICAGO O'HARE INTERNATIONAL AIRPORT (AWOS)       |
| **date**                   | *datetime* | main_df | Date Period of Weather Data (YYYY-MM-DD)                     |
| **tmax**                   | *float*    | main_df | Maximum Daily Temperature (Degrees Celsius)                  |
| **tmin**                   | *float*    | main_df | Minimum Daily Temperature (Degrees Celsius)                  |
| **tavg**                   | *float*    | main_df | Average Daily Temperature (Degrees Celsius)                  |
| **depart**                 | *float*    | main_df | Daily Departure From Normal (Degrees Celsius)                |
| **dewpoint**               | *float*    | main_df | Average Daily Dew Point (Degrees Celsius)                    |
| **wetbulb**                | *float*    | main_df | Average Daily Wetbulb (Degrees Celsius)                      |
| **humidity**               | *float*    | main_df | Average Daily Humidity (Degrees Celsius)                     |
| **heat**                   | *float*    | main_df | Daily Heating (Season Begins In July)                        |
| **cool**                   | *float*    | main_df | Daily Cooling (Season Begins In January)                     |
| **sunrise**                | *float*    | main_df | Daily Sunrise Time (HHMM)                                    |
| **sunset**                 | *float*    | main_df | Daily Sunset Time (HHMM)                                     |
| **codesum**                | *object*   | main_df | Significant Weather Types/Phenomena                          |
| **depth**                  | *int*      | main_df | Measurement of Snow/Ice On Ground(Inches)                    |
| **snowfall**               | *float*    | main_df | Measurement of Snowfall (Inches and Tenths)                  |
| **preciptotal**            | *float*    | main_df | Daily Precipitation (Inches)                                 |
| **stnpressure**            | *float*    | main_df | Average Daily Station Pressure (Inches HG)                   |
| **sealevel**               | *float*    | main_df | Average Daily Sea Level Pressure (Inches HG)                 |
| **resultspeed**            | *float*    | main_df | Daily Resultant Wind Speed (MPH)                             |
| **resultdir**              | *int*      | main_df | Daily Resultant Direction (Whole Degrees)                    |
| **avgspeed**               | *float*    | main_df | Average Daily Resultant Wind Speed (MPH)                     |
| **day**                    | *int*      | main_df | Date Period of Weather Data (Day)                            |
| **month**                  | *int*      | main_df | Date Period of Weather Data (Month)                          |
| **year**                   | *int*      | main_df | Date Period of Weather Data (Year)                           |
| **address**                | *object*   | main_df | Full Address of the Trap (Location)                          |
| **species**                | *object*   | main_df | Species of Mosquitos in the Trap (7 Types)                   |
| **block**                  | *int*      | main_df | Block of the Neighbhorhood (Location)                        |
| **street**                 | *object*   | main_df | Street of the Trap (Location)                                |
| **trap**                   | *int*      | main_df | Apparatus Designed to Catch Mosquitos (Location)             |
| **addressnumberandstreet** | *object*   | main_df | Full Address of the Trap (Location)                          |
| **latitude**               | *float*    | main_df | Geographic Coordinate that Specifies North or South Position (Location) |
| **longitude**              | *float*    | main_df | Geographic Coordinate that Specifies East or West Position (Location) |
| **addressaccuracy**        | *int*      | main_df | Accuracy of Address to Logitude and Latitude (Location)      |
| **nummosquitos**           | *int*      | main_df | Number of Mosquitos Caught in the Trap                       |
| **wnvpresent**             | *int*      | Weather | One or More Mosquitos in the Trap has West Nile Virus        |
| **iswnvspecies**           | *int*      | Weather | Type of Mosquitos tha Carry West Nile Virus                  |
| **is_spray**               | *bool*     | Weather | Location that has been Sprayed                               |



