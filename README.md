# Recycle Reward System

## Overview
This project simulates an automated collection and reward system for recyclable items. The system accepts different types of recyclable items, calculates rewards based on the item type, and provides a simple command-line interface for user interactions.

## Item Types and Rewards
- Type A: INR 0.10
- Type B: INR 0.05
- Type C: INR 0.15

## Features
- Add items to the system.
- View the total reward accumulated.
- Reset the system for a new user session.

## Setup and Running the Project
1. Clone the repository:
    ```sh
    git clone https://github.com/Aayush2025/recycle-reward-system.git
    cd recycle-reward-system
    ```

2. Run the script:
    ```sh
    python recycle_reward_system.py
    ```

## Assumptions and Design Decisions
- The system operates in a command-line interface for simplicity.
- Only valid item types (A, B, C) are accepted.
- Rewards are predefined and stored in a dictionary.
