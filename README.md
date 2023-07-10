# Color-Point-Cloud-Prediction-and-Registration
Project compares inferences run using state-of-the-art networks, PackNet, MiDaS, and RAFT-Stereo for monocular and stereo depth estimation, followed by point cloud reprojection and registration for dense 3D environment representation.

Monocular depth estimation was done using two state-of-the-art networks, PackNet and MiDaS, which have shown promising results in estimating accurate depth maps from single monocular images. Additionally, a stereo depth estimation network, RAFT-Stereo, was implemented, which utilizes stereo image pairs to estimate depth maps. The obtained depth maps were then projected onto a 3D point cloud representation through point cloud reprojection, allowing for a dense 3D representation of the environment.

The following GitHub repositories were used for the implementation of this project:

PackNet : https://github.com/TRI-ML/vidar

MiDaS : https://github.com/isl-org/MiDaS

RAFT-Stereo : https://github.com/princeton-vl/RAFT-Stereo

## PackNet Inference
As the initial experiment, the PackNet implementation was evaluated on the KITTI dataset and then tested with a calibrated Logitech camera. The self-supervised network was pre-trained using the training set in KITTI and weights released along with the source code. This was downloaded and imported onto the default model and was used to evaluate on the test set. The images in KITTI were resized to a smaller dimension, i.e, 192x640 for all training and evaluation purposes. The output, which were depth images for all the input files, were saved and visualized. The single channel depth map was of the same size as the input with each pixel denoting depth at that point in meters.

![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/2bebe554-4542-4519-a826-9dcc141425f5)


## MiDaS Inference
The depth maps recieved in PackNet were not very accurate for point cloud reprojection and moreover were running at 4 frames per second. the next inference was run using MiDaS as the authors had claimed that the models were generalized across different environments and also could run in real-time. The environment setup was using DROID-CAM which connects an iPhone camera and our local PC to run inference in real-time. The input images were full scale, at 640x480 resolution and the output depth maps had the same resolution. But the important thing to be noticed here is that MiDaS could generalize between different contexts and different resolutions across datasets.

![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/4bb4cc93-96ac-466b-b638-875c18786880)

https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/5add4a24-e4c3-4391-9822-2f5f1e4995d2


## RAFT-Stereo Inference
Both of the monocular networks tested were able to produce viable point clouds for registration.The next inference was to be run using a stereo options, out of which RAFT-Stereo stood out as a promising option. RAFT uses optical flow between stereo pairs to predict disparity maps. This fact helped RAFT produce much better and accurate disparity maps, which in turn gave better point clouds which could be used further down the pipeline. The input to this model would be stereo pairs of images in full scale, at 1242x375 for the KITTI dataset. Inference time clocked at about 2 frames per second to get the disparity maps. We also note that there was a trade-off between frame rate and accuracy, to get better point clouds.

![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/5f2af9dd-ef6c-4d9d-9e0e-685d96203c1a)
![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/8cee20fd-b066-47a0-a55e-73aa41ce26b7)
![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/49383160-2ed3-41a0-8c54-8f485044f4a0)

## Point cloud registration
![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/2e10c7e6-fa8f-428a-8627-01228ba066b5)

https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/174a9cbf-914e-4352-bf8c-7eb0cd1b65cb

![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/2d00c7bb-4778-4c5b-8a03-7a34a7a425cf)
![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/8495071a-1578-41cf-ae5e-344cb344c60f)
![image](https://github.com/josejosepht/Color-Point-Cloud-Prediction-and-Registration/assets/97187460/dfe94c49-06c2-484a-a20e-ad21b1c09461)
