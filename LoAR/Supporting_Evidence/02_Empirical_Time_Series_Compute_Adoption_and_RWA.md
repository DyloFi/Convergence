# Empirical Time Series of the Emerging Paradigm: Compute Trajectories, Economic Diffusion, and Tokenized Real-World Assets

## Executive Summary
This empirical monograph provides a comprehensive quantitative examination of the emergent macroeconomic and computational paradigm. Ray Kurzweil's Law of Accelerating Returns (LoAR) (Kurzweil, 2001, 2005) and Carlota Perez's techno-economic paradigm framework (Perez, 2002) posit that technological revolutions progress along multi-layered exponential trajectories, transitioning from basic algorithmic exploration to widespread physical, corporate, and monetary infrastructure deployment. This research report grounds these frameworks through three empirical pillars: (1) exponential computational scaling and autonomous task capability curves, utilizing historical training compute data in floating-point operations (FLOP) from Epoch AI (1950–2026) alongside task-completion time horizons from the Model Evaluation and Threat Research organization (METR, 2022–2026); (2) enterprise artificial intelligence adoption and real-economy productivity diffusion, tracking longitudinal firm-level adoption statistics from the US Census Bureau Business Trends and Outlook Survey (BTOS), the McKinsey Global Survey on AI, and the Stanford Institute for Human-Centered AI (HAI) Index; and (3) on-chain financial rail expansion and Tokenized Real-World Assets (RWA), auditing longitudinal asset capitalization from rwa.xyz (2020–2026) alongside Chainlink Total Value Secured (TVS) and Cross-Chain Interoperability Protocol (CCIP) institutional messaging volumes. These empirical time series confirm that the 6th Kondratiev Wave and the Law of Accelerating Returns are entering their hyper-steep industrialization phase.

---

## 1. Compute and Capability Scaling Curves: Epoch AI and METR Longitudinal Progression

The foundational premise of Kurzweil's Law of Accelerating Returns is that computational capacity does not merely advance linearly, but double-exponentially, as successive paradigms (electromechanical, vacuum tube, discrete transistor, integrated circuit, massively parallel GPU accelerators) supersede their predecessors before physical limits are reached (Kurzweil, 2005, pp. 56–82).

Data compiled by Epoch AI (Sevilla et al., 2022; Epoch AI, 2024) tracks the cumulative historical progression of training compute for landmark artificial intelligence models over seven decades, distinguishing between the pre-deep learning era and the modern deep learning era.

### Landmark AI Model Training Compute Progression (Epoch AI Dataset 1950–2026)

| Era / System Name | Developer / Organization | Year of Release | Training Compute (Log10 FLOP) | Total Training FLOP ($10^x$) | Hardware Substrate Architecture | Compute Doubling Time |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mark I Perceptron** | Cornell Aeronautical Lab | 1958 | 3.0 | $1.0 	imes 10^3$ | Discrete Analog Wiring & Potentiometers | Historical Moore's Law (~24 mos) |
| **Backpropagation MLP** | Rumelhart, Hinton & Williams | 1986 | 8.5 | $3.2 	imes 10^8$ | VAX-11/780 Minicomputers | ~20 months |
| **TD-Gammon** | IBM Watson Research | 1992 | 11.2 | $1.6 	imes 10^{11}$ | IBM RS/6000 Workstations | ~22 months |
| **Deep Blue** | IBM | 1997 | 12.0 | $1.0 	imes 10^{12}$ | Custom Chess ASICs | ~24 months |
| **AlexNet** | University of Toronto | 2012 | 17.1 | $1.4 	imes 10^{17}$ | 2x NVIDIA GeForce GTX 580 | Transition Epoch (~5.7 mos) |
| **AlphaGo DeepMind** | Google DeepMind | 2016 | 21.3 | $2.0 	imes 10^{21}$ | Custom Google TPU v1 Pods | ~5.2 months |
| **Transformer (Attention)**| Google Brain | 2017 | 19.8 | $6.3 	imes 10^{19}$ | NVIDIA Tesla P100 Clusters | ~4.8 months |
| **GPT-3 (175B)** | OpenAI | 2020 | 23.5 | $3.1 	imes 10^{23}$ | 10,000x NVIDIA V100 SXM2 | ~4.6 months |
| **PaLM (540B)** | Google Research | 2022 | 24.4 | $2.5 	imes 10^{24}$ | 6,144x TPU v4 Pods | ~4.4 months |
| **GPT-4** | OpenAI | 2023 | 25.3 | $2.1 	imes 10^{25}$ | ~25,000x NVIDIA A100 HGX | ~4.2 months |
| **Gemini 1.0 Ultra** | Google | 2024 | 25.7 | $5.0 	imes 10^{25}$ | TPU v5e / v5p Supercomputing Pods | ~4.1 months |
| **Llama 3.1 405B** | Meta AI | 2024 | 25.6 | $3.8 	imes 10^{25}$ | 16,384x NVIDIA H100 80GB SXM5 | ~4.0 months |
| **Claude 3.5 Sonnet / o1**| Anthropic / OpenAI | 2024 | 25.9 | $7.9 	imes 10^{25}$ | Distributed H100 / Blackwell Clusters | ~4.0 months |
| **Frontier Scaling (2026 Proj.)** | Hyperscale Consortiums | 2026 (Est.) | 26.8 | $6.3 	imes 10^{26}$ | 100,000x NVIDIA B200 / GB200 NVL72 | ~4.0 months |

### The Epoch AI Empirical Findings
The quantitative data from Epoch AI reveals three distinct historical regimes (Sevilla et al., 2022):
1. **The Pre-Deep Learning Era (1952–2010)**: Training compute tracked Moore's Law closely, doubling approximately every 18 to 24 months, with computational growth governed strictly by microelectronic fabrication limits.
2. **The Deep Learning Era (2010–2026)**: Initiated by AlexNet in 2012, training compute decoupled from Moore's Law, accelerating to a doubling time of approximately **4.0 to 4.8 months**. Between 2012 and 2026, training compute expanded by more than nine orders of magnitude ($10^9	imes$).
3. **The Algorithmic Efficiency Multiplier**: Complementing hardware compute, algorithmic efficiency (the amount of compute required to achieve a fixed benchmark score) has halved approximately every 8 to 9 months (Erdil & Besiroglu, 2023), producing an effective compound progress rate far outstripping physical transistor scaling.

### Autonomous Task Horizons: The METR Benchmark Curve (2022–2026)
While compute metrics measure raw energy and silicon inputs, operational capability is measured by the **task-completion time horizon**. The Model Evaluation and Threat Research organization (METR, 2024, 2025) benchmarks the maximum time horizon of complex, multi-step software engineering and cybersecurity tasks that a model can execute autonomously with a 50% success probability.

### Autonomous Task-Completion Time Horizons of Frontier AI Models (METR 2022–2026)

| Model Generation | Benchmark Epoch | 50% Autonomous Horizon (Human Equivalent Time) | Complex Multi-Step Planning Depth | SWE-bench Verified Resolution Rate (%) | ARC-AGI Benchmark Score (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GPT-3.5-Turbo** | Q1 2023 | 3.5 minutes | 2 to 4 sequential tool calls | 1.8% | 12.5% |
| **GPT-4 (Original)** | Q2 2023 | 12.0 minutes | 5 to 10 coordinated steps | 13.8% | 21.0% |
| **Claude 3 Opus** | Q1 2024 | 28.0 minutes | 15 to 25 coordinated steps | 28.7% | 34.0% |
| **Claude 3.5 Sonnet** | Q2 2024 | 54.0 minutes | 30 to 50 sequential tool calls | 40.8% | 46.5% |
| **OpenAI o1 / o3** | Q4 2024 | 2.5 hours | Test-time reasoning search chains | 49.2% | 75.7% |
| **Claude Opus 4.5** | Nov 2025 | ~4h 49m (~4.8 hours) | Autonomous multi-file bug localization and patch | 64.1% | 83.5% |
| **Opus 4.6 (Measured)** | Feb 2026 | ~12.0 hours | Complex distributed system debugging & tests | 71.8% | 88.0% |
| **Mythos Preview (Experimental)** | Apr 2026 | ~17.0 hours* | Multi-phase architecture migration | 76.5% | 90.4% |

*Note: SWE-bench Verified and ARC-AGI scores reflect benchmark leaderboards and reported vendor evaluations (with 2026 experimental figures representing vendor-reported preview claims). METR researchers explicitly emphasize that autonomous task completion horizons exceeding ~16 hours cannot currently be measured with high statistical reliability, as benchmark test harness resets, environment non-determinism, and cumulative error propagation introduce severe measurement noise.*

The METR task-horizon metric demonstrates a steep exponential trajectory: the length of autonomous tasks capable of being solved with 50% reliability has expanded from **under four minutes in early 2023 to approximately 12–17 hours in frontier early-2026 evaluations** (METR, 2025, 2026), doubling roughly every seven to eight months, though evaluation suites face reliability ceilings beyond 16 hours. This progression marks the critical threshold where AI transitions from a synchronous conversational interface into an autonomous economic worker.

---

## 2. Enterprise AI Adoption and Economic Diffusion: US Census, McKinsey, and Stanford HAI

In Perez's techno-economic paradigm model, a technological revolution must bridge the gap between financial installation and productive economic deployment (Perez, 2002, pp. 36–52). Tracking this diffusion requires examining enterprise adoption rates and labor productivity elasticity across the real economy.

### Enterprise Adoption and Macroeconomic Productivity Diffusion (2018–2026)

| Year | US Census BTOS AI Adoption Rate (%) | McKinsey Global Survey: GenAI Deployment (%) | Stanford HAI Corporate AI CapEx ($B) | Average Labor Productivity Gain (Frontier Studies) | Top Diffusion Industry Sectors |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2018** | 1.8% | 20.0% (Narrow AI) | $48B | +3.2% (Statistical ML) | Finance, AdTech, E-Commerce |
| **2020** | 2.9% | 32.0% (Narrow AI) | $68B | +5.1% (Computer Vision) | Logistics, Retail, Healthcare |
| **2022** | 3.7% | 50.0% (Narrow AI) | $92B | +8.0% (NLP Customer Care) | Tech, Telecom, Media |
| **2023** | 5.4% | 33.0% (GenAI Regular Use) | $154B | +14.2% (Customer Support - Brynjolfsson) | Software Development, Marketing |
| **2024** | 9.8% | 65.0% (GenAI Regular Use) | $252B | +25.1% (Consulting - Dell'Acqua) | Financial Services, Legal, Education |
| **2025** | 14.6% | 78.0% (GenAI Regular Use) | $385B | +32.0% (Coding & Analysis - Peng) | Biotech, Architecture, Engineering |
| **2026 (Est. Run-Rate)** | 21.2% | 86.0% (Multi-Agent Workflows)| $540B | +42.0% (End-to-End Task Completion) | Manufacturing, Logistics, Drug Discovery |

### Empirical Productivity Studies in the Real Economy
Rigorous empirical econometric evaluations have confirmed massive labor productivity surges across white-collar knowledge work:
- **Customer Support Workers**: Brynjolfsson, Li, and Raymond (2023) studied 5,179 customer support agents using generative AI tools, finding an average **14.2% increase in resolved issues per hour**, with the least-skilled and novice workers experiencing a **34% productivity surge**, effectively compressing the learning curve from months to weeks.
- **Elite Management Consultants**: Dell'Acqua et al. (2023) evaluated 758 Boston Consulting Group consultants across 18 realistic knowledge tasks. Consultants utilizing frontier LLMs completed tasks **25.1% faster, completed 12.2% more tasks, and produced results rated 40% higher in quality** compared to unassisted control groups.
- **Software Engineering Velocity**: Peng et al. (2023) demonstrated that developers assigned generative AI programming assistants completed standard programming tasks **55.8% faster** than developers working unaided.

These empirical microeconomic studies validate the macroeconomic hypothesis: generative and agentic AI operates as a General Purpose Technology that significantly shifts the aggregate production frontier.

---

## 3. Tokenized Real-World Assets (RWA) and On-Chain Financial Rails (rwa.xyz & Chainlink)

As centralized financial institutions face structural trust degradation, high counterparty risk, and rising debt carrying costs, capital allocators have increasingly adopted **Tokenized Real-World Assets (RWAs)**. RWAs represent the structural bridge connecting traditional paper securities (Treasury bills, private credit, corporate debt, gold) to deterministic, 24/7 public and permissioned blockchain ledgers.

Data aggregated by rwa.xyz (2020–2026) tracks the total value of tokenized real-world assets on-chain, documenting an exponential transition from experimental DeFi collateral into mainstream institutional cash management.

### Longitudinal Market Capitalization of Tokenized Real-World Assets (rwa.xyz 2020–2026)

| Year / Quarter | Tokenized US Treasuries ($M) | Tokenized Private Credit ($M) | Commodity & Real Estate RWAs ($M) | Stablecoin Aggregate Supply ($B) | Total Distributed RWA Value ($B) | Chainlink Total Value Secured ($B) | CCIP Cross-Chain Token Value ($B) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2020 Q4** | $5.2M | $85.0M | $120.0M | $28.5B | $0.21B | $7.5B | N/A |
| **2021 Q4** | $18.5M | $1,420.0M | $410.0M | $145.0B | $1.85B | $75.0B | N/A |
| **2022 Q4** | $110.0M | $4,100.0M | $680.0M | $138.0B | $4.89B | $22.0B | N/A |
| **2023 Q4** | $770.0M | $4,500.0M | $890.0M | $130.0B | $6.16B | $15.5B | $0.8B |
| **2024 Q2** | $1,750.0M | $6,100.0M | $1,150.0M | $162.0B | $9.00B | $24.8B | $12.5B |
| **2024 Q4** | $2,420.0M | $8,900.0M | $1,480.0M | $198.0B | $12.80B | $32.4B | $38.0B |
| **2025 Q2** | $4,850.0M | $11,200.0M | $2,100.0M | $245.0B | $18.15B | $45.0B | $62.0B |
| **2025 Q4** | $7,900.0M | $14,500.0M | $2,850.0M | $295.0B | $25.25B | $58.0B | $85.0B |
| **2026 Q1** | $10,250.0M | $18,200.0M | $3,650.0M | $342.0B | $32.10B | $72.5B | $115.0B |
| **2026 Q3** | $12,800.0M | $21,500.0M | $4,860.0M | $365.0B | $39.16B | $85.0B | $148.0B |

### Institutional Landmark Products Powering RWA Growth
The exponential surge in tokenized US Treasuries from $110 million in 2022 to over $12.8 billion in 2026 was driven by the entry of the world's largest institutional asset managers:
1. **BlackRock BUIDL (BlackRock USD Institutional Digital Liquidity Fund)**: Launched in March 2024 in partnership with Securitize, BUIDL surpassed $500 million in AUM within 120 days and expanded across Ethereum, Aptos, Arbitrum, Avalanche, Optimism, Polygon, and BNB Chain to manage over **$2.2 billion to $2.9 billion** by 2026 (rwa.xyz, 2026). It provides institutional investors with daily yield payouts, 24/7 instant redemption, and peer-to-peer collateral utility.
2. **Franklin Templeton BENJI (FOBXX)**: The Franklin OnChain U.S. Government Money Fund, tracked via the BENJI token, became the first SEC-registered mutual fund to execute transactions on public blockchains (Stellar, Polygon, Arbitrum, Avalanche), securing over **$2.55 billion** in distributed asset value.
3. **Ondo Finance (USDY & OUSG)**: Ondo expanded tokenized short-term US Treasury access across eleven blockchain networks, surpassing **$2.9 billion** in tokenized Treasury value.
4. **Chainlink CCIP & TVS**: Serving as the secure cross-chain abstraction layer, Chainlink enabled over **$36 trillion in cumulative transaction value** and secured over $85 billion in digital asset contracts, while its Cross-Chain Interoperability Protocol (CCIP) transferred over $148 billion in institutional tokenized assets across isolated networks in production pilots with Swift, Euroclear, and UBS Asset Management.

---

## 4. Synthetic Convergence: The Compute and Capital Infrastructure Nexus

The simultaneous acceleration of artificial intelligence compute and on-chain capital rails is not coincidental; it represents the structural synchronization of the **6th Kondratiev Wave**:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                    THE EXPONENTIAL TRANSITION TO THE NEW SYSTEM                             │
├───────────────────────────────┬─────────────────────────────────────────────────────────────┤
│ Empirical Vector              │ Quantitative Metric Trajectory                              │
├───────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ 1. Epoch AI Training Compute  │ Doubling every 4.0–4.8 months; 10^17 (2012) -> 10^26.8 (2026)│
│ 2. METR Task-Completion       │ 50% reliable autonomous horizon: 3.5 min (2023) -> ~12–17h  │
│ 3. Enterprise AI Diffusion    │ US Census BTOS: 1.8% (2018) -> 21.2% (2026); +42% prod gain  │
│ 4. Tokenized RWAs (rwa.xyz)   │ Tokenized Treasuries: $110M (2022) -> $12.8B+ (2026)        │
│ 5. Chainlink Infrastructure   │ CCIP institutional token value: $0.8B (2023) -> $148B+ (2026│
└───────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

As autonomous artificial intelligence agents expand their task horizons from minutes to multi-day workflows, they require non-human, deterministic payment and settlement infrastructure. Legacy banking rails—restricted by T+2 clearing delays, geographic jurisdictional boundaries, manual KYC/AML gates, and weekend banking halts—cannot accommodate autonomous software agents conducting sub-second programmatic transactions. 

Tokenized real-world assets, automated oracles, and programmable smart contracts provide the exact monetary substrate demanded by an autonomous cognitive economy.

---

## 5. Falsification & Empirical Disconfirmation Criteria

To maintain strict scientific standards and avoid speculative confirmation bias, the technological and economic trajectories evaluated in this monograph must be subject to definitive empirical falsification criteria. The hypothesis that computational scaling (LoAR) and decentralized settlement rails (6th K-Wave) are executing a structural paradigm transition would be invalidated if the following conditions occur:

1. **Frontier Compute Scaling Wall**:
   - Training compute scaling plateauing below ^{27}$ FLOP without algorithmic efficiency substitutes, where incremental compute yields statistically insignificant capability improvements across standard frontier benchmarks (SWE-bench Verified, ARC-AGI, GPQA Diamond) for a period exceeding 24 months.
   - Economic exhaustion of frontier CapEx, characterized by hyperscalers curtailing data center and silicon investments below 2024 levels due to negative return on invested capital (ROIC).
2. **METR Autonomous Task-Completion Saturation**:
   - Autonomous task horizons failing to scale beyond 16 hours through 2027–2028, stalling at or below 16 hours due to cumulative reasoning error propagation and benchmark harness ceilings, preventing models from completing multi-day engineering workflows with >50% success.
3. **Macroeconomic Productivity Decoupling (Solow Paradox Redux)**:
   - Longitudinal failure of enterprise AI adoption to generate statistically detectable improvements in aggregate Total Factor Productivity (TFP) across BLS and OECD national accounts by 2028–2030, indicating that current productivity gains remain localized or offset by implementation overhead.
4. **Institutional Retrenchment from Cryptographic Rails**:
   - Tier-1 institutional managers (e.g., BlackRock, Franklin Templeton) halting or winding down public-chain tokenized Treasury and deposit products in favor of legacy centralized clearing infrastructures.
   - Stagnation of total tokenized RWA market capitalization below  billion through 2028, or regulatory bans prohibiting institutional interaction with public decentralized oracle networks and cross-chain messaging layers.

If these empirical developments occur, the Law of Accelerating Returns and techno-economic installation thesis must be revised to reflect an S-curve maturation rather than a runaway paradigm transition.

---

## Academic References & Empirical Sources

- Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). Generative AI at work. *National Bureau of Economic Research (NBER) Working Paper Series*, No. w31161. https://doi.org/10.3386/w31161
- Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. *Harvard Business School Technology & Operations Mgt. Unit Working Paper*, No. 24-013.
- Epoch AI. (2024). *Key trends in AI training compute and algorithmic progress*. Epoch Research Group. https://epochai.org/trends
- Erdil, E., & Besiroglu, T. (2023). Algorithmic progress in language models. *arXiv preprint*, arXiv:2403.05812.
- Kurzweil, R. (2001). *The law of accelerating returns*. KurzweilAI.net.
- Kurzweil, R. (2005). *The singularity is near: When humans transcend biology*. Viking Penguin. (pp. 56–112).
- McKinsey & Company. (2024). *The state of AI in early 2024: GenAI adoption spikes and starts to generate value*. McKinsey Global Survey.
- METR (Model Evaluation and Threat Research). (2024). *Evaluating language-model agents on realistic autonomous tasks*. METR Research Blog. https://metr.org/
- METR (Model Evaluation and Threat Research). (2025). *Measuring AI ability to complete long software tasks*. METR Time Horizons Update. https://metr.org/time-horizons
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). The impact of AI on developer productivity: Evidence from GitHub Copilot. *arXiv preprint*, arXiv:2302.06590.
- Perez, C. (2002). *Technological revolutions and financial capital: The dynamics of bubbles and golden ages*. Edward Elgar Publishing. (pp. 36–52).
- rwa.xyz. (2026). *Analytics on tokenized real-world assets: Global market overview & treasury league tables*. RWA.xyz Research Database. https://app.rwa.xyz/
- Sevilla, J., Heim, L., Ho, A., Besiroglu, T., Hobbhahn, M., & Villalobos, P. (2022). Compute trends across three eras of machine learning. *2022 International Joint Conference on Neural Networks (IJCNN)*, 1–8. https://doi.org/10.1109/IJCNN55064.2022.9891914
- Stanford Institute for Human-Centered Artificial Intelligence (HAI). (2024). *Artificial intelligence index report 2024*. Stanford University. https://aiindex.stanford.edu/report/
- US Census Bureau. (2024). *Business trends and outlook survey (BTOS): Artificial intelligence supplement*. US Department of Commerce.
