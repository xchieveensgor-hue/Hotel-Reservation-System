import streamlit as st
from datetime import date, timedelta, datetime
import rooms

st.set_page_config(page_title="Hotel Reservation", layout="centered")
st.markdown("""
<style>
.stApp {color: black !important;}
.stApp { 
    background-image: url(https://github.com/xchieveensgor-hue/Hotel-Reservation-System/blob/main/HotelRoom_reservation/hotel_bg.jpg");
    background-size: cover; 
    background-position: center; 
    background-attachment: fixed; 
}
</style>
""", unsafe_allow_html=True)

st.title("Hotel Room Reservation System")
st.markdown("---")

st.subheader("Reservation Details")

col1, col2, col3 = st.columns(3)
with col1:
    guest_name = st.text_input("Guest Name", placeholder="Enter full name")
with col2:
    phone = st.text_input("Phone Number", placeholder="e.g., 012-3456789")
with col3:
    gmail = st.text_input("Gmail", placeholder="name@gmail.com")

col4, col5 = st.columns(2)
with col4:
    room_type = st.radio("Room Type", ["Standard (RM50/night)", "Deluxe (RM150/night)", "Suite (RM250/night)"])
with col5:
    check_in = st.date_input("Check-in Date")

check_out = st.date_input("Check-out Date", value=date.today() + timedelta(days=1))
colt1, colt2 = st.columns(2)
checkin_time = st.time_input("Check-in Time", value=datetime.strptime("1:00 PM", "%I:%M %p").time())
checkout_time = st.time_input("Check-out Time", value=datetime.strptime("12:00 PM", "%I:%M %p").time())

st.markdown("---")

if st.button("Reserve Room", type="primary"):
    try:
        def validate_inputs(name, ph, gm, cin, cout):
            if not name.strip():
                return "Guest name cannot be empty!"
            if not ph.strip() or not ph.replace("-", "").isdigit():
                return "Valid phone number required!"
            if not gm.strip() or "@gmail.com" not in gm:
                return "Valid Gmail required!"
            if cout <= cin:
                return "Check-out must be after check-in!"
            return None

        error = validate_inputs(guest_name, phone, gmail, check_in, check_out)
        if error:
            st.error(f"Error: {error}")
        else:
            nights = max((check_out - check_in).days, 1)
            
            if "Deluxe" in room_type:
                room = rooms.DeluxeRoom(nights)
            elif "Suite" in room_type:
                room = rooms.Room("Suite", 250, nights, 10)
            else:
                room = rooms.Room("Standard", 50, nights)
            
            total = room.calculate_cost()
            details = room.get_details()
            
            st.success("Room reserved successfully!")
            
            st.markdown(f"""
            <div style='background: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #082366;'>
            <h3>Reservation Confirmed</h3>
            <p><b>Guest Name:</b> {guest_name}</p>
            <p><b>Phone:</b> {phone}</p>
            <p><b>Gmail:</b> {gmail}</p>
            <p><b>Room:</b> {details}</p>
            <p><b>Check-in:</b> {check_in} {checkin_time.strftime('%I:%M %p')}</p>
            <p><b>Check-out:</b> {check_out} {checkout_time.strftime('%I:%M %p')}</p>
            <p><b>Nights:</b> {nights}</p>
            <p><b>Total:</b> <span style='color: green; font-size: 18px;'>RM{total:.2f}</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.info("Thank you for reserving with us!")
    
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

st.markdown("---")
