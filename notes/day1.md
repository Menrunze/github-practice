# Day 1 笔记

## GitHub 到底是什么

Git = 装在你电脑上的**版本管理工具**（本地，不需要网）。
GitHub = 放在云端的 Git **仓库托管网站**（2008 年起，现在归 Microsoft）。

类比：Git 是 Word 的"修订记录"，GitHub 是把这些记录存在云端还带社交功能的网盘。
仓库（repository/repo）= 一个被 Git 管理的文件夹。

## 科研里为什么离不开它

| 场景 | 用到的功能 |
| --- | --- |
| 复现论文代码 | `git clone <论文作者仓库>` |
| 自己实验改坏想反悔 | `git commit` 快照 + `git diff` |
| 和师兄/组里合作 | 分支 + Pull Request |
| 记录"这个结果是哪版代码跑出来的" | commit hash |
| 交课程作业 / 放简历 | 公开仓库 + README |

## 三个区域（关键概念）

工作区（你编辑的文件） → `git add` → 暂存区（待提交清单） → `git commit` → 本地仓库（历史）

只有 `commit` 过的东西才进历史；`push` 只是把本地历史复制到 GitHub。
