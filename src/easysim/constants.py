# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

class DoFControlMode:
    """ """
    NONE = 0
    POSITION_CONTROL = 1
    VELOCITY_CONTROL = 2
    TORQUE_CONTROL = 3


class MeshNormalMode:
    """ """
    FROM_ASSET = 0
    COMPUTE_PER_VERTEX = 1
    COMPUTE_PER_FACE = 2
