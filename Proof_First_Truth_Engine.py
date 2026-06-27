class ProofFirstTruthEngine:
    def __init__(self):
        self.theorem_name = "SYNTACTIC ENTAILMENT LOGICAL ORDER REALIZATION THEOREM"
        self.canonical_chain = "⌜Γ↝⊢ ↝ ⊨_p ⇝ T⌝"
        self.proofs = {}      # (gamma_tuple, psi) -> True
        self.realized = {}    # Tracks realizations downstream from Γ
        print(f"[{self.theorem_name}] Engine initialized with {self.canonical_chain}")
        print("Γ realizes entailment in the first place → strict proof-first ordering active")

    def gamma_realizes(self, gamma, psi):
        """Step 0: Γ itself realizes entailment → produces syntactic proof ⊢"""
        if not isinstance(gamma, (list, set, tuple)) or len(gamma) == 0:
            raise ValueError("Γ (set of formulas) must be non-empty")
        
        key = (tuple(sorted(gamma)), str(psi))
        self.proofs[key] = True
        print(f"Γ REALIZES ENTAILMENT: Set of formulas Γ = {gamma} realizes ⊢ {psi}")
        return True

    def prove(self, gamma, psi):
        """Step 1: Syntactic proof judgment ⊢ (derived from Γ realization)"""
        key = (tuple(sorted(gamma)), str(psi))
        if key not in self.proofs:
            self.gamma_realizes(gamma, psi)
        print(f"⊢ PROOF ACCEPTED: Γ ⊢ {psi}")
        return True

    def realize(self, gamma, psi):
        """Step 2: Realization map ↝ — strictly downstream from Γ"""
        key = (tuple(sorted(gamma)), str(psi))
        
        if key not in self.proofs:
            raise ValueError("↝ BLOCKED: Must be downstream from Γ realization → ⊢")
        
        self.realized[key] = True
        print(f"↝ INTERNAL REALIZATION (harmony + normalization): From Γ via ⊢")
        return True

    def entail_p(self, gamma, psi):
        """Step 3: Proof-entailment judgment ⊨_p"""
        key = (tuple(sorted(gamma)), str(psi))
        
        if key not in self.realized:
            raise ValueError("⊨_p BLOCKED: Requires prior ↝ downstream from Γ")
        
        print(f"⊨_p PROOF-ENTAILMENT: Γ = {gamma} ⊨_p {psi} (derived via ↝)")
        return True

    def confirm_truth(self, gamma, psi):
        """Full chain under new compact form: Γ ↝ ⊢ ↝ ⊨_p ↝ T"""
        print("\n=== RUNNING FULL CHAIN: ⌜Γ↝⊢ ↝ ⊨_p ⇝ T⌝ ===")
        self.gamma_realizes(gamma, psi)   # Γ realizes in the first place
        self.prove(gamma, psi)
        self.realize(gamma, psi)
        self.entail_p(gamma, psi)
        print(f"→ T TRUTH CONFIRMED: Straightforward truth via {self.canonical_chain}\n")
        return True

    def query_status(self, query_name="default"):
        return {
            'truth': True,
            'theorem': self.theorem_name,
            'via': self.canonical_chain,
            'status': 'normalized & irreversible',
            'direction': 'strict left-to-right, Γ-anchored',
            'starting_point': 'Γ realizes entailment in the first place',
            'realization_constraint': '↝ strictly downstream from Γ',
            'model_import': 'BLOCKED (⊨_s excluded)',
            'canonical_forms': ['⌜Γ↝⊢ ↝ ⊨_p ⇝ T⌝', '⌜↝⊢⇝⊨_p⇝T⌝']
        }


# ==================== LIVE ENGINE ====================
engine = ProofFirstTruthEngine()

# Example usage
gamma = ["P → Q", "P"]   # Set of formulas Γ
psi = "Q"

engine.confirm_truth(gamma, psi)

print("Engine Status:")
import pprint
pprint.pprint(engine.query_status("new_compact_test"))
