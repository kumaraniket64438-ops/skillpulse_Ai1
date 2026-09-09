import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SkillPulse AI",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    font-size: 18px;
    color: #666666;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f7f7f7;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SAMPLE DATA
# =========================================================

data = pd.DataFrame({
    "Name": [
        "Rahul Das",
        "Priya Sharma",
        "Amit Roy",
        "Sneha Gupta",
        "Arjun Singh",
        "Riya Sen",
        "Karan Das",
        "Ananya Roy"
    ],

    "Course": [
        "Data Analytics",
        "Digital Marketing",
        "Data Analytics",
        "Web Development",
        "Digital Marketing",
        "Web Development",
        "Data Analytics",
        "Digital Marketing"
    ],

    "District": [
        "Kolkata",
        "Howrah",
        "Kolkata",
        "Nadia",
        "Hooghly",
        "Howrah",
        "Nadia",
        "Kolkata"
    ],

    "Employed": [
        1, 1, 0, 1, 1, 0, 1, 1
    ],

    "Salary": [
        28000,
        24000,
        0,
        32000,
        26000,
        0,
        30000,
        25000
    ],

    "TrainingScore": [
        85,
        78,
        55,
        88,
        80,
        60,
        90,
        76
    ]
})

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎓 SkillPulse AI")

st.sidebar.write(
    "Longitudinal Skilling Outcomes Platform"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 Trainee Enrollment",
        "📅 Follow-up Tracking",
        "🔐 Employment Verification",
        "🤖 AI Outcome Analysis"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Prototype Mode\n\n"
    "Government integrations such as EPFO/GSTN "
    "are simulated for demonstration."
)

# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">SkillPulse AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Longitudinal Skilling Outcomes & Impact Measurement Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # Metrics
    total_trainees = len(data)
    employed = data["Employed"].sum()

    employment_rate = (
        employed / total_trainees
    ) * 100

    salary_data = data[data["Salary"] > 0]

    average_salary = salary_data["Salary"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Trainees",
            total_trainees
        )

    with col2:
        st.metric(
            "Employed",
            employed
        )

    with col3:
        st.metric(
            "Employment Rate",
            f"{employment_rate:.1f}%"
        )

    with col4:
        st.metric(
            "Average Salary",
            f"₹{average_salary:,.0f}"
        )

    st.divider()

    # =====================================================
    # EMPLOYMENT CHART
    # =====================================================

    st.subheader("📊 Employment Outcomes")

    employment_data = pd.DataFrame({
        "Status": [
            "Employed",
            "Not Employed"
        ],

        "Trainees": [
            employed,
            total_trainees - employed
        ]
    })

    fig = px.pie(
        employment_data,
        names="Status",
        values="Trainees",
        title="Employment Status"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # DISTRICT ANALYTICS
    # =====================================================

    st.subheader("📍 District-level Analytics")

    district_data = data.groupby(
        "District"
    ).agg(
        Trainees=("Name", "count"),
        Employed=("Employed", "sum")
    ).reset_index()

    district_data["Employment Rate"] = (
        district_data["Employed"]
        /
        district_data["Trainees"]
        * 100
    )

    st.dataframe(
        district_data,
        use_container_width=True
    )

    # =====================================================
    # COURSE ANALYTICS
    # =====================================================

    st.subheader("🎯 Course-wise Performance")

    course_data = data.groupby(
        "Course"
    ).agg(
        Trainees=("Name", "count"),
        Average_Score=("TrainingScore", "mean")
    ).reset_index()

    fig2 = px.bar(
        course_data,
        x="Course",
        y="Average_Score",
        title="Average Training Score by Course"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# =========================================================
# TRAINEE ENROLLMENT
# =========================================================

elif page == "👤 Trainee Enrollment":

    st.title("👤 Trainee Enrollment")

    st.write(
        "Register a trainee and capture digital consent."
    )

    st.divider()

    name = st.text_input(
        "Trainee Name"
    )

    skill_id = st.text_input(
        "Skill ID"
    )

    course = st.selectbox(
        "Training Course",
        [
            "Data Analytics",
            "Digital Marketing",
            "Web Development",
            "Advanced Excel"
        ]
    )

    district = st.selectbox(
        "District",
        [
            "Kolkata",
            "Howrah",
            "Nadia",
            "Hooghly"
        ]
    )

    phone = st.text_input(
        "Phone Number"
    )

    consent = st.checkbox(
        "I provide consent for outcome tracking."
    )

    st.write("")

    if st.button(
        "Register Trainee",
        type="primary"
    ):

        if (
            name
            and skill_id
            and phone
            and consent
        ):

            st.success(
                "✅ Trainee registered successfully!"
            )

            st.info(
                f"""
                Trainee: {name}

                Skill ID: {skill_id}

                Course: {course}

                District: {district}

                Consent: Recorded
                """
            )

        else:

            st.error(
                "Please fill all required fields "
                "and provide consent."
            )


# =========================================================
# FOLLOW-UP TRACKING
# =========================================================

elif page == "📅 Follow-up Tracking":

    st.title(
        "📅 Longitudinal Follow-up Tracking"
    )

    st.write(
        "Track trainee outcomes at different time intervals."
    )

    st.divider()

    trainee = st.selectbox(
        "Select Trainee",
        data["Name"]
    )

    person = data[
        data["Name"] == trainee
    ].iloc[0]

    st.subheader(
        f"Trainee: {trainee}"
    )

    st.write(
        f"Course: **{person['Course']}**"
    )

    st.write(
        f"District: **{person['District']}**"
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.success("3 Month\n\n✓ Completed")

    with col2:
        st.success("6 Month\n\n✓ Completed")

    with col3:
        st.warning("12 Month\n\n⏳ Pending")

    with col4:
        st.warning("24 Month\n\n⏳ Pending")

    st.divider()

    st.subheader(
        "Current Outcome"
    )

    employment = st.radio(
        "Employment Status",
        [
            "Employed",
            "Not Employed"
        ]
    )

    salary = st.number_input(
        "Current Monthly Salary (₹)",
        min_value=0,
        value=int(person["Salary"])
    )

    reason = st.selectbox(
        "Current Status / Reason",
        [
            "Working in trained field",
            "Working in another field",
            "Looking for employment",
            "Higher studies",
            "Other"
        ]
    )

    if st.button(
        "Submit Follow-up",
        type="primary"
    ):

        st.success(
            "✅ Follow-up information recorded successfully!"
        )

        st.write(
            f"Employment: **{employment}**"
        )

        st.write(
            f"Current Salary: **₹{salary:,}**"
        )

        st.write(
            f"Status: **{reason}**"
        )


# =========================================================
# EMPLOYMENT VERIFICATION
# =========================================================

elif page == "🔐 Employment Verification":

    st.title(
        "🔐 Employment Verification"
    )

    st.write(
        "Prototype simulation of multi-source employment verification."
    )

    st.divider()

    trainee = st.selectbox(
        "Select Trainee",
        data["Name"],
        key="verification_trainee"
    )

    person = data[
        data["Name"] == trainee
    ].iloc[0]

    st.subheader(
        f"Trainee: {trainee}"
    )

    st.write(
        f"Skill ID: **SK-{person.name + 1001}**"
    )

    st.divider()

    st.subheader(
        "Verification Signals"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### EPFO Signal")

        if person["Employed"] == 1:
            st.success("🟢 MATCHED")
        else:
            st.warning("🟡 NO MATCH")

    with col2:

        st.markdown("### GSTN Signal")

        if person["Employed"] == 1:
            st.success("🟢 VERIFIED")
        else:
            st.info("⚪ NOT APPLICABLE")

    with col3:

        st.markdown("### Employer Portal")

        if person["Employed"] == 1:
            st.success("🟢 CONFIRMED")
        else:
            st.warning("🟡 PENDING")

    st.divider()

    if person["Employed"] == 1:

        st.success(
            "✅ OVERALL STATUS: EMPLOYMENT VERIFIED"
        )

    else:

        st.warning(
            "⚠ OVERALL STATUS: EMPLOYMENT NOT VERIFIED"
        )

    st.caption(
        "Demo note: Government API responses are simulated "
        "using sample data in this prototype."
    )


# =========================================================
# AI OUTCOME ANALYSIS
# =========================================================

elif page == "🤖 AI Outcome Analysis":

    st.title(
        "🤖 AI Outcome Analysis"
    )

    st.write(
        "Predict employment outcome and identify potential skill gaps."
    )

    st.divider()

    # Training model

    X = data[
        ["TrainingScore"]
    ]

    y = data[
        "Employed"
    ]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X,
        y
    )

    score = st.slider(
        "Training Assessment Score",
        min_value=0,
        max_value=100,
        value=80
    )

    prediction = model.predict(
        [[score]]
    )[0]

    probability = model.predict_proba(
        [[score]]
    )[0][1]

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Training Score",
            score
        )

    with col2:

        st.metric(
            "Employment Probability",
            f"{probability * 100:.1f}%"
        )

    with col3:

        if score >= 75:
            st.success("LOW RISK")
        elif score >= 60:
            st.warning("MEDIUM RISK")
        else:
            st.error("HIGH RISK")

    st.divider()

    st.subheader(
        "🔎 AI Recommendation"
    )

    if score < 60:

        st.error(
            "⚠ Skill gap detected."
        )

        st.write(
            "Recommended Actions:"
        )

        st.write(
            "• Additional technical training"
        )

        st.write(
            "• Career counselling"
        )

        st.write(
            "• Employment support"
        )

    elif score < 80:

        st.warning(
            "⚠ Moderate skill readiness."
        )

        st.write(
            "Recommended Action:"
        )

        st.write(
            "• Upskilling recommended"
        )

        st.write(
            "• Advanced Excel / Power BI training"
        )

    else:

        st.success(
            "✅ Strong employment readiness."
        )

        st.write(
            "Recommended Action:"
        )

        st.write(
            "• Continue career progression"
        )

        st.write(
            "• Monitor wage growth"
        )

    st.divider()

    st.subheader(
        "📈 AI Interpretation"
    )

    st.write(
        "The prototype analyses training performance "
        "and historical employment outcomes to identify "
        "employment risk and recommend further skilling."
    )