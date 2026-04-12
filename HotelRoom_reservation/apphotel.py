import streamlit as st
from datetime import date, timedelta, datetime
import rooms
st.set_page_config(page_title="Hotel Reservation", layout="centered")
st.markdown("""<style>.stApp {background-image: url("https://raw.githubusercontent.com/xchieveensgor-hue/Hotel-Room-Reservation-System/main/hotel_bg.jpg");background-size: cover;background-position: center;background-attachment: fixed;}</style>""", unsafe_allow_html=True)
st.title("Hotel Room Reservation System")
st.subheader("Reservation Details")
guest_name = st.text_input("Guest Name")
phone = st.text_input("Phone Number")
gmail = st.text_input("Gmail")
room_type = st.radio("Room Type", ["Standard (RM50)", "Deluxe (RM150)", "Suite (RM250)"])
check_in = st.date_input("Check-in")
check_out = st.date_input("Check-out", value=date.today()+timedelta(days=1))
checkin_time = st.time_input("Check-in Time", value=datetime.strptime("1:00 PM", "%I:%M %p").time())
checkout_time = st.time_input("Check-out Time", value=datetime.strptime("12:00 PM", "%I:%M %p").time())
if st.button("Reserve Room"):
    try:
        def validate_inputs(n,p,g,ci,co,cit,cot):
            if not n.strip():return"Name empty"
            if not p.isdigit():return"Phone digits"
            if "@gmail.com"not in g:return"Gmail invalid"
            if co<=ci:return"Date error"
            return None
        error=validate_inputs(guest_name,phone,gmail,check_in,check_out,checkin_time.strftime("%I:%M %p"),checkout_time.strftime("%I:%M %p"))
        if error:st.error(error)
        else:
            nights=max((check_out-check_in).days,1)
            if "Deluxe"in room_type:room=rooms.DeluxeRoom(nights)
            else:room=rooms.Room()
            total=room.calculate_cost()
            st.success("Reserved!")
            col1,col2=st.columns(2)
            with col1:st.write("**Name:**\n**Phone:**\n**Email:**\n**Room:**\n**Check-in:**\n**Nights:**\n**Total:**")
            with col2:st.write(guest_name,phone,gmail,room.get_details(),f"{check_in} {checkin_time.strftime('%I:%M %p')}",nights,f"RM{total:.2f}")
    except:st.error("Error occurred")