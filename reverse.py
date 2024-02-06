import random

variable=0
rdom = []
rdom_rev = []
for taylor in range(10):
    x = random.randint(1, 10)
    rdom.append(x)
    
abc = 9

for taylor in range(10):
    rdom_rev.append(rdom[abc])
    abc -= 1


print(rdom)
print(rdom_rev)