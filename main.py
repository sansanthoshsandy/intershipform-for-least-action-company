import streamlit as st
from supabase import create_client

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Least Action Internship",
    layout="wide"
)

# ---------------- TOP BANNER IMAGE ----------------
st.image(
    "la-footer logo-MnbXDllf.png",
    use_container_width=True
)

# ---------------- SUPABASE CONFIG ----------------
SUPABASE_URL = "https://mpmfrppwlqcvcarwbqxa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1wbWZycHB3bHFjdmNhcndicXhhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYxMTg3MDQsImV4cCI6MjA4MTY5NDcwNH0.amiUFLYjeHAijrG_N7fEK-JJXhfwLjeltEjz85ALTds"   # keep your key here

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------- WEBSITE CONTENT ----------------
st.title("🚀 MERN Stack Developer Internship – Least Action")

st.markdown("""
**Experience:** 0–1 year  
**Work Mode:** Remote  
**Job Type:** Internship (Full-time opportunity based on performance)

📩 **Apply via:** hr@leastactioncompany.com
""")

st.subheader("📍 Company Location")

st.components.v1.iframe(
    "https://maps.google.com/maps?width=600&height=400&hl=en&q=(12.9364630,79.1481580)&t=&z=16&ie=UTF8&iwloc=B&output=embed",
    width=900,
    height=400
)


st.divider()

# ---------------- FORM LAYOUT ----------------
st.subheader("📄 Internship Application Form")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    college = st.text_input("College / University")

with col2:
    skills = st.text_area("Skills (React, Node, MongoDB etc.)")
    experience = st.selectbox("Experience", ["Fresher", "0–1 Year"])
    resume_link = st.text_input("Resume / GitHub / Portfolio Link")

# ---------------- SUBMIT BUTTON ----------------
if st.button("✅ Submit Application"):
    if name and email and phone and skills:
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "college": college,
            "skills": skills,
            "experience": experience,
            "resume_link": resume_link
        }

        supabase.table("applications").insert(data).execute()
        st.success("🎉 Application submitted successfully!")
    else:
        st.warning("⚠ Please fill all required fields")

# ---------------- ADMIN VIEW ----------------
st.divider()

if st.checkbox("🔐 Admin View"):
    response = supabase.table("applications").select("*").execute()
    st.dataframe(response.data)
