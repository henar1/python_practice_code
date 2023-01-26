#Make the list (iterable) an iterable object with help of the iter() function.
loops = ["while", "for", "nested"]
iter_obj = iter(loops)
#Run an infinite while loop and break only if the StopIteration is raised.
while True:
#In the try block, we fetch the next element of fruits with the next() function.    
    try:
        fruit = next(iter_obj)#getting the next item
        print(fruit)
    except StopIteration:# if StopIteration is raised, break from loop
        break

#here we are calling the iter() and next() method


