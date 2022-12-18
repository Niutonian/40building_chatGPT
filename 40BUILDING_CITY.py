import bpy
import random

# Set the number of houses to generate
num_houses = 40

# Set the dimensions of the city
city_width = 100
city_depth = 100

# Set the maximum size of each house
max_house_width = 10
max_house_depth = 10
max_house_height = 10

# Set the minimum distance between houses
min_house_spacing = 2

# Set the materials for the houses
roof_material = bpy.data.materials.new(name="Roof Material")
roof_material.diffuse_color = (0.8, 0.6, 0.4, 1)
wall_material = bpy.data.materials.new(name="Wall Material")
wall_material.diffuse_color = (0.9, 0.9, 0.9, 1)

# Generate the houses
for i in range(num_houses):
    # Generate a random size for the house
    house_width = random.uniform(1, max_house_width)
    house_depth = random.uniform(1, max_house_depth)
    house_height = random.uniform(1, max_house_height)
    
    # Generate a random position for the house
    house_x = random.uniform(-city_width/2, city_width/2)
    house_y = 0
    house_z = random.uniform(-city_depth/2, city_depth/2)
    
    # Make sure the house is not too close to any other houses
    too_close = True
    while too_close:
        too_close = False
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                # Calculate the distance between the new house and the existing house
                dist_x = abs(obj.location.x - house_x)
                dist_y = abs(obj.location.y - house_y)
                dist_z = abs(obj.location.z - house_z)
                total_dist = (dist_x ** 2 + dist_y ** 2 + dist_z ** 2) ** 0.5
                if total_dist < min_house_spacing:
                    too_close = True
                    break
        if too_close:
            house_x = random.uniform(-city_width/2, city_width/2)
            house_z = random.uniform(-city_depth/2, city_depth/2)
    
    # Create the house mesh
    bpy.ops.mesh.primitive_cube_add(location=(house_x, house_y, house_z))
    house = bpy.context.active_object
    house.scale = (house_width, house_height, house_depth)
    bpy.ops.object.transform_apply(scale=True)
    
    # Add the roof
    bpy.ops.mesh.primitive_cube_add(location=(house_x, house_y + house_height, house_z))
    roof = bpy.context.active_object
    roof.scale = (house_width * 1.1, house_height * 0.1, house_depth * 1.1)
bpy.ops.object.transform_apply(scale=True)

# Assign materials to the house and roof
house.data.materials.append(wall_material)
roof.data.materials.append(roof_material)

