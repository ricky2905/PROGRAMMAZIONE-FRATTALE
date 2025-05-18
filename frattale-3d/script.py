import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sierpinski_tetrahedron(order, points):
    """Genera punti per il tetraedro di Sierpinski"""
    import random
    vertices = [(0,0,0), (1,0,0), (0.5,0.87,0), (0.5,0.29,0.82)]
    p = (0.25, 0.25, 0.25)
    result = []
    for _ in range(points):
        v = vertices[random.randint(0,3)]
        p = tuple([(p[i]+v[i])/2 for i in range(3)])
        result.append(p)
    return zip(*result)

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = sierpinski_tetrahedron(5, 10000)
    ax.scatter(x, y, z, s=0.1, color='purple')
    plt.show()

if __name__ == "__main__":
    main()

