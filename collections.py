# List: Ordered, Mutable, Allows Duplicates, Indexed, Heterogeneous
mylist = ["Pramod", 25, "Bangalore", True, "Pramod"]    
mylist = list(["Pramod", 25, "Bangalore", True, "Pramod"]) # Alternative way to create a list
print("List", mylist)

# Tuple: Ordered, Immutable, Allows Duplicates, Indexed, Heterogeneous
myTuple = ("Pramod", 25, "Bangalore", True, "Pramod")
myTuple = tuple("Pramod", 25, "Bangalore", True, "Pramod") # Alternative way to create a tuple
print("Tuple", myTuple)

# Set: Unordered, Mutable, No Duplicates, Not Indexed, Heterogeneous
mySet = {"Pramod", 25, "Bangalore", True, "Pramod"}
mySet = set({"Pramod", 25, "Bangalore", True, "Pramod"}) # Alternative way to create a set 
mySet.add("New Value")
print("Set", mySet)

# Frozenset: Unordered, Immutable, No Duplicates, Not Indexed, Heterogeneous
myFrozenset = frozenset(("Pramod", 25, "Bangalore", True, "Pramod"))
myFrozenset.add("New Value")  # This will raise an AttributeError
print("Frozenset", myFrozenset)