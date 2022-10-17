
numbers = list(map(int, input('Enter 10 numbers').split()))


# ******************************
# Make your Code
# ******************************
average = float(sum(numbers)/len(numbers))
distance = []
for i in range(len(numbers)):
    dist = (abs(average - i))
    distance.append(dist)

for dist in distance:
    print(f'{dist:.2f}', end =' ')
# Use this statement to print out the list element. # Replace the variable 'dist' with your variable

