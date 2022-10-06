import random
import statistics
print(random.random()*100)
#U can apply calculation on random values
print(random.random()*(35-15)+20)

#U can provide a range for random values
print(random.randint(3,100))

#learning randrange() - giving stopvalue --isse jada nhi
print(random.randrange(2))

#-- giving start,stop - 11,12,13,14
print(random.randrange(11,15))

# -- giving start,stop, step value, 21,23
print(random.randrange(21,25,3))

