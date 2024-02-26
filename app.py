import streamlit as st
import pandas as pd 
import pickle

# Set wide layout
st.set_page_config(layout="wide")

# Load data
df = pd.read_json('df.json')
with open("ct.pkl", 'rb') as f:
    ct = pickle.load(f)
with open("cbr.pkl", 'rb') as f:
    cbr = pickle.load(f)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

        .title {
            font-family: 'Lobster', cursive;
            font-size: 65px;
            font-weight: 400; /* Set font weight to normal */
            color: #FFFFFF; /* Set color to white */
            text-align: center;
            margin-top: -50px;
        }
    </style>
    <h1 class="title">CarDekho Resale Car Price Prediction</h1>
    """, unsafe_allow_html=True)

# Create the form
with st.form("Details"):
    # Split form fields into three columns
    col1, col2, col3 = st.columns(3)

    # Define form fields for the first column
    with col1:
        City = st.selectbox("City Name", df['CITY'])
        OEM = st.selectbox("Company Name", df['OEM'])
        Fuel = st.selectbox("Fuel Type", df['FUEL'])
        Body_Type = st.selectbox("Body Type", df['TYPE'])
        Km_travelled = st.number_input("Km Travelled", value=20000)

    # Define form fields for the second column
    with col2:
        
        Transmission = st.selectbox("Transmission Type", df['TRANSMISSION'])
        Owner_Number = st.number_input("Owner Number",value=1)
        Model = st.selectbox("Model", df['MODEL'])
        Reg_year = st.selectbox("Registration Year", df['REG_YEAR'])
        Insurance = st.selectbox("Insurance", df['INSURANCE'])

    # Define form fields for the third column
    with col3:
        Seats = st.selectbox("Seats", df['SEATS'])
        Engine = st.number_input("Engine CC", value=1197)
        Mileage = st.number_input("Mileage",value=19)
        Color = st.selectbox("Color", df['COLOR'])

    # Add a submit button
    btn = st.form_submit_button('Submit')

# Handle form submission
if btn:
    # Prepare input data
    input_data = pd.DataFrame([[City, OEM, Fuel, Body_Type, Km_travelled, Transmission, Owner_Number,
        Model, Reg_year, 0, Insurance, Seats, Engine, Mileage, Color]],
                        columns=['CITY', 'OEM', 'FUEL', 'TYPE', 'KM_TRAVELLED', 'TRANSMISSION',
        'OWNER_NO', 'MODEL', 'REG_YEAR', 'PRICE', 'INSURANCE', 'SEATS',
        'ENGINE', 'mileage', 'COLOR'])

    # Transform input data
    input_data = ct.transform(input_data)

    # Predict price
    price = cbr.predict(input_data)[0]
    st.write("\n")
    st.write("\n")
    st.markdown("### Predicted Price:")
    st.write(f"<h2 style='color: #4CAF50;'>Rs {price:,.2f} Lakhs</h2>", unsafe_allow_html=True)

   