bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())

print(bicycles[-1].title())
print(bicycles[-2].title())

#f's replace the name of a string with the values inside.
#[] allows us to pull an item from a list starting at 0 for first item
#.title puts it in title case and () ends the title command
#{} lets you put the name or names of a variable(s) inside a string 
message= f"My first bike was a {bicycles[0].title()}."
print(message)
