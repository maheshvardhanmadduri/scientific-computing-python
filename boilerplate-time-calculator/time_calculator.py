def change_bool_am (bool_am, start_splitted, days_later):
  if(bool_am):
    return (False, "PM", 0)
  else:
    return (True, "AM", 1)

def add_time(start, duration, days_of_the_week = ""):

  start_splitted = []
  start_splitted.append(int(start.split(":")[0]))
  start_splitted.append(int(start.split(":")[1].split(" ")[0]))
  start_splitted.append(start.split(":")[1].split(" ")[1].upper())

  duration_hour = int(duration.split(":")[0])
  duration_minute = int(duration.split(":")[1])

  bool_am = False
  if start_splitted[2] == "AM":
    bool_am = True
  else:
    bool_am = False

  days_later = 0

  #Adding hours
  quotient, remainder = divmod(duration_hour, 24)
  days_later += quotient
  if((start_splitted[0] + remainder) < 12):
    start_splitted[0] += remainder
  else:
    if((start_splitted[0] + remainder) == 12):
      start_splitted[0] = 12
      bool_am, start_splitted[2], temp = change_bool_am(bool_am, start_splitted, days_later)
      days_later += temp
    else:
      start_splitted[0] = (start_splitted[0] + remainder) % 12
      bool_am, start_splitted[2], temp = change_bool_am(bool_am, start_splitted, days_later)
      days_later += temp

  #Adding minutes
  if((start_splitted[1] + duration_minute) < 60):
    start_splitted[1] += duration_minute
  # Turn of the Hour
  else:
    start_splitted[1] = (start_splitted[1] + duration_minute) % 60
    # Basic Increment
    if(start_splitted[0] < 11):
      start_splitted[0] += 1
    # Critical Points
    else:
      # AM to PM or PM to AM
      if(start_splitted[0] == 11):
        start_splitted[0] += 1
        bool_am, start_splitted[2], temp = change_bool_am(bool_am, start_splitted, days_later)
        days_later += temp 
      # 12:59 to 1:00
      else:
        start_splitted[0] = 1

  #Writing Results
  new_time = str(start_splitted[0]) + ":" 
  
  if(start_splitted[1] < 10):
    new_time += "0" + str(start_splitted[1])
  else:
    new_time += str(start_splitted[1])

  new_time += " " + start_splitted[2]

  #Calculating the final day of the week
  week = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6}
  if(days_of_the_week != ""):
    value_day = week[days_of_the_week.lower()]
    value_day = (value_day + days_later) % 7
    
    key_list = list(week.keys())
    day_week = key_list[value_day]

    new_time += ", " + str(day_week.capitalize()) 
    

  if(days_later == 1):
    new_time += " (next day)"
  elif(days_later > 1):
    new_time += " (" + str(days_later) + " days later)"

  return new_time