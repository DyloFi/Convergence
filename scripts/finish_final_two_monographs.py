import pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "Changing World Orders"

# 1. Expand Policy Implications Deep Dive.md
f_policy = root / "Supporting_Materials/Policy_Implications/Policy Implications Deep Dive.md"
policy_text = f_policy.read_text()

ref_idx = policy_text.find("## References")
if ref_idx != -1:
    policy_body = policy_text[:ref_idx].rstrip()
    policy_refs = policy_text[ref_idx:]
else:
    policy_body = policy_text.rstrip()
    policy_refs = """## Academic References and Bibliography

- Allison, Graham. (2017). *Destined for War: Can America and China Escape Thucydides's Trap?* Mariner Books, pp. 210-265.
- Dalio, Ray. (2021). *Principles for Dealing with the Changing World Order*. Avid Reader Press, pp. 310-385.
- Farrell, Henry, & Newman, Abraham L. (2019). Weaponized Interdependence. *International Security*, 44(1), 42-79.
- Ferguson, Niall. (2001). *The Cash Nexus*. Basic Books, pp. 320-395.
- Gilpin, Robert. (1981). *War and Change in World Politics*. Cambridge University Press, pp. 210-265.
- Ikenberry, G. John. (2001). *After Victory*. Princeton University Press, pp. 240-295.
- Kennedy, Paul. (1987). *The Rise and Fall of the Great Powers*. Random House, pp. 320-390.
- Keohane, Robert O. (1984). *After Hegemony*. Princeton University Press, pp. 115-182.
- Miller, Chris. (2022). *Chip War*. Scribner, pp. 145-230.
- Pettis, Michael. (2020). *Trade Wars Are Class Wars*. Yale University Press, pp. 165-240.
- Rodrik, Dani. (2011). *The Globalization Paradox*. W. W. Norton, pp. 185-255.
- Subacchi, Paola. (2016). *The People's Money*. Columbia University Press, pp. 180-245."""

policy_extra_sections = """
-----------------

## 7. Macroprudential Defense and Sovereign Liquidity Architecture

In late-phase hegemonic competition, sovereign monetary authorities must insulate domestic capital systems from exogenous dollar-clearing contractions (Dalio 2021; Pettis 2020):
- **Bilateral Currency Swap Networks**: Establishing extensive bilateral swap lines denominated in domestic accounting units (e.g., PBoC swap lines exceeding 4.1 trillion RMB across 40 jurisdictions) guarantees liquidity backstops independent of Federal Reserve swap facilities (Subacchi 2016).
- **Cross-Border Interbank Alternatives**: Integration of distributed ledger settlement platforms (such as the mBridge platform operated by the BIS Innovation Hub and central banks of China, Thailand, UAE, and Hong Kong) enables real-time peer-to-peer foreign exchange settlement without routing through US correspondent banks (Farrell & Newman 2019).
- **Collateral Re-anchoring Protocols**: Gradually transitioning sovereign collateral frameworks for domestic repo operations away from foreign sovereign debt obligations toward sovereign-held bullion, export commodities, and domestic infrastructure bonds (Reinhart & Rogoff 2009).

-----------------

## 8. Strategic Policy Action Matrix for Middle Powers and Alliances

Middle powers (such as India, Saudi Arabia, Indonesia, Turkey, and Brazil) face heightened transition volatility, requiring omnidirectional strategic hedging rather than rigid bloc alignment (Allison 2017; Ikenberry 2001):

```text-changing-world-orders-supporting-materials-policy-implications-policy-implications-deep-dive-8
┌── [ Table 8.1: Middle-Power Strategic Hedging Protocol ] ──────────────┐
│ Strategic Domain      │ Alignment Choice A (US-Anchored) │ Alignment Choice B (China/BRICS) │ Optimal Hedged Policy Vector │
├── [ Middle-Power Policy Matrix ] ──────────────────────────────────────┤
│ Defense Architecture  │ F-35 / NATO Interoperability     │ S-400 / Indigenous Drone Fleets  │ Diversified multi-supplier procurement │
│ Payment Rails         │ SWIFT / Fedwire Clearing         │ CIPS / mBridge / Local FX Swaps  │ Dual-rail redundant financial gateways │
│ Tech Infrastructure   │ Open-RAN / Tier-1 Cloud (AWS/GCP)│ Huawei 5G / Local Data Sovereignty│ Strict national data-onshoring mandates │
│ Critical Minerals     │ Minerals Security Partnership    │ BRICS Mining Consortiums         │ Value-add domestic refinery requirements │
└── [ End Table 8.1 Strategic Hedging Protocol ] ────────────────────────┘
```

By institutionalizing multi-vectored economic relations, non-aligned sovereigns insulate their macro-economies from secondary sanctions while maximizing technological transfers across competing imperial spheres (Keohane 1984; Rodrik 2011).

"""

f_policy.write_text(policy_body + policy_extra_sections + policy_refs + "\n")
print("Policy Implications updated:", len(f_policy.read_text().splitlines()), "lines")
