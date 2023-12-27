import datetime

def file_with_current():
   current_time=datetime.datetime.now().strftime("%Y-%B-%d-%H-%M-%S")
   print(current_time)
   file_name =f"C:\\Users\\Admin\\Desktop\\{current_time}.txt"
   with open(file_name, "w") as file:
      file.write("Current date and time is"+current_time)

file_with_current()