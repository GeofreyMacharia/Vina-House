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
## Testing amd Discusion 
- For accurate results, the new test data (not split training or test data) was preprocessed inaccordance to the data used for training the moded, i.e, log transforming certain features and ultimatly transforming the data using standard scaler.
- While the model performance of xgb-regressor and random forest were good(based on r2_score and mean squared error) they each peformed differently when it came to testing them to completely new data.
- Xgb-regressor's home price result was slightly lower than that of random forest, however this occurance could be used to our advantage. How so? - As a range.
- The price of a house fluctuates on a number of factors as such having a range price enables the future customer to purchase a house given his budget range.
- Xgb-result will be the lower limit price while the result of random-forest will be the upper limit house price.

## Improvements
  - In-depth Hyperparameter tuning to attain best results
  - Trainng other models with the data for better results. eg, neural networks, naive bayes.
## Explore Notebook  
![alt text](https://github.com/GeofreyMacharia/vina-house-model-codebase/blob/main/House_Sales.ipynb)
# Deployment
The web application is already deployed using render. To access it click the link below:
https://vina-homes.onrender.com

### Disclaimer.
The deployed website is slow, as i am using the free version. For better usage kindly load it up on local machine.


The requirements for its functionality are given on "requirement.txt" file. Inaddition kindly use python version 3.11.3, as the predicting models were created using that version.
