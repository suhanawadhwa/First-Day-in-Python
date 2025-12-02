import streamlit as st

# Title of the app
st.title(Donuteria Game Demo")

# Add some description for the app
st.write("Welcome to the Donuteria game! In this demo, you can customize your donut.")

# Choose the donut base
base = st.selectbox("Choose your donut base:", ["Plain", "Chocolate", "Strawberry", "Glazed"])

# Choose icing
icing = st.selectbox("Choose your icing:", ["Vanilla", "Chocolate", "Strawberry", "None"])

# Choose toppings
toppings = st.multiselect(
    "Select your toppings:",
    ["Sprinkles", "Cherries", "Nuts", "Whipped Cream", "Candy Pieces"]
)

# Button to create donut
if st.button("Create my donut!"):
    # Show the donut creation summary
    st.subheader("Your Donut Creation!")
    st.write(f"**Base:** {base}")
    st.write(f"**Icing:** {icing}")
    if toppings:
        st.write(f"**Toppings:** {', '.join(toppings)}")
    else:
        st.write("**Toppings:** No toppings")

    # Simulate a little feedback message
    st.success("Your donut is ready! Enjoy!")

    # Optionally, show a fun message based on selections
    if base == "Glazed" and icing == "Chocolate":
        st.balloons()  # Just some fun confetti when a certain combination is selected
        st.write("Looks like you're a fan of chocolate and glaze! 🍩")
