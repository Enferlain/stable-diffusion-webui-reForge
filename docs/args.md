# Complete Command-Line Argument List

This document contains a complete list of all command-line arguments available for this application, combined from both the standard and backend argument definition files.

## Standard Arguments
*Defined in `modules/cmd_args.py`*

*   `--update-all-extensions`: launch.py argument: download updates for all extensions when starting the program
*   `--skip-python-version-check`: launch.py argument: do not check python version
*   `--skip-torch-cuda-test`: launch.py argument: do not check if CUDA is able to work properly
*   `--reinstall-xformers`: launch.py argument: install the appropriate version of xformers even if you have some version already installed
*   `--reinstall-torch`: launch.py argument: install the appropriate version of torch even if you have some version already installed
*   `--update-check`: launch.py argument: check for updates at startup
*   `--test-server`: launch.py argument: configure server for testing
*   `--log-startup`: launch.py argument: print a detailed log of what's happening at startup
*   `--skip-prepare-environment`: launch.py argument: skip all environment preparation
*   `--skip-google-blockly`: launch.py argument: do not initialize google blockly modules
*   `--skip-install`: launch.py argument: skip installation of packages
*   `--use-uv`: launch.py argument: use uv instead of pip for package installation
*   `--dump-sysinfo`: launch.py argument: dump limited sysinfo file (without information about extensions, options) to disk and quit
*   `--loglevel`: log level; one of: CRITICAL, ERROR, WARNING, INFO, DEBUG
*   `--do-not-download-clip`: do not download CLIP model even if it's not included in the checkpoint
*   `--data-dir`: base path where all user data is stored
*   `--models-dir`: base path where models are stored; overrides --data-dir
*   `--config`: path to config which constructs model
*   `--ckpt`: path to checkpoint of stable diffusion model; if specified, this checkpoint will be added to the list of checkpoints and loaded
*   `--ckpt-dir`: Path to directory with stable diffusion checkpoints
*   `--vae-dir`: Path to directory with VAE files
*   `--text-encoder-dir`: Path to directory with text encoder models
*   `--gfpgan-dir`: GFPGAN directory
*   `--gfpgan-model`: GFPGAN model file name
*   `--no-half`: do not switch the model to 16-bit floats
*   `--no-half-vae`: do not switch the VAE model to 16-bit floats
*   `--no-progressbar-hiding`: do not hide progressbar in gradio UI (we hide it because it slows down ML if you have hardware acceleration in browser)
*   `--embeddings-dir`: embeddings directory for textual inversion (default: embeddings)
*   `--textual-inversion-templates-dir`: directory with textual inversion templates
*   `--hypernetwork-dir`: hypernetwork directory
*   `--localizations-dir`: localizations directory
*   `--allow-code`: allow custom script execution from webui
*   `--medvram`: enable stable diffusion model optimizations for sacrificing a little speed for low VRM usage
*   `--medvram-sdxl`: enable --medvram optimization just for SDXL models
*   `--lowvram`: enable stable diffusion model optimizations for sacrificing a lot of speed for very low VRM usage
*   `--lowram`: load stable diffusion checkpoint weights to VRAM instead of RAM
*   `--precision`: evaluate at this precision
*   `--upcast-sampling`: upcast sampling. No effect with --no-half. Usually produces similar results to --no-half with better performance while using less memory.
*   `--share`: use share=True for gradio and make the UI accessible through their site
*   `--ngrok`: ngrok authtoken, alternative to gradio --share
*   `--enable-insecure-extension-access`: enable extensions tab regardless of other options
*   `--xformers`: enable xformers for cross attention layers
*   `--force-enable-xformers`: enable xformers for cross attention layers regardless of whether the checking code thinks you can run it; do not make bug reports if this fails to work
*   `--listen`: launch gradio with 0.0.0.0 as server name, allowing to respond to network requests
*   `--port`: launch gradio with given server port, you need root/admin rights for ports < 1024, defaults to 7860 if available
*   `--ui-config-file`: filename to use for ui configuration
*   `--hide-ui-dir-config`: hide directory configuration from webui
*   `--freeze-settings`: disable editing of all settings globally
*   `--ui-settings-file`: filename to use for ui settings
*   `--gradio-debug`: launch gradio with --debug option
*   `--gradio-auth`: set gradio authentication like "username:password"
*   `--gradio-auth-path`: set gradio authentication file path
*   `--gradio-allowed-path`: add path to gradio's allowed_paths
*   `--opt-channelslast`: change memory type for stable diffusion to channels last
*   `--styles-file`: path or wildcard path of styles files, allow multiple entries.
*   `--autolaunch`: open the webui URL in the system's default browser upon launch
*   `--theme`: launches the UI with light or dark theme
*   `--use-textbox-seed`: use textbox for seeds in UI (no up/down, but possible to input long seeds)
*   `--disable-console-progressbars`: do not output progressbars to console
*   `--vae-path`: Checkpoint to use as VAE; setting this argument disables all settings related to VAE
*   `--disable-safe-unpickle`: disable checking pytorch models for malicious code
*   `--api`: use api=True to launch the API together with the webui (use --nowebui instead for only the API)
*   `--api-auth`: Set authentication for API like "username:password"
*   `--api-log`: use api-log=True to enable logging of all API requests
*   `--nowebui`: use api=True to launch the API instead of the webui
*   `--ui-debug-mode`: Don't load model to quickly launch UI
*   `--device-id`: Select the default CUDA device to use
*   `--administrator`: Administrator rights
*   `--cors-allow-origins`: Allowed CORS origin(s) in the form of a comma-separated list (no spaces)
*   `--cors-allow-origins-regex`: Allowed CORS origin(s) in the form of a single regular expression
*   `--tls-keyfile`: Partially enables TLS, requires --tls-certfile to fully function
*   `--tls-certfile`: Partially enables TLS, requires --tls-keyfile to fully function
*   `--disable-tls-verify`: When passed, enables the use of self-signed certificates.
*   `--server-name`: Sets hostname of server
*   `--no-gradio-queue`: Disables gradio queue; causes the webpage to use http requests instead of websockets
*   `--no-hashing`: disable sha256 hashing of checkpoints to help loading performance
*   `--no-download-sd-model`: don't download SD1.5 model even if no model is found in --ckpt-dir
*   `--disable-all-extensions`: prevent all extensions from running regardless of any other settings
*   `--disable-extra-extensions`: prevent all extensions except built-in from running regardless of any other settings

## Advanced Backend Arguments
*Defined in `backend/args.py`*

#### Floating Point Precision
*   `--all-in-fp32`: Use full 32-bit precision for everything.
*   `--all-in-fp16`: Use half 16-bit precision for everything.
*   `--unet-in-bf16`: Use bf16 precision for the UNet.
*   `--unet-in-fp16`: Use fp16 precision for the UNet.
*   `--unet-in-fp8-e4m3fn`: Use 8-bit precision for the UNet.
*   `--unet-in-fp8-e5m2`: Use a different 8-bit precision for the UNet.
*   `--vae-in-fp16`: Use fp16 for the VAE.
*   `--vae-in-fp32`: Use fp32 for the VAE.
*   `--vae-in-bf16`: Use bf16 for the VAE.
*   `--clip-in-fp8-e4m3fn`: Use 8-bit for the CLIP model.
*   `--clip-in-fp8-e5m2`: Use a different 8-bit for the CLIP model.
*   `--clip-in-fp16`: Use fp16 for the CLIP model.
*   `--clip-in-fp32`: Use fp32 for the CLIP model.
*   `--allow-fp16-accumulation`: Enable FP16 accumulation in cuBLAS operations.

#### Attention Mechanisms
*   `--attention-split`: Use Split Attention.
*   `--attention-quad`: Use Quad Attention.
*   `--attention-pytorch`: Use the default PyTorch attention.
*   `--use-sage-attention`: Use SAGE Attention.
*   `--use-sage-attention3`: Use SAGE Attention 3 (for Blackwell GPUs).
*   `--use-flash-attention`: Use FlashAttention.
*   `--disable-xformers`: Explicitly disable xformers.

#### Memory & CUDA
*   `--cuda-malloc`: (No help text provided, but likely enables CUDA's memory allocator).
*   `--cuda-stream`: (No help text provided, but likely enables CUDA Streams for parallel operations).
*   `--pin-shared-memory`: (No help text provided, likely pins memory for faster data transfer).
*   `--always-gpu`: Force all models to stay on the GPU.
*   `--always-high-vram`: Corresponds to the High VRAM setting in the UI.
*   `--always-normal-vram`: Corresponds to the Normal VRAM setting.
*   `--always-low-vram`: Corresponds to the Low VRAM setting.
*   `--always-no-vram`: Corresponds to the "No VRAM" (CPU) setting.
*   `--always-cpu`: Force everything to the CPU.
*   `--always-offload-from-vram`: Always offload models from VRAM when they're not in active use.
*   `--vae-in-cpu`: Force the VAE to run on the CPU.

#### Device & Platform
*   `--gpu-device-id <ID>`: Specify which GPU to use.
*   `--directml [DEVICE_ID]`: Use DirectML for AMD/Intel GPUs on Windows.
*   `--disable-ipex-hijack`: Disable Intel Extension for PyTorch hijacking.

#### Other Optimizations
*   `--force-upcast-attention`: Force attention upcasting.
*   `--disable-attention-upcast`: Disable attention upcasting.
*   `--pytorch-deterministic`: Try to make PyTorch operations deterministic (less random).
*   `--disable-gpu-warning`: Disable the GPU warning.
