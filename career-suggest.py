import json
import streamlit as st

# Function to load career knowledge from JSON
def load_career_knowledge(json_file):
    with open(json_file, 'r') as file:
        career_knowledge = json.load(file)
    return career_knowledge

# Load career knowledge from JSON
career_knowledge = load_career_knowledge('career_knowledge.json')

# Function to calculate career scores
def match_careers(user_data):
    scores = {}
    matches = {}

    for career, criteria in career_knowledge.items():
        score = 0
        match_details = []

        for key, value in user_data.items():
            if key in criteria and any(item in criteria[key] for item in value if isinstance(value, list)):
                score += 1
                match_details.append(f"{key.capitalize()}: {', '.join(value)}")
            elif key in criteria and value in criteria[key]:
                score += 1
                match_details.append(f"{key.capitalize()}: {value}")

        scores[career] = score
        matches[career] = match_details

    # Sort careers by highest score
    top_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    
    return [(career[0], matches[career[0]]) for career in top_careers]

# Program title
st.title("Career Suggestion System")

# Link to MBTI test
st.markdown("[Don't know your MBTI? Take the test here.](https://www.16personalities.com/free-personality-test)")

# Get options from career knowledge
education_options = sorted({edu for career in career_knowledge.values() for edu in career.get("education", [])})
experience_options = sorted({exp for career in career_knowledge.values() for exp in career.get("experience", [])})
skills_options = sorted({skill for career in career_knowledge.values() for skill in career.get("skills", [])})
interests_options = sorted({interest for career in career_knowledge.values() for interest in career.get("interests", [])})
mbti_options = sorted({mbti for career in career_knowledge.values() for mbti in career.get("mbti", [])})

# User input
mbti = st.selectbox("Select your MBTI type", mbti_options)
education = st.multiselect("Select your education background", education_options)
experience = st.multiselect("Select your experience", experience_options)
skills = st.multiselect("Select your skills", skills_options)
interests = st.multiselect("Select your interests", interests_options)

user_data = {
    "education": education,
    "experience": experience,
    "skills": skills,
    "interests": interests,
    "mbti": mbti
}

#Output button
if st.button("Get Career Suggestions"):
    best_matches = match_careers(user_data)
    st.write("Top 3 Career Matches:")
    for career, details in best_matches:
        st.write(f"**{career}**")
        for detail in details:
            st.write(f"- {detail}")