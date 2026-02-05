class AvailabilityManager:
    def __init__(self):
        self.schedules = {}

    def add_user(self, user):
        if user not in self.schedules:
            self.schedules[user] = []

    def add_meeting(self, user, meeting):
        self.schedules[user].append(meeting)

    def get_meetings(self, user):
        return self.schedules.get(user, [])