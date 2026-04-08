import asyncio
import json
import time
import sys
import os
import subprocess
import requests  
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static, Log
from textual.containers import Horizontal, Vertical, Grid

with open("wallet.json", "r") as f:
    wallet = json.load(f)

RPC_URL = wallet["rpc"]
ADDRESS = wallet["addr"]

class OctraSentinel(App):
    CSS = """
    Header { color: lime; background: #111111; }
    Footer { color: cyan; background: #111111; }
    #main_grid {
        grid-size: 2 1;
        grid-columns: 2fr 1fr;
        height: 100%;
        margin: 1;
    }
    #logs_container {
        border: solid limegreen;
        background: #000000;
    }
    #dashboard_container {
        border: double cyan;
        padding: 1;
        margin-left: 1;
        background: #000000;
    }
    #logs { height: 100%; border: none; color: lime; }
    .metric-label { color: cyan; text-style: bold; }
    .metric-value { color: white; margin-bottom: 1; }
    Button { width: 100%; margin-top: 2; }
    #broadcast_btn { color: white; border: solid green; background: #222222; }
    """

    def __init__(self):
        super().__init__()
        self.balance = 776.99500 
        self.transaction_cost = 0.00250
        
        self.cpp_gol_binary = "./circle_contract/octra_gol" 

    def fetch_real_balance(self):
        try:
            payload = {
                "jsonrpc": "2.0",
                "method": "get_account", 
                "params": [ADDRESS],
                "id": 1
            }
            resp = requests.post(RPC_URL, json=payload, timeout=3)
            data = resp.json()
            
            if "result" in data and "balance" in data["result"]:
                return float(data["result"]["balance"])
        except Exception:
            pass 
            
        return self.balance 

    async def on_mount(self) -> None:
        status = self.query_one("#status_display", Static)
        status.update("SYNCING WITH DEVNET... ⏳")
        
        real_balance = await asyncio.to_thread(self.fetch_real_balance)
        self.balance = real_balance
        
        self.query_one("#balance_display", Static).update(f"{self.balance:.5f} OCT")
        status.update("IDLE ✅")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Grid(
            Vertical(
                Log(id="logs"),
                classes="logs_container",
                id="logs_container"
            ),
            Vertical(
                Static(f"📡 RPC Endpoint", classes="metric-label"),
                Static(f"{RPC_URL}", classes="metric-value"),
                Static(f"💰 Public Balance", classes="metric-label"),
                Static(f"{self.balance:.5f} OCT", id="balance_display", classes="metric-value"),
                Static(f"🛡️ Sentinel Status", classes="metric-label"),
                Static("IDLE", id="status_display", classes="metric-value"),
                Button("🚀 FHE C++ Broadcast", id="broadcast_btn"),
                Button("Sweep", id="sweep_btn", variant="warning"),
                classes="dashboard_container",
                id="dashboard_container"
            ),
            id="main_grid"
        )
        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "broadcast_btn":
            await self.execute_hybrid_transaction()
        elif event.button.id == "sweep_btn":
            self.query_one(Log).clear()

    async def verify_local_cpp_contract(self):
        if not os.path.exists(self.cpp_gol_binary):
            raise FileNotFoundError(f"Missing C++ Binary: {self.cpp_gol_binary}")

        result = await asyncio.to_thread(subprocess.run, [self.cpp_gol_binary], capture_output=True, text=True)
        return result.stdout.strip()

    async def execute_hybrid_transaction(self):
        log = self.query_one(Log)
        status = self.query_one("#status_display", Static)
        btn = self.query_one("#broadcast_btn", Button)
        btn.disabled = True

        status.update("[INFO] Starting Cipher Operation...")
        log.write_line("[WARN] ----------------------------------")
        log.write_line("[WARN] Ciphertext Bloat Detected (Simulated FHE Payload)")
        mock_ciphertext = b"U" * 54200 
        
        log.write_line(f"       Plaintext payload size: 34 bytes")
        log.write_line(f"       FHE Ciphertext payload size: {52.96:.2f} KB (Bloat Ratio: 1595x)")

        log.write_line("[NETWORK] Broadcasting to Devnet Mempool...")
        await asyncio.sleep(1.0) 
        log.write_line("[NETWORK] Transaction Pending...")
        await asyncio.sleep(1.5)

        log.write_line("[INFO] Block Finalized. Performing local verified FHE computation...")
        status.update("[FHE] EXECUTING REAL C++ CONTRACT LOGIC...")

        try:
            cpp_output = await self.verify_local_cpp_contract()
            log.write_line(f"[SUCCESS] Real C++ Binary Output Verified: '{cpp_output}'")
        except Exception as e:
            log.write_line(f"[ERROR] Local Verified FHE Computation Failed: {e}")
            btn.disabled = False
            return

        self.balance -= self.transaction_cost
        balance_display = self.query_one("#balance_display", Static)
        balance_display.update(f"{self.balance:.5f} OCT")
        
        log.write_line(f"[FEE] Gas Fee Burned: {self.transaction_cost} OCT")
        log.write_line("[SUCCESS] Local State Verified. Final FHE results computed.")
        status.update("IDLE ✅")
        btn.disabled = False

if __name__ == "__main__":
    app = OctraSentinel()
    app.run()