# 计算机视觉入门：图像处理练习

这是我的计算机视觉学习项目第 1 周。

## 文件结构

```text
week01/
├─ day01-basic-image-processing/  # 第 1 天的代码、笔记、原图和结果图
├─ .venv/                         # 本地 Python 环境，不上传到 GitHub
└─ README.md
```

## 已完成的练习

1. 读取并显示彩色图片。
2. 将彩色图片转换为灰度图。
3. 对图片进行高斯模糊处理。
4. 用 Canny 算法提取图片边缘。
5. 对比不同边缘检测参数的效果。
6. 用阈值分割生成黑白剪影图。
7. 对比不同阈值对结果的影响。

## 核心学习方法

每次实验都遵循相同流程：

```text
原始图片 → 图像处理算法 → 显示并保存新图片 → 调整参数并比较结果
```

## 使用的工具

- Python
- OpenCV
- NumPy
- Matplotlib
- Visual Studio Code

## 运行示例

先在 VS Code 中打开当天的文件夹：

```text
day01-basic-image-processing
```

然后在终端中运行：

```powershell
..\.venv\Scripts\python.exe edge_compare.py
```

## 下一步

继续学习形态学操作、图像几何变换，以及机器学习和深度学习基础。
