import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def transform_point(R, o, plocal):
    return o + R.dot(plocal)

def plot_frame(ax, R, o, label, length=0.5):
    x_axis = o + R.dot(np.array([length, 0, 0]))
    y_axis = o + R.dot(np.array([0, length, 0]))
    z_axis = o + R.dot(np.array([0, 0, length]))

    ax.quiver(o[0], o[1], o[2], x_axis[0]-o[0], x_axis[1] - o[1], x_axis[2] - o[2], color = 'r', arrow_length_ratio = 0.1)
    ax.quiver(o[0], o[1], o[2], y_axis[0]-o[0], y_axis[1] - o[1], y_axis[2] - o[2], color = 'g', arrow_length_ratio = 0.1)
    ax.quiver(o[0], o[1], o[2], z_axis[0]-o[0], z_axis[1] - o[1], z_axis[2] - o[2], color = 'b', arrow_length_ratio = 0.1)

    ax.text(o[0], o[1], o[2], label, fontsize = 12, color = 'k')

def Rz(alpha):
    c = np.cos(alpha)
    s = np.sin(alpha)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
 
def Ry(beta):
    c = np.cos(beta)
    s = np.sin(beta)
    return np.array([[c, 0, -s], [0, 1, 0], [-s, 0, c]])


def Rx(gamma):
    c = np.cos(gamma)
    s = np.sin(gamma)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

def rpy_to_rot(roll, pitch,jaw):
    return Rz(roll).dot(Ry(pitch)).dot(Rx(jaw))

if __name__ == "__main__":
   
    roll = np.deg2rad(30)
    pitch = np.deg2rad(45)
    jaw = np.deg2rad(60)
    
    #R_z = Rz(alpha)
    #R_x = Rx(gamma)
    Rz_Rx_Ry= Rz(roll)@ Ry(pitch) @ Rx(jaw)
    R_rpy = rpy_to_rot(roll, pitch, jaw)
    print(R_rpy)
    
    fig = plt.figure(figsize=(12,6))

    # subplot 1
    ax1 = fig.add_subplot(121, projection='3d')
    plot_frame(ax1, np.eye(3), np.array([0,0,0]), "World Frame")
    plot_frame(ax1,R_rpy, np.array([0,0,0]), "R")
    
    ax1.set_title("Rz Rx Ry rotation")
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.set_zlim(0, 1)
    ax1.legend()
    plt.show()
    # ax2 = fig.add_subplot(122, projection='3d')
    # plot_frame(ax2, np.eye(3), np.array([0, 0, 0]), "World Base")
    # plot_frame(ax2, R_x, np.array([0, 0, 0]), "Rx")
"""
    ax2.set_title("Rx rotation")
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_zlim(0, 1)
    ax2.legend()
   
   """ 

  