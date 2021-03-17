#You live 4 miles from thr university.
#the bus drives at 25 mph but spends 2 minutes at the each of the 10 stops on the way .
#how long will the bus journey take ?
#alternativelyt , you could run to university.
#you jog first time at 7mph ; then run the  next two at 15 mph ; before jogging the last at 7 mph again .
#will this be quicker or slower then the bus?

living_miles_apart = 4
drives_velocity = 25
time_taken = ((living_miles_apart/drives_velocity)*60)

#2 minutes in each stop
time_spends=20
total_time=time_taken + time_spends

print(f"total time taken by bus is{total_time}")

jog_one=((1/7)* 60)
jog_two=((2/15)*60)
jog_three=((1/7)*60)

total_walk_time= jog_one + jog_two + jog_three

print(f"time taken by running is {total_walk_time}")

if (total_time > total_walk_time):
    print("taking bus is slower than running!!")
else:
    print("taking bus is quiker than running!!")




