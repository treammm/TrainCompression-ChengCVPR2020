#!/usr/bin/env python3


import argparse
import tensorflow as tf
from network import train


def main():
  args = argparse.Namespace()
  args.verbose = True
  args.train_glob = "train_images/*.png"
  args.checkpoint_dir = "train"
  args.num_filters = 128
  args.lmbda = 0.01
  args.batchsize = 8
  args.patchsize = 256
  args.last_step = 1000000
  args.preprocess_threads = 16
  
  tf.reset_default_graph()
  train(args) 

    
if __name__ == "__main__":
  main()
