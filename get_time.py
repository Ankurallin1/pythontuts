import time
#above line will get time of execution of program
#it can varries from device to device and time to time
#print(start)
#checking time taken by a while loop and for loop
start=time.time()
k=0
while(k<45):
    print("hello")
    k=k+1
    #time.sleep(2)
print("while loop time",time.time()-start)
t_for=time.time()
for i in range(45):
    print("hello")
print("for loop time",time.time()-t_for)
#below line will get real time by clock
local=time.asctime(time.localtime(time.time()))
print(local)
#above line 18 can also be written as
print(time.ctime(time.time()))
t = (2020, 1, 13, 13, 18, 9, 0, 3, 0)
date = time.asctime(t)
#print(date)
# seconds = time.time()
# date2 = time.ctime(seconds)
# print(date2)
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)