import streamlit as st
import random
import time

st.set_page_config(
    page_title="🦀 Super Crab Carnival",
    page_icon="🦀",
    layout="centered"
)

# ---------------- STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "combo" not in st.session_state:
    st.session_state.combo = 0
if "high_score" not in st.session_state:
    st.session_state.high_score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "last_click" not in st.session_state:
    st.session_state.last_click = 0

GAME_TIME = 30

# ---------------- UI ----------------
st.title("🦀 Super Crab Carnival 🦀")
st.write("Click fast. Build combos. Avoid the bombs.")

# ---------------- START ----------------
if st.button("🎮 Start Game"):
    st.session_state.score = 0
    st.session_state.combo = 0
    st.session_state.start_time = time.time()
    st.session_state.last_click = 0
    st.rerun()

# ---------------- GAME LOOP ----------------
if st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    time_left = max(0, GAME_TIME - elapsed)

    st.progress(time_left / GAME_TIME)
    st.metric("⭐ Score", st.session_state.score)
    st.metric("🔥 Combo", st.session_state.combo)

    if time_left > 0:
        crab_roll = random.random()

        if crab_roll < 0.6:
            crab = "🦀"
            points = 1
            combo_add = 1
            label = "Crab +1"
        elif crab_roll < 0.85:
            crab = "🦀✨"
            points = 5
            combo_add = 2
            label = "Golden Crab +5"
        else:
            crab = "💣🦀"
            points = -5
            combo_add = -st.session_state.combo
            label = "BOMB CRAB -5"

        col = st.columns([random.randint(1,3), 1, random.randint(1,3)])[1]

        with col:
            if st.button(f"{crab} {label}"):
                now = time.time()

                if now - st.session_state.last_click < 1:
                    st.session_state.combo += combo_add
                else:
                    st.session_state.combo = max(0, combo_add)

                st.session_state.score += points + st.session_state.combo
                st.session_state.last_click = now
                st.rerun()

    else:
        st.session_state.high_score = max(
            st.session_state.high_score,
            st.session_state.score
        )

        st.success("🏁 GAME OVER!")
        st.subheader(f"Final Score: {st.session_state.score}")
        st.subheader(f"🏆 High Score: {st.session_state.high_score}")

        if st.session_state.score == st.session_state.high_score:
            st.balloons()
            st.write("🦀 **NEW CRAB RECORD!!!** 🦀")

st.caption("Built with claws, combos, and chaos 🦀")
