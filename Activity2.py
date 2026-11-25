setx = {"green", "blue"}

sety = {"blue", "yellow"}
print("Original Set:")
print(setx)
print(sety)
print("\nElements of setx that are not in sety:")
setz = setx.intersection(sety)
print(setz)

seta = {"green", "blue"}
setb = {"blue", "yellow"}

print("\nElements of seta that are not in setb:")
setc = seta.difference(setb)