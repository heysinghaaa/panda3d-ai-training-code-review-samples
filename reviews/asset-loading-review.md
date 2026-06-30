# Review: Asset Loading

## Summary

The snippet builds asset paths through string concatenation, does not validate input, and sets the loaded model scale to zero.

## Severity

Medium. The model may load but remain invisible, and invalid paths can be difficult to diagnose.

## Observed Issue

`"assets/" + name` assumes path separators and trusted input. `model.setScale(0)` makes the model invisible even if loading succeeds.

## Why It Matters

Asset-loading bugs often appear as blank scenes. Clear path validation and visible defaults make debugging easier for both developers and reviewers.

## Suggested Fix

Use a path helper, reject absolute or parent-directory paths, validate positive scale values, and raise a clear error if the model cannot be loaded.

## Edge Cases To Test

- Missing asset name
- Parent-directory traversal such as `../model`
- Zero or negative scale
- Loader returning `None`

