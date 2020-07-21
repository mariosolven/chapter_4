import pandas as pd

print("- Veterinary's Register -\nMonday, July 20.\n")
# Step 1: creating a Data Frame.
df = pd.DataFrame(
  {
    'NAME':['Blake', 'Coco', 'Flash', 'Bobby', 'Nala'], 
    'BREAD':['Bulldog', 'Chihuahua', 'Schnauzer', 'Poodle', 'Mastif'], 
    'AGE':[3, 3, 7, 8, 12], 
    'DISEASE':['Parvovirus', 'Rabies', 'Ringworm', 'Heartworm', 'Diabetes']
    }
) 
print("\n", df)

# Step 2: changing index data with their ID.
df.index = [10730, 21125 ,31222, 41433, 52100]
print("\n-> Updated table with ID's: \n\n", df)

# Step 3: getting one specific column values.
print(" \n-> Most common dog's diseases:\n", df.DISEASE.unique())

# Step 4: getting the min and max of values from 'AGE'.
print(" \n-> Dog's age:")
min_v = df['AGE'].min() 
print("  - Min =", min_v)
max_v  = df['AGE'].max() 
print("  - Max. =", max_v)

# Step 5: getting the avg of values from 'AGE'.
mean = df['AGE'].mean() 
print("  - Average =",mean)

# Step 6: Creating a dictionary.
print('\n -> Bread dictionary:')
dict = {'Bulldog' : 'B', 'Chihuahua' : 'C', 'Schnauzer' : 'S', 'Poodle' : 'P', 'Mastif' : 'M'}
print('\n', dict)

#Step 7: Remaping values from the Data Frame with the dictionary values.
print('\n -> Remaping Bread names:\n')
print((df.replace({'BREAD': dict})))