# Day 3 笔记：远端与 Pull Request

## 远端（remote）是什么

远端只是"另一个仓库的地址 + 一个别名"。`origin` 就是默认别名。

```bash
git remote -v                        # 看别名对应哪个地址
git remote set-url origin <新地址>   # 改地址
git remote add upstream <原项目地址> # 加第二个远端（fork 场景用）
```

本地 main 和远端 main 是两条独立的线，`git push` 是把本地推上去，`git pull` 是拉下来。

`## main...origin/main` 表示两者一致；如果显示 `ahead 2` 就是本地多 2 个提交（忘了 push）。

## 分支 + PR 的正确姿势

科研项目和实验室仓库都禁止直接改 main，流程是：

1. `git switch -c feature/xxx` —— 开分支
2. 改代码，`git add` + `git commit`（可以多次）
3. `git push -u origin feature/xxx` —— 把分支推上去
4. 网页上点 **Compare & pull request**，写清"改了什么、为什么"
5. 等 review，通过后 **Merge**

## 为什么科研要这么麻烦

- 导师/师兄能在合并前看到你的每一行改动
- main 永远是可运行状态（不会因为你的半成品挂掉）
- commit 历史 = 你的工作记录，答辩和写论文时能查"哪个版本出的结果"

## 命令速记

```bash
git switch -c 分支名     # 建并切换
git push -u origin 分支名
git switch main          # 回主分支
git pull                 # 每天开工第一件事
git branch -d 分支名     # 合并后删本地分支
```
