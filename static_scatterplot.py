import matplotlib.pyplot as plt

def create_scatter_plot(x_values, y_values, title="Static Scatter Plot", x_label="X-axis", y_label="Y-axis"):
    if not isinstance(x_values, (list, tuple)) or not isinstance(y_values, (list, tuple)):
        raise TypeError("x_values and y_values must be lists or tuples.")
    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have the same length.")
    if len(x_values) == 0:
        raise ValueError("Data lists cannot be empty.")

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, color='blue', marker='o', edgecolors='black', s=100, alpha=0.7)

    # Add labels and title
    plt.title(title, fontsize=14)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)

    # Add grid for better readability
    plt.grid(True, linestyle='--', alpha=0.6)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    # Example data
    x_data = [5, 7, 8, 7, 6, 9, 5, 6, 7, 8]
    y_data = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

    try:
        create_scatter_plot(x_data, y_data, title="Sample Static Scatter Plot", x_label="X Values", y_label="Y Values")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
