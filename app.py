
+
import pickle
import streamlit as st
import warnings


warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
# Set page config
st.set_page_config(
    layout="wide"
)

# Load the trained model and scaler
with open('model4.pkl', 'rb') as file:
    model1 = pickle.load(file)


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.

    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# sidebar navigation
def main():
    set_bg_hack_url()  # Set background image

    st.title('Scholarhsip Recommender System',)

    st.header('Student Data')


    with st.container(border=True):
        st.write("Personal Details")
        col1,col2,col3 = st.columns(3)
        
        with col1:
            Gender = st.selectbox('Gender', ["Male", "Female"],placeholder=  "Choose an Option")
            Religion = st.selectbox('Religion', ["Christianity", "Islam","Traditional Religion"],placeholder=  "Choose an Option")
        with col2:
            Age = st.selectbox('Age', ["14-16", "17-19","20-22","23-25","26-Abov"],placeholder=  "Choose an Option")
            Hobbies = st.selectbox('Hobbies', ["Football", "Reading","Singing","Table Tennis", "Others"],placeholder=  "Choose an Option")
        with col3:
            Ethnicity = st.selectbox('Ethinicity', ["Yoruba", "Igbo","Hausa","Other Tribes"],placeholder=  "Choose an Option")
            Employment_Status = st.selectbox('Employment_Status', ["Yes", "No",],placeholder=  "Choose an Option")
    with st.container(border=True):
        st.write("Education")
        col1,col2,col3 = st.columns(3)  
        with col1:
            UTME_Score = st.selectbox('UTME Score', ["1-150", "151-200","201-250","251-Above"],placeholder=  "Choose an Option")
            Subject1 = st.selectbox('Subject 1', ["A1", "B2","B3", "C4", "C5", "C6","D7", "E8","F9"],placeholder=  "Choose an Option")
            University_Type = st.selectbox('University Type', ["Privately Owned", "State Government Owned","Federal Government Owned"],placeholder=  "Choose an Option")
            
        with col2:
            English = st.selectbox('English', ["A1", "B2","B3", "C4", "C5", "C6","D7", "E8","F9"],placeholder=  "Choose an Option")
            Subject2 = st.selectbox('Subject 2', ["A1", "B2","B3", "C4", "C5", "C6","D7", "E8","F9"],placeholder=  "Choose an Option")
        with col3:
            
            Mathematics = st.selectbox('Mathematics', ["A1", "B2","B3", "C4", "C5", "C6","D7", "E8","F9"],placeholder=  "Choose an Option")
            Subject3 = st.selectbox('Subject 3', ["A1", "B2","B3", "C4", "C5", "C6","D7", "E8","F9"],placeholder=  "Choose an Option")
        
    with st.container(border=True): 
        st.write("General Questions")
        col1,col2,col3,col4 = st.columns(4)  
        with col1:
            Family_Income = st.selectbox('Family_Income', ["1-100,000", "101,000-200,000","201,000-300,000","301,000-400,000","401,000-500,000","Above N500,000"],placeholder=  "Choose an Option")
            Father_Level_Of_Education = st.selectbox('Father Level of Education', ["Primary Education", "Secondary Education","Tertiary Education"],placeholder=  "Choose an Option")
            Father_Ethnicity = st.selectbox('Father Ethnicity', ["Yoruba", "Igbo","Hausa","Other Tribes"],placeholder=  "Choose an Option")
            Father_Religion = st.selectbox('Father Religion', ["Christianity", "Islam","Traditional Religion"],placeholder=  "Choose an Option")
            
        with col2:
            House_Type = st.selectbox('House Type', ["Flat", "Bungalow","Duplex", "Face and Face You", "Others"],placeholder=  "Choose an Option")
            Mother_Level_Of_Education = st.selectbox('Mother Level of Education', ["Primary Education", "Secondary Education","Tertiary Education"],placeholder=  "Choose an Option")
            Mother_Ethnicity = st.selectbox('Mother Ethnicity', ["Yoruba", "Igbo","Hausa","Other Tribes"],placeholder=  "Choose an Option")
            Mother_Religion = st.selectbox('Mother Religion', ["Christianity", "Islam","Traditional Religion"],placeholder=  "Choose an Option")
        with col3:
            Father_Alive_or_dead = st.selectbox('Father Alive or Dead', ["Alive", "Dead"],placeholder=  "Choose an Option")
            Home_Ownership = st.selectbox('Home Ownership', ["Yes", "No"],placeholder=  "Choose an Option")
            Geopolitical_Zone = st.selectbox('Geopolitical Zone', ["South West", "South East","North Central", "South South", "North East", "North West"],placeholder=  "Choose an Option")
            Position_in_the_family = st.selectbox('Posiiton in the Family', ["1st", "2nd","3rd","4th", "5th","6th","7th - Above"],placeholder=  "Choose an Option")
        with col4:
            Mother_Alive_or_dead = st.selectbox('Mother Alive or Dead', ["Alive", "Dead"],placeholder=  "Choose an Option")
            Location_Type = st.selectbox('Location Type', ["Urban", "Rural"],placeholder=  "Choose an Option")
            Family_Size = st.number_input('Family Size', min_value=1, max_value=20, step=1)
            Parental_Marital_Status = st.selectbox('Parental Marital Status', ["Married", "Divorced","Seperated"],placeholder=  "Choose an Option")
           
    with st.container(border=True):
        st.write("Mental Health")
        col1,col2,col3 = st.columns(3)
        
        with col1:
            Felt_You_Were_Playing_A_Useful_Part_In_Things = st.selectbox('Felt.You.Were.Playing.A.Useful.Part.In.Things', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
        
            Been_Feeling_Reasonably_Happy_All_Things_Considered = st.selectbox('Been.Feeling.Reasonably.Happy.All.Things.Considered', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option") 
            
            Been_Able_To_Enjoy_Your_Day_To_Day_Activities = st.selectbox('Been.Able.To.Enjoy.Your.Day.To.Day.Activities', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")   
            Been_Feeling_Unhappy_And_Depressed = st.selectbox('Been.Feeling.Unhappy.And.Depressed', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
        with col2:
            Felt_Capable_Of_Making_Decisions_About_Things = st.selectbox('Felt.Capable.Of.Making.Decisions.About.Things', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
        
            Lost_Much_Sleep_Over_Worry = st.selectbox('Lost.Much.Sleep.Over.Worry', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
            Been_Able_To_Face_Up_To_Your_Problems = st.selectbox('Been.Able.To.Face.Up.To.Your.Problems', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
            Been_Thinking_Of_Yourself_As_A_Worthless_Person = st.selectbox('Been.Thinking.Of.Yourself.As.A.Worthless.Person', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
        
        

        with col3:
            Felt_You_Could_Not_Overcome_Your_Difficulties = st.selectbox('Felt.You.Could.Not.Overcome.Your.Difficulties', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")

            Felt_Constantly_Under_Strain = st.selectbox('Felt.Constantly.Under.Strain', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
    
            Been_Able_To_Concentrate_On_What_You_Are_Doing = st.selectbox('Been.Able.To.Concentrate.On.What.You.Are.Doing', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
            Been_Losing_Confidence_In_Yourself = st.selectbox('Been.Losing.Confidence.In.Yourself', ["Not More Than Usual", "Not at all","Much More Than Usual","Rather More Than Usual"],placeholder=  "Choose an Option")
            
    gender_map = {"Male": 1, "Female": 0}
    family_income_map = {"1-100,000": 1, "101,000-200,000": 2, "201,000-300,000": 3, "301,000-400,000": 4,"401,000-500,000": 5, "Above N500,000": 0}
    house_type_map = {"Flat": 3, "Bungalow": 0, "Duplex": 1, "Face and Face You": 2}
    self_religion_map = {"Christianity": 0, "Islam": 1, "Traditional Religion": 2}
    father_rel = {"Christianity": 0, "Islam": 2, "Traditional Religion": 3}
    response_map = {"Not More Than Usual": 1, "Not at all": 0, "Much More Than Usual": 2, "Rather More Than Usual": 3}
    age_map = {"14-16": 0, "17-19": 1, "20-22": 2, "23-25": 3, "26-Abov": 5}
    father_dead = {"Alive": 0, "Dead": 2}
    mother_dead = {"Alive": 0, "Dead": 1}
    binary_map = { "Yes": 1, "No": 0}
    education_map = {"Primary Education": 0, "Secondary Education": 1, "Tertiary Education": 2}
    ethnicity_map = {"Yoruba": 3, "Igbo": 1, "Hausa": 0, "Other Tribes": 2}
    location_map = {"Urban": 1, "Rural": 0}
    math_map = {"A1": 0, "B2": 1, "B3": 2, "C4": 3, "C5": 4, "C6": 5, "D7": 6}
    english_map = {"A1": 0, "B2": 1, "B3": 2, "C4": 3, "C5": 4, "C6": 5}
    sub1_map = {"A1": 0, "B2": 1, "B3": 2, "C4": 3, "C5": 4, "C6": 5}
    sub2_map = {"A1": 0, "B2": 1, "B3": 2, "C4": 3, "C5": 4, "C6": 5}
    sub3_map = {"A1": 0, "B2": 1, "B3": 2, "C4": 3, "C5": 4, "C6": 5, "D7": 6}
    university_map = {"Privately Owned": 1, "State Government Owned": 2, "Federal Government Owned": 0}
    marital_status_map = {"Married": 1, "Divorced": 0, "Seperated": 3}
    hobbies_map = {"Football": 0, "Reading": 2, "Singing": 3, "Table Tennis": 4, "Others": 1}
    geopolitical_zone_map = {"South West": 6, "South East": 4, "North Central": 0, "South South": 5, "North East": 1, "North West": 2}
    position_in_family_map = {"1st": 2, "2nd": 3, "3rd": 4, "4th": 6, "5th": 7, "6th": 9, "7th - Above": 10}
    utme_score_map = {"1-150": 0, "151-200": 1, "201-250": 2, "251-Above": 3}

    Gender = gender_map[Gender]
    Family_Income = family_income_map[Family_Income]
    House_Type = house_type_map[House_Type]
    Religion = self_religion_map[Religion]
    Felt_You_Were_Playing_A_Useful_Part_In_Things = response_map[Felt_You_Were_Playing_A_Useful_Part_In_Things]
    Been_Feeling_Reasonably_Happy_All_Things_Considered = response_map[Been_Feeling_Reasonably_Happy_All_Things_Considered]
    Age = age_map[Age]
    Father_Alive_or_dead = father_dead[Father_Alive_or_dead]
    Home_Ownership = binary_map[Home_Ownership]
    Mother_Level_Of_Education = education_map[Mother_Level_Of_Education]
    Lost_Much_Sleep_Over_Worry = response_map[Lost_Much_Sleep_Over_Worry]
    Ethnicity = ethnicity_map[Ethnicity]
    Mother_Alive_or_dead = mother_dead[Mother_Alive_or_dead]
    Location_Type = location_map[Location_Type]
    English = english_map[English]
    Felt_Capable_Of_Making_Decisions_About_Things = response_map[Felt_Capable_Of_Making_Decisions_About_Things]
    University_Type = university_map[University_Type]
    Father_Level_Of_Education = education_map[Father_Level_Of_Education]
    Mathematics = math_map[Mathematics]
    Felt_You_Could_Not_Overcome_Your_Difficulties = response_map[Felt_You_Could_Not_Overcome_Your_Difficulties]
    Felt_Constantly_Under_Strain = response_map[Felt_Constantly_Under_Strain]
    Employment_Status = binary_map[Employment_Status]
    Father_Ethnicity = ethnicity_map[Father_Ethnicity]
    Subject1 = sub1_map[Subject1]
    Parental_Marital_Status = marital_status_map[Parental_Marital_Status]
    Been_Able_To_Enjoy_Your_Day_To_Day_Activities = response_map[Been_Able_To_Enjoy_Your_Day_To_Day_Activities]
    Hobbies = hobbies_map[Hobbies]
    Mother_Ethnicity = ethnicity_map[Mother_Ethnicity]
    Subject2 = sub2_map[Subject2]
    Geopolitical_Zone = geopolitical_zone_map[Geopolitical_Zone]
    Been_Able_To_Face_Up_To_Your_Problems = response_map[Been_Able_To_Face_Up_To_Your_Problems]
    Father_Religion = father_rel[Father_Religion]
    Subject3 = sub3_map[Subject3]
    Been_Able_To_Concentrate_On_What_You_Are_Doing = response_map[Been_Able_To_Concentrate_On_What_You_Are_Doing]
    Been_Feeling_Unhappy_And_Depressed = response_map[Been_Feeling_Unhappy_And_Depressed]
    Position_in_the_family = position_in_family_map[Position_in_the_family]
    Mother_Religion = self_religion_map[Mother_Religion]
    UTME_Score = utme_score_map[UTME_Score]
    Been_Thinking_Of_Yourself_As_A_Worthless_Person = response_map[Been_Thinking_Of_Yourself_As_A_Worthless_Person]
    Been_Losing_Confidence_In_Yourself = response_map[Been_Losing_Confidence_In_Yourself]

    # Make prediction when 'Predict' button is clicked
    if st.button('Predict'):
            # Scale the input data
        scaled_data = [[Gender,Age,Ethnicity,	University_Type,	Employment_Status,	Religion,	Hobbies,Family_Size, Position_in_the_family, Parental_Marital_Status, Family_Income, Father_Alive_or_dead, Mother_Alive_or_dead, Father_Level_Of_Education, Mother_Level_Of_Education, Father_Ethnicity, Mother_Ethnicity,  Father_Religion,   Mother_Religion, Geopolitical_Zone, House_Type, Home_Ownership, Location_Type,  Mathematics, English, Subject1,   Subject2, Subject3,   UTME_Score,  
        Been_Able_To_Concentrate_On_What_You_Are_Doing,  Lost_Much_Sleep_Over_Worry, 
        Felt_You_Were_Playing_A_Useful_Part_In_Things, Felt_Capable_Of_Making_Decisions_About_Things,	
        Felt_Constantly_Under_Strain,	Felt_You_Could_Not_Overcome_Your_Difficulties,	
        Been_Able_To_Enjoy_Your_Day_To_Day_Activities,	Been_Able_To_Face_Up_To_Your_Problems,	
        Been_Feeling_Unhappy_And_Depressed,	Been_Losing_Confidence_In_Yourself, Been_Thinking_Of_Yourself_As_A_Worthless_Person,Been_Feeling_Reasonably_Happy_All_Things_Considered]]
            
            # Make prediction using the model
        prediction = model1.predict(scaled_data)
            
            # Display prediction result
        if prediction[0] == 0:
                st.success('Based on the information you provided , you may likely belong to a "First Class", therefore you are recommended for Scholarship')
        elif prediction[0] == 1:
                st.success('Based on the information you provided , you may likely belong to a "Second Class Upper", therefore you are recommended for Scholarship')
        elif prediction[0] == 2:
                st.success('Based on the information you provided , you may likely belong to a "Second Class Lower", therefore you are on the Waiting list')
        elif prediction[0] == 3:
                st.error('Based on the information you provided , you may likely belong to a "Third Class", therefore you are not elligible for Scholarship')
        else:
                st.error('Based on the information you provided , you may likely belong to a "Pass", therefore you are not elligible for Scholarship')
# Call the main function
if __name__ == '__main__':
    main()           
    
