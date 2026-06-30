# Review: Task Loop Movement

## Summary

The snippet updates camera position by a fixed amount every frame, so movement speed depends on frame rate.

## Severity

Medium. The code may appear acceptable on one machine but move too quickly or too slowly on another.

## Observed Issue

`self.camera.setY(self.camera.getY() + self.speed)` applies the full speed value on every task update. Panda3D tasks usually run once per frame, so this creates frame-dependent behavior.

## Why It Matters

Interactive movement should be consistent across different displays and performance conditions. Without delta time, a 120 FPS system can move roughly twice as fast as a 60 FPS system.

## Suggested Fix

Use `globalClock.getDt()` or an injected clock and multiply movement by `speed * dt`. Also combine opposing key states into one normalized direction to avoid duplicated movement branches.

## Edge Cases To Test

- `W` only moves forward
- `S` only moves backward
- `W` and `S` together cancel out
- Large frame delta does not create unreasonable jumps

