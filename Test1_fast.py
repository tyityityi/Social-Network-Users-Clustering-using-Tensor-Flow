import classify_image_fast as classify
import csv
import argparse
import LoadImage
import time
import gc
import importlib
import tensorflow as tf
import time


# f = urlopen('http://tva4.sinaimg.cn/crop.0.0.180.180.50/67c2fbe9jw1e8qgp5bmzyj2050050aa8.jpg')

def Classifier(path, min, max):
    id, img = LoadImage.getImage(path, min, max)

    classify.FLAGS = None
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model_dir',
        type=str,
        default='/tmp/imagenet',
        help="""\
                  Path to classify_image_graph_def.pb,
                  imagenet_synset_to_human_label_map.txt, and
                  imagenet_2012_challenge_label_map_proto.pbtxt.\
                  """
    )
    parser.add_argument(
        '--image_file',
        type=str,
        default='',
        help='Absolute path to image file.'
    )
    parser.add_argument(
        '--num_top_predictions',
        type=int,
        default=1,
        help='Display this many predictions.'
    )
    classify.FLAGS, unparsed = parser.parse_known_args()

    classify.maybe_download_and_extract()
    image = []
    for i in range(min, max):
        # TODO
        image.append(path + '/img/' + str(i) + '.jpg')
    with tf.Graph().as_default():
        classify.run_inference_on_image(id, image, img, min, max)


if __name__ == '__main__':
    print(time.time())
    Classifier('./', 150000, 160000)
    print(time.time())
    # print(id[4], img[105], genre, score)
