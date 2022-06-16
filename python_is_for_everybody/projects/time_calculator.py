import math 
def add_time(start, duration, day = None):
  hr_count = 0
  am_pm_flip = {"AM": "PM", "PM": "AM"}
  
  start_time = (start.split()[0])
  time_marker = (start.split()[1])
  hr = int(start_time.split(':')[0] )
  min = int(start_time.split(':')[1])
  
  dur_hr = int(duration.split(':')[0])
  dur_min = int(duration.split(':')[1])
  
  final_min = min + dur_min
  while final_min >= 60:
    final_min -= 60
    hr_count += 1

  final_hr = dur_hr + hr + hr_count
  day_count = int(final_hr / 24)
  am_pm_flips = int(final_hr / 12)
  if time_marker == "PM" and final_hr > 12:
    final_hr -= 12
    day_count += 1
    time_marker = "AM"
    am_pm_flips -= 1
  final_hr = final_hr % 12
  final_hr = 12 if final_hr == 0 else final_hr
  time_marker = time_marker if am_pm_flips % 2 == 0 else am_pm_flip[time_marker]
  
  if day is not None:
    week_dict = {"monday": 1, "tuesday": 2, "wednesday":3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
    day = day.lower()
    day_numb = week_dict[day]
    day_numb = int((day_numb + day_count) % 7)
    day_numb = 7 if day_numb == 0 else day_numb
    day_result = dict((v,k) for k,v in week_dict.items()).get(day_numb)
    day_result = day_result.capitalize()

  day_count = math.ceil(day_count)
  
  if day is None:
    if day_count < 1:
      return_time = (f"{final_hr}:%02d {time_marker}" % (final_min))
    elif day_count < 2:
      return_time = (f"{final_hr}:%02d {time_marker} (next day)" % (final_min))
    elif day_count >= 2:
      return_time = (f"{final_hr}:%02d {time_marker} ({day_count} days later)" % (final_min))

  elif day is not None:
    if day_count < 1:
      return_time = f"{final_hr}:%02d {time_marker}, {day_result}" % (final_min)
    if day_count == 1:
      return_time = (f"{final_hr}:%02d {time_marker}, {day_result} (next day)" % (final_min))
    elif day_count > 1:
      return_time = (f"{final_hr}:%02d {time_marker}, {day_result} ({int(day_count)} days later)" % (final_min))

  return(return_time)
