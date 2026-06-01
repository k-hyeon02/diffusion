import numpy as np
import matplotlib.pyplot as plt

T = 10.0
dt = 0.001
N = int(T / dt)

x = np.zeros(N)
x[0] = 2.0

for i in range(N - 1):
    drift_coe = -1  # drift 항 계수
    drift = drift_coe * x[i]  # drift 항
    diffusion = 0.5  # diffusion 항 계수
    noise = np.random.randn()  # 평균=0, 분산=1인 정규분포에서 랜덤한 수 
    x[i + 1] = x[i] + drift * dt + diffusion * np.sqrt(dt) * noise

t = np.linspace(0, T, N)

plt.plot(t, x)
plt.xlabel("time")
plt.ylabel("x(t)")
plt.title(f"Example SDE: dx = {drift_coe}x dt + {diffusion} dw")
plt.show()