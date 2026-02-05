from meeting import Meeting
from conflict_resolver import has_conflict

class SchedulerAgent:
    def __init__(self, availability_manager):
        self.availability_manager = availability_manager

    def schedule_meeting(self, title, participants, start_time, end_time):
        for user in participants:
            meetings = self.availability_manager.get_meetings(user)
            if has_conflict(meetings, start_time, end_time):
                print(f"❌ Conflict detected for {user}")
                return None

        meeting = Meeting(title, participants, start_time, end_time)

        for user in participants:
            self.availability_manager.add_meeting(user, meeting)

        print("✅ Meeting scheduled successfully")
        return meeting