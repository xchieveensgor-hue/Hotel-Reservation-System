import streamlit as st
from datetime import date, timedelta, datetime
import rooms

st.set_page_config(page_title="Hotel Reservation", layout="centered")
st.markdown("""<style>.stApp {background-image: url("https://raw.githubusercontent.com/xchieveensgor-hue/Hotel-Room-Reservation-System/main/hotel_bg.jpg");background-size: cover;background-position: center;background-attachment: fixed;}</style>""", unsafe_allow_html=True)

st.title(" Hotel Room Reservation System")
st.markdown("---")

# Inputs
st.subheader(" Reservation Details")
col1, col2, col3 = st.columns(3)
with col1:
    guest_name = st.text_input(" Name", "Gayathiri")
with col2:
    phone = st.text_input(" Phone", "0137153518")
with col3:
    gmail = st.text_input(" Email", "xchieveensgor@gmail.com")

col4, col5 = st.columns(2)
with col4:
    room_type = st.radio(" Room", ["Standard (RM50)", "Deluxe (RM150)*", "Suite (RM250)*"])
with col5:
    check_in = st.date_input(" Check-in", date.today()+timedelta(days=1))

check_out = st.date_input(" Check-out", date.today()+timedelta(days=2))
colt1, colt2 = st.columns(2)
checkin_time = st.time_input(" In Time", datetime.strptime("01:15 PM", "%I:%M %p").time())
checkout_time = st.time_input(" Out Time", datetime.strptime("12:00 PM", "%I:%M %p").time())

if st.button(" Reserve Room", type="primary"):
    try:
        def validate(n,p,g,ci,co): 
            if not n:return"Name required"; 
            if not p.isdigit():return"Phone digits"; 
            if "@"not in g:return"Valid email"; 
            if co<=ci:return"Check-out after check-in"; 
            return None
        error = validate(guest_name,phone,gmail,check_in,check_out)
        if error: st.error(f" {error}")
        else:
            nights = max((check_out-check_in).days,1)
            if "Deluxe"in room_type: room=rooms.DeluxeRoom(nights)
            else: room=rooms.Room("Standard"if"Standard"in room_type else"Suite",50if"Standard"in room_type else250,nights)
            total = room.calculate_cost()
            st.success(" Reserved!")
            
            # PERFECT FORMATTED OUTPUT
            st.markdown(f"""
            <div style='background: linear-gradient(45deg, #f0f8ff, #e6f3ff); padding:25px; border-radius:15px; border-left:5px solid #4CAF50;'>
            <h3>🎊 Confirmation</h3>
            <table style='width:100%; font-size:16px;'>
            <tr><td><b> Name:</b></td><td>{guest_name}</td></tr>
            <tr><td><b> Phone:</b></td><td>{phone}</td></tr>
            <tr><td><b> Email:</b></td><td>{gmail}</td></tr>
            <tr><td><b> Room:</b></td><td>{room.get_details()}</td></tr>
            <tr><td><b> Check-in:</b></td><td>{check_in} {checkin_time.strftime('%I:%M %p')}</td></tr>
            <tr><td><td><b> Check-out:</b></td><td>{check_out} {checkout_time.strftime('%I:%M %p')}</td></tr>
            <tr><td><b> Nights:</b></td><td>{nights}</td></tr>
            <tr><td><b> Total:</b></td><td style='color:green;font-size:18px;font-weight:bold;'>RM{total:.2f}</td></tr>
            </table>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
    except Exception as e: st.error(f"Error: {e}")

st.markdown("---")
