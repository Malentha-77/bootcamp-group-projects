# Blackjack — Bootcamp Group Project

A simple, console-based Blackjack (21) game implemented in Python as part of the Bootcamp Group Projects repository. This project demonstrates basic game logic, object-oriented design, and some simple unit tests and CLI interactions to play rounds of Blackjack.

Repository: https://github.com/Malentha-77/bootcamp-group-projects

---

## Table of contents
- [Overview](#overview)
- [Game rules (short)](#game-rules-short)
- [Features](#features)
- [Requirements](#requirements)
- [Install & Run](#install--run)
- [How to play](#how-to-play)
- [Project structure](#project-structure)
- [Participants & contributions](#participants--contributions)
- [How to contribute](#how-to-contribute)
- [Acknowledgements](#acknowledgements)
- [License](#license)

---

## Overview
This project implements the classic card game Blackjack (also known as 21). Players play against a dealer (the computer). The goal is to get a hand value as close to 21 as possible without going over (busting). This implementation focuses on clear game rules, readable Python code, and easy extensibility for additional features (multiple players, betting, GUI, etc.).

---

## Game rules (short)
- Each card has a value: number cards are worth their number, face cards (J/Q/K) are worth 10, Aces are worth 1 or 11.
- Player and dealer each start with two cards. The player may "hit" (take another card) or "stand" (end their turn).
- If a hand totals over 21, that hand busts and automatically loses.
- After the player stands, the dealer reveals cards and must hit until the dealer's total is at least 17.
- Highest hand ≤ 21 wins. Blackjack (an Ace + 10-valued card on the initial deal) is a special strong hand.

---

## Features
- Command-line playable Blackjack game.
- Deck creation, shuffling, dealing.
- Hand evaluation with Ace handling (1 or 11).
- Dealer behavior (hits until 17+).
- Clear prompts and basic input validation.
- (Optional) Unit tests for core logic (if included in the repo).

---

## Requirements
- Python 3.8+ (recommended)
- No external dependencies required for the basic game.
- (Optional) pytest to run unit tests.

---

## Install & Run

1. Clone the repository:
   git clone https://github.com/Malentha-77/bootcamp-group-projects.git

2. Change directory to the Blackjack project folder (example):
   cd bootcamp-group-projects/blackjack

3. Run the game:
   python blackjack.py

Replace `blackjack.py` with the actual entry point filename in the repo if different.

To run tests (if present):
   pip install pytest
   pytest tests/

---

## How to play
- Start the game and follow on-screen prompts.
- When prompted, choose:
  - `hit` to draw another card,
  - `stand` to keep your total and let the dealer play.
- The program will announce the winner at the end of the round.
- You can play multiple rounds until you quit.

---

## Project structure
(Adjust these paths to match the repository)
- blackjack/
  - blackjack.py — main game entry point / CLI
  - deck.py — deck and card utilities
  - hand.py — hand evaluation logic
  - dealer.py — dealer logic
  - tests/ — unit tests for core functions
  - README.md — this file

---

## Participants & contributions
This project was completed as part of a group assignment during the bootcamp. Participants contributed to design, implementation, and testing. Below is a template to list participants — please update with real names/roles in the repo.

- patek2014 — Project lead, game design, main implementation
- Makhotso — Gameplay logic, unit tests
- KwenzokuhleMvelase — CLI, user prompts, input validation
- Malenyha-77 — Testing, bug fixes, documentation

If you want me to automatically populate this section with the repository's GitHub contributors, tell me and I can fetch and insert the current contributor list.

Roles often performed:
- Implementation (game logic, classes)
- Testing and QA
- Documentation and README authoring
- Project coordination and pull request reviews

Consider adding a CONTRIBUTORS.md file to keep a canonical list of people and roles. Example entry format:
- Full Name (GitHub handle) — Role(s) — Short note

---

## How to contribute
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make changes with tests where appropriate.
4. Open a Pull Request describing the change.
5. Add yourself to CONTRIBUTORS.md or ask to be added to the Participants section.

Please follow the repository's code style and run tests before submitting a PR.

---

## Acknowledgements
- Bootcamp instructors and peers for guidance and code reviews.
- Standard Blackjack rules and game design references.

---

## License
This project is provided under the MIT License. See LICENSE for details (or add a LICENSE file to apply a license).
