# 计算机导论大作业——五子棋

计试2101仲星焱 2215112536

## 环境

使用了windows simhei.ttf 字体库，请确保“C:/Windows/Fonts/simhei.ttf”存在

windows 11下 安装 pygame ：pip install pygame

安装后打开 Gomoku.py即可运行

## 运行方式

鼠标左键单机未落子的位置即可。

## 实现方式

使用了 pygame 库的工具来获取鼠标的位置，计算得到用户落子的位置，落子后计算是否存在五子连线的情况来判断胜负。

可以修改代码中 CONSNUM 的值来将游戏规则修改为需要其他数量的棋子连成一线方胜利