import matplotlib.pyplot as plt
import numpy as np

def get_int_input(prompt, min_val=1, max_val=None):
    """Safely get an integer input from the user within optional bounds."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or (max_val is not None and value > max_val):
                print(f"Please enter a number between {min_val} and {max_val if max_val else '∞'}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("=== Dynamic Subplot Generator ===")
    num_plots = get_int_input("Enter number of subplots (1-6): ", 1, 6)

    rows = int(np.ceil(np.sqrt(num_plots)))
    cols = int(np.ceil(num_plots / rows))
    
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
    axes = np.array(axes).reshape(-1)
    
    for i in range(num_plots):
        print(f"\n--- Chart {i+1} ---")
        chart_type = input("Enter chart type (line/bar/scatter): ").strip().lower()

        n_points = get_int_input("Enter number of data points (min 2): ", 2)

        x = np.arange(1, n_points + 1)

        y = []
        for j in range(n_points):
            y_val = float(input(f"Enter Y value for point {j+1}: "))
            y.append(y_val)
        
        ax = axes[i]

        if chart_type == "line":
            ax.plot(x, y, marker='o')
        elif chart_type == "bar":
            ax.bar(x, y)
        elif chart_type == "scatter":
            ax.scatter(x, y)
        else:
            print("Invalid chart type. Defaulting to line chart.")
            ax.plot(x, y, marker='o')
        
        ax.set_title(f"Chart {i+1} ({chart_type})")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.grid(True)

    for j in range(num_plots, len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
