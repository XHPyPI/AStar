- A*寻路算法 `pip install xhAStar`

# 使用方法

```python3
import astar
w, h = 6, 3
start, goal = (0, 0), (3, 2)
walls = [(2, 1), (3, 1), (4, 1)]
obj = astar.AStar(w, h, start, goal, walls, astar.MANHATTAN)
print(obj.result)
```

AStar参数说明:

- w (int): 长
- h (int): 宽
- start (Tuple[int, int]): 起始点
- goal (Tuple[int, int]): 终点
- walls (List[Tuple[int, int]]): 墙壁坐标列表
- type (int, optional): 寻路类型. 默认为曼哈顿寻路 MANHATTAN.