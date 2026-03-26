# Git

切换提交历史

```bash
git checkout 1a
```

其中1a是提交记录的tag

还原初始状态：

```bash
git reset --hard
```

拉取更新：

```bash
$ git fetch --all
$ git fetch --tags
$ git reset --hard origin/master
```

比较不同的版本：

```bash
git diff 2a 2b
```

比较tag是2a和2b版本