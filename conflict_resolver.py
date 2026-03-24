class ConflictResolver:
    def suggest_time_slots(self, start, end):
        # Simple suggestions (example logic)
        return [
            f"{start + 1} - {end + 1}",
            f"{start + 2} - {end + 2}"
        ]