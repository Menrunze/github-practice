"""环境自检脚本：conda 建好后运行 python env_check.py

用途：确认 Python 版本、关键库、GPU 是否就绪。
科研里复现别人代码前，先跑一遍这个，比事后 debug 省很多时间。
"""
import platform
import sys


def main() -> None:
    print("=" * 46)
    print(f"Python 版本 : {sys.version.split()[0]}")
    print(f"解释器路径  : {sys.executable}")
    print(f"操作系统    : {platform.system()} {platform.release()}")
    print("=" * 46)

    libs = ["numpy", "pandas", "matplotlib", "torch", "sklearn"]
    for name in libs:
        try:
            mod = __import__(name)
            print(f"{name:<12} OK   {getattr(mod, '__version__', '?')}")
        except ImportError:
            print(f"{name:<12} 未安装")

    try:
        import torch

        print("-" * 46)
        print(f"CUDA 可用   : {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"GPU         : {torch.cuda.get_device_name(0)}")
            print(f"CUDA 版本   : {torch.version.cuda}")
        else:
            print("（无 GPU 时 PyTorch 会跑在 CPU 上，小实验完全够用）")
    except ImportError:
        pass

    print("=" * 46)
    print("自检结束")


if __name__ == "__main__":
    main()
