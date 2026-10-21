# Wireless Pointing Controller — Roadmap

## Project Goal

Build a motion-controlled game input system, starting with a mouse-based prototype and progressing toward an ESP32-based wireless controller, IMU motion tracking, 3D interaction, and wearable haptic feedback.

## Milestones

- [x] M0 — Development Environment & GitHub
- [x] M1 — Basic Pygame Target Game
- [ ] M2 — Input Abstraction & Latency Experiments
- [ ] M3 — ESP32 Communication
- [ ] M4 — IMU Motion Tracking
- [ ] M5 — Motion-Controlled Pointing Prototype
- [ ] M6 — 3D Spatial Control
- [ ] M7 — Wearable Haptic Feedback Prototype
- [ ] M8 — Evaluation & Technical Portfolio

## M1 — Basic Pygame Target Game

**Goal:** Build a playable target-shooting game with an input system that can later support external controllers.

### Tasks

- [x] M1.1 — Create Pygame window
- [x] M1.2 — Draw background and target
- [x] M1.3 — Add game loop and FPS control
- [x] M1.4 — Generate random targets
- [x] M1.5 — Implement mouse hit detection
- [x] M1.6 — Add scoring system
- [x] M1.7 — Implement custom crosshair (verify)
- [x] M1.8 — Separate input coordinates from game state (verify)
- [x] M1.9 — Create mouse input function (verify)
- [x] M1.10 — Abstract the fire action
- [x] M1.11 — Refactor, test, commit and push

### Completion Criteria

- The game runs without errors.
- The player can aim and shoot targets.
- The score updates correctly.
- Input acquisition is separated from game logic.
- The project is committed and pushed to GitHub.

## Development Principles

1. Build and test one feature at a time.
2. Understand the code before adding complexity.
3. Keep mouse and motion-controller modes compatible.
4. Measure latency and drift rather than guessing.
5. Document experiments and technical decisions.
6. Use Git to track stable milestones.

## Current Status

Current milestone: M1
