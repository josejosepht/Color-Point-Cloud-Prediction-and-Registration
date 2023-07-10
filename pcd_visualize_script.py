# Import necessary modules and functions
import open3d as o3d
import numpy as np
from scipy.spatial.transform import Rotation
import cv2

# Import read_pfm function from utils module
from utils import read_pfm

if __name__ == "__main__":
    # Define image and depth map paths
    images = ['/home/josejt/Downloads/data/0000000030.png']
    depths = ['/home/josejt/Downloads/data/out/0000000030-dpt_beit_large_512.pfm']

    # Create Open3D visualization window
    vis = o3d.visualization.Visualizer()
    vis.create_window()

    # Define camera intrinsic parameters
    fx, fy, cx, cy = [658.94, 661.46, 325.66, 229.53]
    wd = 1242
    ht = 375

    # Read the depth map from disk in PFM format using read_pfm function
    idepth = read_pfm(depths[0])[0]

    # Normalize the depth values
    idepth = idepth - np.amin(idepth)
    idepth /= np.amax(idepth)

    # Read the image from disk using OpenCV
    image = cv2.imread(images[0])

    # Construct X, Y, and Z values for each pixel in the image
    y, x = np.meshgrid(np.arange(wd).astype(np.float32), np.arange(ht).astype(np.float32))
    X = (x - cx) / fx
    Y = (y - cy) / fy
    Z = 1 / idepth

    # Stack the X, Y, and Z values into a single array
    xyz = np.zeros((wd*ht, 3))
    xyz[:, 1] = (X*Z).reshape(-1)
    xyz[:, 0] = (Y*Z).reshape(-1)
    xyz[:, 2] = Z.reshape(-1)

    # Filter the point cloud by removing points outside of a certain depth range
    # and outside a certain region of interest
    mask = (xyz[:, 2] > 0) & (xyz[:, 2] < 5) & (abs(xyz[:, 1]) < 5) & (abs(xyz[:, 0]) < 5)
    xyz = xyz[mask]

    # Extract the colors of each pixel in the image
    colors = image.reshape(-1, 3)  # BGR
    colors = colors[:, [2, 1, 0]] / 255
    colors = colors[mask]

    # Construct an Open3D point cloud from the filtered point cloud data and the corresponding colors
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    # Add the point cloud to the Open3D visualization window
    vis.add_geometry(pcd)

    # Render the point cloud in the visualization window
    vis.run()

    # Close the visualization window
    vis.destroy_window()