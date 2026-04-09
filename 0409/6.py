
a = set(input("첫 번째 집합: ").split())
b = set(input("두 번째 집합: ").split())    
print("합집합:", a | b)
print("교집합:", a & b)
print("차집합 (a - b):", a - b)
print("차집합 (b - a):", b - a)
