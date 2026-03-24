import streamlit as st
from scheduler import Scheduler

st.set_page_config(page_title="Meeting Scheduler", page_icon="📅")

st.title("📅 Meeting Scheduler Agent")
st.write("Smart meeting scheduling with conflict detection and suggestions.")

st.sidebar.title("⚙️ About")
st.sidebar.info("AI-inspired meeting scheduler with conflict detection and optimized scheduling logic.")

# Inputs
title = st.text_input("📌 Meeting Title")

participants_input = st.text_input(
    "👥 Enter Participants (comma separated)",
    "Alice, Bob, Charlie"
)
participants = [p.strip() for p in participants_input.split(",") if p.strip()]

start = st.number_input("⏰ Start Time (0-23)", min_value=0, max_value=23)
end = st.number_input("⏰ End Time (0-23)", min_value=0, max_value=23)

if st.button("🚀 Schedule Meeting"):
    if not title:
        st.warning("Please enter a meeting title")
    elif start >= end:
        st.warning("End time must be greater than start time")
    else:
        scheduler = Scheduler()
        result = scheduler.schedule_meeting(title, start, end, participants)

        if result["status"] == "success":
            st.success("✅ Meeting Scheduled Successfully!")

            meeting = result["meeting"]

            st.write("### 📌 Meeting Details")
            st.write(f"**Title:** {meeting['title']}")
            st.write(f"**Time:** {meeting['start']} - {meeting['end']}")
            st.write(f"**Participants:** {', '.join(meeting['participants'])}")
        else:
            st.error("❌ Conflict detected!")

            st.write("### 🚫 Unavailable Participants:")
            for person in result["unavailable"]:
                st.write(f"- {person}")

            st.write("### 💡 Suggested Available Time Slots:")
            for slot in result["suggestions"]:
                st.write(f"- {slot}")

st.caption("⚡ Uses intelligent conflict detection and optimized scheduling logic")