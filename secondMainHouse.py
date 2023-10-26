import streamlit as st
st.set_page_config(
        page_title="Vina Homes",
        page_icon="house",
        layout="centered",
    )
from PIL import Image
import joblib as jb
import xgboost as xgb
import numpy as np
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')
from streamlit_modal import Modal
from streamlit_option_menu import option_menu

# -------------------------------------------------FRONT END UI-------------------------------------------------------------------------------------------
st.markdown("<h1 style='text-align: center;'>VINA HOMES</h1>", unsafe_allow_html=True)
# Horizontal Menu
selected = option_menu(
    menu_title="",
    options=['Guide', 'House Details','Prediction'],
    icons=['house','book','clock'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)

if selected=='Prediction':
    st.markdown("[Prediction](#prediction)")
if selected == 'House Details':
    st.markdown("[House Details](#house-details)")

main = st.container()
with main:
    img_main = Image.open('images//Home.png')
    st.image(img_main)
#Heading
st.markdown("<h1 style='text-align: center; text-decoration: underline; margin-top: -2.5%;'>Guide</h1>", unsafe_allow_html=True)


# Personal Guide

con_1 = st.container()
con_2 = st.container()
con_3 = st.container()
con_4 = st.container()
con_5 = st.container()
con_6 = st.container()
con_7 = st.container()

with con_1:
    st.write('**Step 1:**')
    st.write('Click on the arrow key on the top-left side of the screen, to access sidebar.')
    img_1 = Image.open('images//Demo_click.png')
    st.image(img_1)
    st.markdown('---')

with con_2:
    st.write('**Step 2**')
    st.write('Select Values of the house you desire')
    img_column_1, img_column_2 = st.columns(2)
    with img_column_1:
        sample_1 = Image.open('images//input_sample1.png')
        st.image(sample_1)
    with img_column_2:
        st.write(' ')
        sample_2 = Image.open('images//input_sample2.png')
        st.image(sample_2)
    st.markdown('---')
with con_3:
    st.write('**Step 3:**')
    st.write('With your values selected, click the "Submit" button at the bottom of the side bar.')
    submit_col, submitted_col = st.columns(2)
    with submit_col:
        sample_3 = Image.open('images//submit.png') 
        st.image(sample_3)
    with submitted_col:
        sample_4 = Image.open('images//submitted.png') 
        st.image(sample_4)
    st.markdown('---')
with con_4:
    st.write('**Step 4:**')
    st.write('Click the "predict house price" button located at the bottom of the page to get two price ranges of your house.')
    sample_5 = Image.open('images//pred.png')
    st.image(sample_5)
    st.markdown('---')
with con_5:
    st.markdown("<h2 style='text-align: center; text-decoration: underline; margin-top: -1%;'>House Details</h1>", unsafe_allow_html=True)

with con_6:
    st.write('**Bedroom:**')
    st.write('* The value reflects the total number of bedrooms located in each individual house property.')
    st.write('**Bathroom:**')
    st.write('* The value reflects the total number of bathrooms present in the individual house.')
    st.write('**Floors:**')
    st.write('* The value reflects the corresponding number of floors within the storey based house.')
    st.write('**Water Front:**')
    st.write('* The value reflects the total number of waterbodies that surround the house area.')
    st.write('**View:**')
    st.write('* The value reflects the number of times the house has been viewed for the purpose of selling it.')
    st.write('**Condition:**')
    st.write('* The value reflects the categorical physical condition of the house.')
    st.write('* *0: awful , 1: bad , 2: Good , 3: Great , 4: Perfect , 5: Luxury*')

with con_7:
    st.write('**Grade:**')
    st.write('''* Additional Information regarding water and homes,
     it is recommended to choose between 6-9, with 7 being the most chosen value.''')
    st.write('**Sqft Living Area:**')
    st.write('''* The value reflects the square foot size of the house living area. The living area can include
     the living room, dining room, foyer, recreation or family room and special-purpose rooms such as a sunroom or home office.''')
    st.write('**Sqft Lot Area:**')
    st.write('* The value reflects the sqft size of the area with which the house is built on.')
    st.write('**Sqft Above:**')
    st.write('* The Value reflects all living square feet in a home that is above the ground.The house built inturn will have a floor.')
    st.write('**Sqft Basement:**')
    st.write('* The value reflects the square foot size of the basement area.')
    st.write('**Year Built:**')
    st.write('* The value reflects the year with which the house was constructed.')
    st.write('**Year Renovated:**')
    st.write('* The value reflects the year when the house underwent any significant renovations ot capital expenditures.')
    st.markdown('---')





# -------------------------------------------------------FUNCTIONS FOR USER INFO RETRIEVAL------------------------------------------------------------------------------------


# function to get all user info from sliders
def bedroom_value():
    if 'bedroom' not in st.session_state:
        default_1 = st.session_state['bedroom']= 2.0
        return default_1
    else:
        return st.session_state.bedroom



def bathroom_value():
    if 'bathroom' not in st.session_state:
        default_2 = st.session_state['bathroom']= 1.0
        return default_2
    else:
        return st.session_state.bathroom



def sqft_living_value():
    if 'sqft_living' not in st.session_state:
        default_3 = st.session_state['sqft_living']= 2800
        return default_3
    else:
        return st.session_state.sqft_living



def sqft_lot_value():
    if 'sqft_lot' not in st.session_state:
        default_4 = st.session_state['sqft_lot']= 3500
        return default_4
    else:
        return st.session_state.sqft_lot


def floors_value():
    if 'floors' not in st.session_state:
        default_5 = st.session_state['floors']= 1.0
        return default_5
    else:
        return st.session_state.floors


def waterfront_value():
    if 'water_front' not in st.session_state:
        default_6 = st.session_state['waterfront']= 0
        return default_6
    else:
        return st.session_state.waterfront


def view_value():
    if 'view' not in st.session_state:
        default_7 = st.session_state['view']= 0
        return default_7
    else:
        return st.session_state.view



def condition_value():
    if 'condition' not in st.session_state:
        default_8 = st.session_state['condition']= 3
        return default_8
    else:
        return st.session_state.condition



def room_grade_value():
    if 'room_grade' not in st.session_state:
        default_9 = st.session_state['room_grade']= 7
        return default_9
    else:
        return st.session_state.room_grade



def sqft_above_value():
    if 'sqft_above' not in st.session_state:
        default_10 = st.session_state['sqft_above']= 2800
        return default_10
    else:
        return st.session_state.sqft_above


def sqft_bass_value():
    if 'sqft_bass' not in st.session_state:
        default_11 = st.session_state['sqft_bass']= 0
        return default_11
    else:
        return st.session_state.sqft_bass

def yr_built_value():
    if 'yr_built' not in st.session_state:
        default_12 = st.session_state['yr_built']= 2010
        return default_12
    else:
        return st.session_state.yr_built



def yr_renov_value():
    if 'yr_renov' not in st.session_state:
        default_13 = st.session_state['yr_renov']= 0
        return default_13
    else:
        return st.session_state.yr_renov

#-----------------------------------------------------MODELLING AND PREDICTING------------------------------------------------------------------

# get user info
bedroom_val = bedroom_value()
bathoom_val = bathroom_value()
sqft_living_val = sqft_living_value()
sqft_loft_val = sqft_lot_value()
floors_val = floors_value()
waterfront_val = waterfront_value()
view_val = view_value()
condition_val = condition_value()
room_val = room_grade_value()
sqft_above_val = sqft_above_value()
sqft_bass_val = sqft_bass_value()
yr_built_val = yr_built_value()
yr_renov_val = yr_renov_value()

# button function
def retrieve_info():
    user_data = []
    # append all user info to single list
    user_data.append(bedroom_val)
    user_data.extend([bathoom_val,sqft_living_val,sqft_loft_val,floors_val,waterfront_val,view_val,condition_val,
                    room_val, sqft_above_val,sqft_bass_val,yr_built_val,yr_renov_val,47.5,-122.35])
    
    return user_data
inpt_data = retrieve_info()


# load scaler 
Sc = 'Sc.sav'
scaler = jb.load(Sc)
def isit_new():
    input_data_scaled = scaler.transform([inpt_data])
    #    load models
    XGBPRED_House_sales = 'XGBPRED_House_sales.sav'
    RF_Regressor = 'RF_REGRESSOR_House_sales.sav'

    # Rf and Xgb models
    RF_model = jb.load(RF_Regressor)
    XGB_model = jb.load(XGBPRED_House_sales)

    #  Random Forest regressor model
    rf_pred = RF_model.predict(input_data_scaled)
    rf_result = int(np.exp(rf_pred))

    # Adding comma to results
    comma_rf = ('{:,}'.format(rf_result))
    # print("Low Price Range: " + str(comma_rf))

    # xgb regressor model
    xgb_pred = XGB_model.predict(input_data_scaled)
    xgb_result = int(np.exp(xgb_pred))

    # Adding comma to results
    comma_xgb = ('{:,}'.format(xgb_result))
    # print("High Price Range: " + str(comma_xgb))


    return comma_rf, comma_xgb

rf_ans, xgb_ans = isit_new()
# -------------------------------------------------------SIDE BAR--------------------------------------------------------------------------------------------------------

# side bar
st.sidebar.markdown("<h1 style='text-align: center; text-decoration: underline; margin-top:-20%;'>House Inputs</h1>", unsafe_allow_html=True)
# add elementd in side bar
with st.sidebar:
    # bedroom slider
    st.slider("Bedroom",min_value=1.0, max_value=7.0, step=0.5,key="bedroom",on_change=bedroom_value)
    # bathroom slider
    st.slider('Bathroom',min_value=0.0, max_value=5.0, step=.5,key='bathroom',on_change=bathroom_value)
    # floors
    st.slider('Floors',min_value=0.0, max_value=5.0, step=.5,key='floors',on_change=floors_value)
    # water front
    st.selectbox('WaterFront', (0,1,2,3,4,5),key='water_front',on_change=waterfront_value)
    # view
    st.selectbox('Views',(0,1,2,3,4,5),key='view',on_change=view_value)
    # condition
    st.selectbox('Condition',(0,1,2,3,4,5),key='condition',on_change=condition_value)
    # grade
    st.slider('Grade',min_value=1,max_value=10,step=1,key='room_grade',on_change=room_grade_value)
    # sqft living area
    st.number_input('Sqft Living area',value=2000, min_value=100, max_value=10000,step=10, key='sqft_living',on_change=sqft_living_value)
    # Sqft lot area
    st.number_input('Sqft Lot area', value=3000, min_value=300, max_value=10000, step=10,key='sqft_lot',on_change=sqft_lot_value)
    # sqft above
    st.number_input('Sqft Above', value=3000, min_value=100, max_value=10000, step = 10,key='sqft_above',on_change=sqft_above_value)
    # sqft basement
    st.number_input('Sqft Basement', value=0, min_value=0, max_value=1000, step=10,key='sqft_bass',on_change=sqft_bass_value)
    # Year Built
    st.number_input('Year Built', value=1990, min_value=1800,max_value=2020,step=1,key='yr_built' ,on_change=yr_built_value)
    # year renovated
    st.number_input('Year Renovated',value=0,min_value=0, max_value=2020,step =1,help ='0 if not renovated',key='yr_renov',on_change=yr_renov_value)
    # buttons
    submit_col, predict_col = st.columns(2)
    with submit_col:
        data_acquired = st.button('Submit',on_click=retrieve_info,key='2')
    with predict_col:
        if data_acquired:
            st.markdown(f'''
            <div style="height: 5.5vh; width:100%; background-color: #0E1117; color: #FF2C2C; border-radius: 10px;
                text-align: center; font-size:18px;  padding-top:.5vh;  text-shadow: 2px 2px 10px #FF2C2C;"> <b>Data Submitted.</b>
            </div>
            ''',unsafe_allow_html=True)


# confirmation container

st.markdown("<h2 style='text-align: center; text-decoration: underline; margin-top: -1%;'>Prediction</h1>", unsafe_allow_html=True)
confirm_contain = st.container()
with confirm_contain:
    btn_result = st.button('**Predict House Price**',on_click=isit_new) 
    if btn_result:
        st.markdown(f'''
                <div style=" height: 10vh; width:100%; background-color: #262730; color: #FF2C2C; border-radius: 10px;
                text-align: center; font-bold:450;  font-size:20px; padding-top:2.5vh;">
                The Price of Your House ranges between: {rf_ans} and {xgb_ans} $
                </div>''', unsafe_allow_html=True)
    
st.markdown('---')
st.write('**Disclaimer:** This application has been trained and modelled using data collected in 2015 from a specific county of the United States as such the results may not be accurate for other parts of the world.')

