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

⚠️ You need to have [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) installed to use it. In installer you can select only "toolkit". And after installation you need to reboot your PC

For Windows it also requires **sd-webui 1.10** (i.e. [this patch](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/16231/files) add `call "%VENV_DIR%\Scripts\activate.bat"` in `webui.bat`)

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
