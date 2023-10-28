# Vina-Homes.
![alt text](https://github.com/GeofreyMacharia/Vina-House/blob/main/images/Home.png)
## Objective:Create ML algorithims to predicting house prices based on train/test house data as well as new data.
## Data Sauce
https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
## Technology Used
- Python(Language written in)
- Streamlit(Deplyoment API)
- sckit(Library module used)
## Methods
- Exploratory Data Analysis(Log transformations, visualizations)
- Data Preprocessing(Outlier removal)
- Predictive modeling(ML Algorithms)
- Testing
- Deployment(Streamlit API and Render.com as host)
## Result Preview
Correlation heatmap

![alt text](https://github.com/GeofreyMacharia/Vina-House/blob/main/images/heatmap.png)

Outlier Removal Boxplot
![alt text](https://github.com/GeofreyMacharia/Vina-House/blob/main/images/outliers.png)

Feature Importance

![alt text](https://github.com/GeofreyMacharia/Vina-House/blob/main/images/featurs.png)

Model performance

![alt text](https://github.com/GeofreyMacharia/Vina-House/blob/main/images/result.png)
## Testing and Discussion 
- For accurate results, the new test data (not split training or test data) was preprocessed inaccordance to the data used for training the moded, i.e, log transforming certain features and ultimatly transforming the data using standard scaler.
- While the model performance of xgb-regressor and random forest were good(based on r2_score and mean squared error) they each peformed differently when it came to testing them to completely new data.
- Xgb-regressor's home price result was slightly lower than that of random forest, however this occurance could be used to our advantage. How so? - As a range.
- The price of a house fluctuates on a number of factors as such having a range price enables the future customer to purchase a house given his budget range.
- Xgb-result will be the lower limit price while the result of random-forest will be the upper limit house price.

## Improvements
  - In-depth Hyperparameter tuning to attain best results
  - Trainng other models with the data for better results. eg, neural networks, naive bayes.
## Explore Notebook  
![Click here for notebook](https://github.com/GeofreyMacharia/vina-house-model-codebase/blob/main/House_Sales.ipynb)

## Project Showcase
https://github.com/GeofreyMacharia/Vina-House/assets/120192941/940a93eb-b765-44ec-9aaa-fd81a21bb7cd

## Deployment - Internet
The web application is already deployed using render. 
Kindly note the site is slow and the memory provided for free hosting is not enough to allow full functionality of the program.
To access it click the link below:
https://vina-homes.onrender.com
## Deployment - Locally
- Make sure all packages written in requirements.txt are downloaded, in addition make sur to use python 3.11.3
- Open your IDE's terminal
- Type "Streamlit run main_house.py"
- Enjoy
## Regards.
- Geofrey Macharia
![have a cookiee](https://github.com/GeofreyMacharia/Vina-House/assets/120192941/f03b5401-4f62-4b32-9f21-b408a99b323c)

