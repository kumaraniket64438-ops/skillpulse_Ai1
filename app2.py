import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="SkillPulse AI",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# SAMPLE DATA
# -----------------------------
data = pd.DataFrame({
    "Trainee_ID": ["TR001","TR002","TR003","TR004",
                   "TR005","TR006","TR007","TR008"],

    "Name": ["Rahul","Priya","Amit","Sneha",
             "Rohan","Ananya","Arjun","Puja"],

    "District": ["Kolkata","Howrah","Hooghly","Kolkata",
                 "North 24 Parganas","Howrah","Hooghly","Kolkata"],

    "Course": ["Data Analytics","Digital Marketing",
               "Web Development","Data Analytics",
               "Digital Marketing","Web Development",
               "Data Analytics","Web Development"],

    "Training_Score": [85,72,91,78,65,82,88,70],

    "Employment": [
        "Employed","Employed","Employed","Employed",
        "Employed","Searching","Searching","Employed"
    ],

    "Salary": [32000,26000,35000,28000,
               24000,0,0,30000],

    "3_Months": [
        "Employed","Employed","Employed","Searching",
        "Employed","Searching","Searching","Employed"
    ],

    "6_Months": [
        "Employed","Employed","Employed","Employed",
        "Employed","Searching","Searching","Employed"
    ],

    "12_Months": [
        "Employed","Employed","Employed","Employed",
        "Employed","Searching","Employed","Employed"
    ]
})

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🎓 SkillPulse AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 Trainee Enrollment",
        "📅 Follow-up Tracking",
        "🔐 Employment Verification",
        "🤖 AI Outcome Analysis",
        "📊 Analytics"
    ]
)

st.sidebar.info("Prototype Mode")

# -----------------------------
# DASHBOARD
# -----------------------------
if page == "🏠 Dashboard":

    st.title("🎓 SkillPulse AI")
    st.subheader("Longitudinal Skilling Outcomes & Impact Measurement Platform")

    total = len(data)
    employed = len(data[data["Employment"] == "Employed"])
    employment_rate = employed / total * 100

    employed_salary = data[data["Salary"] > 0]["Salary"].mean()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Trainees", total)
    c2.metric("Employed", employed)
    c3.metric("Employment Rate", f"{employment_rate:.1f}%")
    c4.metric("Average Salary", f"₹{employed_salary:,.0f}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Employment Outcomes")

        status = data["Employment"].value_counts()

        fig = px.pie(
            values=status.values,
            names=status.index,
            hole=0.4
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🎯 Course-wise Performance")

        course_score = data.groupby(
            "Course"
        )["Training_Score"].mean().reset_index()

        fig = px.bar(
            course_score,
            x="Course",
            y="Training_Score",
            text_auto=".1f",
            title="Average Training Score"
        )

        st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# TRAINEE ENROLLMENT
# -----------------------------
elif page == "👤 Trainee Enrollment":

    st.title("👤 Trainee Enrollment")

    st.write("Register and monitor trainee training information.")

    with st.form("enrollment"):

        name = st.text_input("Trainee Name")
        district = st.selectbox(
            "District",
            sorted(data["District"].unique())
        )

        course = st.selectbox(
            "Course",
            sorted(data["Course"].unique())
        )

        score = st.slider(
            "Training Score",
            0,
            100,
            70
        )

        submitted = st.form_submit_button(
            "Enroll Trainee"
        )

        if submitted:
            st.success(
                f"{name} successfully enrolled!"
            )

    st.subheader("Current Trainees")

    st.dataframe(
        data[
            [
                "Trainee_ID",
                "Name",
                "District",
                "Course",
                "Training_Score"
            ]
        ],
        use_container_width=True
    )

# -----------------------------
# FOLLOW-UP
# -----------------------------
elif page == "📅 Follow-up Tracking":

    st.title("📅 Longitudinal Follow-up Tracking")

    st.write(
        "Track trainee outcomes after completion of training."
    )

    selected = st.selectbox(
        "Select Trainee",
        data["Trainee_ID"]
    )

    trainee = data[
        data["Trainee_ID"] == selected
    ].iloc[0]

    st.subheader(
        f"{trainee['Name']} — {trainee['Course']}"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "3 Months",
        trainee["3_Months"]
    )

    c2.metric(
        "6 Months",
        trainee["6_Months"]
    )

    c3.metric(
        "12 Months",
        trainee["12_Months"]
    )

    st.success(
        "Longitudinal outcome successfully tracked."
    )

# -----------------------------
# EMPLOYMENT VERIFICATION
# -----------------------------
elif page == "🔐 Employment Verification":

    st.title("🔐 Employment Verification")

    st.info(
        "Government integrations such as EPFO/GSTN "
        "are simulated for demonstration."
    )

    selected = st.selectbox(
        "Select Trainee",
        data["Trainee_ID"]
    )

    trainee = data[
        data["Trainee_ID"] == selected
    ].iloc[0]

    st.subheader("Verification Result")

    if trainee["Employment"] == "Employed":

        st.success("🟢 Employment Verified")

        st.write("Employment Status: Employed")
        st.write(
            f"Reported Salary: ₹{trainee['Salary']:,}"
        )

        st.write("Verification Source: Simulated EPFO/GSTN")

    else:

        st.warning("🟡 Employment Not Yet Verified")

        st.write(
            "Recommended action: initiate follow-up."
        )

# -----------------------------
# AI ANALYSIS
# -----------------------------
elif page == "🤖 AI Outcome Analysis":

    st.title("🤖 AI Outcome Analysis")

    st.write(
        "AI-assisted identification of employment risk "
        "and recommended interventions."
    )

    selected = st.selectbox(
        "Select Trainee",
        data["Trainee_ID"]
    )

    trainee = data[
        data["Trainee_ID"] == selected
    ].iloc[0]

    score = trainee["Training_Score"]

    # Simple prototype scoring logic
    if trainee["Employment"] == "Employed":
        probability = min(95, score + 10)
        risk = "🟢 Low Risk"
        recommendation = "Continue career progression support."

    elif score >= 80:
        probability = score
        risk = "🟡 Medium Risk"
        recommendation = (
            "Provide job matching and interview assistance."
        )

    elif score >= 65:
        probability = score - 5
        risk = "🟠 High Risk"
        recommendation = (
            "Recommend advanced skill training and "
            "placement support."
        )

    else:
        probability = score - 10
        risk = "🔴 Very High Risk"
        recommendation = (
            "Recommend re-skilling, mentoring and "
            "employment assistance."
        )

    st.subheader(
        f"Outcome Analysis — {trainee['Name']}"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Training Score",
        f"{score}%"
    )

    c2.metric(
        "Employment Probability",
        f"{probability}%"
    )

    c3.metric(
        "Risk Level",
        risk
    )

    st.divider()

    st.subheader("🎯 Recommended Intervention")

    st.info(recommendation)

    st.caption(
        "Prototype AI model uses sample rule-based scoring. "
        "A production system can use trained ML models "
        "on historical skilling outcomes."
    )

# -----------------------------
# ANALYTICS
# -----------------------------
elif page == "📊 Analytics":

    st.title("📊 District & Course Analytics")

    st.subheader("📍 District-level Employment Rate")

    district_stats = (
        data.groupby("District")
        .apply(
            lambda x:
            (x["Employment"] == "Employed").mean() * 100
        )
        .reset_index(name="Employment_Rate")
    )

    fig = px.bar(
        district_stats,
        x="District",
        y="Employment_Rate",
        text_auto=".1f",
        title="Employment Rate by District"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("🎯 Course Performance")

    course_stats = data.groupby(
        "Course"
    ).agg(
        Average_Score=("Training_Score", "mean"),
        Trainees=("Trainee_ID", "count")
    ).reset_index()

    st.dataframe(
        course_stats,
        use_container_width=True
    )