# PDA Visualizer & Simulator

A comprehensive tool for defining, simulating, and visualizing **Pushdown Automata (PDA)**. This project was developed as part of a Theory of Computation course to help students and enthusiasts understand the mechanics of non-deterministic and deterministic PDAs.

## 🚀 Features

- **Dynamic PDA Builder**: Easily define states, input alphabets, stack alphabets, and transitions through an intuitive interface.
- **Real-time Simulation**: Test input strings against your PDA and see the results immediately.
- **Step-by-Step Trace**: Explore the simulation's execution path, including stack changes, state transitions, and remaining input at every step.
- **SVG Visualization**: Automatically generate a visual graph of your PDA's states and transitions.
- **Sample Library**: Load pre-defined examples such as:
  - $a^n b^n$ (Matching counts of 'a' and 'b')
  - Palindromes over $\{a, b\}$
  - Balanced Parentheses
- **Experimental CFG Converter**: Preliminary support for converting specific PDA samples into Context-Free Grammars (CFG).

## 🛠️ Project Structure

```text
pda_project/
├── backend/                # Flask Backend
│   ├── core/               # Core PDA and Simulator logic
│   ├── routes/             # API Endpoints (simulate, render, samples)
│   ├── services/           # Helper services (JSON loading, Graph formatting)
│   ├── converters/         # PDA-to-CFG conversion logic
│   └── samples/            # Pre-defined PDA JSON files
├── newfront/               # Frontend Assets
│   └── index.html          # Single-file Vanilla JS visualizer
└── README.md               # You are here!
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- A modern web browser

### Backend Setup
1. **Clone the repository** (or navigate to the project directory).
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
3. **Activate the environment**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. **Install dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```
5. **Run the server**:
   ```bash
   python backend/app.py
   ```
   The backend will be available at `http://127.0.0.1:5000`.

### Frontend Setup
Simply open `newfront/index.html` in any web browser. 
> **Note**: Ensure the "API Base URL" in the frontend points to your running backend (usually `http://127.0.0.1:5000/api`).

## 📖 Usage

1. **Build or Load**: Use the "Builder" panel to define your PDA or select a "Sample" from the dropdown.
2. **Visualize**: Click **Render Graph** to see the automaton's structure.
3. **Simulate**: Enter an input string in the simulation panel and click **Run Simulation**.
4. **Analyze**: Review the **Step-by-Step Trace** table to see exactly how the stack and states evolved.

## 🧪 Testing

You can run the sample tests for CFG conversion using:
```bash
python test.py
```

## 📝 Technologies Used

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: Vanilla HTML5, CSS3 (Modern Glassmorphism), JavaScript (ES6+), SVG for Graph Rendering
- **Logic**: Custom PDA Simulation Engine supporting ε-transitions.

---
*Created for the Theory of Computation Final Project.*
