print("\nSphere & Hemisphere All formulas Solution : ")
r = float(input("\nEnter radius : "))
s_s = 4 * 3.14 * r * r
s_v = 4 / 3 * 3.14 * r * r
s_t = 4 * 3.14 * r * r
s_d = 2*r

h_s = 2 * 3.14 * r * r
h_v = 2 / 3 * 3.14 * r  * r * r
h_t = 3 * 3.14 * r * r
h_b = 3.14 * r * r

print("\nSolution of all formulas of Sphere : - ")
print("\tDiameter of Sphere : ",s_d)
print("\tSurface are of Sphere :",s_s)
print("\tVolume of Sphere : ", s_v)
print("\tTotal Surface area of Sphere : ", s_t)

print("\nSolution of all formulas of Hemisphere : - ")
print("\tBase area of Hemiphere : ",h_b)
print("\tSurface are of Hemiphere :",h_s)
print("\tVolume of Hemiphere : ", h_v)
print("\tTotal Surface area of Sphere : ", h_t)
