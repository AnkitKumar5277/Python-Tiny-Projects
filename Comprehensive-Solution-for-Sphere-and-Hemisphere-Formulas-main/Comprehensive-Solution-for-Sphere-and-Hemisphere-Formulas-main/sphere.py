import math

def sphere_formulas(radius):
    # Formulas for Sphere
    surface_area = 4 * math.pi * radius * radius
    volume = (4 / 3) * math.pi * radius ** 3
    total_surface_area = 4 * math.pi * radius ** 2
    diameter = 2 * radius
    
    return surface_area, volume, total_surface_area, diameter

def hemisphere_formulas(radius):
    # Formulas for Hemisphere
    surface_area = 2 * math.pi * radius ** 2
    volume = (2 / 3) * math.pi * radius ** 3
    base_area = math.pi * radius ** 2
    total_surface_area = 3 * math.pi * radius ** 2
    
    return surface_area, volume, base_area, total_surface_area

def main():
    print("\nSphere & Hemisphere Formulas:")
    radius = float(input("\nEnter the radius: "))
    
    # Calculating sphere formulas
    s_surface, s_volume, s_total_surface, s_diameter = sphere_formulas(radius)
    
    # Calculating hemisphere formulas
    h_surface, h_volume, h_base_area, h_total_surface = hemisphere_formulas(radius)
    
    # Outputting results
    print("\nSphere:")
    print(f"\tDiameter: {s_diameter}")
    print(f"\tSurface Area: {s_surface}")
    print(f"\tVolume: {s_volume}")
    print(f"\tTotal Surface Area: {s_total_surface}")
    
    print("\nHemisphere:")
    print(f"\tBase Area: {h_base_area}")
    print(f"\tSurface Area: {h_surface}")
    print(f"\tVolume: {h_volume}")
    print(f"\tTotal Surface Area: {h_total_surface}")

if __name__ == "__main__":
    main()
