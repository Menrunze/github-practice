# github-practice

我的第一个 Git 仓库。目标：把 GitHub 上"看得懂、改得动、推得上去"跑通一遍。

## 我在练什么

1. `git init` —— 把一个普通文件夹变成 Git 仓库（多了一个 `.git/` 隐藏目录，里面是全部历史）
2. `git add` + `git commit` —— 把改动存成一个个快照
3. `git branch` + `git merge` —— 开分支做事、做完合回来
4. `git remote` + `git push` —— 把本地历史同步到 GitHub
5. `git clone` —— 把别人的仓库（比如一篇论文的官方代码）搬到自己电脑

## 几条日常命令

```bash
git status          # 现在改了什么？（最常用，先看它）
git diff            # 具体改了哪几行
git add .           # 把改动放进"待提交"
git commit -m "说明" # 存一个快照
git log --oneline   # 看过往快照
git push            # 传到 GitHub
```

## 备注

- 作者：Mark（北京大学，智能方向大二）
- 这个仓库同时是我的学习笔记，commit 记录就是学习轨迹。
