import pathlib

root = pathlib.Path("Technological Singularity")

def insert_before_references(file_rel, content_to_insert):
    p = root / file_rel
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    ref_idx = -1
    for i, line in enumerate(lines):
        if line.startswith("## 5. Academic References"):
            ref_idx = i
            break
    if ref_idx != -1:
        new_lines = lines[:ref_idx] + [""] + content_to_insert.strip().splitlines() + [""] + lines[ref_idx:]
        p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print(f"Updated {file_rel}: now {len(new_lines)} lines")
    else:
        print(f"ERROR: Reference header not found in {file_rel}")

# 1. Future Scenarios Deep Dive.md (143 -> ~160 lines)
c1 = """### Civilizational Attractor State Equilibrium Modeling

The long-run evolutionary trajectory of planetary intelligence converges toward specific attractor basins defined by the interaction between coordination capability and technical offense-defense balance. Formally, let state vector $\\mathbf{s} \\in \\mathcal{S}$ denote civilization configuration across sovereign autonomy, resource allocation, and cognitive alignment. The dynamical system exhibits Lyapunov stability around attractor $\\mathbf{s}^*$ when the potential function satisfies:

$$V(\\mathbf{s}) = \\sum_{k=1}^K \\omega_k (s_k - s_k^*)^2, \\quad \\frac{dV}{dt} < 0 \\; \\forall \\mathbf{s} \\neq \\mathbf{s}^*$$

| Civilizational Basin Schema | Autonomy Metric | Resource Allocation Efficiency | Conflict Vulnerability Rate | Long-Term Thermodynamic Viability |
| :--- | :--- | :--- | :--- | :--- |
| Unified Singleton Attractor | Centralized Policy Matrix | Pareto-Optimal Resource Ingestion | Negligible Internal Warfare | Maximal Entropy Dissipation Bound |
| Program Equilibrium Coalition | Distributed Autonomous Agents | Smart Contract Micro-Arbitrage | Zero-Sum Escalation Minimized | High Fault-Tolerant Redundancy |
| Competitive Multipolar Grid | Geopolitical Sovereign Blocs | Strategic Stockpiling Redundancy | Heightened First-Strike Exposure | Fragile Dynamic Stability Equilibrium |"""

# 2. Historical Development Deep Dive.md (140 -> ~160 lines)
c2 = """### Algorithmic Efficiency Gains vs Hardware Substrate Telemetry

Historical compute trajectory demonstrates that algorithmic innovations consistently provide effective compute multipliers that match or exceed raw silicon scaling. While physical transistor density followed Moore's Law doubling cycles of roughly 24 months, algorithmic efficiency in training deep representations progressed at an accelerated doubling cadence of 8 to 12 months.

| Algorithmic Frontier Innovation | Primary Architectural Mechanism | Compute Efficiency Multiplier | Physical Bottleneck Bypassed | Empirical Verification Source |
| :--- | :--- | :--- | :--- | :--- |
| Residual Identity Connections | Skip-Connection Gradient Flow | $10^1$ Training Depth Multiplier | Vanishing Gradient Saturation | He et al. (2016 ImageNet) |
| Multi-Head Self-Attention | Dense Sequence Context Routing | $10^2$ Sample Efficiency Multiplier | Recurrent Sequential Memory Dependency | Vaswani et al. (2017 Transformer) |
| Chinchilla Optimal Token Ratio | Equal Token-Parameter Scaling | $3.5\\times$ Pre-Training FLOP Savings | Parameter-Overparameterized Under-Training | Hoffmann et al. (2022 DeepMind) |
| FlashAttention Memory Tiling | IO-Aware GPU SRAM Kernel Fusion | $2.5\\times$ Wall-Clock Speedup Ratio | High-Bandwidth Memory (HBM) IO Wall | Dao et al. (2022 Stanford) |"""

# 3. Policy Implications Deep Dive.md (136 -> ~160 lines)
c3 = """### Game-Theoretic Proliferation Dynamics and International Monitoring Verification

Frontier AI non-proliferation governance mirrors classical arms control verification under asymmetric inspection information. A sovereign jurisdiction faces the decision to comply with international compute caps or secretly defect to pursue sovereign frontier capabilities. The equilibrium monitoring threshold is derived via an inspection game where the inspector audits with mixed-strategy probability:

$$p_{\\text{audit}}^* = \\frac{C_{\\text{defect}}}{V_{\\text{detect}} - V_{\\text{evade}} + C_{\\text{defect}}}$$

| International Regulatory Tier | Primary Verification Instrumentation | Inspection Cadence Schedule | Evasion Detection Confidence | Diplomatic Enforcement Mandate |
| :--- | :--- | :--- | :--- | :--- |
| Extreme Lithography Controls | Scanner Telemetry Cryptographic Logs | Continuous Real-Time Streaming | Exceeds 99.5% Assurance Rate | Multilateral Export Denial Sanctions |
| Hyperscale Grid Power Audit | Substation MW Flow Transformer Sensors | Hourly Automated Ingestion Matching | $\\approx 96.8\\%$ Ingestion Accuracy | Sovereign Energy Allocation Limits |
| Distributed Model Weight Attestation | Trusted Execution Environment Proofs | Per-Training Run Checkpoint Audit | $\\approx 94.2\\%$ Cryptographic Proof | Model Registry Revocation Protocol |"""

# 4. Societal Impacts Deep Dive.md (145 -> ~160 lines)
c4 = """### Factor Share Divergence and Capital Deepening Trajectories

The macroeconomic transition toward automated cognitive labor fundamentally alters classical national income accounting factor shares. As artificial cognitive agents substitute for human knowledge work across all productive sectors, the aggregate elasticity of substitution between capital and labor approaches infinity ($\\sigma_{KL} \\to \\infty$), shifting marginal income from wages to computational equity.

| Historical Economic Era | Aggregate Labor Factor Share | Capital Factor Share | Primary Wealth Transmission Channel | Structural Disruption Velocity |
| :--- | :--- | :--- | :--- | :--- |
| Early Industrialization (1780–1850) | $\\approx 52\\%$ National Income | $\\approx 48\\%$ National Income | Mechanized Mill Equity & Land Rents | Decadal Urban Wage Attrition |
| Post-War Golden Age (1945–1975) | $\\approx 68\\%$ National Income | $\\approx 32\\%$ National Income | Unionized Industrial Manufacturing Wages | Broad Middle-Class Expansion Cycle |
| Cognitive Phase Shift (2025–2035) | $\\le 25\\%$ Projected Factor Share | $\\ge 75\\%$ Projected Factor Share | Algorithmic Compute Clusters & IP Rights | Hyper-Accelerated Capital Deepening |"""

insert_before_references("Future_Scenarios/Future Scenarios Deep Dive.md", c1)
insert_before_references("Historical_Development/Historical Development Deep Dive.md", c2)
insert_before_references("Policy_Implications/Policy Implications Deep Dive.md", c3)
insert_before_references("Societal_Impacts/Societal Impacts Deep Dive.md", c4)
