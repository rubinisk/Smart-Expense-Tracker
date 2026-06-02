import streamlit as st
import pandas as pd

from database import (
    create_table,
    add_expense,
    get_category_summary,
    get_expenses,
    get_total_expenses,
    delete_expense,
    update_expense,
    expense_exists
)

create_table()

# ---------------- TITLE ----------------

st.title("💰 Smart Expense Manager")
st.write("Track and manage your expenses efficiently!")

# ---------------- ADD EXPENSE ----------------

st.divider()

with st.form("expense_form"):

    date = st.date_input("Date")

    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Others"]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        format="%.2f"
    )

    description = st.text_input("Description")

    submitted = st.form_submit_button("Add Expense")

    if submitted:

        add_expense(
            str(date),
            category,
            amount,
            description
        )

        st.success("Expense added successfully!")
        st.toast("Expense added successfully! 🎉")

# ---------------- DATA ----------------

total = get_total_expenses()
expenses = get_expenses()

df = pd.DataFrame(
    expenses,
    columns=[
        "ID",
        "Date",
        "Category",
        "Amount",
        "Description"
    ]
)

avg_expense = (
    df["Amount"].mean()
    if not df.empty
    else 0
)

# ---------------- SUMMARY ----------------

st.divider()

st.subheader("📊 Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "💰 Total Expenses",
        f"₹{total:.2f}"
    )

with col2:
    st.metric(
        "📈 Average Expense",
        f"₹{avg_expense:.2f}"
    )

st.write(f"📄 Total Transactions: {len(df)}")

# ---------------- LATEST EXPENSE ----------------

if not df.empty:

    latest = df.iloc[0]

    st.info(
        f"Latest Expense: {latest['Category']} - ₹{latest['Amount']:.2f}"
    )

# ---------------- FILTER ----------------

st.divider()

st.subheader("🔍 Filter Expenses")

if not df.empty:

    selected_category = st.selectbox(
        "Select Category",
        ["All"] + list(df["Category"].unique())
    )

    if selected_category == "All":
        filtered_df = df
    else:
        filtered_df = df[
            df["Category"] == selected_category
        ]

else:
    filtered_df = df

# ---------------- EXPENSE TABLE ----------------

st.divider()

st.subheader("📋 All Expenses")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# ---------------- CATEGORY SUMMARY ----------------

st.divider()

st.subheader("📂 Category Summary")

summary = get_category_summary()

summary_df = pd.DataFrame(
    summary,
    columns=["Category", "Total"]
)

st.dataframe(summary_df, hide_index=True)

# ---------------- UPDATE EXPENSE ----------------

st.divider()

st.subheader("✏️ Update Expense")

update_id = st.number_input(
    "Expense ID to Update",
    min_value=1,
    step=1,
    key="update_id"
)

new_date = st.date_input(
    "New Date",
    key="update_date"
)

new_category = st.selectbox(
    "New Category",
    ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Others"],
    key="update_category"
)

new_amount = st.number_input(
    "New Amount",
    min_value=0.0,
    format="%.2f",
    key="update_amount"
)

new_description = st.text_input(
    "New Description",
    key="update_description"
)


if st.button("Update Expense"):

    if expense_exists(update_id):

        update_expense(
            update_id,
            str(new_date),
            new_category,
            new_amount,
            new_description
        )

        st.success("Expense updated successfully!")
        st.rerun()

    else:
        st.error("Expense ID not found!")

# ---------------- DELETE EXPENSE ----------------

st.divider()

st.subheader("🗑️ Delete Expense")

if not df.empty:
    st.write("Available IDs:")
    st.write(df["ID"].tolist())

expense_id = st.number_input(
    "Expense ID",
    min_value=1,
    step=1
)

if st.button("Delete"):

    rows_deleted = delete_expense(expense_id)

    if rows_deleted > 0:
        st.success("Expense deleted successfully!")
        st.rerun()
    else:
        st.error("Expense ID not found!")