from PORTHUB.COM import PortTypeHub, auto_hub_files  # From the repo

class ProofFirstAdapter:
    def __init__(self):
        self.hub = PortTypeHub()
        self.port_map = {}  # Logical key → port / representation
        
        print("[ProofFirstAdapter] Initialized with PORTHUB.COM backend")
    
    def register_gamma(self, gamma, psi):
        """Register after gamma_realizes()"""
        key = (tuple(sorted(gamma)), str(psi))
        
        # Use PORTHUB to create persistent mapping
        port_info = self.hub.register_port(
            port_type="realization",
            source=key,
            metadata={
                "stage": "Γ realizes entailment",
                "gamma": gamma,
                "psi": psi
            }
        )
        
        self.port_map[key] = port_info
        print(f"Γ REALIZED & PORT MAPPED: {port_info['port_id']}")
        return port_info
    
    def register_proof(self, gamma, psi, proof_data=None):
        """After ⊢ step"""
        key = (tuple(sorted(gamma)), str(psi))
        if key not in self.port_map:
            raise ValueError("↝ BLOCKED: Must register Γ realization first")
        
        port_info = self.hub.update_port(
            self.port_map[key]['port_id'],
            stage="⊢ PROOF ACCEPTED",
            proof_data=proof_data
        )
        print(f"⊢ PROOF PORT UPDATED: {port_info['port_id']}")
        return port_info
    
    def realize_and_entail(self, gamma, psi):
        """Handle ↝ → ⊨_p"""
        key = (tuple(sorted(gamma)), str(psi))
        port_info = self.hub.update_port(
            self.port_map[key]['port_id'],
            stage="↝ REALIZATION → ⊨_p",
            status="harmony_normalized"
        )
        print(f"↝ INTERNAL REALIZATION PORTED: {port_info['port_id']}")
        return port_info
    
    def confirm_truth(self, gamma, psi):
        """Final T with PORTHUB exposure"""
        key = (tuple(sorted(gamma)), str(psi))
        port_info = self.hub.update_port(
            self.port_map[key]['port_id'],
            stage="⇝ T TRUTH CONFIRMED",
            status="normalized_irreversible"
        )
        print(f"→ T CONFIRMED & EXPOSED via PORTHUB: {port_info['port_id']}")
        return port_info
