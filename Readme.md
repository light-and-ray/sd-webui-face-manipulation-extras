# Face Manipulation - extras

This extension adds [avivga/zerodim](https://github.com/avivga/zerodim) zerodim-ffhq-x256 model into extras tab if [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

![](/images/ui.jpg)

**Factors:**
- **Age**: `kid, teen, adult, old`
- **Gender**: `male, female`
- **Ethnicity**: `black, white, asian`
- **Hair**: `brunette, blond, bald, red, black, white`
- **Facial hair**: `beard, mustache, goatee, shaved`
- **Glasses**: `glasses, shades, no glasses`

> [!WARNING]
> You need to have [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) installed to use it. In installer you can select only "toolkit". And after installation you need to reboot your PC
> 
> For Windows it seems that itn't compatible: https://github.com/light-and-ray/sd-webui-face-manipulation-extras/issues/2#issuecomment-2262731519
> 
> ```The error message indicates that the package aimrocks==0.5.* is not found. This package is a dependency for the aim package, which in turn is a dependency for stylegan2_pytorch.```
>
> ```The aimrocks package is a Python wrapper for the RocksDB library and is used by the aim package for storing experiment data. However, aimrocks is not compatible with Windows, which is why you're seeing this error.```

Limitations:
- 256p resolution + only aligned faces
- changes persona a bit
- changes background

### Example:
![](/images/input.jpg)

*input*

![](/images/goatee.jpg)

*goatee*

![](/images/glasses.jpg)

*glasses*

![](/images/black.jpg)

*black*

![](/images/kid.jpg)

*kid*


## Reactor

You can use [Reactor](https://github.com/Gourieff/sd-webui-reactor) to fix the persona

![](/images/reactor.jpg)
