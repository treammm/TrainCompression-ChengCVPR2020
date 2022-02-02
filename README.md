# Training code for "Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules"

This repository contains the **training code** for the paper [1]. We implemented the training code based on the official inference code written in `Tensorflow 1.14`. The official repository can be found at [This GitHub Repo](https://github.com/ZhengxueCheng/Learned-Image-Compression-with-GMM-and-Attention), where the authors only provided inference code. 

## Environment

- python3
- Tensorflow==1.15.0
- Tensorflow-Compression==1.3
```
pip install tensorflow-compression==1.3
```
- RangeCoder
```
pip install range-coder
```

## Usage

```
TBD
```

## Notes

If you find this useful to your reseach, feel free to cite

The original CVPR paper written by Zhengxue:
```
@inproceedings{cheng2020image,
    title={Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules},
    author={Cheng, Zhengxue and Sun, Heming and Takeuchi, Masaru and Katto, Jiro},
    booktitle= "Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)",
    year={2020}
}
```

And of course, our preprint paper based on her work:
```
TBD
```

## Reference
[1] Zhengxue Cheng et al. "Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules," in *Proc. IEEE Conf. Comput. Vision Pattern Recog.*, Jul. 2020, pp. 7939–7948.
