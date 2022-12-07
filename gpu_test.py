import tensorflow as tf
from tensorflow.python.client import device_lib


tf.test.is_gpu_available('GPU')
print(device_lib.list_local_devices())