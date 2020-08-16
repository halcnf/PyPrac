string = "   Hi this is a line of CODE  "

print(len(string))
print(string)
print(string[11])

print(string[3:10])

print(string.strip())

print(string.lower())

print(string.upper())

list = string.split()
print(list)

x = "line of CODE" in string

print(x)


name = "Rakib"
location = "Chittagong"
area = "Agrabad"

myself = "My name is {}, I live in {}, and it located in {}."
myself2 =  "My name is {1}, I live in {1}, and it located in {1}."
print (myself.format(name,area,location))
print(myself2.format(name,area,location))












