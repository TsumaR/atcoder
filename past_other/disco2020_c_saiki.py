import numpy as np

H, W, K = map(int, input().split())

A = np.array([list(input()) for _ in range(H)])
ans = np.array([[0] * W for _ in range(H)])