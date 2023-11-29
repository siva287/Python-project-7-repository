friends = {'1':'siva', '2':'vinjam', '3':'krishna'}
friends[4] = 'raj'
print(friends)
friends[4] = 'rajakuamr'
print(friends)
del friends['3']
print(friends)
for x in friends:
    print(x, ":", friends[x])
