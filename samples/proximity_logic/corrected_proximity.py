"""Corrected proximity check using squared radius comparison."""


def is_player_near_object(player_pos, object_pos, trigger_distance):
    if trigger_distance < 0:
        raise ValueError("trigger_distance cannot be negative")

    dx = player_pos.x - object_pos.x
    dy = player_pos.y - object_pos.y
    dz = player_pos.z - object_pos.z
    distance_squared = dx * dx + dy * dy + dz * dz
    return distance_squared <= trigger_distance * trigger_distance

