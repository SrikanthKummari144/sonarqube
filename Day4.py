import streamlit as st
import random
from Day5 import TicketBooking, password_creator, secrete_santa


st.title("Welcome to the Resource Zone")
input = st.radio("Please select the Option you want",['NumberGuesser','Head and Tails',"Roll a Dice","Password Generator",
                                                      "Secrete Santa","Book a Travel"])


if input == 'NumberGuesser':
    st.write("Welcome to NumberGuesser Game")
    number = random.randint(1,10)
    guess = st.number_input("Please enter a number between 1 and 10")
    submit = st.button("Submit")
    if submit:
        if guess == number:
            st.write("You guessed it right")
        else:
            st.write("Sorry, you guessed it wrong. The number was", number)
elif input == 'Head and Tails':
    st.write("Welcome to Head and Tails Game")
    coin = random.randint(0,1)
    guess = st.selectbox("Please choose Head or Tails",['Heads','Tails'])
    submit = st.button("Submit")
    if submit:
        if guess == 'Heads' and coin == 0:
            st.write("You guessed it right")
        elif guess == 'Tails' and coin == 1:
            st.write("You guessed it right")
        else:
            st.write("Sorry, you guessed it wrong. The coin was", 'Heads' if coin == 0 else 'Tails')
elif input == 'Password Generator':
    password_creator()
elif input == 'Secrete Santa':
    secrete_santa()
elif input == "Book a Travel":
    TicketBooking()
else:
    st.write("welcome to Roll a Dice")
    roll = st.button("Roll the Dice")
    if roll:
        dice = random.randint(1,6)
        st.write("You rolled a", dice)
        sys_role = random.randint(1,6)
        st.write("System rolled a", sys_role)
        if dice > sys_role:
            st.write("You win")
        elif dice < sys_role:
            st.write("You lose")
        else:
            st.write("Draw")










