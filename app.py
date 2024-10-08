import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model (replace 'vs_xgb_model.pkl' with your model file)
model = joblib.load('vs_xgb_model.pkl')

# Define the feature columns expected by the model
expected_features = [
    'age_at_screening', 'out_of_school', 'ever_had_sex', 'is_head',
    'undergone_gbv_last_12mnths', 'sexual_partners_last_12mnths',
    'received_gifts_for_sex', 'ever_had_sti', 'no_condom_use',
    'is_orphan', 'has_child', 'used_drugs_last_12mnths'
]

def process_input_data(age, out_of_school, ever_had_sex, 
                       is_head, undergone_gbv_last_12mnths, 
                       sexual_partners_last_12mnths, received_gifts_for_sex, 
                       ever_had_sti, no_condom_use, 
                       is_orphan, has_child, used_drugs_last_12mnths):
    # Create DataFrame
    input_data = pd.DataFrame({
        'age_at_screening': [age],
        'out_of_school': [out_of_school],
        'ever_had_sex': [ever_had_sex],
        'is_head': [is_head],
        'undergone_gbv_last_12mnths': [undergone_gbv_last_12mnths],
        'sexual_partners_last_12mnths': [sexual_partners_last_12mnths],
        'received_gifts_for_sex': [received_gifts_for_sex],
        'ever_had_sti': [ever_had_sti],
        'no_condom_use': [no_condom_use],
        'is_orphan': [is_orphan],
        'has_child': [has_child],
        'used_drugs_last_12mnths': [used_drugs_last_12mnths]
    })

    # Convert binary attributes from 'Yes'/'No' to 1/0
    binary_attributes = [
        'out_of_school', 'ever_had_sex', 'is_head', 
        'undergone_gbv_last_12mnths', 'sexual_partners_last_12mnths', 
        'received_gifts_for_sex', 'ever_had_sti', 'no_condom_use', 
        'is_orphan', 'has_child', 'used_drugs_last_12mnths'
    ]

    for attr in binary_attributes:
        input_data[attr] = input_data[attr].map({'Yes': 1, 'No': 0})

    # Ensure all expected features are present
    aligned_data = pd.DataFrame(
        {feature: input_data.get(feature, [0]) for feature in expected_features}
    )

    # Convert to NumPy array for prediction
    return aligned_data.values

def main():
    # Streamlit UI
    st.title("Eligibility for Enrollment Model")

    # Age input
    age_at_screening = st.text_input("Enter AGYW Age at Screening")

    # Validate age input
    try:
        age_at_screening = int(age_at_screening)
        if age_at_screening < 10 or age_at_screening > 24:
            st.error("Please enter an age between 10 and 24.")
            st.stop()
    except ValueError:
        st.error("Please enter a valid number for age.")
        st.stop()

    # Default all variables to 'No'
    out_of_school = "No"
    ever_had_sex = "No"
    is_head = "No"
    undergone_gbv_last_12mnths = "No"
    sexual_partners_last_12mnths = "No"
    received_gifts_for_sex = "No"
    ever_had_sti = "No"
    no_condom_use = "No"
    is_orphan = "No"
    has_child = "No"
    used_drugs_last_12mnths = "No"

    # Variables for ages 10-14
    if 10 <= age_at_screening <= 14:
        out_of_school = st.selectbox("Out of School", ["Select an option", "Yes", "No"])
        ever_had_sex = st.selectbox("Ever had sex", ["Select an option", "Yes", "No"])
        is_head = st.selectbox("Is the head of the household or in a child headed household", ["Select an option", "Yes", "No"])
        undergone_gbv_last_12mnths = st.selectbox("Undergoing violence or has undergone violence in the last 12 Months? (Physical, Emotional, Sexual, Social economic Violence)", ["Select an option", "Yes", "No"])
        has_child = st.selectbox("Has a child of her own/is pregnant/has been pregnant?", ["Select an option", "Yes", "No"])
        used_drugs_last_12mnths = st.selectbox("Has used alcohol/drugs or abused or struggled with addiction in the last 12 months?", ["Select an option", "Yes", "No"])
        is_orphan = st.selectbox("Is an orphan (partial or total)", ["Select an option", "Yes", "No"])
        
    # Variables for ages 15-19
    elif 15 <= age_at_screening <= 19:
        out_of_school = st.selectbox("Out of School", ["Select an option", "Yes", "No"])
        has_child = st.selectbox("Has a child of her own/is pregnant/has been pregnant?", ["Select an option", "Yes", "No"])
        is_head = st.selectbox("Is the head of the household or in a child headed household", ["Select an option", "Yes", "No"])
        undergone_gbv_last_12mnths = st.selectbox("Undergoing violence or has undergone violence in the last 12 Months? (Physical, Emotional, Sexual, Social economic Violence)", ["Select an option", "Yes", "No"])
        sexual_partners_last_12mnths = st.selectbox("Has had more than one sexual partner in the last 12 months?", ["Select an option", "Yes", "No"])
        received_gifts_for_sex = st.selectbox("Has ever received money gifts or favors in exchange for sex?", ["Select an option", "Yes", "No"])
        ever_had_sti = st.selectbox("Have been diagnosed or treated for STI?", ["Select an option", "Yes", "No"])
        no_condom_use = st.selectbox("No or irregular condom use with a non-marital /non-cohabiting partner?", ["Select an option", "Yes", "No"])
        used_drugs_last_12mnths = st.selectbox("Has used alcohol/drugs or abused or struggled with addiction in the last 12 months?", ["Select an option", "Yes", "No"])

    # Variables for ages 20-24
    elif 20 <= age_at_screening <= 24:
        out_of_school = st.selectbox("Out of School", ["Select an option", "Yes", "No"])
        sexual_partners_last_12mnths = st.selectbox("Has had more than one sexual partner in the last 12 months?", ["Select an option", "Yes", "No"])
        received_gifts_for_sex = st.selectbox("Has ever received money gifts or favors in exchange for sex?", ["Select an option", "Yes", "No"])
        undergone_gbv_last_12mnths = st.selectbox("Undergoing violence or has undergone violence in the last 12 Months? (Physical, Emotional, Sexual, Social economic Violence)", ["Select an option", "Yes", "No"])
        is_head = st.selectbox("Is the head of the household or in a child headed household", ["Select an option", "Yes", "No"])
        ever_had_sti = st.selectbox("Have been diagnosed or treated for STI?", ["Select an option", "Yes", "No"])
        no_condom_use = st.selectbox("No or irregular condom use with a non-marital /non-cohabiting partner?", ["Select an option", "Yes", "No"])
        used_drugs_last_12mnths = st.selectbox("Has used alcohol/drugs or abused or struggled with addiction in the last 12 months?", ["Select an option", "Yes", "No"])

    # Ensure required fields are filled out
    required_fields = []

    # Additional required fields based on age
    if 10 <= age_at_screening <= 14:
        required_fields += [out_of_school, ever_had_sex, is_head, has_child, used_drugs_last_12mnths, undergone_gbv_last_12mnths, is_orphan]
    elif 15 <= age_at_screening <= 19:
        required_fields += [out_of_school,has_child, is_head,undergone_gbv_last_12mnths, sexual_partners_last_12mnths, received_gifts_for_sex, ever_had_sti, no_condom_use, used_drugs_last_12mnths]
    elif 20 <= age_at_screening <= 24:
        required_fields += [out_of_school, sexual_partners_last_12mnths, received_gifts_for_sex, undergone_gbv_last_12mnths, is_head, ever_had_sti, no_condom_use, used_drugs_last_12mnths] 

    # Check if any required field is not selected
    if any(field == "Select an option" for field in required_fields):
        st.error("Please fill out all required fields.")
    else:
        # Make prediction when button is clicked
        if st.button("Check Eligibility"):
            input_data = process_input_data(
                age_at_screening, out_of_school, ever_had_sex, 
                is_head, undergone_gbv_last_12mnths, 
                sexual_partners_last_12mnths, received_gifts_for_sex, 
                ever_had_sti, no_condom_use, 
                is_orphan, has_child, used_drugs_last_12mnths
            )

            prediction = model.predict(input_data)
            
            if prediction == 1:
                st.success("Not Eligible for Enrollment in the DREAMS Program.")
            else:
                st.warning("Eligible to be Enrolled into DREAMS Program.")

if __name__ == "__main__":
    main()