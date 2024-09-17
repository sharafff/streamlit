import streamlit as st

from Forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/test.jpeg", width=230)

with col2:
    st.title("Chafaa Achraf", anchor=False)
    st.write(
        "Software Developper, Robot maker."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.markdown(
    """
- Over 3 years of experience in robotics and software engineering.
- Developed and implemented semantic mapping and localization solutions for autonomous robots using ROS.
- Created communication gateways between ROS and digital object representation platforms like Thing'in.
- Built web applications from scratch for robot manipulation and data visualization.
- Developed a robot to assist humans in environments like hospitals, schools, and shopping malls, focusing on vision and object detection, path following and planning (indoor/outdoor), and system architecture.
- Containerized and deployed components of a medical application as micro-services.
- Optimized existing code and performed cross-compilation for Windows and Linux platforms.
- Established APIs and communication channels between containers and orchestrated Docker containers in the cloud.
- Excellent team player with a strong sense of initiative and problem-solving skills.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.markdown(
    """
- **Programming Languages:** C/C++, Python, JavaScript, Node.js
- **Robotics Frameworks:** ROS, SemanticSLAM, Rostful, RosBridge
- **Web Development:** Flask, web-server-video
- **APIs:** REST API, Ros-API
- **Containerization and Orchestration:** Docker, Kubernetes
- **Frameworks and Tools:** RestSDK, OMQ, Ontologies
- **Other Skills:** LiDAR, Embedded Software
    """
)
