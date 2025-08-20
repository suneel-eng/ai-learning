# Sets - Unordered, Unique items
skills = {"Python", "AWS", "Python"}
print(skills) # Duplicates removed

skills.add("AI") # Add new item
print(skills)

# check if a value exists
skill = "AI" if "AI" in skills else None
print(skill)

skill = "Java" if "Java" in skills else None
print(skill)