import cv2
import numpy as np
from config import config
import os
from gen_traininig_data import gen_labels
from gen_mtcnn_data import gen_12net_data, gen_24net_data, gen_48net_data
from gen_mtcnn_data import gen_imglist_pnet  #, gen_imglist_rnet, gen_imglist_onet
from gen_pnet_tfrecords import gen_pnet_tfrecords
from gen_rnet_tfrecords import gen_rnet_tfrecords
from gen_onet_tfrecords import gen_onet_tfrecords
from train_pnet import train_pnet
from train_mtcnn_nets import train_pnet, train_rnet, train_onet

train_dir = config.ROOT_DIR + '/data/train/images/'
val_dir = config.ROOT_DIR + '/data/val/images/'
train_labels = config.ROOT_DIR + '/data/train/opencv_labels.csv'
# val_images = os.listdir(val_dir)

mtcnn_datadir = config.ROOT_DIR + '/data/train/'
gen_labels(train_dir, train_labels)

""" Train PNet: prepare data + model training """
gen_12net_data(anno_file=train_labels, save_dir=os.path.join(mtcnn_datadir, '12'))
gen_imglist_pnet(mtcnn_datadir)
gen_pnet_tfrecords(dataset_dir=mtcnn_datadir, output_dir=os.path.join(mtcnn_datadir, 'imglists/'))

# train_pnet()


""" Train RNet: prepare data + model training """
gen_24net_data(anno_file=train_labels + '.format2')
# gen_rnet_tfrecords(dataset_dir=mtcnn_datadir, output_dir=os.path.join(mtcnn_datadir, 'imglists_noLM/RNet'))

""" Train ONet: prepare data + model training """
# gen_onet_tfrecords(dataset_dir=mtcnn_datadir, output_dir=os.path.join(mtcnn_datadir, 'imglists/ONet'))


