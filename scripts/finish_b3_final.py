import pathlib

root = pathlib.Path("4th Turning")

files_and_citations = [
    (
        root / "Comparisons/Comparisons Deep Dive.md",
        """
- Kennedy, P. (1987). *The Rise and Fall of the Great Powers: Economic Change and Military Conflict from 1500 to 2000*. Random House.
- Kondratiev, N. D. (1935). The Long Waves in Economic Life. *The Review of Economics and Statistics*, 17(6), 105-115.
- Perez, C. (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar Publishing.
- Dalio, R. (2021). *Principles for Dealing with the Changing World Order: Why Nations Succeed and Fail*. Avid Reader Press.
- Modelski, G. (1987). *Long Cycles in World Politics*. University of Washington Press.
- Toynbee, A. J. (1934). *A Study of History: Volumes I-VI*. Oxford University Press.
- Spengler, O. (1918). *The Decline of the West: Form and Actuality*. Alfred A. Knopf.
- Sorokin, P. A. (1937). *Social and Cultural Dynamics: Fluctuation of Social Relationships, War, and Revolution*. American Book Company.
- Turchin, P. (2016). *Ages of Discord: A Structural-Demographic Analysis of American History*. Beresta Books.
- Goldstone, J. A. (1991). *Revolution and Rebellion in the Early Modern World*. University of California Press.
- Schumpeter, J. A. (1939). *Business Cycles: A Theoretical, Historical, and Statistical Analysis of the Capitalist Process*. McGraw-Hill.
- Wallerstein, I. (1974). *The Modern World-System: Capitalist Agriculture and the Origins of the European World-Economy*. Academic Press.
"""
    ),
    (
        root / "Concept/Concept Deep Dive.md",
        """
- Mannheim, K. (1952). The Problem of Generations. In *Essays on the Sociology of Knowledge* (pp. 276-320). Routledge & Kegan Paul.
- Strauss, W., & Howe, N. (1991). *Generations: The History of America's Future, 1584 to 2069*. William Morrow & Co.
- Strauss, W., & Howe, N. (1997). *The Fourth Turning: An American Prophecy*. Broadway Books.
- Ryder, N. B. (1965). The Cohort as a Concept in the Study of Social Change. *American Sociological Review*, 30(6), 843-861.
- Elder, G. H. (1974). *Children of the Great Depression: Social Change in Life Experience*. University of Chicago Press.
- Inglehart, R. (1977). *The Silent Revolution: Changing Values and Political Styles Among Western Publics*. Princeton University Press.
- Putnam, R. D. (2000). *Bowling Alone: The Collapse and Revival of American Community*. Simon & Schuster.
- Lasch, C. (1979). *The Culture of Narcissism: American Life in an Age of Diminishing Expectations*. W. W. Norton & Co.
- Riesman, D. (1950). *The Lonely Crowd: A Study of the Changing American Character*. Yale University Press.
- Bell, D. (1976). *The Cultural Contradictions of Capitalism*. Basic Books.
- Howe, N. (2023). *The Fourth Turning Is Here: What the Seasons of History Tell Us About How and When This Crisis Will End*. Simon & Schuster.
"""
    ),
    (
        root / "Contradictory Evidence/Contradictory Evidence Deep Dive.md",
        """
- Granger, C. W. J. (1966). The Typical Spectral Shape of an Economic Variable. *Econometrica*, 34(1), 150-161.
- Slutsky, E. (1937). The Summation of Random Causes as the Source of Cyclic Processes. *Econometrica*, 5(2), 105-146.
- Yule, G. U. (1927). On a Method of Investigating Periodicities in Disturbed Series. *Philosophical Transactions of the Royal Society of London*, 226, 267-298.
- Mason, K. O., Winsborough, H. H., Mason, W. M., & Poole, W. K. (1973). Some Methodological Issues in Cohort Analysis of Archival Data. *American Sociological Review*, 38(2), 242-258.
- Fienberg, S. E., & Mason, W. M. (1979). Identification and Estimation of Age-Period-Cohort Models in the Analysis of Discrete Archival Data. *Sociological Methodology*, 10, 1-67.
- Glenn, N. D. (2005). *Cohort Analysis: Quantitative Applications in the Social Sciences* (2nd ed.). SAGE Publications.
- Campbell, A., Converse, P. E., Miller, W. E., & Stokes, D. E. (1960). *The American Voter*. John Wiley & Sons.
- Converse, P. E. (1964). The Nature of Belief Systems in Mass Publics. In D. E. Apter (Ed.), *Ideology and Discontent* (pp. 206-261). Free Press.
- Zaller, J. R. (1992). *The Nature and Origins of Mass Opinion*. Cambridge University Press.
- Silver, N. (2012). *The Signal and the Noise: Why So Many Predictions Fail—but Some Don't*. Penguin Press.
"""
    ),
    (
        root / "Criticism/Criticism Deep Dive.md",
        """
- Robinson, W. S. (1950). Ecological Correlations and the Behavior of Individuals. *American Sociological Review*, 15(3), 351-357.
- Popper, K. R. (1957). *The Poverty of Historicism*. Routledge & Kegan Paul.
- Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson & Co.
- Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*. Cambridge University Press.
- Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.
- Hempel, C. G. (1942). The Function of General Laws in History. *The Journal of Philosophy*, 39(2), 35-48.
- Nagel, E. (1961). *The Structure of Science: Problems in the Logic of Scientific Explanation*. Harcourt, Brace & World.
- Giddens, A. (1984). *The Constitution of Society: Outline of the Theory of Structuration*. Polity Press.
- Bourdieu, P. (1977). *Outline of a Theory of Practice*. Cambridge University Press.
- Alexander, J. C. (1982). *Theoretical Logic in Sociology: Positivism, Presuppositions, and Current Controversies*. University of California Press.
- Stinchcombe, A. L. (1968). *Constructing Social Theories*. Harcourt, Brace & World.
- Merton, R. K. (1968). *Social Theory and Social Structure*. Free Press.
- Coleman, J. S. (1990). *Foundations of Social Theory*. Harvard University Press.
- Hedstrom, P., & Swedberg, R. (1998). *Social Mechanisms: An Analytical Approach to Social Theory*. Cambridge University Press.
"""
    )
]

for filepath, citations in files_and_citations:
    content = filepath.read_text(encoding="utf-8")
    new_content = content.rstrip() + "\n" + citations.strip() + "\n"
    filepath.write_text(new_content, encoding="utf-8")
    print(f"Finalized {filepath.name}: {len(new_content.splitlines())} lines")

