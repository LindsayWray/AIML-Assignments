import streamlit as st
import base64
import time
from package import animals
from package import superpowers

main_bg = "assignment_3/images/background.jpeg"
main_bg_ext = "jpeg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.header("Which Super Powered Animal Are You?")
st.write("Did you always wonder which superpowered animal is harbouring in you?")
st.write("Take this quiz and find out!")
query_1 = st.radio("Pick your favourite element:",["⛰ Earth" ,"🌊 Water" ,"🔥 Fire", "🌪 Air"])
query_2 = st.radio("Pick your favourite time of the day:", ["🌅 Morning", "🌞 Afternoon", "🌚 Night"])
query_3 = st.radio("Pick a type of food:", ["🍭 Candy", "🥦 Vegetables", "🍝 Carbs", "☕️ Coffee", "🌰 Nuts"])
query_4 = st.radio("Do you prefer books or movies?", ["📚 Books", "🎬 Movies"])
if st.button("Confirm"):
	animal = animals.which_animal(query_1, query_2)
	superpower = superpowers.which_superpower(query_3, query_4)
	my_bar = st.progress(0)
	for percent_complete in range(100):
		time.sleep(0.01)
		my_bar.progress(percent_complete + 1)
	st.info(f"The results are in 🥁:\n\nYou are a{superpower} {animal}!\n")