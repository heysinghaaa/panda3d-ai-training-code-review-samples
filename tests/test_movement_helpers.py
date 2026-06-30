import pytest

from panda3d_review_helpers.movement import (
    Position,
    distance_squared,
    frame_scaled_movement,
    is_within_radius,
    normalized_axis,
)


def test_frame_scaled_movement_uses_delta_time():
    assert frame_scaled_movement(1, 12.0, 0.5) == 6.0
    assert frame_scaled_movement(-1, 12.0, 0.25) == -3.0
    assert frame_scaled_movement(0, 12.0, 0.25) == 0


def test_normalized_axis_handles_conflicting_inputs():
    assert normalized_axis(True, False) == 1
    assert normalized_axis(False, True) == -1
    assert normalized_axis(False, False) == 0
    assert normalized_axis(True, True) == 0


def test_distance_squared_avoids_unneeded_square_root():
    assert distance_squared(Position(0, 0), Position(3, 4)) == 25
    assert distance_squared(Position(1, 2, 3), Position(1, 2, 3)) == 0


def test_is_within_radius_includes_boundary():
    assert is_within_radius(Position(0, 0), Position(3, 4), 5)
    assert not is_within_radius(Position(0, 0), Position(3, 4), 4.99)


def test_is_within_radius_rejects_negative_radius():
    with pytest.raises(ValueError):
        is_within_radius(Position(0, 0), Position(1, 1), -1)

