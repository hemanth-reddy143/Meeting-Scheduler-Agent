from availability import AvailabilityManager
from scheduler import SchedulerAgent

def main():
    availability = AvailabilityManager()
    scheduler = SchedulerAgent(availability)

    users = ["Alice", "Bob", "Charlie"]
    for user in users:
        availability.add_user(user)

    print("📅 Meeting Scheduler Agent")

    title = input("Enter meeting title: ")
    start_time = int(input("Enter start time (hour): "))
    end_time = int(input("Enter end time (hour): "))

    meeting = scheduler.schedule_meeting(
        title,
        users,
        start_time,
        end_time
    )

    if meeting:
        print("\n📌 Meeting Details:")
        print(meeting)

if __name__ == "__main__":
    main()