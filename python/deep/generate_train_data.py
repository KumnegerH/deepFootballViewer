import sys
sys.path.append('../')

import scipy.io as sio
from util.synthetic_util import SyntheticUtil

data = sio.loadmat('../../data/worldcup_sampled_cameras.mat')
pivot_cameras = data['pivot_cameras']
positive_cameras = data['positive_cameras']

n = 10000  # change this number to set training dataset
save_file = 'train_data_10k.mat'
pivot_cameras = pivot_cameras[0:n, :]
positive_cameras = positive_cameras[0:n,:]



data = sio.loadmat('../../data/worldcup2014.mat')
print(data.keys())
model_points = data['points']
model_line_index = data['line_segment_index']

pivot_images, positive_images = SyntheticUtil.generate_database_images(pivot_cameras, positive_cameras,
                                                         model_points, model_line_index)

#print('{} {}'.format(pivot_images.shape, positive_images.shape))
sio.savemat(save_file, {'pivot_images':pivot_images,
                                  'positive_images':positive_images,
                                   'cameras':pivot_cameras})
print('save training file to {}'.format(save_file))