import uproot

# Open the ROOT file
filename = "jetTuple_extended.root"
file = uproot.open(filename)

# Print top-level keys
print("Top-level keys:")
for key in file.keys():
    print(f"  {key}")

# Navigate to TTree inside the directory
tree_path = "outnano/Jets"

if tree_path in file:
    tree = file[tree_path]
    print(f"\nBranches in '{tree_path}':\n")
    
    for name, branch in tree.items():
        try:
            print(f"{name}: {branch.interpretation}")
        except Exception as e:
            print(f"{name}: could not interpret branch ({e})")
else:
    print(f"\nTTree '{tree_path}' not found in the file.")
