import itertools

def draw_kmap(num_vars):
    # Draw a K-map table based on the number of variables
    if num_vars == 2:
        kmap = [[0, 0], [0, 0]]
    elif num_vars == 3:
        kmap = [[0, 0, 0, 0], [0, 0, 0, 0]]
    elif num_vars == 4:
        kmap = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    else:
        print("Unsupported number of variables")
        return

    # Populate the K-map with terms
    terms = list(itertools.product([0, 1], repeat=num_vars))
    for i in range(len(terms)):
        for j in range(num_vars):
            kmap[i][j] = terms[i][j]

    # Print the K-map
    for row in kmap:
        print(row)

def simplify_boolean_function(kmap):
    # Group adjacent cells with the same value together
    grouped_cells = []
    # Implementation of grouping logic goes here

    # Make the enclosed result a Boolean function
    simplified_sop = ""
    simplified_pos = ""
    # Implementation of Boolean function simplification goes here

    return simplified_sop, simplified_pos

def main():
    # Get the number of variables from the user
    num_vars = int(input("Enter the number of variables: "))

    # Draw the K-map
    draw_kmap(num_vars)

    # Get the Boolean function from the user (assuming a simple format like "x'y + xy'")
    boolean_function = input("Enter the Boolean function: ")

    # Convert the Boolean function to a K-map representation (0s and 1s)
    kmap_representation = [[int(char) for char in row] for row in boolean_function.split('+')]

    # Simplify the Boolean function using the K-map
    simplified_sop, simplified_pos = simplify_boolean_function(kmap_representation)

    # Print the simplified Boolean function
    print("Simplified SOP:", simplified_sop)
    print("Simplified POS:", simplified_pos)

if __name__ == "__main__":
    main()
