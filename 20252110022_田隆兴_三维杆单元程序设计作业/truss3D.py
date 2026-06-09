import numpy as np

def truss3d_element_stiffness(x1, x2, E, A):
    """
    计算三维杆单元刚度矩阵及几何参数
    x1, x2: 两个节点的坐标列表或数组 [x,y,z]
    E: 弹性模量 (Pa)
    A: 截面积 (m^2)
    返回: L, (cx,cy,cz), Ke (6x6)
    """
    x1 = np.asarray(x1, dtype=float)
    x2 = np.asarray(x2, dtype=float)
    delta = x2 - x1
    L = np.linalg.norm(delta)
    cx, cy, cz = delta / L
    # 构建 B0 矩阵 (1x6)
    B0 = np.array([-cx, -cy, -cz, cx, cy, cz])  # 形状 (6,)
    # 刚度矩阵 = (EA/L) * B0^T * B0
    Ke = (E * A / L) * np.outer(B0, B0)
    return L, (cx, cy, cz), Ke

def truss3d_element_stress(x1, x2, E, A, de):
    """
    de: 节点位移数组 [u1,v1,w1,u2,v2,w2]
    返回: epsilon, sigma, N
    """
    x1 = np.asarray(x1, dtype=float)
    x2 = np.asarray(x2, dtype=float)
    delta = x2 - x1
    L = np.linalg.norm(delta)
    cx, cy, cz = delta / L
    B0 = np.array([-cx, -cy, -cz, cx, cy, cz])
    de = np.asarray(de, dtype=float)
    delta_L = np.dot(B0, de)          # 轴向伸长
    epsilon = delta_L / L
    sigma = E * epsilon
    N = sigma * A
    return epsilon, sigma, N