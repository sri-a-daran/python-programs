import math
init_degree = 0
final_degree = 90
step_degree = 15
print(f"{'Angle (°)':>10} {'Sine':>10} {'Cosine':>10}")
print("-" * 32)
for angle in range(init_degree, final_degree + 1, step_degree):
    rad = math.radians(angle)  
    sine= math.sin(rad)
    cosine= math.cos(rad)
    print(f"{angle:10} {sine:10.4f} {cosine:10.4f}")
