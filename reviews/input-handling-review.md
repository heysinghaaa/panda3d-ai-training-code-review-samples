# Review: Input Callback Registration

## Summary

The snippet calls `self.keys.update(...)` immediately while registering events instead of passing a callback to Panda3D.

## Severity

High. The key state is set during initialization, and the registered callback value is not callable.

## Observed Issue

`base.accept` expects a callable plus optional arguments. The current code executes `dict.update` immediately and passes its return value, which is `None`.

## Why It Matters

The application can fail when the event fires, and the initial key state may not represent actual user input.

## Suggested Fix

Register a method such as `self.set_key` and pass the key/value pair as event arguments. Initialize expected keys with default values so reads do not raise `KeyError`.

## Edge Cases To Test

- Reading state before any key event
- Pressing and releasing the same key repeatedly
- Opposite directional keys pressed together
- Missing or unknown key names

