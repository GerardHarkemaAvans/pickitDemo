# Values that 'model_type' can take.
uint8 UNINITIALIZED = 0
uint8 FROM_CAMERA   = 1
uint8 FROM_CAD      = 2
uint8 CYLINDER      = 3
uint8 CIRCLE        = 4

uint32                 id
uint32                 points
bool                   is_saved
bool                   is_enabled
uint8                  model_type
int32                  priority
float64                max_visibility_angle
float64                min_visibility_ratio

# Flag indicating this model is newly taught that if it's saved it will overwrite an existing model.
# Used to indicate that this model can be reverted to the previous one with identical id and
# saving this model will lose the previously saved model.
bool                   overwrites_existing

# Model dimensions. The contents of the x, y and z elements depend on the
# model type.
# - Models taught from camera or CAD: Size of the model bounding box.
# - Cylinder primitives: [length, diameter, diameter].
geometry_msgs/Vector3  dimensions

# TODO(viktorku): Publish thumbnail of a model, but it will have to be done on a separate topic.
#                 See comment in Localiser::publishModelsInfo method.
# sensor_msgs/Image    thumbnail
