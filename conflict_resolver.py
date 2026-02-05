def has_conflict(existing_meetings, new_start, new_end):
    for meeting in existing_meetings:
        if not (new_end <= meeting.start_time or new_start >= meeting.end_time):
            return True
    return False
