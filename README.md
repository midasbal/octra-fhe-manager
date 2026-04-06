# Octra FHE Terminal & Branchless Logic Sandbox

This repository is a technical deep-dive into the world of Fully Homomorphic Encryption (FHE) via the Octra Network. It bridges the gap between high-level terminal interfaces and low-level cryptographic assembly, proving that we can compute complex logic on data that remains entirely encrypted.

# The Vision: Privacy Without Compromise

In a standard blockchain, every transaction is a public book. With FHE, we imagine a world where the book is written in a language even the nodes cannot read, yet they can still perform calculations on its pages. This project explores **Encrypted State Processing**, the ability to evolve a system (like a game or a database) while the data stays locked behind a wall of math.

## **Why "Branchless"?**

FHE nodes compute on encrypted ciphertexts. They cannot use **if/else** statements because they don't know the values they are comparing. To solve this, we implemented **Branchless Mathematics**, where logical flows are transformed into polynomial equations.

> Traditional: ```if (cell_is_alive) { stay_alive } ```

> FHE Math: ```NextState = Current * IsAlive ```

# What We Accomplished

## 1) The Async TUI (VS Code Environment)

We built a responsive, asynchronous terminal interface using Python's **Textual** library. It handles mock RPC communication with the Octra Devnet without blocking the UI, providing a real-time visualization of the encryption noise and network metrics.

## 2) The C++ Computation Engine

To simulate the heavy lifting of a **Circle** (Octra's smart contract model), we developed a C++ engine that executes Conway’s Game of Life using strictly branchless logic. This simulates the exact mathematical constraints of an FHE environment.

## 3) AppliedML & Rehovot Compilation (Webcli IDE)

We successfully ported our branchless logic into **AppliedML**, Octra’s native functional language. Using the local Rehovot compiler, we achieved:

```Total Instructions: 35```

```Bytecode Size: 217 bytes of pure Octra Assembly (.oasm)```

```Encryption Testing: We used local FHE tools to encrypt integers into massive Base64 ciphertexts, proving the "Ciphertext Bloat" reality where a single bit becomes a 50KB+ string for security.```

# Faucet Reality & Local Simulation

While our networking bridge and bytecode are production-ready, the official Octra Devnet Faucet has been **deprecated/discontinued.** Without the required **0.2 OCT** deployment fee, a public broadcast was not possible.

However, this limitation became a feature. This project evolved into a high-fidelity **Local Sandbox.** It proves that a developer can build, compile, and mathematically verify a privacy-preserving dApp entirely in a local environment, ready for the moment the network economics open up.

# Setup & Execution

## Prerequisites

Python 3.8+

C++17 Compiler (g++ or clang)

Octra Webcli (For local IDE & AppliedML tests)

## Step 1: Run the Terminal & C++ Engine

```
# Compile the Branchless C++ Logic
cd circle_contract
g++ -std=c++17 main.cpp -o octra_gol
cd ..

# Start the Terminal UI
chmod +x run.sh
./run.sh
```

## Step 2: Test the Smart Contract (AppliedML)

To see the code we compiled into 217-byte assembly:

Run the official Octra webcli and open ```http://127.0.0.1:8420.```

Copy the contents of ```circle_contract/FHEGameOfLife.aml.```

Paste into the ```Dev Tools``` section and hit ```Compile.```

# What's Next?

If this project were fully funded with OCT tokens, it would transition from a sandbox to a **Live Sentinel.** We envision a decentralized guardian that processes sensitive sensor data or game states across the Octra network, where the "truth" is computed but the "data" is never revealed.

---

Note: This repository is for educational purposes, showcasing the intersection of TUI design, C++ performance, and cutting-edge FHE cryptography.
