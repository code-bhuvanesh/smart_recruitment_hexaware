import streamlit as st
import job_description_ai
import json

st.title("Job Description Prompt")
msg = st.text_input("Enter Job Title")

if msg:
    response = job_description_ai.generate_job_description(msg)
    print(response)
    response_dict = json.loads(response)
    
    # st.json(response_dict)
    
    st.markdown(f"### **{response_dict['Job Title']}**")
    st.markdown(f"**Department**: {response_dict['Department']}")
    st.markdown(f"**Job Location**: {response_dict['Job Location']}")
    st.markdown(f"**Employment Type**: {response_dict['Employment Type']}")
    st.markdown(f"**Salary Range**: {response_dict['Salary Range']}")
    st.markdown(f"**Application Deadline**: {response_dict['Application Deadline']}")
    st.markdown(f"### **Job Description**")
    st.write(response_dict['Job Description'])
    
    st.markdown(f"### **Required Qualifications**")
    for qualification in response_dict['Required Qualifications']:
        st.markdown(f"- {qualification}")
    
    st.markdown(f"### **Preferred Qualifications**")
    for qualification in response_dict['Preferred Qualifications']:
        st.markdown(f"- {qualification}")
    
    st.markdown(f"### **Responsibilities**")
    for responsibility in response_dict['Responsibilities']:
        st.markdown(f"- {responsibility}")