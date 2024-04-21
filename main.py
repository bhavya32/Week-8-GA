import streamlit as st
st.set_page_config(page_title='Largest number finder')
st.title('Largest among three numbers') 
num1=st.number_input('Enter the first number',step=1)
num2=st.number_input('Enter the second number',step=1)
num3=st.number_input('Enter the third number',step=1)
st.write('Largest of the 3 numbers is: **'+ str(max([num1, num2, num3])) + "**")