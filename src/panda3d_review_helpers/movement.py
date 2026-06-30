from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: float
    y: float
    z: float = 0.0


def frame_scaled_movement(direction: int, speed: float, dt: float) -> float:
    """Return movement distance for a frame-rate independent update."""
    return direction * speed * dt


def normalized_axis(positive_pressed: bool, negative_pressed: bool) -> int:
    """Convert opposite input states into a stable axis value."""
    return int(positive_pressed) - int(negative_pressed)


def distance_squared(a: Position, b: Position) -> float:
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return dx * dx + dy * dy + dz * dz


def is_within_radius(a: Position, b: Position, radius: float) -> bool:
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return distance_squared(a, b) <= radius * radius

