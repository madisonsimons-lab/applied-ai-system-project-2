# AI Music Recommendation System

## Original Project
This project extends my Music Recommender Simulation, which originally matched songs to user mood using simple rules.

## Overview
This system generates playlists using AI by combining retrieval, reasoning, and evaluation.

## Architecture
The system follows this pipeline:
Input → Retrieval → AI Generation → Critique → Refinement → Evaluation → Logging

## System Diagram
![System Diagram](assets/system_diagram.png)

## Setup

pip install openai python-dotenv

Create .env file:
OPENAI_API_KEY=your_key_here

Run:
python main.py

## Sample Output

Input: sad music  
Output: Playlist with calm songs and explanations  

Input: workout  
Output: High-energy playlist  

## Design Decisions
I used retrieval to improve relevance, an agent workflow to improve outputs, and evaluation to measure quality.

## Testing
4/4 test cases passed. Performance improved after adding genre rules.

## Reflection
This project showed how AI systems can be improved through iteration and structured workflows.

## Demo Video
(Add Loom link here)
