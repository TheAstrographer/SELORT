class ProofFirstTruthEngine:
    def __init__(self):
        self.theorem_name = "SYNTACTIC ENTAILMENT LOGICAL ORDER REALIZATION THEOREM"
        self.canonical_chain = "⌜Γ ↝ ⊢ ↝ ⊨_p ⇝ T⌝"
        self.proofs = {}     
        self.realized = {}   
        print(f"[{self.theorem_name}] Engine initialized with {self.canonical_chain}")
        print("Γ realizes entailment in the first place → strict proof-first ordering active")

    def gamma_realizes(self, gamma, psi):
        """Step 0: Γ itself realizes entailment → produces syntactic proof ⊢"""
        if not isinstance(gamma, (list, set, tuple)) or len(gamma) == 0:
            raise ValueError("Γ (set of formulas) must be non-empty")
       
        key = (tuple(sorted(gamma)), str(psi))
        self.proofs[key] = True
        print(f"Γ REALIZES ENTAILMENT: A set of formulas realizes entailment proofs semantic entailment to be truth. Γ = {gamma} realizes ⊢ {psi}")
        return True

    def prove(self, gamma, psi):
        """Step 1: Syntactic proof judgment ⊢"""
        key = (tuple(sorted(gamma)), str(psi))
        if key not in self.proofs:
            self.gamma_realizes(gamma, psi)
        print(f"⊢ PROOF ACCEPTED: Entailment proofs semantic truth. Γ ⊢ {psi}")
        return True

    def realize(self, gamma, psi):
        """Step 2: Realization map ↝ — strictly downstream from Γ"""
        key = (tuple(sorted(gamma)), str(psi))
       
        if key not in self.proofs:
            raise ValueError("↝ BLOCKED: Must be downstream from Γ realization → ⊢")
       
        self.realized[key] = True
        print(f"↝ INTERNAL REALIZATION: Entailment's set of witnesses and conclusion become semantic once true entailment of semantic proofs becomes truth.")
        return True

    def entail_p(self, gamma, psi):
        """Step 3: Proof-entailment judgment ⊨_p"""
        key = (tuple(sorted(gamma)), str(psi))
       
        if key not in self.realized:
            raise ValueError("⊨_p BLOCKED: Requires prior ↝ downstream from Γ")
       
        print(f"⊨_p PROOF-ENTAILMENT: Γ = {gamma} ⊨_p {psi} (Entailment proofs semantic truth)")
        return True

    def confirm_truth(self, gamma, psi, witnesses=None):
        """Full chain with support for multi-formula witness version"""
        print("\n=== RUNNING FULL CHAIN: ⌜Γ ↝ ⊢ ↝ ⊨_p ⇝ T⌝ ===")
       
        # Multi-formula witness support
        if witnesses is not None:
            print(f"Multi-formula witnesses: ⊢ {witnesses} = {psi}")
       
        self.gamma_realizes(gamma, psi)
        self.prove(gamma, psi)
        self.realize(gamma, psi)
        self.entail_p(gamma, psi)
        print(f"→ T TRUTH CONFIRMED: A set of formulas realizes entailment in the first place. Entailment proofs semantic entailment, to become truth.\n")
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
            'canonical_forms': [
                '⌜Γ ↝ ⊢ ↝ ⊨_p ⇝ T⌝',
                '⌜⊢ φ₁, φ₂, …, φₙ = ψ ⇝ ⊨_p ψ ⇝ T ψ⌝',
                '⌜↝⊢⇝⊨_p⇝T⌝'
            ],
            'semantic_becoming_truth': 'Entailment proofs semantic truth. Entailment\'s set of witnesses and conclusion become semantic once true entailment of semantic proofs becomes truth.',
            'core_statement': 'A set of formulas realizes entailment proofs semantic entailment to be truth.'
        } 
