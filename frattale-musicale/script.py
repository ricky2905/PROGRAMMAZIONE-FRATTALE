import matplotlib.pyplot as plt
import numpy as np

def recursive_plot(level, x=0, y=0, size=1):
    """Disegna un frattale musicale semplice ricorsivo."""
    if level == 0:
        return
    plt.plot([x, x+size], [y, y], color='blue')
    plt.plot([x+size, x+size], [y, y+size], color='red')
    plt.plot([x+size, x], [y+size, y+size], color='green')
    plt.plot([x, x], [y+size, y], color='orange')
    recursive_plot(level-1, x+size/4, y+size/4, size/2)

def main():
    plt.figure(figsize=(6,6))
    recursive_plot(5)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()

