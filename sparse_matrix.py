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

# Example Usage
if __name__ == "__main__":
    # Assuming 10 million merchants and 30,000 pincodes
    sparse_matrix = SparseMatrix(10000000, 30000)

    # Adding sample entries
    sparse_matrix.add_entry(500000, 200, 1)
    sparse_matrix.add_entry(7500000, 15000, 1)
    sparse_matrix.add_entry(2000000, 500, 1)

    # Retrieving values for specific merchants and pincodes
    value1 = sparse_matrix.retrieve_value(500000, 200)
    value2 = sparse_matrix.retrieve_value(7500000, 15000)
    value3 = sparse_matrix.retrieve_value(2000000, 500)

    print("Value for (500000, 200):", value1)
    print("Value for (7500000, 15000):", value2)
    print("Value for (2000000, 500):", value3)
