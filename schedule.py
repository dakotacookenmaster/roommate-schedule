import csv
import pendulum
from collections import deque
import sys

roommates = ["Logan Bateman", "Marc Butler", "Dakota Cookenmaster", "Brandon Gustrowsky"]
chores = deque(["Do Dishes", "Take Out Trash", "Vacuum Living Room & Kitchen", "Clean Countertops & Table"])

with open("schedule.csv", "w") as file:
    arguments = sys.argv
    pendulum.week_starts_at(pendulum.SUNDAY) # make sure week starts on Sunday
    pendulum.week_ends_at(pendulum.SATURDAY) # make sure the week ends on Sabbath
    today = pendulum.now()

    if(len(arguments) == 3):
        if arguments[1] == "--period":
            if arguments[2] == "next":
                today = today.add(days=7) # start for the next week
                
    
    week_of_month = today.week_of_month

    sunday = today.start_of('week')
    tuesday = sunday.add(days=2)
    thursday = tuesday.add(days=2)
    friday = thursday.add(days=1)

    days=[sunday, tuesday, thursday, friday]

    chores.rotate(week_of_month % len(roommates))

    csv_writer = csv.writer(file)
    csv_writer.writerow([day.to_formatted_date_string() for day in days])

    # write people & chores togther
    chores = [f"{roommates[i]}-{chore}" for i, chore in enumerate(chores)]
    csv_writer.writerow(chores)

