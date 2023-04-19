import streamlit as st
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names, but .* was fitted with feature names")

# Load the model
model = joblib.load("forest_model.pkl")

# Define the predict_score function
def predict_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5):
    prediction_array = []
    # Batting Team
    if batting_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
    elif batting_team == 'Delhi Daredevils':
        prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
    elif batting_team == 'Kings XI Punjab':
        prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
    elif batting_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
    elif batting_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
    elif batting_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
    elif batting_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
    elif batting_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
    # Bowling Team
    if bowling_team == 'Chennai Super Kings':
        prediction_array = prediction_array + [1,0,0,0,0,0,0,0]
    elif bowling_team == 'Delhi Daredevils':
        prediction_array = prediction_array + [0,1,0,0,0,0,0,0]
    elif bowling_team == 'Kings XI Punjab':
        prediction_array = prediction_array + [0,0,1,0,0,0,0,0]
    elif bowling_team == 'Kolkata Knight Riders':
        prediction_array = prediction_array + [0,0,0,1,0,0,0,0]
    elif bowling_team == 'Mumbai Indians':
        prediction_array = prediction_array + [0,0,0,0,1,0,0,0]
    elif bowling_team == 'Rajasthan Royals':
        prediction_array = prediction_array + [0,0,0,0,0,1,0,0]
    elif bowling_team == 'Royal Challengers Bangalore':
        prediction_array = prediction_array + [0,0,0,0,0,0,1,0]
    elif bowling_team == 'Sunrisers Hyderabad':
        prediction_array = prediction_array + [0,0,0,0,0,0,0,1]
    prediction_array = prediction_array + [runs, wickets, overs, runs_last_5, wickets_last_5]
    prediction_array = np.array([prediction_array])
    pred = model.predict(prediction_array)
    return int(round(pred[0]))

# Create the Streamlit app
def app():
    st.title("IPL Score Predictor")

    # Get user input
    batting_team = st.selectbox("Select the batting team", ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])
    bowling_team = st.selectbox("Select the bowling team", ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])
    runs = st.number_input("Enter the runs scored", value=0)
    wickets = st.number_input("Enter the wickets lost", value=0)
    overs = st.number_input("Enter the number of overs played", value=0.0)
    runs_last_5 = st.number_input("Enter the runs scored in the last 5 overs", value=0)
    wickets_last_5 = st.number_input("Enter the wickets lost in the last 5 overs", value=0)

    # Predict the score
    if st.button("Predict"):
        score = predict_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5)
        st.write(f"Predicted score for {batting_team} against {bowling_team}: {score}")

# Run the app
if __name__ == "__main__":
    app()

# App creator information
# Add app creator information
st.markdown("<p style='text-align: center; font-size: 18px; margin-top: 50px;'>Created by</p>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-size: 30px;'>Manish Choudhary</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Follow me on <a href='https://www.instagram.com/expert.py' target='_blank'>Instagram</a></p>", unsafe_allow_html=True)
