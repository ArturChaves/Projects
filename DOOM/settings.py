from math import *



#Game settings
res = width, height = 1600, 900
half_width = width // 2
half_height = height // 2
fps = 60

player_position = 1.5, 5 #mini_map
player_angle = 0
player_speed = 0.004
player_rot_speed = 0.002

fov = pi / 3
half_fov = fov / 2
num_rays = width // 2
helf_num_rays = num_rays // 2
delta_angle = fov / num_rays
max_depth = 20

screen_distance = half_width / tan(half_fov)
scale = width // num_rays

texture_size = 256
half_texture_size = texture_size // 2