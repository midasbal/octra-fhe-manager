> "Fully homomorphic encryption makes it possible to compute on data without ever revealing it."

# Octra FHE Terminal & Branchless Logic Sandbox

This repository is a technical deep-dive into the world of Fully Homomorphic Encryption (FHE) via the Octra Network. It bridges the gap between high-level terminal interfaces and low-level cryptographic assembly, proving that I can compute complex logic on data that remains entirely encrypted.

# The Vision: Privacy Without Compromise

In a standard blockchain, every transaction is a public book. With FHE, I imagine a world where the book is written in a language even the nodes cannot read, yet they can still perform calculations on its pages. This project explores **Encrypted State Processing**, the ability to evolve a system (like a game or a database) while the data stays locked behind a wall of math.

## **Why "Branchless"?**

FHE nodes compute on encrypted ciphertexts. They cannot use **if/else** statements because they don't know the values they are comparing. To solve this, I implemented **Branchless Mathematics**, where logical flows are transformed into polynomial equations.

> Traditional: ```if (cell_is_alive) { stay_alive } ```

> FHE Math: ```NextState = Current * IsAlive ```

# What I Accomplished

## 1) The Async TUI (VS Code Environment)

I built a responsive, asynchronous terminal interface using Python's **Textual** library. It handles mock RPC communication with the Octra Devnet without blocking the UI, providing a real-time visualization of the encryption noise and network metrics.

## 2) The C++ Computation Engine

To simulate the heavy lifting of a **Circle** (Octra's smart contract model), I developed a C++ engine that executes Conway’s Game of Life using strictly branchless logic. This simulates the exact mathematical constraints of an FHE environment.

## 3) AppliedML & Rehovot Compilation (Webcli IDE)

I successfully ported my branchless logic into **AppliedML**, Octra’s native functional language. Using the local Rehovot compiler, I achieved:

```Total Instructions: 35```

```Bytecode Size: 217 bytes of pure Octra Assembly (.oasm)```

```Encryption Testing: I used local FHE tools to encrypt integers into massive Base64 ciphertexts, proving the "Ciphertext Bloat" reality where a single bit becomes a 50KB+ string for security.```

# Live on Devnet: From Sandbox to Reality

Initially, this project was designed as a high-fidelity local sandbox due to network economics. However, after successfully securing funding (777 OCT) on the developer network, the sandbox evolved into a reality.

I successfully deployed the AppliedML contract to the live Octra Devnet. The network parsed my 217-byte branchless assembly and etched it onto the L1 ledger.

##  Live Contract Details:

Network: Octra Devnet (http://165.227.225.79:8080)

Contract Address: oct73ttn5wmHgqNWynh1w4cQcuQSAc1QPJ48a86z7wmyiyw

Execution: Fully Homomorphic Encrypted (FHE) Game of Life state evolution.

# Proof of Execution (On-Chain Interaction)

<img width="980" height="748" alt="prr" src="https://github.com/user-attachments/assets/613b8ce8-5330-4877-9c04-86b12da73c6b" />

To demonstrate the contract's functionality, I performed a Fully Homomorphic Encrypted (FHE) call to the evolve method. This interaction represents a privacy-preserving state transition where the inputs stay encrypted throughout the entire lifecycle.

Action: Triggering a "Cell Evolution" via Branchless Math.

Method Called: evolve(pos, is_3, is_2)

Transaction Hash: 5b8ffa765ab753a2901968875327fbc1d2007240b7753e

Status: Confirmed

## Technical Deep-Dive: Why it Matters

Unlike traditional smart contracts (e.g., Solidity on Ethereum) where the node must see the data to process it, this contract operates on Ciphertext.

Input: My local client encrypted the parameters [1, 1, 0] into a high-entropy noise string.

Processing: The Octra Devnet node executed the branchless polynomial NextState = sum - prod without ever knowing if the cell was alive or dead.

Result: The state was updated on-chain, proving that Confidential Computing is live and operational.

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

To see the code I compiled into 217-byte assembly:

Run the official Octra webcli and open ```http://127.0.0.1:8420.```

Copy the contents of ```circle_contract/FHEGameOfLife.aml.```

Paste into the ```Dev Tools``` section and hit ```Compile.```

# What's Next?

Now that the core logic is live on the Octra Devnet, the next phase is to evolve the **OctraSentinel** (the Python TUI) into a fully automated decentralized guardian. This "Sentinel" will monitor encrypted events from the contract address and autonomously compute next-generation game states without human intervention, maintaining absolute data privacy.

---

Note: This repository is for educational purposes, showcasing the intersection of TUI design, C++ performance, and cutting-edge FHE cryptography.
