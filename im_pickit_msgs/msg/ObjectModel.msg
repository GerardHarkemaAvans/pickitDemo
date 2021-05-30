# Copyright (c) 2017, Pick-it NV.
# All rights reserved.

# Definition of different object models used for registration, reliability score calculation and more.

# Unspecified
uint8 NONE          = 0

# 2D models:
uint8 SQUARE        = 21
uint8 RECTANGLE     = 22
uint8 CIRCLE        = 23
uint8 ELLIPSE       = 24

# 3D models:
uint8 CYLINDER      = 32
uint8 SPHERE        = 33
uint8 POINT_CLOUD   = 35  # Object model given as point cloud (Pickit-Teach).

# Other models:
uint8 BLOB          = 50  # Object without specified shape -> No object fitting is performed.

# 2D engine related:
uint8 CONTOUR_TREE  = 60

# Models of internal use only:
uint8 CLUSTER       = 250

uint8 type  # Model type, takes one of the above defined models types as value.
