# Generate HoG feature from testset edge images


import cv2 as cv
import scipy.io as sio
import numpy as np

# HoG parameters
win_size = (128, 128)
block_size = (32, 32)
block_stride = (32, 32)
cell_size = (32, 32)
n_bins = 9


im_h, im_w = 180, 320
save_file = 'testset_feature_HoG.mat'

hog = cv.HOGDescriptor(win_size, block_size, block_stride, cell_size, n_bins)

# database camera
data = sio.loadmat('../../data/features/testset_feature.mat')
edge_map = data['edge_map'] # (720, 1280, 1, 186)

h, w, _, n = edge_map.shape

features = []
for i in range(n):
    edge_image = edge_map[:,:,:,i]
    edge_image = cv.resize(edge_image, (im_w, im_h))
    feat = hog.compute(edge_image)
    features.append(feat)

features = np.squeeze(np.asarray(features), axis=2)

print('feature dimension {}'.format(features.shape))

sio.savemat(save_file, {'features':features,
                        'edge_map':edge_map})

print('save to file: {}'.format(save_file))
