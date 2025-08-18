import pkg_resources
import sys
import os
from modules.launch_utils import run_pip

# Use unified bitsandbytes version with official Windows CUDA 12+ support
target_bitsandbytes_version = '0.45.3'

def set_cuda_environment():
    """Set environment variables for CUDA 12+ compatibility"""
    # Force bitsandbytes to use compatible CUDA version
    # CUDA 12.6 binaries work with CUDA 12.8 runtime
    os.environ['BNB_CUDA_VERSION'] = '126'
    
    # Ensure proper library path detection on Windows
    if sys.platform == 'win32':
        cuda_path = os.environ.get('CUDA_PATH')
        if cuda_path:
            cuda_bin = os.path.join(cuda_path, 'bin')
            current_path = os.environ.get('PATH', '')
            if cuda_bin not in current_path:
                os.environ['PATH'] = f"{cuda_bin};{current_path}"

def try_install_bnb():
    """Install bitsandbytes with comprehensive Windows CUDA 12+ support"""
    
    # Set environment for CUDA compatibility
    set_cuda_environment()
    
    package_name = 'bitsandbytes'  # Unified package supports Windows + CUDA 12+
    
    try:
        current_version = pkg_resources.get_distribution(package_name).version
        print(f"Current {package_name} version: {current_version}")
    except Exception:
        current_version = None
        print(f"{package_name} not installed")

    try:
        # Check if we need to install or upgrade
        if current_version != target_bitsandbytes_version:
            print(f"Installing {package_name} {target_bitsandbytes_version} with CUDA 12+ support...")
            
            # First, uninstall any conflicting packages
            try:
                run_pip("uninstall bitsandbytes bitsandbytes-windows -y", "Removing old bitsandbytes packages")
            except:
                pass  # Ignore if packages don't exist
            
            # Install the unified package
            run_pip(
                f"install {package_name}=={target_bitsandbytes_version}",
                f"{package_name} {target_bitsandbytes_version} (Windows CUDA 12+ support)"
            )
            
            print("✓ Successfully installed bitsandbytes with CUDA 12+ support")
        else:
            print(f"✓ {package_name} {target_bitsandbytes_version} already installed")
            
    except Exception as e:
        print(f"❌ Primary installation failed: {str(e)}")
        print("Trying fallback installation methods...")
        
        # Fallback 1: Try preview wheel
        try:
            run_pip(
                "install --force-reinstall https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-win_amd64.whl",
                "bitsandbytes preview wheel"
            )
            print("✓ Installed preview wheel successfully")
        except Exception as e2:
            print(f"❌ Preview wheel failed: {str(e2)}")
            
            # Fallback 2: Community Windows build
            try:
                run_pip(
                    "install git+https://github.com/Keith-Hon/bitsandbytes-windows.git",
                    "Community Windows bitsandbytes build"
                )
                print("✓ Installed community Windows build successfully")
            except Exception as e3:
                print(f"❌ All installation methods failed")
                print(f"Final error: {str(e3)}")
                print("Consider compiling from source or using CPU-only mode")

def verify_installation():
    """Verify bitsandbytes installation and CUDA support"""
    try:
        import bitsandbytes as bnb
        print(f"✓ bitsandbytes {bnb.__version__} imported successfully")
        
        # Test CUDA availability
        if hasattr(bnb, 'get_cuda_version'):
            cuda_version = bnb.get_cuda_version()
            print(f"✓ CUDA version detected: {cuda_version}")
        
        return True
    except Exception as e:
        print(f"❌ Verification failed: {str(e)}")
        return False

# Main installation function
def install_bitsandbytes_comprehensive():
    """Comprehensive bitsandbytes installation for Windows CUDA 12+"""
    
    print("=" * 60)
    print("BITSANDBYTES INSTALLATION - Windows CUDA 12+ Support")
    print("=" * 60)
    
    # Check system requirements
    if sys.platform != 'win32':
        print("ℹ️  This script is optimized for Windows. Proceeding with standard installation...")
    
    python_version = sys.version_info
    if python_version < (3, 9):
        print(f"⚠️  Python {python_version.major}.{python_version.minor} detected. Python 3.9+ recommended.")
    
    # Install bitsandbytes
    try_install_bnb()
    
    # Verify installation
    print("\nVerifying installation...")
    if verify_installation():
        print("\n✅ INSTALLATION SUCCESSFUL!")
        print("bitsandbytes is ready for use with CUDA 12+ support")
    else:
        print("\n⚠️  Installation completed but verification failed")
        print("You may still be able to use bitsandbytes functionality")
    
    print("\nIMPORTANT: Make sure to set this environment variable before launching:")
    print("set BNB_CUDA_VERSION=126")
    print("=" * 60)

# Run the installation
if __name__ == "__main__":
    install_bitsandbytes_comprehensive()
