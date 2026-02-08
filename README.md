# Mobile-Based Pathfinding Algorithms (BFS, DFS, A*)

<p align="center">
  <img src="images/image.png" width="600" alt="Pathfinding Comparison">
</p>


A complete implementation of **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **A\*** pathfinding algorithms with **real-time console-based grid visualization**, developed and tested entirely in a **mobile-based cloud Python environment**.

This project demonstrates how classical Artificial Intelligence (AI) search algorithms can be efficiently implemented without relying on heavy graphical libraries or desktop-only tools, making it lightweight, portable, and highly accessible.

---

## 🚀 Project Overview

Pathfinding algorithms form the foundation of many real-world technologies including robotics navigation, autonomous vehicles, game AI, network routing, logistics optimization, and maze solving.

This project focuses on **grid-based pathfinding**, where an intelligent agent must move from a **start node (S)** to a **goal node (G)** while avoiding obstacles. Three major search algorithms are implemented and compared:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **A\* Search Algorithm (Heuristic-Guided Optimal Search)**

Each algorithm explores the grid differently, producing distinct performance characteristics in terms of:
- Nodes explored
- Path length
- Efficiency
- Optimality

Results are visualized using a **console-based grid visualization system** optimized for **mobile Python execution environments**.

---

## 📱 Mobile-Based Cloud Development

This entire project was:

- Designed  
- Implemented  
- Debugged  
- Tested  
- Executed  

**Completely on a mobile device using a cloud-based Python environment.**

This demonstrates:
- Platform-independent software engineering
- Resource-efficient algorithm design
- Adaptability to constrained computing environments
- Practical engineering creativity

Instead of depending on heavy visualization frameworks, the project uses **terminal-based visualization**, ensuring seamless execution inside **mobile Python apps and cloud interpreters**.

---

## 🧠 Algorithms Implemented

### Breadth-First Search (BFS)
- Explores the grid level by level.
- Guarantees the **shortest path** in unweighted environments.
- Explores more nodes before finding the goal.

### Depth-First Search (DFS)
- Explores deeply along one path before backtracking.
- Does **not guarantee shortest path**.
- Often explores unnecessary branches.

### A\* Search Algorithm
- Uses **Manhattan distance heuristic**.
- Combines actual cost and estimated future cost.
- Produces **optimal paths efficiently**.
- Explores significantly fewer nodes.

---

## 🗺️ Grid Visualization System

Instead of graphical plotting, this project implements **text-based grid visualization**, optimized for mobile environments.

### Symbol Legend

| Symbol | Meaning |
|----------|-----------|
| `S` | Start node |
| `G` | Goal node |
| `*` | Path |
| `#` | Obstacle / Wall |
| `.` | Free space |

### Sample Visualization Output
This visualization allows:
- Immediate visual interpretation
- Direct algorithm comparison
- Lightweight execution without graphics libraries

---

## ⚙️ How It Works

### Grid Environment
The environment is represented as a **2D matrix**:
- `S` marks the start position.
- `G` marks the target destination.
- `#` represents obstacles.
- `.` represents open cells.

### Algorithm Execution Flow
Each algorithm:
1. Starts from the start cell.
2. Explores valid neighboring cells.
3. Tracks visited nodes.
4. Stops when the goal is reached.
5. Reconstructs the final path.
6. Visualizes the result on the grid.

### Algorithm Logic

**BFS**
- Uses a queue
- Expands uniformly
- Always finds the shortest path

**DFS**
- Uses a stack
- Explores deeply before backtracking
- May produce longer paths

**A\***
- Uses a priority queue
- Applies heuristic guidance
- Efficient and optimal

---

## 📊 Performance Comparison

| Algorithm | Nodes Visited | Path Length | Optimal |
|-------------|----------------|---------------|------------|
| BFS | 21 | 11 | ✅ |
| DFS | 22 | 13 | ❌ |
| A* | 14 | 11 | ✅ |

A* achieves optimal results with significantly fewer explored nodes.

---

## 🏗️ Project Structure
---

## ▶️ How To Run

### Mobile (Recommended)
Use any mobile-based Python cloud environment:
- Learn Python App
- Pydroid
- Replit Mobile

Paste the code and run directly.

### Desktop
```bash
python pathfinding.py
