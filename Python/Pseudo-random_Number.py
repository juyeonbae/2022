import random
import time
random.seed(time.time())
a = []
for i in range(100):
    a.append(random.randint(1,1000))

start_time = time.time()

print("---%s seconds ---" % (time.time() - start_time))
