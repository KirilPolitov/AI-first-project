import streamlit as st
import random
import time

st.set_page_config(page_title="Catch the Golden Crab!", page_icon="🦀")

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "crab_type" not in st.session_state:
    st.session_state.crab_type = "normal"

st.title("🦀 Catch the Golden Crab! 🦀")
st.write("Click the crab as many times as you can in **30 seconds**!")

# Start game
if st.button("Start Game"):
    st.session_state.score = 0
    st.session_state.start_time = time.time()

# Game running
if st.session_state.start_time:
    elapsed = int(time.time() - st.session_state.start_time)
    time_left = max(0, 30 - elapsed)

    st.subheader(f"⏱️ Time Left: {time_left}s")
    st.subheader(f"⭐ Score: {st.session_state.score}")

    if time_left > 0:
        # Randomly choose crab type
        st.session_state.crab_type = random.choice(
            ["normal", "normal", "normal", "golden"]
        )

        if st.session_state.crab_type == "golden":
            crab = "🦀✨"
            points = 5
            label = "GOLDEN CRAB! +5"
        else:
            crab = "🦀"
            points = 1
            label = "+1"

        if st.button(f"{crab} {label}"):
            st.session_state.score += points
            st.rerun()
    else:
        st.success(f"🎉 Game Over! Final Score: {st.session_state.score} 🦀")
        st.write("You are officially a **Crab Champion** 🏆")

st.caption("Made with ❤️ and many claws")
