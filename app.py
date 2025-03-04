import streamlit as st
import time

# Set up the page configuration
st.set_page_config(page_title="Growth Mindset", page_icon="⭐")
st.title("The Unstoppable Growth Mindset Challenge: Web App With Streamlit")

# Welcome section
st.header("🥇 Embrace your Growth Journey 🧠🌱📈")
st.write("""
Welcome to a space where growth has no limits! 🌿💡
This journey is about embracing challenges, learning from every experience, and evolving into the best version of yourself. 🌟
Whether you're taking small steps or giant leaps, every moment counts. Keep blooming, keep thriving, and let’s make this journey extraordinary! 🚀💫
""")

# Quote section
st.header("Today's Growth Mindset Quote")
st.write("🌱 Growth is not about speed, but about consistency. Keep watering your dreams, and one day, they'll bloom beyond imagination. 🌸✨")

# What's your challenge today? Input section
st.header("🚀💫 What's your challenge today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Condition for user input
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal!🚀💫")
else:
    st.warning("Tell us about your challenge to get started!")

# Progress bar to track the completion of the challenge
st.header("⏳ Track Your Progress")
progress = st.slider("How close are you to completing your challenge?", 0, 100, 0)

if progress == 100:
    st.success("You did it! You've completed your challenge! 🎉")
else:
    st.progress(progress)
    st.write(f"Keep going! You're {progress}% of the way there. 💪")

# Reflection Section
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experiences helps you grow! Share your difficulties.")

# Achievements Section
st.header("🏆 Celebrate your Wins! 🥇")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"⭐ Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🧸ྀི ")

# Footer
st.write("- - -")
st.write("🚀 Keep believing in yourself and love yourself! Success lies in your growth. Growth is a journey, not a destination. ✨")
st.write("**˚🎀 Created by Ashii Malik˚˖𓍢ִ໋🌷͙֒✧**")
