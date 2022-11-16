import numpy as np
import matplotlib.pyplot as plt
  
# 対象データ
x = np.linspace(-np.pi * 2, np.pi * 2, 100)
y = np.sin(x)
  
# figureを生成する
fig = plt.figure()
  
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
  
# axesにplot
ax.plot(x, y, c="blue")
  
# 表示する
plt.show()