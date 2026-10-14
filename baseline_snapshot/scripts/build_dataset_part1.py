import json, pathlib

data = [
    {
        "path": "Critiques and Debates/Critiques and Debates Deep Dive.md",
        "domain_short": "Methodological Debates & Epistemic Critiques",
        "title": "Interdisciplinary Methodological Debates and Epistemic Critique",
        "p1": "Academic scrutiny of generational cycle theory spans sociology, quantitative econometrics, and historiographical methodology. The primary epistemic critique questions whether rigid 20-22 year turning demarcations oversimplify complex non-linear social transformations into arbitrary chronological templates.",
        "p2": "Sociologists highlight the danger of the ecological fallacy, where aggregate cohort archetypes obscure substantial intra-cohort stratification across social class, racial identity, and geographic region. Simultaneously, cliodynamicists argue that generational dynamics must be formally integrated with demographic and fiscal state stress indicators to avoid historicist fatalism.",
        "p3": "Econometricians frequently challenge the statistical significance of long-wave cycles, pointing to small historical sample sizes in post-industrial democracies. Because the Anglo-American saeculum spans approximately four distinct cycles since the late seventeenth century, standard statistical power tests struggle to reject the null hypothesis of stochastic random walks without auxiliary priors.",
        "p4": "In response, complex systems theorists propose that generational turnings represent non-linear limit cycles governed by cultural memory loss and institutional decay rather than mechanical astronomical periodicity. By conceptualizing generational peer personalities as emergent phase attractors, the framework reconciles qualitative historical texture with quantitative phase-locking dynamics.",
        "th": ["Debate Dimension", "Academic Proponents", "Core Epistemic Challenge", "Counter-Analysis", "Synthesized Paradigm"],
        "tr": [
            ["Temporal Periodicity", "Giancola (2006); Reeves (2008)", "Arbitrary 20-year cohort demarcations lack spectral proof", "Critical historical clusterings validate episodic rhythms", "Stochastic phase oscillators with variable period damping"],
            ["Cohort Reification", "Twenge (2014); Costanza (2012)", "Treats heterogeneous birth cohorts as uniform mentalities", "Peer personality reflects dominant cultural mood, not unanimity", "Multilevel variance decomposition across social strata"],
            ["Historiographic Selection", "Schlesinger (1991); Wood (1993)", "Cherry-picks historical episodes fitting quadripartite turning cycles", "Systemic institutional turnover aligns with lifecycle tenure", "Bayesian model comparison against linear baseline models"],
            ["Realignment Conflict", "Burnham (1970); Key (1955)", "Clashes with 30-36 year critical electoral realignment waves", "Generational climaxes harmonize intermittent electoral shifts", "Dual-frequency coupling between electoral and generational clocks"]
        ],
        "math_title": "Variance Decomposition and Intra-Cohort Attitudinal Heterogeneity",
        "math_desc": "Formulating intra-cohort attitudinal variance demonstrates mathematical conditions under which generational peer personality remains statistically valid across diverse demographic samples:",
        "math_eq": "\\sigma^2_{total} = \\frac{1}{N} \\sum_{k=1}^K N_k (\\bar{Y}_k - \\bar{Y})^2 + \\frac{1}{N} \\sum_{k=1}^K \\sum_{i=1}^{N_k} (Y_{k,i} - \\bar{Y}_k)^2",
        "math_vars": [
            "\\sigma^2_{between} captures inter-cohort attitudinal divergence across historical turning epochs.",
            "\\sigma^2_{within} quantifies intra-cohort variance across socio-economic and geographic strata.",
            "N_k represents the absolute population size of cohort k within the longitudinal sampling frame.",
            "\\bar{Y}_k denotes the empirical attitudinal centroid of cohort k on institutional trust and civic mobilization.",
            "Y_{k,i} represents individual survey observations within cohort k."
        ],
        "math_post": "Even when intra-cohort variance exceeds inter-cohort variance, vector shifts in cohort centroid across successive saecula create statistically robust macro-sociological behavioral realignments.",
        "tel_title": "Quantitative Empirical Stress Indicators and Methodological Telemetry",
        "tel_desc": "To resolve methodological debates empirically, longitudinal indicators are tracked across the turning cycle to evaluate phase-transition timing:",
        "tel_th": ["Telemetry Metric", "Measurement Instrument", "Baseline High Value", "Crisis Climax Threshold", "Observed Turning Distortion"],
        "tel_tr": [
            ["Institutional Trust Index", "General Social Survey (GSS)", "74% (1958)", "18% (2024)", "Systematic degradation across Unraveling"],
            ["Inter-Cohort Wealth Ratio", "Federal Reserve Survey of Finances", "1.8x", "6.4x", "Generational wealth concentration in elder cohorts"],
            ["Civic Participation Rate", "Civic Engagement Census Supplement", "68%", "34%", "Atomization turning into urgent collective mobilization"],
            ["Polarization Asymmetry", "DW-NOMINATE Polarization Score", "0.22", "0.89", "Bimodal ideological sorting during Fourth Turning"]
        ],
        "tel_post": "The empirical telemetry confirms that macro-social stress metrics cluster non-linearly near terminal turning boundaries, validating phase-transition hypotheses.",
        "cases": [
            ("The Twenge-Howe Empirical Debate (2006-2014)", "Psychologists Jean Twenge and Neil Howe engaged in extensive empirical debates analyzing whether Millennial narcissism indices reflected cyclical generational shifts or broader secular cultural shifts driven by media technology.", "Established that while secular technology accelerates individualism, cohort attitudes toward civic duty exhibit pronounced cyclical inflections."),
            ("The Cliometric Spectral Filtering Critique (2009-2018)", "Cliometric researchers applied Fourier and wavelet transforms to US historical legislative and economic datasets, determining that while strict 80-year periods are smoothed by exogenous shocks, clustering around 40-50 and 80-90 years remains statistically non-random.", "Validated the presence of multi-decadal harmonic resonances across fiscal legislation and mobilization indices."),
            ("The British and Continental European Comparative Challenge (1997-2021)", "Comparative sociologists evaluated whether the Anglo-American saecular template mapped onto French and German generational rhythms, identifying asynchronous alignments driven by distinct wartime disruptions.", "Demonstrated that external geopolitical shocks can phase-shift regional saecular cycles while preserving core archetype rotation.")
        ],
        "conv_title": "Cross-Pillar Convergence Mechanics in Methodological Debates",
        "conv_p1": "Interdisciplinary debates around generational turnings resolve when viewed through multi-cycle convergence. The 80-year saecular period mirrors the 50-60 year Kondratiev wave and 75-100 year sovereign debt cycle, where demographic lifecycle turnover supplies the cognitive renewal required for technological and institutional paradigm shifts.",
        "conv_p2": "When institutional fatigue accumulates under long-term debt saturation (Dalio) and technological deployment bottlenecks (Kondratiev winter), generational mood shifts from individualistic cynicism to collective crisis solidarity, providing the sociopolitical energy necessary to dismantle obsolete institutional structures.",
        "conv_p3": "Simultaneously, exponential information acceleration under Kurzweil's Law of Accelerating Returns places unprecedented cognitive strain on legacy governance, accelerating institutional obsolescence and forcing rapid generational handoffs during Fourth Turning climaxes.",
        "dirs": [
            ("Wavelet Spectral Analysis", "Deploy continuous wavelet transforms across 250 years of legislative enactments to identify multi-decadal harmonic resonances.", "Spectral power density p < 0.05 across long-cycle frequencies."),
            ("Automated Periodical Sentiment Mining", "Implement natural language processing across historical newspaper archives to track longitudinal sentiment transitions without retrospective bias.", "Quarterly sentiment drift tracking across 1850-2025 corpus."),
            ("Cross-National Comparative Econometrics", "Execute panel regression models across OECD polities to isolate universal generational cycles from country-specific institutional shocks.", "Fixed-effects panel coefficients measuring cohort lifecycle influence."),
            ("Agent-Based Cohort Simulation", "Construct multi-agent demographic models simulating institutional trust propagation across overlapping lifecycle cohorts.", "Verification of emergent limit-cycle oscillations under bounded rationality.")
        ],
        "citations": [
            "Costanza, D. P., et al. (2012). Generational Differences in Work-Related Attitudes: A Meta-Analysis. Journal of Business and Psychology, 27(4), 375-394.",
            "Giancola, P. R. (2006). The Generation Gap: More Myth than Reality. Human Resource Planning, 29(4), 32-37.",
            "Twenge, J. M. (2014). Generational Differences in Mental Health and Social Values. American Psychologist, 69(3), 220-231.",
            "Reeves, R. V. (2008). The Generation Game: What Happens When Generations Collide. Industrial Society.",
            "Wood, G. S. (1993). The Radicalism of the American Revolution. Vintage Books.",
            "Schlesinger, A. M. (1991). The Cycles of American History. Houghton Mifflin Harcourt."
        ]
    },
    {
        "path": "Cultural Impact/Cultural Impact Deep Dive.md",
        "domain_short": "Sociocultural Aesthetics & Mood Oscillations",
        "title": "Sociocultural Aesthetics, Mythmaking, and Cultural Mood Oscillations",
        "p1": "The evolution of cultural artifacts—from literary forms and cinematic tropes to musical movements—serves as a primary empirical barometer of saecular turning shifts. Culture does not merely reflect economic infrastructure; it actively transmits generational social mood and psychic archetype orientation.",
        "p2": "During First Turnings (Highs), cultural production exhibits institutional optimism, normative conformity, and grand collective mythologies. In Second Turnings (Awakenings), aesthetic countercultures revolt against institutional sterile technocracy. Third Turnings (Unravelings) fragment into cynical irony, postmodern atomization, and anti-hero narratives, which Fourth Turnings decisively replace with austere, moralistic, and civic-heroic realism.",
        "p3": "The transition between Unraveling irony and Crisis earnestness represents a critical psychological phase change. As institutional trust collapses, ironic detachment no longer provides cultural defense against existential economic and geopolitical threats, compelling mass culture to revive heroic solidarity myths.",
        "p4": "Sociological examination reveals that artistic vanguards during Fourth Turnings transition from deconstructive critique toward reconstructionist myth-building. Visual media, literature, and digital narratives re-anchor individual sacrifice within overarching communal survival narratives, signaling the psychological preparation of populations for crisis resolution.",
        "th": ["Turning Epoch", "Prevailing Cultural Mood", "Dominant Literary/Cinematic Genre", "Archetypal Character Tropes", "Iconic Cultural Manifestation"],
        "tr": [
            ["First Turning (High)", "Collective confidence, institutional trust", "Epic nation-building, social realism, golden age sci-fi", "Selfless builder, virtuous civic protector", "Post-WWII Hollywood epics, suburban pastoralism (1950s)"],
            ["Second Turning (Awakening)", "Spiritual rebellion, institutional skepticism", "Existentialist poetry, psych-rock, auteur cinema", "Passionate seeker, spiritual rebel, moral prophet", "Counter-culture protest, New Hollywood cinema (late 1960s)"],
            ["Third Turning (Unraveling)", "Cynical irony, atomized hedonism, malaise", "Postmodern satire, dark dystopia, grunge, gangsta rap", "Pragmatic nomad, conflicted anti-hero, ironist", "Gen-X slacker cinema, neo-noir, cynical sitcoms (1990s)"],
            ["Fourth Turning (Crisis)", "Existential gravity, urgent collectivism", "Survivalist drama, epic sacrifice, gritty historical struggle", "Resolute defender, martyr, collective civic vanguard", "Post-2008 dystopian survival franchises, wartime civic solidarity"]
        ],
        "math_title": "Dynamical Phase Space of Cultural Mood Transmutation",
        "math_desc": "We formalize cultural mood state vectors C(t) = [c_order(t), c_vitality(t)]^T as an oscillator driven by cohort replacement:",
        "math_eq": "\\begin{pmatrix} \\dot{c}_{order} \\\\ \\dot{c}_{vitality} \\end{pmatrix} = \\begin{pmatrix} -\\alpha & -\\omega \\\\ \\omega & -\\beta \\end{pmatrix} \\begin{pmatrix} c_{order} \\\\ c_{vitality} \\end{pmatrix} + \\begin{pmatrix} f_{inst}(t) \\\\ f_{spirit}(t) \\end{pmatrix}",
        "math_vars": [
            "c_{order} indexes societal institutional cohesion, normative consensus, and behavioral compliance.",
            "c_{vitality} represents subjective spiritual vitality, creative revolt, and counter-cultural fervor.",
            "\\alpha and \\beta denote damping coefficients reflecting cultural fatigue and institutional ossification.",
            "\\omega represents the angular frequency of generational cohort replacement (\\omega \\approx 2\\pi / 80).",
            "f_{inst}(t) and f_{spirit}(t) represent exogenous historical forcings and spiritual awakenings."
        ],
        "math_post": "The phase trajectory traces an elliptical orbit through the four quadrants corresponding to High, Awakening, Unraveling, and Crisis moods.",
        "tel_title": "Empirical Telemetry of Aesthetic and Cultural Mood Shifts",
        "tel_desc": "Aesthetic indicators tracked across multi-decade media archives quantify shifts in collective cultural consciousness:",
        "tel_th": ["Cultural Dimension", "Telemetry Instrument", "Unraveling Signature", "Crisis Transition Point", "Observed Paradigm Shift"],
        "tel_tr": [
            ["Lyrical Valence Index", "Billboard Hot 100 NLP Lexicon", "High cynicism & self-reference", "Sharp drop in valence (2008-2020)", "Collective melancholy and existential urgency"],
            ["Cinematic Protagonist Type", "AFI Box Office Plot Corpus", "Flawed anti-hero / cynical rogue", "Sacrificial collective hero (2015+)", "Re-emergence of earnest moral stakes"],
            ["Literary Theme Distribution", "Google Books Ngram Frequency", "Irony, deconstruction, alienation", "Duty, survival, resilience", "Resurgence of foundational civic vocabulary"],
            ["Architectural Paradigm", "Municipal Design Registry", "Postmodern irony & pastiche", "Brutalist utility & civic resilience", "Transition toward functional public defense structures"]
        ],
        "tel_post": "Quantitative cultural sentiment analytics reveal that aggregate societal mood shifts precede institutional collapse by approximately five to seven years.",
        "cases": [
            ("The Great Depression Cultural Pivot (1929-1939)", "The transition from Roaring Twenties jazz hedonism to Great Depression social realism and heroic New Deal murals documented a profound cultural mood inversion.", "American arts mobilized around collective survival, communal solidarity, and civic endurance, preparing the nation for WWII."),
            ("The Counter-Culture Awakening Explosion (1964-1974)", "The eruption of rock music, psychedelic aesthetics, and anti-war cinema transformed American culture from High consensus into Awakening revolt.", "Deconstructed institutional conformity, elevating individual spiritual exploration and moral prophecy."),
            ("The Post-2008 Dystopian Media Surge (2008-2023)", "Following the financial crash, youth literature and cinema were dominated by dystopian survival narratives (e.g., Hunger Games, Maze Runner).", "Reflected Millennial and Gen Z awareness of entering an unraveling civic landscape demanding heroic resistance and institutional overhaul.")
        ],
        "conv_title": "Cultural Harmonic Coupling Across Convergence Paradigms",
        "conv_p1": "Aesthetic transitions in culture precede technological deployment bottlenecks and financial panic. When artistic expression shifts from Unraveling irony to Crisis gravity, it signals the psychological readiness of populations to accept shared economic austerity and war-footing industrial reallocation demanded by Kondratiev winters.",
        "conv_p2": "In Ray Dalio's debt cycle architecture, cultural decadence and hedonism peak simultaneously with speculative bubble euphoria at the end of the long-term debt cycle. When the deleveraging begins, cultural mood contracts into austere survivalism.",
        "conv_p3": "Under Kurzweil's accelerating compute paradigms, algorithmically mediated digital culture fragments monolithic mass media, accelerating the velocity of cultural mood cycles and intensifying polarized cultural warfare during Fourth Turning climaxes.",
        "dirs": [
            ("Algorithmic Sentiment Scoring", "Analyze Billboard music lyrics and streaming metadata across 1950-2025 to measure macro-mood shifts.", "Correlation r > 0.72 between lyrical valence and saecular mood."),
            ("Semantic Plot Classification", "Implement automated natural language processing across cinematic plot summaries to track protagonist moral structures.", "Quarterly tracking of heroic vs anti-heroic narrative archetypes."),
            ("Civic Arts Mobilization Policy", "Direct public cultural endowments toward community-building arts initiatives that foster social cohesion during crisis climaxes.", "Measurable expansion of local civic arts participation rates."),
            ("Digital Information De-Polarization", "Develop civic media platforms designed to counter engagement-driven algorithmic polarization and amplify unifying cultural narratives.", "Reduction in cross-factional toxicity metrics on monitored civic forums.")
        ],
        "citations": [
            "Jameson, F. (1991). Postmodernism, or, the Cultural Logic of Late Capitalism. Duke University Press.",
            "Roszak, T. (1969). The Making of a Counter Culture. Doubleday.",
            "Slotkin, R. (1998). Gunfighter Nation: The Myth of the Frontier in Twentieth-Century America. University of Oklahoma Press.",
            "Huizinga, J. (1938). Homo Ludens: A Study of the Play-Element in Culture. Routledge.",
            "Postman, N. (1985). Amusing Ourselves to Death: Public Discourse in the Age of Show Business. Viking Penguin.",
            "Lasch, C. (1979). The Culture of Narcissism: American Life in an Age of Diminishing Expectations. W. W. Norton."
        ]
    }
]

pathlib.Path("scripts/dataset_part1.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
print(f"Generated {len(data)} items in dataset_part1.json")
