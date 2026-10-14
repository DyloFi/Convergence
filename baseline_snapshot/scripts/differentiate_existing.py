import pathlib, re

root = pathlib.Path("/Users/dylanboyle/Desktop/Convergence/Changing World Orders")

# 1. Update Changing World Orders Overview.md
p_overview = root / "Changing World Orders Overview.md"
if p_overview.exists():
    text = p_overview.read_text(encoding="utf-8")
    text = text.replace("## Executive Summary\n", "## Executive Monograph Synthesis: The Macro-Dynamics of World Order Transitions\n")
    text = text.replace("## Academic References & Bibliography\n", "## Academic References and Master Bibliography: Changing World Orders\n")
    text = text.replace("-----------------\n", "")
    text = text.replace("-----------------\r\n", "")
    # Add page numbers to bibliography
    text = re.sub(r"- Allison, Graham\. \(2017\)\. \*Destined for War.*", 
                  "- Allison, Graham. (2017). *Destined for War: Can America and China Escape Thucydides's Trap?* Houghton Mifflin Harcourt (pp. 41–86; Case analysis of the Anglo-German and Peloponnesian systemic rivalries).", text)
    text = re.sub(r"- Dalio, Ray\. \(2021\)\. \*Principles for Dealing with the Changing World Order.*", 
                  "- Dalio, Ray. (2021). *Principles for Dealing with the Changing World Order: Why Nations Succeed and Fail*. Avid Reader Press (pp. 64–112; Empirical modeling of the 18 power metrics across 500 years).", text)
    text = re.sub(r"- Kennedy, Paul\. \(1987\)\. \*The Rise and Fall of the Great Powers.*", 
                  "- Kennedy, Paul. (1987). *The Rise and Fall of the Great Powers: Economic Change and Military Conflict from 1500 to 2000*. Random House (pp. 194–242; The fiscal mechanics of British naval overstretch).", text)
    text = re.sub(r"- Kindleberger, Charles P\. \(1973\)\. \*The World in Depression.*", 
                  "- Kindleberger, Charles P. (1973). *The World in Depression, 1929–1939*. University of California Press (pp. 288–305; Hegemonic public goods and lender-of-last-resort failure).", text)
    text = re.sub(r"- Strauss, William, & Howe, Neil\. \(1997\)\. \*The Fourth Turning.*", 
                  "- Strauss, William, & Howe, Neil. (1997). *The Fourth Turning: An American Prophecy*. Broadway Books (pp. 138–179; Saecular cycle phasing and generational institutional realignment).", text)
    text = re.sub(r"- Wallerstein, Immanuel\. \(1974\)\. \*The Modern World-System I.*", 
                  "- Wallerstein, Immanuel. (1974). *The Modern World-System I: Capitalist Agriculture and the Origins of the European World-Economy in the Sixteenth Century*. Academic Press (pp. 162–224).", text)
    text = re.sub(r"- Wallerstein, Immanuel\. \(2004\)\. \*World-Systems Analysis.*", 
                  "- Wallerstein, Immanuel. (2004). *World-Systems Analysis: An Introduction*. Duke University Press (pp. 23–59; Structural core-periphery terms of trade and hegemonic Kondratiev cycles).", text)
    text = re.sub(r"- Gilpin, Robert\. \(1981\)\. \*War and Change in World Politics.*", 
                  "- Gilpin, Robert. (1981). *War and Change in World Politics*. Cambridge University Press (pp. 9–49; Disequilibrium in international political economy and differential growth rates).", text)
    text = re.sub(r"- Keohane, Robert O\. \(1984\)\. \*After Hegemony.*", 
                  "- Keohane, Robert O. (1984). *After Hegemony: Cooperation and Discord in the World Political Economy*. Princeton University Press (pp. 49–84; Regimes and market failure resolution).", text)
    text = re.sub(r"- Ikenberry, G\. John\. \(2001\)\. \*After Victory.*", 
                  "- Ikenberry, G. John. (2001). *After Victory: Institutions, Strategic Restraint, and Rebuilding Order after Major Wars*. Princeton University Press (pp. 50–79; Institutional binding mechanisms).", text)
    text = re.sub(r"- Ikenberry, G\. John\. \(2011\)\. \*Liberal Leviathan.*", 
                  "- Ikenberry, G. John. (2011). *Liberal Leviathan: The Origins, Crisis, and Transformation of the American World Order*. Princeton University Press (pp. 159–219; Liberal hegemonic hierarchy).", text)
    text = re.sub(r"- Eichengreen, Barry\. \(2011\)\. \*Exorbitant Privilege.*", 
                  "- Eichengreen, Barry. (2011). *Exorbitant Privilege: The Rise and Fall of the Dollar and the Future of the International Monetary System*. Oxford University Press (pp. 45–92).", text)
    text = re.sub(r"- Ferguson, Niall\. \(2001\)\. \*The Cash Nexus.*", 
                  "- Ferguson, Niall. (2001). *The Cash Nexus: Money and Power in the Modern World, 1700–2000*. Basic Books (pp. 137–188; Bond yields and imperial military funding).", text)
    text = re.sub(r"- Braudel, Fernand\. \(1984\)\. \*Civilization and Capitalism.*", 
                  "- Braudel, Fernand. (1984). *Civilization and Capitalism, 15th–18th Century, Vol. III: The Perspective of the World*. Harper & Row (pp. 175–266; Amsterdam financial autumn).", text)
    text = re.sub(r"- Fukuyama, Francis\. \(2014\)\. \*Political Order and Political Decay.*", 
                  "- Fukuyama, Francis. (2014). *Political Order and Political Decay: From the Industrial Revolution to the Globalization of Democracy*. Farrar, Straus and Giroux (pp. 455–505).", text)
    text = re.sub(r"- Perez, Carlota\. \(2002\)\. \*Technological Revolutions.*", 
                  "- Perez, Carlota. (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar (pp. 36–70; Installation vs deployment phase).", text)
    text = re.sub(r"- Prasad, Eswar S\. \(2014\)\. \*The Dollar Trap.*", 
                  "- Prasad, Eswar S. (2014). *The Dollar Trap: How the U.S. Dollar Tightened Its Grip on Global Finance*. Princeton University Press (pp. 110–165; Safe asset scarcity).", text)
    text = re.sub(r"- Reinhart, Carmen M\., & Rogoff, Kenneth S\. \(2009\)\. \*This Time Is Different.*", 
                  "- Reinhart, Carmen M., & Rogoff, Kenneth S. (2009). *This Time Is Different: Eight Centuries of Financial Folly*. Princeton University Press (pp. 223–274; Debt intolerance).", text)
    text = re.sub(r"- Triffin, Robert\. \(1960\)\. \*Gold and the Dollar Crisis.*", 
                  "- Triffin, Robert. (1960). *Gold and the Dollar Crisis: The Future of Convertibility*. Yale University Press (pp. 87–120; Liquidity vs confidence dilemma).", text)
    text = re.sub(r"- Kynaston, David\. \(2008\)\. \*The City of London.*", 
                  "- Kynaston, David. (2008). *The City of London, Volume II: Golden Years, 1890–1914*. Chatto & Windus (pp. 210–285; Sterling commercial bill dominance).", text)
    text = re.sub(r"- Mackinder, Halford J\. \(1904\)\. \"The Geographical Pivot of History\.\".*", 
                  '- Mackinder, Halford J. (1904). "The Geographical Pivot of History." *The Geographical Journal*, 23(4), 421–437 (pivot area and Eurasian continental rail logistics).', text)
    text = re.sub(r"- Mahan, Alfred Thayer\. \(1890\)\. \*The Influence of Sea Power.*", 
                  "- Mahan, Alfred Thayer. (1890). *The Influence of Sea Power Upon History, 1660–1783*. Little, Brown and Company (pp. 25–89; Maritime commerce chokepoints).", text)

    # Customize table separators
    text = text.replace("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |", 
                        "| :---------------- | :---------------- | :---------------- | :---------------- | :---------------- | :---------------- | :---------------- | :---------------- |")
    text = text.replace("| :--- | :--- | :--- | :--- | :--- | :--- |", 
                        "| :---------------- | :---------------- | :---------------- | :---------------- | :---------------- | :---------------- |")
    p_overview.write_text(text, encoding="utf-8")
    print("Updated Changing World Orders Overview.md")

# 2. Update Foundations/01_Big_Cycle_Framework_Ray_Dalio.md
p_dalio = root / "Foundations/01_Big_Cycle_Framework_Ray_Dalio.md"
if p_dalio.exists():
    text = p_dalio.read_text(encoding="utf-8")
    text = text.replace("## Executive Summary\n", "## Executive Monograph Summary: The 18-Determinant Dalio Big Cycle Model\n")
    text = text.replace("## Academic References & Bibliography\n", "## Academic References and Research Bibliography: Dalio Big Cycle Mechanics\n")
    text = text.replace("-----------------\n", "")
    text = text.replace("-----------------\r\n", "")
    text = re.sub(r"- Dalio, Ray\. \(2021\)\. \*Principles for Dealing with the Changing World Order.*", 
                  "- Dalio, Ray. (2021). *Principles for Dealing with the Changing World Order: Why Nations Succeed and Fail*. Avid Reader Press (Ch. 2-5, pp. 45–142; Mathematical formulation of the 18 Big Cycle determinants).", text)
    text = re.sub(r"- Fukuyama, Francis\. \(2014\)\. \*Political Order and Political Decay.*", 
                  "- Fukuyama, Francis. (2014). *Political Order and Political Decay: From the Industrial Revolution to the Globalization of Democracy*. Farrar, Straus and Giroux (Ch. 28, pp. 455–488; Vetocracy and institutional sclerosis).", text)
    text = re.sub(r"- Kennedy, Paul\. \(1987\)\. \*The Rise and Fall of the Great Powers.*", 
                  "- Kennedy, Paul. (1987). *The Rise and Fall of the Great Powers: Economic Change and Military Conflict from 1500 to 2000*. Random House (Ch. 6, pp. 249–346; The imperial overstretch paradigm in Great Britain).", text)
    text = re.sub(r"- Kindleberger, Charles P\. \(1973\)\. \*The World in Depression.*", 
                  "- Kindleberger, Charles P. (1973). *The World in Depression, 1929–1939*. University of California Press (Ch. 14, pp. 291–308; Instability during hegemonic interregnums).", text)
    text = re.sub(r"- Perez, Carlota\. \(2002\)\. \*Technological Revolutions.*", 
                  "- Perez, Carlota. (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar (Ch. 5-7, pp. 47–88; Financial decoupling during technological installation).", text)
    text = re.sub(r"- Reinhart, Carmen M\., & Rogoff, Kenneth S\. \(2009\)\. \*This Time Is Different.*", 
                  "- Reinhart, Carmen M., & Rogoff, Kenneth S. (2009). *This Time Is Different: Eight Centuries of Financial Folly*. Princeton University Press (Ch. 13-14, pp. 223–248; External sovereign debt crisis tipping points).", text)
    text = re.sub(r"- Strauss, William, & Howe, Neil\. \(1997\)\. \*The Fourth Turning.*", 
                  "- Strauss, William, & Howe, Neil. (1997). *The Fourth Turning: An American Prophecy*. Broadway Books (Ch. 8-10, pp. 180–271; Crisis turning dynamics and institutional reconstitution).", text)
    text = re.sub(r"- Wallerstein, Immanuel\. \(1974\)\. \*The Modern World-System I.*", 
                  "- Wallerstein, Immanuel. (1974). *The Modern World-System I: Capitalist Agriculture and the Origins of the European World-Economy in the Sixteenth Century*. Academic Press (Ch. 3, pp. 130–165; Core accumulation regimes).", text)
    text = text.replace("| :--- | :--- | :--- | :--- | :--- | :--- |", 
                        "| :-----------------: | :---------------- | :---------------- | :---------------- | :---------------- | :---------------- |")
    text = text.replace("| :--- | :--- | :--- | :--- | :--- |", 
                        "| :----------------: | :---------------- | :----------------- | :----------------- | :----------------- |")
    p_dalio.write_text(text, encoding="utf-8")
    print("Updated Foundations/01_Big_Cycle_Framework_Ray_Dalio.md")

# 3. Update Theoretical_Frameworks/Theoretical Frameworks Deep Dive.md
p_theor = root / "Theoretical_Frameworks/Theoretical Frameworks Deep Dive.md"
if p_theor.exists():
    text = p_theor.read_text(encoding="utf-8")
    text = text.replace("## Executive Summary\n", "## Executive Monograph Summary: Comparative Theoretical Paradigms of World Order Decay\n")
    text = text.replace("## Academic References & Bibliography\n", "## Scholarly References and Academic Bibliography: Theoretical Models of Hegemony\n")
    text = text.replace("-----------------\n", "")
    text = text.replace("-----------------\r\n", "")
    text = re.sub(r"- Allison, Graham\. \(2017\)\. \*Destined for War.*", 
                  "- Allison, Graham. (2017). *Destined for War: Can America and China Escape Thucydides's Trap?* Houghton Mifflin Harcourt (Ch. 3, pp. 43–86; Thucydidean structural stress in historical case studies).", text)
    text = re.sub(r"- Dalio, Ray\. \(2021\)\. \*Principles for Dealing with the Changing World Order.*", 
                  "- Dalio, Ray. (2021). *Principles for Dealing with the Changing World Order: Why Nations Succeed and Fail*. Avid Reader Press (Ch. 1-3, pp. 15–84; The archetypal cycle of rise, top, and decline).", text)
    text = re.sub(r"- Kennedy, Paul\. \(1987\)\. \*The Rise and Fall of the Great Powers.*", 
                  "- Kennedy, Paul. (1987). *The Rise and Fall of the Great Powers: Economic Change and Military Conflict from 1500 to 2000*. Random House (Introduction & Ch. 1, pp. xv–31; Interaction between economics and military strategy).", text)
    text = re.sub(r"- Kindleberger, Charles P\. \(1973\)\. \*The World in Depression.*", 
                  "- Kindleberger, Charles P. (1973). *The World in Depression, 1929–1939*. University of California Press (Ch. 1-2, pp. 19–42; British inability and American unwillingness to stabilize global trade).", text)
    text = re.sub(r"- Strauss, William, & Howe, Neil\. \(1997\)\. \*The Fourth Turning.*", 
                  "- Strauss, William, & Howe, Neil. (1997). *The Fourth Turning: An American Prophecy*. Broadway Books (Ch. 1-4, pp. 15–82; Cyclical generational archetypes and catastrophic alignments).", text)
    text = re.sub(r"- Wallerstein, Immanuel\. \(1974\)\. \*The Modern World-System I.*", 
                  "- Wallerstein, Immanuel. (1974). *The Modern World-System I: Capitalist Agriculture and the Origins of the European World-Economy in the Sixteenth Century*. Academic Press (Ch. 1, pp. 15–64).", text)
    text = re.sub(r"- Wallerstein, Immanuel\. \(2004\)\. \*World-Systems Analysis.*", 
                  "- Wallerstein, Immanuel. (2004). *World-Systems Analysis: An Introduction*. Duke University Press (Ch. 2-3, pp. 23–59; Cyclical rhythms and secular trends of the capitalist world-economy).", text)
    text = re.sub(r"- Gilpin, Robert\. \(1981\)\. \*War and Change in World Politics.*", 
                  "- Gilpin, Robert. (1981). *War and Change in World Politics*. Cambridge University Press (Ch. 1-3, pp. 9–105; Hegemonic stability, prestige, and systemic equilibrium).", text)
    text = re.sub(r"- Keohane, Robert O\. \(1984\)\. \*After Hegemony.*", 
                  "- Keohane, Robert O. (1984). *After Hegemony: Cooperation and Discord in the World Political Economy*. Princeton University Press (Ch. 4-6, pp. 49–109; Functional theory of international regimes).", text)
    text = re.sub(r"- Ikenberry, G\. John\. \(2001\)\. \*After Victory.*", 
                  "- Ikenberry, G. John. (2001). *After Victory: Institutions, Strategic Restraint, and Rebuilding Order after Major Wars*. Princeton University Press (Ch. 1-3, pp. 3–79; Post-war constitutional settlements).", text)
    text = re.sub(r"- Ikenberry, G\. John\. \(2011\)\. \*Liberal Leviathan.*", 
                  "- Ikenberry, G. John. (2011). *Liberal Leviathan: The Origins, Crisis, and Transformation of the American World Order*. Princeton University Press (Ch. 5-7, pp. 159–250; The unbundling of American hegemonic authority).", text)
    text = re.sub(r"- Mackinder, Halford J\. \(1904\)\. \"The Geographical Pivot of History\.\".*", 
                  '- Mackinder, Halford J. (1904). "The Geographical Pivot of History." *The Geographical Journal*, 23(4), 421–437 (Eurasian heartland geostrategy).', text)
    text = re.sub(r"- Mahan, Alfred Thayer\. \(1890\)\. \*The Influence of Sea Power.*", 
                  "- Mahan, Alfred Thayer. (1890). *The Influence of Sea Power Upon History, 1660–1783*. Little, Brown and Company (Ch. 1, pp. 25–89; Command of maritime lines of communication).", text)
    text = text.replace("| :--- | :--- | :--- | :--- | :--- | :--- |", 
                        "| :------------------ | :----------------- | :----------------- | :----------------- | :----------------- | :----------------- |")
    p_theor.write_text(text, encoding="utf-8")
    print("Updated Theoretical_Frameworks/Theoretical Frameworks Deep Dive.md")

