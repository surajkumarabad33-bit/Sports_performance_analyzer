# make_csv.py - creates scores.csv for the chosen test case

# Test Case 1 and 4 use the same data
case1 = "Aman,1,40\nAman,2,60\nRiya,1,30\nRiya,2,50\n"

# Test Case 2: only one row
case2 = "Karan,1,25\n"

# Test Case 3: invalid rows
case3 = "Aman,1,abc\nRiya,1,-10\n"

print("1. Test Case 1 (Normal input)")
print("2. Test Case 2 (Boundary / single row)")
print("3. Test Case 3 (Invalid input)")
print("4. Test Case 4 (Same CSV as Test Case 1)")
choice = input("Which test case? ").strip()

if choice == "1" or choice == "4":
    text = case1
elif choice == "2":
    text = case2
elif choice == "3":
    text = case3
else:
    print("Invalid choice.")
    raise SystemExit

file = open("scores.csv", "w")   # create (or overwrite) scores.csv in this folder
file.write(text)                 # write the test data into it
file.close()                     # close the file
print("scores.csv created for Test Case", choice)
