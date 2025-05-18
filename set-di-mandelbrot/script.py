import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """Calcola il set di Mandelbrot per un'area e risoluzione dati"""
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            c = complex(r1[i], r2[j])
            z = 0
            iter = 0
            while abs(z) <= 2 and iter < max_iter:
                z = z*z + c
                iter += 1
            n3[i,j] = iter
    return n3.T

def main():
    mandelbrot_image = mandelbrot_set(-2.0, 1.0, -1.5, 1.5, 800, 800, 100)
    plt.imshow(mandelbrot_image, cmap='inferno', extent=(-2,1,-1.5,1.5))
    plt.colorbar()
    plt.title("Set di Mandelbrot")
    plt.show()

if __name__ == "__main__":
    main()

