from availability import AvailabilityChecker
from conflict_resolver import ConflictResolver

class Scheduler:
    def __init__(self):
        self.availability_checker = AvailabilityChecker()
        self.conflict_resolver = ConflictResolver()

    def schedule_meeting(self, title, start, end, participants):
        unavailable = self.availability_checker.check_availability(participants, start, end)

        if unavailable:
            suggestions = self.conflict_resolver.suggest_time_slots(start, end)
            return {
                "status": "conflict",
                "unavailable": unavailable,
                "suggestions": suggestions
            }

        meeting = {
            "title": title,
            "start": start,
            "end": end,
            "participants": participants
        }

        return {
            "status": "success",
            "meeting": meeting
        }