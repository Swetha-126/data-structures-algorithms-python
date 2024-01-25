''' 1. Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this'''

exp = [2200, 2350, 2600, 2130, 2190]
months = ["January", "February", "March", "April", "May"]
flag = 0
print(f"1. {exp[1]-exp[0]}")
print(f"2. {exp[0]+exp[1]+exp[2]}")

for i in range(0,5) :
    if exp[i] == 2000 :
        flag = 1
        break
if flag == 1 :
    print(f"3. {months[i]}")
else :
    print("3. None")

exp.append(1980)
print(exp)
months.append("June")
print(months)

n = exp[3] + 200
exp[3] = n
print(exp)

'''2. You have a list of your favourite marvel super heros.
```
heros=['spider man','thor','hulk','iron man','captain america']
```

Using this find out,

    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
       so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
       So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       Do that with one line of code.
    5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)'''

heros=['spider man','thor','hulk','iron man','captain america']

print(f"1. {len(heros)}")

heros.append("black panther")
print(heros)

heros[5] = " "
for i in range (3,5) :
    heros[i+1] = heros[i]
heros[5] = "captain america"
heros[3] = "black panther"
print(heros)

heros[1] = "doctor strange"
heros.remove('hulk')
print(heros)

s = sorted(heros)
print(s)

'''3. Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function'''

l = []
n = int(input())
for i in range (1,n+1) :
    if i%2 != 0 :
        l.append(i)
print(l)
