# Asteroids Game

An arcade-style space shooter written in Python with [pygame](https://www.pygame.org/). Fly a ship around the screen, shoot incoming asteroids, and break them into smaller pieces before they hit you.

## Features

- Ship that rotates and moves in any direction
- Shooting with a cooldown, so holding space doesn't flood the screen
- Asteroids that spawn from random screen edges at random speeds and angles
- Large asteroids split into two smaller, faster ones when shot
- Score in the window title (+10 for each smallest asteroid destroyed)
- Game over when an asteroid hits the ship, with your final score printed to the terminal

## Controls

| Key | Action |
|-----|--------|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

## Getting started

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/Ibrobar/asteroid_game.git
cd asteroid_game
uv run main.py
```

`uv run` installs the pinned dependency (pygame 2.6.1) into a virtual environment the first time you run it.

## How it works

- **Game loop (`main.py`):** runs at 60 FPS and passes delta time (`dt`) to every update, so movement speed doesn't depend on frame rate. Each frame it updates all objects, checks collisions, and redraws the screen.
- **Shared base class (`circleshape.py`):** `CircleShape` extends `pygame.sprite.Sprite` and gives every game object a position, velocity, radius, and circle-to-circle collision check (two objects collide when the distance between their centers is at most the sum of their radii).
- **Sprite groups:** `Player`, `Asteroid`, and `Shot` subclass `CircleShape` and register themselves into `updatable` / `drawable` groups, so the main loop can update and draw everything without knowing each type.
- **Player (`player.py`):** draws the ship as a triangle, uses vector rotation for steering and movement, and uses a shot timer to enforce the firing cooldown.
- **Asteroid splitting (`asteroid.py`):** when shot, an asteroid is removed. If it was bigger than the minimum size, it spawns two smaller asteroids whose velocity is rotated a random 20-50 degrees in opposite directions and sped up by 1.2x.
- **Spawning (`asteroidfield.py`):** spawns a new asteroid of random size from a random screen edge every 0.8 seconds.
- **Tuning (`constants.py`):** screen size, speeds, sizes, spawn rate, and cooldown all live in one place.

## Project structure

```
main.py           # entry point and game loop
circleshape.py    # base class for all game objects
player.py         # the ship: movement, rotation, shooting
shot.py           # bullets
asteroid.py       # asteroids and splitting logic
asteroidfield.py  # spawns asteroids from the screen edges
constants.py      # game tuning values
logger.py         # writes game state/events to .jsonl files for debugging
```
