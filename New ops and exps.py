hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

new_mins = (mins + dura)%60# Write your code here.
new_hours = int(((hour*60+mins+dura)//60)%24)
print("total duration: ",str(new_hours)+":"+str(new_mins))
