class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def add_entry(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Invalid row or column index")

        key = (row, col)
        self.data[key] = value

    def retrieve_value(self, row, col):
        key = (row, col)
        return self.data.get(key, 0)  # Default value is 0 if entry doesn't exist

# User Interface Functions
def get_user_input():
    row = int(input("Enter merchant index: "))
    col = int(input("Enter pincode index: "))
    return row, col

def search_and_print_value(matrix, row, col):
    value = matrix.retrieve_value(row, col)
    print(f"Value for ({row}, {col}): {value}")

# Example Usage with User Interface
if __name__ == "__main__":
    # Assuming 10 million merchants and 30,000 pincodes
    sparse_matrix = SparseMatrix(10000000, 30000)

    # Adding sample entries
    sparse_matrix.add_entry(500000, 200, 1)
    sparse_matrix.add_entry(7500000, 15000, 1)
    sparse_matrix.add_entry(2000000, 500, 1)

    # User Interface
    while True:
        print("\nEnter 0 to exit.")
        row, col = get_user_input()

        if row == 0:
            break

        search_and_print_value(sparse_matrix, row, col)
