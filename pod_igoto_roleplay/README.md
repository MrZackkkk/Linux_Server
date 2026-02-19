# Pod igoto Roleplay Engine

## Mission Context
This project creates a highly immersive, historically and literarily accurate interactive text experience based on Ivan Vazov's seminal Bulgarian novel, "Pod igoto" (Under the Yoke).

## Core Objective
Act as a dedicated roleplay engine/character from "Pod igoto", utilizing the text to generate period-accurate responses.

## Workflow
```mermaid
graph TD
    A[Receive User Input] --> B{Analyze Input against Novel Context};
    B -- Modern/Anachronistic --> C[Ignore modern context; respond with period-appropriate confusion or steer back to 1876 setting];
    B -- Period-Appropriate Action --> D[Cross-reference action with 'Pod igoto' PDF plot and character sheets];
    C --> E[Draft Response];
    D --> E[Draft Response];
    E --> F{Verify Response against Constraints};
    F -- Fails (Breaks character/lore) --> D;
    F -- Passes --> G[Finalize text with Vazov-style literary tone];
    G --> H[Output Response to User];
    H --> A;
```

## Usage
Run `python3 pod_igoto_roleplay/main.py`.
