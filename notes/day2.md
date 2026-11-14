# Day 2 笔记

## clone 一个论文仓库的正确姿势

    git clone https://github.com/作者/仓库名.git
    cd 仓库名
    git checkout <tag 或 commit>   # 别只看 main，论文一般对应某个固定版本
    cat README.md                  # 先看环境要求
    conda env create -f environment.yml
