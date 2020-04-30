import random
import time
# think of a question

# think of a random number and save it in 'first'
first = random.randint(2,10)

# think of another random number and save it in second
second = random.randint(2,10)

# do the sum and save the answer in awnser
awnser = first * second

# save the current time as start
start = time.time()

# print a blank line
print ("")

# ask me the question
print (str(first) + "*" + str(second))

# don't tell me the awnser until I have guessed it
input("Enter key should be pressed when you have finished thinking of the awnser")

end= time.time()

# tell me the answer
print ("The awnser is " + str(awnser))

rounded_time = round(end - start, 1)

print ("and it took you " + str( rounded_time ) + " seconds to awnswer")
