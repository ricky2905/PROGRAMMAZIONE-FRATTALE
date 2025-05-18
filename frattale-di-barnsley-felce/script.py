import random
import matplotlib.pyplot as plt

def barnsley_fern(iterations):
    """Genera punti del felce di Barnsley usando IFS"""
    x, y = 0, 0
    points_x, points_y = [], []
    for _ in range(iterations):
        r = random.random()
        if r < 0.01:
            x, y = 0, 0.16*y
        elif r < 0.86:
            x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
        elif r < 0.93:
            x, y = 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
        else:
            x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
        points_x.append(x)
        points_y.append(y)
    return points_x, points_y

def main():
    x, y = barnsley_fern(100000)
    plt.scatter(x, y, s=0.2, color='green')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()

