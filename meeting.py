class Meeting:
    def __init__(self, title, participants, start_time, end_time):
        self.title = title
        self.participants = participants
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.title} | {self.start_time}-{self.end_time} | Participants: {', '.join(self.participants)}"