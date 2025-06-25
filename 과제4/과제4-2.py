import matplotlib.pyplot as plt
import numpy as np

# 각각의 그래프 그리기
x = np.linspace(-10, 10, 400)
y1 = x**2
plt.figure(figsize=(10, 7))
plt.plot(x, y1)
plt.title('$y = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

y2 = np.sin(x)
plt.figure(figsize=(10, 7))
plt.plot(x, y2)
plt.title('$y = sin(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

y3 = np.cos(x)
plt.figure(figsize=(10, 7))
plt.plot(x, y3)
plt.title('$y = cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# tan(x) 그래프와 점근선 추가
y4 = np.tan(x)
y4[np.abs(y4) > 10] = np.nan  # 그래프가 너무 길어지는 것을 방지하기 위해 값을 NaN으로 설정
plt.figure(figsize=(10, 7))
plt.plot(x, y4)
plt.title('$y = tan(x)$')
plt.xlabel('x')
plt.ylabel('y')

# 점근선 그리기
pi = np.pi
asymptotes = np.arange(-10, 10, 1) * pi + pi/2
for a in asymptotes:
    plt.axvline(x=a, color='red', linestyle='--')  # 점근선의 색과 스타일 설정

plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.show()

# 임의의 함수 추가로 그리기
y5 = np.log(x + 11)  # x에 11을 더해 음수가 되지 않게 조정
plt.figure(figsize=(10, 7))
plt.plot(x, y5)
plt.title('$y = log(x + 11)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 모든 그래프를 하나의 창에 겹쳐서 그리기
plt.figure(figsize=(10, 7))
plt.plot(x, y1, label='$y = x^2$')
plt.plot(x, y2, label='$y = sin(x)$')
plt.plot(x, y3, label='$y = cos(x)$')
plt.plot(x, y4, label='$y = tan(x)$')  # 여기에서는 점근선을 그리지 않음
plt.plot(x, y5, label='$y = log(x + 11)$')
plt.title('Combined Graphs')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-5, 5)
plt.legend()
plt.show()


