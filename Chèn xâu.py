a  = input()
b = input()
position = int(input())-1
newstring = a[:position]+b+a[position:]
print(newstring)