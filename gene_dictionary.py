# Create  an empty dictionary
gene_dict = {}

# Start a while loop to allow multiple entries
while True:
    # gene name
    gene_name = input("Enter a gene name (or type 'stop' to stop): ")
    
    # Condition to stop the loop if 'stop' is entered, no case sensitive
    if gene_name.lower() == 'stop':
        break
    
    # Information about the gene
    gene_info = input(f"Enter information about {gene_name}: ")
    
    # Add the gene and its information to the dictionary
    gene_dict[gene_name] = gene_info

# Print the dictionary and a description
print ("\nDictionary of genes and their descriptions:")
for gene, information in gene_dict.items():
    print(f"{gene}: {information}")
