# Manual Installation Guide for SageAttention (Standalone or within stable-diffusion-webui-reForge)

This guide explains how to manually build and install the SageAttention package, particularly when integrating it into an existing Python environment like the one used by `stable-diffusion-webui-reForge`.

## Prerequisites

1.  **Compatible Python Environment:** Ensure you have a Python environment (preferably 3.12, as 3.13 might not be supported by PyTorch versions required by SageAttention) where you can install packages. This could be your system Python, a dedicated venv, or the venv used by another project (like `stable-diffusion-webui-reForge`).
2.  **PyTorch:** A compatible version of PyTorch (e.g., `torch 2.7.1+cu128`) must already be installed in your target Python environment.
3.  **CUDA Toolkit:** Ensure the CUDA toolkit version matches the one PyTorch was compiled for (e.g., CUDA 12.8 for `torch 2.7.1+cu128`). The build process will use `nvcc` from this toolkit.
4.  **Build Tools:** Standard C++ build tools (like Visual Studio Build Tools on Windows, `gcc` on Linux) and CUDA development libraries are required to compile the CUDA extensions.
5.  **Git:** (Optional, if cloning the repo) To clone the SageAttention repository.

## Steps

1.  **Ensure PyTorch is Installed:**
    *   Verify that the correct PyTorch version is installed in your target Python environment.
        *   If not, install it. For example, for `torch 2.7.1+cu128`:
        ```bash
            # Using pip with the correct index URL for cu128 wheels
            pip install torch==2.7.1+cu128 --extra-index-url https://download.pytorch.org/whl/cu128
        ```
    *   **Note:** If you are integrating into `stable-diffusion-webui-reForge`, its venv likely already contains the required PyTorch version.
    
    2.  **Activate Your Target Environment:**
        *   Activate the Python virtual environment where PyTorch is installed and where you want SageAttention to be available.
        ```bash
            # Example for Windows venv activation
            path\to\your\venv\Scripts\activate.bat
            # Example for Linux/macOS venv activation
            # source path/to/your/venv/bin/activate
        ```
                                
    3.  **Clone and navigate to the SageAttention Directory:**
        *   Clone this sage attention repo
        ```bash
            git clone https://github.com/woct0rdho/SageAttention.git
        ```
        *   Change your current directory to the root of the cloned or downloaded SageAttention source code.
        ```bash
            cd path/to/stable-diffusion-webui-reForge/SageAttention
        ```
                    
    4.  **Install Build Dependencies:**
        *   Install the necessary Python packages required to build SageAttention. These are typically listed in `pyproject.toml` under `build-system.requires` (excluding `torch` which is already installed).
        ```bash
            pip install numpy packaging pybind11 setuptools
        ```
        *   You will also need triton:
        ```bash
            pip install triton
        ```
        *   And on Windows:
        ```bash
            pip install -U "triton-windows<3.4"
        ```

    5.  **(Optional) Update Project Configuration:**
        *   The `update_pyproject.py` script can be used to tailor `pyproject.toml` and `simpleindex.toml` for a specific PyTorch/CUDA version. This step might not be strictly necessary if PyTorch is already correctly installed, but it ensures consistency.
        *   Set the appropriate environment variables and run the script. Adjust versions (`TORCH_MINOR_VERSION`, `TORCH_PATCH_VERSION`, `CUDA_MINOR_VERSION`) as needed.
        ```bash
            # On Windows (Command Prompt style)
            set TORCH_MINOR_VERSION=7 && set TORCH_PATCH_VERSION=1 && set CUDA_MINOR_VERSION=8 && python update_pyproject.py
            # On Linux/macOS or PowerShell
            # TORCH_MINOR_VERSION=7 TORCH_PATCH_VERSION=1 CUDA_MINOR_VERSION=8 python update_pyproject.py
        ```
                                
    6.  **Build and Install the Package:**
        *   Run the `setup.py` script to compile the CUDA/C++ extensions and install the `sageattention` package into the currently active Python environment.
        ```bash
            python setup.py install
        ```
        *   **Important:** Use `python` from the activated environment. This command handles compiling the native extensions for your specific hardware and PyTorch/CUDA setup and then installs the package.
        
        ## Notes
        
        *   **Virtual Environments:** It's highly recommended to use a virtual environment to avoid dependency conflicts.
        *   **CUDA Compatibility:** Ensure your GPU and installed CUDA driver are compatible with the CUDA toolkit version used by PyTorch and required by SageAttention.
        *   **Compilation Time:** The `python setup.py install` step will compile CUDA kernels, which can take a few minutes.
        *   **Errors:** If you encounter errors during compilation, check that your CUDA installation is correct, `nvcc` is available in your PATH, and build tools are properly set up.
        *   **Cleanup:** After it installs, you can delete the cloned folder.

        By following these steps, you should have SageAttention successfully built and installed, ready to be imported and used in Python scripts within that environment.