"""
マスターオブ整数
"""
import fractions

N, X = map(int, input().split())
cities = list(map(int, input().split()))

dist = [abs(i - X) for i in cities]
division = dist[0]
for i in dist[1:]:
    division = fractions.gcd(division, i)

print(division)