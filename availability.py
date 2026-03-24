class AvailabilityChecker:
    def __init__(self):
        # Example: predefined unavailable times
        self.busy_schedule = {
            "Alice": [(10, 11)],
            "Bob": [(11, 12)],
            "Charlie": []
        }

    def check_availability(self, participants, start, end):
        unavailable = []

        for person in participants:
            if person in self.busy_schedule:
                for busy_start, busy_end in self.busy_schedule[person]:
                    if not (end <= busy_start or start >= busy_end):
                        unavailable.append(person)
                        break

        return unavailable