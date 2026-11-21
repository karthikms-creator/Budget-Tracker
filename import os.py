
import streamlit as st

# TITLE
st.title("💰 My Budget Tracker")
st.write("Manage your monthly money easily!")

# USER INPUTS
st.header("Enter Your Monthly Details")

income = st.number_input("Monthly Income (₹)", min_value=0)
needs = st.number_input("Needs (₹)", min_value=0)
wants = st.number_input("Wants (₹)", min_value=0)
savings = st.number_input("Savings (₹)", min_value=0)

# CALCULATE BUTTON
if st.button("Calculate Budget"):

    # CALCULATIONS
    expenses = needs + wants
    remaining = income - expenses - savings

    # DISPLAY RESULTS
    st.header("Your Financial Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Income", f"₹{income}")
    col2.metric("Expenses", f"₹{expenses}")
    col3.metric("Savings", f"₹{savings}")
    col4.metric("Remaining", f"₹{remaining}")

    # CHECK MONEY
    if income == 0:
        st.warning("Please enter your income.")

    elif remaining < 0:
        st.error("Your expenses exceed your income!")

    else:
        # SHOW EXPENSE CHART
        st.subheader("Spending Breakdown")

        chart = {
            "Category": ["Needs", "Wants", "Savings"],
            "Amount": [needs, wants, savings]
        }

        st.bar_chart(chart, x="Category", y="Amount")

        # CALCULATE PERCENTAGES
        need_percent = needs / income * 100
        want_percent = wants / income * 100
        save_percent = savings / income * 100

        st.subheader("Budget Analysis")

        st.write("Needs:", round(need_percent), "%")
        st.write("Wants:", round(want_percent), "%")
        st.write("Savings:", round(save_percent), "%")

        # CHECK 50/30/20 RULE
        if (need_percent <= 50 and
            want_percent <= 30 and
            save_percent >= 20):

            st.success("Great! You follow the 50/30/20 rule!")

        else:
            st.warning("Your budget needs improvement.")
