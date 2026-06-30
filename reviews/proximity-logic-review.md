# Review: Proximity Logic

## Summary

The snippet computes squared distance but compares it to a non-squared trigger distance.

## Severity

Medium. The trigger area will be much smaller than intended for distances greater than one.

## Observed Issue

`distance_squared <= trigger_distance` mixes squared and linear units. If the intended radius is `5`, squared distance should be compared to `25`.

## Why It Matters

Collision and proximity checks are common in gameplay logic. Unit mismatches create subtle bugs where interactions trigger inconsistently.

## Suggested Fix

Compare `distance_squared <= trigger_distance * trigger_distance`, and reject negative trigger distances.

## Edge Cases To Test

- Player exactly on the radius boundary
- Player just outside the radius
- Same position as the object
- Negative trigger distance

