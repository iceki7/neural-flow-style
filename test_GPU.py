import tensorflow as tf
print('--------------------zxc start--------------------------------')
print(tf.__version__)

gpus=tf.config.list_physical_devices('GPU')
print("----zxc GPU state")
print(gpus)

gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
cpus = tf.config.experimental.list_physical_devices(device_type='CPU')
print(gpus, cpus)

print(tf.test.is_gpu_available())
print(tf.test.is_built_with_cuda()) #作者：正版_月华JUN https://www.bilibili.com/read/cv22047241/ 出处：bilibili
exit(0)