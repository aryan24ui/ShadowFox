# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate number of members
print("Number of members:", len(justice_league))
print("\n")

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)
print("\n")

# 3. Move Wonder Woman to beginning (leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)
print("\n")

# 4. Separate Aquaman and Flash by adding Superman in between
justice_league.remove("Superman")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("After separating Flash and Aquaman:", justice_league)
print("\n")

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)
print("\n")

# 6. Sort alphabetically
justice_league.sort()
print("Alphabetically sorted team:", justice_league)
print("\n")

# BONUS: Predict new leader
print("BONUS: The new leader is:", justice_league[0])
