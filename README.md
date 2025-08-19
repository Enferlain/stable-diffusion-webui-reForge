# Personal fork with random stuff I come up with, if useful will pr back to upstream

# Stable Diffusion WebUI reForge2
reForge continuation based on latest forge2.

Stable Diffusion WebUI Forge is a platform on top of [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (based on [Gradio](https://www.gradio.app/) <a href='https://github.com/gradio-app/gradio'><img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>) to make development easier, optimize resource management, speed up inference, and study experimental features.

The name "Forge" is inspired from "Minecraft Forge". This project is aimed at becoming SD WebUI's Forge.

Forge is currently based on SD-WebUI 1.10.1 at [this commit](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/82a973c04367123ae98bd9abdf80d9eda9b910e2). (Because original SD-WebUI is almost static now, Forge will sync with original WebUI every 90 days, or when important fixes.)

# Forge2/reForge2

You can read more on https://github.com/Panchovix/stable-diffusion-webui-reForge/discussions/377#discussioncomment-14010687. You can tell me here if you want to keep these branches here or do something like "reForge2".

* newmain_newforge: Based on latest forge2 (gradio4, flux, etc) with some small changes that I plan to add very slowly. For now it has python 3.12 support, sage/flash attention support, all the samplers and schedulers from reForge (1), and recently, support for CFG++ samplers.
* newforge_dendev: Based on latest ersatzForge fork which is based on forge2 (gradio4, flux, chroma, cosmos, longclip, and a ton more) from @DenOfEquity (https://github.com/DenOfEquity/ersatzForge). Many thanks Den for letting me to work on base on your fork on reForge. I will try to add new features from old reforge as well, like all the samplers.

# Suggestion: For stability based on old forge, use forge classic

reForge(1) is not really stable for all tasks sadly.

So if you want to keep using old forge backend as it is, for sd1.x,2.x and SDXL, I suggest to use forge classic by @Haoming02 instead https://github.com/Haoming02/sd-webui-forge-classic, as at the moment that is the real succesor to old forge.

Other branches:
* main: Main branch with multiple changes and updates. But not stable as main-old branch.
* dev: Similar to main but with more unstable changes. I.e. using comfy/ldm_patched backend for sd1.x and sdxl instead of A1111.
* dev2: More unstable than dev, for now same as dev.
* experimental: same as dev2 but with gradio 4.
* main-old: Branch with old forge backend. Possibly the most stable and older one (2025-03)

# Quick List

[Gradio 4 UI Must Read (TLDR: You need to use RIGHT MOUSE BUTTON to move canvas!)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/853)

[Flux Tutorial (BitsandBytes Models, NF4, "GPU Weight", "Offload Location", "Offload Method", etc)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/981)

[Flux Tutorial 2 (Seperated Full Models, GGUF, Technically Correct Comparison between GGUF and NF4, etc)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1050)

[Forge Extension List and Extension Replacement List (Temporary)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1754)

[How to make LoRAs more precise on low-bit models; How to Skip" Patching LoRAs"; How to only load LoRA one time rather than each generation; How to report LoRAs that do not work](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1038)

[Report Flux Performance Problems (TLDR: DO NOT set "GPU Weight" too high! Lower "GPU Weight" solves 99% problems!)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1181)

[How to solve "Connection errored out" / "Press anykey to continue ..." / etc](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1474)

[(Save Flux BitsandBytes UNet/Checkpoint)](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/1224#discussioncomment-10384104)

[LayerDiffuse Transparent Image Editing](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/854)

[Tell us what is missing in ControlNet Integrated](https://github.com/lllyasviel/stable-diffusion-webui-forge/discussions/932)

# UV Support for Faster Installation

This repository now supports [uv](https://github.com/astral-sh/uv) for significantly faster package installation and virtual environment creation.

To use uv instead of pip, you can add the `--use-uv` flag to your `webui-user.bat` file.

Open `webui-user.bat` and add `--use-uv` to the `COMMANDLINE_ARGS` variable, for example:

```bat
set COMMANDLINE_ARGS=--use-uv --api --theme dark
```

Alternatively, you can launch `webui.bat` with the flag:

```bash
# On Windows
webui.bat --use-uv
```

Benefits:
- Much faster package installation
- Faster virtual environment creation
- Automatic fallback to pip if uv is not available
- No configuration required

See [docs/uv_support.md](docs/uv_support.md) for more details.
