
import numpy as np
import truss3D

# 算例2
x1 = [0.0, 0.0, 0.0]
x2 = [1.0, 2.0, 2.0]
E = 210e9      # 210 GPa
A = 2.0e-4     # 2e-4 m^2
de = [0.0, 0.0, 0.0, 1.0e-3, 2.0e-3, 2.0e-3]

# 调用函数
eps, sig, N = truss3D.truss3d_element_stress(x1, x2, E, A, de)
L, (cx, cy, cz), Ke = truss3D.truss3d_element_stiffness(x1, x2, E, A)
print("=" * 60)
print("算例2：空间任意⽅向杆单元")
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