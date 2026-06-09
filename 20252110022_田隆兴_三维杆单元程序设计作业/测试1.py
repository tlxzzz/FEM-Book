
import numpy as np
import truss3D

# 算例1
x1 = [0,0,0]
x2 = [2,0,0]
E = 200e9
A = 1e-4
de = [0,0,0,1e-3,0,0]

# 调用函数
eps, sig, N = truss3D.truss3d_element_stress(x1, x2, E, A, de)
L, (cx, cy, cz), Ke = truss3D.truss3d_element_stiffness(x1, x2, E, A)
print("=" * 60)
print("算例1：沿 x 轴的一维杆单元验证结果")
print("=" * 60)

# 1. 单元长度
print(f"1.  L = {L:.6f} m ")

# 2. 方向余弦
print(f"2. 方向余弦({cx:.6f}, {cy:.6f}, {cz:.6f}) ")

# 3. 刚度矩阵退化检验
print(f"刚度矩阵：Ke = \n{Ke} ")

# 4. 轴向应变
print(f"4. 轴向应变 ε = {eps:.6e} ")
# 5. 轴向应力
sig_MPa = sig / 1e6
print(f"5. 轴向应力 σ = {sig_MPa:.2f} MPa ")
# 6. 轴力
print(f"6. 轴力 N = {N:.2f} N ")
print("=" * 60)