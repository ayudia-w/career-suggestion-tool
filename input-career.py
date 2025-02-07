import json
import streamlit as st

def add_career_to_json(json_file, new_career):
    with open(json_file, 'r') as file:
        career_knowledge = json.load(file)
    
    career_knowledge.update(new_career)
    
    with open(json_file, 'w') as file:
        json.dump(career_knowledge, file, indent=4)

st.title("Add New Career")

career_name = st.text_input("Career Name")

education = st.text_area("Education (comma separated)").split(',')
experience = st.text_area("Experience (comma separated)").split(',')
skills = st.text_area("Skills (comma separated)").split(',')
interests = st.text_area("Interests (comma separated)").split(',')
mbti = st.text_area("MBTI (comma separated)").split(',')

if st.button("Add Career"):
    new_career = {
        career_name: {
            "education": [edu.strip() for edu in education],
            "experience": [exp.strip() for exp in experience],
            "skills": [skill.strip() for skill in skills],
            "interests": [interest.strip() for interest in interests],
            "mbti": [mbti_type.strip() for mbti_type in mbti]
        }
    }
    add_career_to_json('career_knowledge.json', new_career)
    st.success(f"Career '{career_name}' added successfully!")