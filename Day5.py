# password creator

import random
import streamlit as st

def password_creator():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    st.title("Password Generator")

    user_letters = st.number_input("How many letters would you like in your password?")
    user_symbols = st.number_input("How many symbols would you like in your password?") 
    user_numbers = st.number_input("How many numbers would you like in your password?")

    list = []

    for i in range(0,int(user_letters)):
        list.append(random.choice(letters))

    for i in range(0,int(user_symbols)):
        list.append(random.choice(numbers))

    for i in range(0,int(user_numbers)):
        list.append(random.choice(symbols))

    random.shuffle(list)

    password = ""
    for char in list:
        password += char

    st.header("Your password is:")
    st.write(password)
    st.download_button("Download Password",password)

def secrete_santa():
    st.write("Welcome to the Secret Santa Game")
    name = st.text_input("Please enter your name")
    button = st.button("Submit")
    names = ["srikanth","ramesh","suresh","kiran"]
    if button:
        if name in names:
            names.remove(name)
            random_name = random.choice(names)
            st.write("Your secret santa is",random_name)
            names.remove(random_name)
        else:
            st.write("Already Santa is assigned to you")

def TicketBooking():
    username = st.text_input("Please enter your name")
    Mobileno = int(st.number_input("Please enter your mobile number"))
    email = st.text_input("Please enter your email")
    date = st.date_input("Please enter your date of travel")
    location = st.text_input("Please enter your location")
    destination = st.text_input("Please enter your destination")
    Modeoftravel = st.radio("Please select your mode of travel",["Bus","Train","Flight"])
    button = st.button("Submit")
    if button:
        st.write("Username:",username)
        st.write("Mobileno:",Mobileno)
        st.write("Email:",email)
        st.write("Date:",date)
        st.write("Location:",location)
        st.write("Destination:",destination)
        st.write("Mode of travel:",Modeoftravel)
        st.write("Ticket Booked successfully")
    else:
        st.write("Tickets Not Available")
   

