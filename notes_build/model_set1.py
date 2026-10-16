"""Biology Model Set 1: content and answer key."""
import model_figs as F

CODE = "BCSE/22-3/MODEL-1"

# (question, [A,B,C,D], answer letter, reason, figure)
MCQS = [
 ("Which structure is present in both plant cells and animal cells?", ["Cell wall", "Chloroplast", "Mitochondrion", "Large central vacuole"], "C", "Mitochondria are found in all eukaryotic cells; cell wall, chloroplast and large vacuole are plant features.", ""),
 ("<i>Helicobacter pylori</i> infection of the stomach can be diagnosed by", ["an electrocardiogram.", "a urea breath test.", "a blood sugar test.", "a spirometer test."], "B", "The urea breath (or stool antigen) test detects H. pylori.", ""),
 ("A plant cell placed in a hypertonic solution", ["becomes turgid.", "becomes plasmolysed.", "bursts.", "does not change."], "B", "Water leaves by osmosis, the membrane pulls away from the wall: plasmolysis.", ""),
 ("Root hair cells absorb mineral ions from soil that has a lower concentration of the ions than the cell. This happens by", ["osmosis.", "diffusion.", "active transport.", "transpiration."], "C", "Movement against the concentration gradient needs ATP: active transport.", ""),
 ("The figure shows a cell during division. Which phase is shown?", ["Prophase", "Metaphase", "Anaphase", "Telophase"], "C", "Sister chromatids have separated and are moving to opposite poles: anaphase.", F.anaphase()),
 ("Which products of the light reaction are used in the Calvin cycle?", ["Oxygen and glucose", "ATP and NADPH", "Carbon dioxide and water", "Starch and ATP"], "B", "ATP gives energy and NADPH gives hydrogen to reduce CO<sub>2</sub> to glucose.", ""),
 ("The light reaction of photosynthesis takes place in the", ["stroma.", "grana.", "mitochondria.", "cytoplasm."], "B", "Chlorophyll is in the thylakoid membranes of the grana.", ""),
 ("The graph shows the effect of light intensity on the rate of photosynthesis. Beyond point X the rate does not rise. Which factor is most likely limiting?", ["Light intensity", "Oxygen concentration", "Carbon dioxide concentration", "Amount of soil"], "C", "Light is no longer limiting; CO<sub>2</sub> (or temperature) now limits the rate.", F.light_graph()),
 ("A difference between xylem vessels and phloem sieve tubes is that xylem vessels", ["carry food.", "are made of dead cells.", "have companion cells.", "carry substances in both directions."], "B", "Xylem vessels are dead, hollow, lignified tubes carrying water upward only.", ""),
 ("Sugars are loaded into the phloem by", ["osmosis.", "diffusion.", "active transport.", "transpiration pull."], "C", "Loading of sucrose into the phloem needs energy from the companion cells.", ""),
 ("Digestion of starch begins in the mouth because saliva contains", ["pepsin.", "salivary amylase.", "lipase.", "trypsin."], "B", "Salivary amylase changes starch to maltose.", ""),
 ("The function of bile in digestion is to", ["digest proteins.", "emulsify fats.", "digest starch.", "kill bacteria in the stomach."], "B", "Bile breaks fat into tiny droplets, increasing the area for lipase.", ""),
 ("Villi in the small intestine are adapted for absorption because they", ["increase the surface area.", "secrete bile.", "kill bacteria.", "produce enzymes for protein digestion only."], "A", "Villi and microvilli give a very large absorbing surface.", ""),
 ("A person of blood group B has", ["A antigen and anti-B antibody.", "B antigen and anti-A antibody.", "A and B antigens and no antibody.", "no antigen and both antibodies."], "B", "Group B: B antigen on the red cells, anti-A in the plasma.", ""),
 ("A patient of blood group AB can safely receive blood from", ["AB only.", "A and B only.", "O only.", "A, B, AB and O."], "D", "AB plasma has no antibodies, so AB is the universal recipient.", ""),
 ("An invasive species is a species that", ["is protected by law.", "is not native, spreads quickly and harms native species.", "is rare in the wild.", "is found nowhere else in the world."], "B", "Invasive species are non-native organisms that spread rapidly and damage ecosystems.", ""),
 ("In the nephron shown, all the glucose in the filtrate is reabsorbed in the part labelled", ["A", "B", "C", "E"], "B", "B is the proximal convoluted tubule, which reabsorbs all glucose and amino acids (A = Bowman's capsule, C = loop of Henle, D = DCT, E = collecting duct).", F.nephron()),
 ("The hormone that increases reabsorption of water in the collecting duct is", ["insulin.", "ADH.", "adrenaline.", "gibberellin."], "B", "Antidiuretic hormone (ADH) makes the collecting duct more permeable to water.", ""),
 ("Which of the following is a reflex action?", ["Writing a letter", "Blinking when dust enters the eye", "Riding a bicycle", "Reading a book"], "B", "Blinking is rapid, automatic and involuntary.", ""),
 ("Gametes are produced by", ["mitosis.", "meiosis.", "binary fission.", "budding."], "B", "Meiosis halves the chromosome number to make gametes.", ""),
 ("A diploid cell has 8 chromosomes. After meiosis each gamete has", ["2", "4", "8", "16"], "B", "Haploid number = 8 &divide; 2 = 4.", ""),
 ("Tall (TT) pea plants are crossed with dwarf (tt) plants and the F<sub>1</sub> plants are self-pollinated. The F<sub>2</sub> ratio of tall : dwarf is", ["1 : 1", "3 : 1", "1 : 3", "2 : 1"], "B", "Tt &times; Tt gives TT, Tt, Tt, tt = 3 tall : 1 dwarf.", ""),
 ("Colour blindness is more common in males than in females because", ["the gene is on the Y chromosome.", "males have only one X chromosome.", "males have two X chromosomes.", "the gene is dominant."], "B", "A male needs only one recessive allele on his single X chromosome.", ""),
 ("Bacteria become resistant to an antibiotic because", ["they decide to survive.", "resistant bacteria survive and reproduce.", "the antibiotic makes them resistant.", "they learn to avoid it."], "B", "Natural selection: resistant mutants survive and pass on the allele.", ""),
 ("Which is an example of ecosystem diversity?", ["Different breeds of cattle", "Coral reef, desert and forest", "Many varieties of rice", "Genes of a tiger population"], "B", "Different ecosystems in a region = ecosystem diversity.", ""),
]

FILL = [
 ("The loss of water vapour from the leaves through the stomata is called ____________.", "transpiration"),
 ("The end product of protein digestion is ____________.", "amino acids"),
 ("The cell fragments that help blood to clot are ____________.", "platelets"),
 ("A random change in allele frequency in a small population is called genetic ____________.", "drift"),
 ("The movement of sugars from the leaves to other parts of a plant is called ____________.", "translocation"),
]
TF = [
 ("Osmosis does not need energy from ATP.", "TRUE"),
 ("The dark reaction can continue for a long time without the products of the light reaction.", "FALSE"),
 ("A spinal reflex is controlled mainly by the spinal cord.", "TRUE"),
 ("Mitosis produces genetically different cells.", "FALSE"),
 ("A large, randomly mating population with no mutation, migration or selection keeps constant allele frequencies.", "TRUE"),
]
MATCH_A = ["Controls reabsorption of water in the collecting duct", "Use of microbes to clean up an oil spill", "Exchange of alleles between populations", "Site of the Calvin cycle", "Carries oxygen in red blood cells"]
MATCH_B = ["Stroma", "Bioremediation", "ADH", "Haemoglobin", "Gene flow", "Thylakoid", "Platelets"]
MATCH_ANS = ["c", "b", "e", "a", "d"]

# Section B: question -> list of (label, text, marks, figure, answer-box mm, model answer)
QB = {
 2: [
  ("a)", "A student set up potato strips of equal length (6.0 cm) in sugar solutions of different concentrations. The final lengths after one hour are given.<br><table class='tab' style='width:auto'><tr><th>Sugar solution (%)</th><th>0</th><th>10</th><th>20</th><th>30</th><th>40</th></tr><tr><th>Final length (cm)</th><td>6.6</td><td>6.3</td><td>6.0</td><td>5.7</td><td>5.4</td></tr></table>Plot a line graph of final length against concentration of sugar solution.", 3, "", 70,
   "Axes: x = concentration of sugar solution (%), y = final length (cm) with units (1); correct plotting of the five points (1); ruled line / smooth line through the points and a title (1). The line slopes downwards from 6.6 cm to 5.4 cm."),
  ("b)", "Which solution is isotonic to the potato cells? Give a reason.", 1, "", 14, "<b>20 %</b>; the length did not change (6.0 cm), so there is no net movement of water."),
  ("c)", "Explain why the strip in 0 % sugar solution became longer.", 2, "", 24, "Pure water is <b>hypotonic</b> to the cell sap (1). Water enters the cells by <b>osmosis</b> through the selectively permeable membrane, so the cells become turgid and the strip lengthens (1)."),
  ("d)", "State ONE way to make the results more reliable.", 1, "", 14, "Repeat the experiment with several strips in each solution and calculate the <b>average</b> (or use strips of the same size, same temperature and time)."),
  ("e)", "A gardener adds too much fertiliser (salt) around the roots of vegetables and the plants wilt. Explain.", 2, "", 24, "Excess fertiliser makes the soil solution <b>hypertonic</b> to the root cells (1). Water leaves the root cells by osmosis, cells lose turgor and the plant wilts (1)."),
  ("f)", "How is facilitated diffusion different from simple diffusion?", 1, "", 14, "Facilitated diffusion needs <b>carrier or channel proteins</b>; simple diffusion passes directly through the lipid bilayer. (Neither uses ATP.)"),
 ],
 3: [
  ("a)", "The graph shows the effect of light intensity on the rate of photosynthesis of a water plant. (See the graph in Q1(a)(viii).)<br>(i) Name the independent variable and the dependent variable.", 1, "", 14, "Independent: <b>light intensity</b>; dependent: <b>rate of photosynthesis</b> (e.g. bubbles of oxygen per minute)."),
  ("", "(ii) Explain the shape of the graph.", 2, "", 24, "Rate rises at first because more light means more ATP and NADPH made in the light reaction (1). At X another factor (CO<sub>2</sub> or temperature) becomes limiting, so the rate levels off (1)."),
  ("", "(iii) Suggest how a greenhouse farmer could increase the rate beyond X.", 2, "", 24, "Raise the <b>CO<sub>2</sub></b> concentration (burn fuel/CO<sub>2</sub> enrichment) (1) and keep the temperature near the optimum (35&ndash;40 &deg;C) / provide water (1)."),
  ("b)", "Write the word equation (or chemical equation) for photosynthesis.", 1, "", 14, "Carbon dioxide + water &rarr; (light, chlorophyll) glucose + oxygen. (6CO<sub>2</sub> + 6H<sub>2</sub>O &rarr; C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6O<sub>2</sub>)"),
  ("c)", "Give TWO differences between the light reaction and the dark reaction.", 2, "", 24, "Light reaction: in the <b>grana</b>, needs <b>light and water</b>, produces ATP, NADPH and O<sub>2</sub>. Dark reaction: in the <b>stroma</b>, needs CO<sub>2</sub>, ATP and NADPH, produces glucose. (any two, 1 mark each)"),
  ("d)", "Why is photosynthesis important to animals?", 1, "", 14, "It provides <b>food</b> (glucose) at the start of food chains and <b>oxygen</b> for respiration."),
  ("e)", "State the role of chlorophyll.", 1, "", 14, "Chlorophyll <b>absorbs light energy</b> and converts it into chemical energy."),
 ],
 4: [
  ("a)", "A ring of bark is removed completely around the stem of a woody plant and the plant is observed for a few months.<br>(i) Draw a labelled diagram to show the expected result.", 2, "", 40, "Stem with a bulge/swelling <b>above</b> the ring, no swelling below; labels: ring (gap) where bark is removed, swelling, bark/phloem, xylem, leaves green. (1 mark drawing, 1 mark labels)"),
  ("", "(ii) Explain the result.", 2, "", 24, "The ring removes the <b>phloem</b> (1). Sugars made in the leaves cannot move down past the gap and accumulate above it, causing swelling; the xylem is intact so water still rises (1)."),
  ("b)", "Name the process by which food is moved in a plant. Give ONE example each of a source and a sink.", 2, "", 24, "<b>Translocation</b> (1). Source: mature leaf; sink: root / fruit / growing bud / seed (1)."),
  ("c)", "State THREE differences between xylem and phloem.", 3, "", 36, "Xylem: carries water and minerals; dead cells; upward only; no ATP needed. Phloem: carries food (sucrose); living cells; up and down; needs ATP. (any three, 1 mark each)"),
  ("d)", "Name the plant hormone used (i) to stop potatoes from sprouting in storage and (ii) to ripen fruits early.", 1, "", 14, "(i) <b>Auxin (NAA)</b> (ii) <b>Ethylene</b> (0.5 mark each)."),
 ],
 5: [
  ("a)", "Complete the table.<br><table class='tab'><tr><th>Food</th><th>Enzyme</th><th>Organ</th><th>End product</th></tr><tr><td>Starch</td><td>(i)</td><td>Mouth</td><td>(ii)</td></tr><tr><td>Protein</td><td>Pepsin</td><td>(iii)</td><td>Peptides</td></tr><tr><td>Fat</td><td>Lipase</td><td>Small intestine</td><td>(iv)</td></tr></table>", 2, "", None, "(i) salivary amylase; (ii) maltose; (iii) stomach; (iv) fatty acids and glycerol. (0.5 mark each)"),
  ("b)", "State the role of hydrochloric acid in the stomach.", 1, "", 14, "Kills bacteria in food and provides the acid medium for pepsin; activates pepsinogen to pepsin. (any one)"),
  ("c)", "(i) What is <i>Helicobacter pylori</i>? (ii) Why is it a concern in Bhutan? (iii) How is it treated?", 3, "", 36, "(i) A spiral bacterium living in the stomach lining that causes gastritis and ulcers (1). (ii) High rate of infection and gastric cancer in Bhutan (1). (iii) Triple therapy (two antibiotics + acid-reducing drug) for 14 days (1)."),
  ("d)", "Give TWO ways to prevent constipation.", 1, "", 14, "Eat fibre (vegetables, fruits, whole grain); drink plenty of water; regular exercise (any two, 0.5 each)."),
  ("e)", "How is the small intestine adapted for absorption?", 2, "", 24, "Very long and coiled; wall folded into villi and microvilli giving a large surface area (1); thin one-cell lining and rich capillary/lacteal supply (1)."),
  ("f)", "Why is bile not an enzyme but still important in digestion?", 1, "", 14, "Bile has no enzymes but it <b>emulsifies fats</b> so lipase can act faster."),
 ],
 6: [
  ("a)", "A doctor mixed blood samples P, Q, R and S with anti-A and anti-B antibodies.<br><table class='tab' style='width:auto'><tr><th>Sample</th><th>Anti-A</th><th>Anti-B</th></tr><tr><td>P</td><td>clumps</td><td>clumps</td></tr><tr><td>Q</td><td>clumps</td><td>no clumping</td></tr><tr><td>R</td><td>no clumping</td><td>no clumping</td></tr><tr><td>S</td><td>no clumping</td><td>clumps</td></tr></table>Identify the blood group of P, Q, R and S.", 2, "", 18, "P = <b>AB</b>, Q = <b>A</b>, R = <b>O</b>, S = <b>B</b> (0.5 mark each)."),
  ("b)", "Which sample is the universal donor? Give a reason.", 1, "", 14, "<b>R (group O)</b> &mdash; it has no A or B antigens, so no clumping occurs in any recipient."),
  ("c)", "Explain why a person of group A cannot receive blood of group B.", 2, "", 24, "Group B red cells carry B antigen (1). The recipient's plasma has anti-B antibody, which attaches to the antigen and makes the red cells clump (agglutination) (1)."),
  ("d)", "State ONE function of platelets and ONE adaptation of red blood cells.", 2, "", 24, "Platelets help the blood to clot (1). RBCs have no nucleus / biconcave shape / contain haemoglobin to carry more oxygen (1)."),
  ("e)", "Give TWO ways in which HIV spreads and ONE way to reduce stigma against people living with HIV.", 3, "", 36, "Spreads by unprotected sex, sharing needles or shaving blades, infected blood, mother to child (any two, 1 mark each). Stigma: awareness education / counselling and equal treatment (1)."),
 ],
 7: [
  ("a)", "The figure shows the pathway of a reflex action.<br>(i) Name the parts A to E.", 2, F.reflex(), 24, "A = receptor (skin), B = sensory neuron, C = spinal cord (relay neuron), D = motor neuron, E = effector (muscle). (5 correct = 2, 3&ndash;4 correct = 1)"),
  ("", "(ii) Write the sequence of the pathway when the hand touches a hot object.", 2, "", 24, "Receptor &rarr; sensory neuron &rarr; interneuron (spinal cord) &rarr; motor neuron &rarr; effector (muscle) &rarr; hand pulled away."),
  ("b)", "Why is a reflex action faster than a voluntary action?", 1, "", 14, "The signal passes through the spinal cord only and not through the brain, so the pathway is shorter."),
  ("c)", "Relate the following parts of a computer to the nervous system: (i) keyboard, (ii) CPU, (iii) monitor, (iv) hard disk.", 2, "", 24, "(i) receptors / sense organs; (ii) brain and spinal cord; (iii) effectors (muscles, glands); (iv) memory in the brain. (0.5 mark each)"),
  ("d)", "Why do some athletes use anabolic steroids? Give TWO harmful effects.", 3, "", 36, "To build muscle and body mass quickly (1). Harmful effects: infertility, heart/liver damage, high blood pressure, aggression, depression, mood swings (any two, 1 mark each)."),
 ],
 8: [
  ("a)", "A pure tall pea plant (TT) is crossed with a pure dwarf plant (tt). Use Punnett squares to show the F<sub>1</sub> and the F<sub>2</sub> generations. State the phenotypic ratio of the F<sub>2</sub>.", 3, "", 60, "F<sub>1</sub>: all Tt, all tall (1). F<sub>2</sub> (Tt &times; Tt): TT, Tt, Tt, tt (1). Phenotypic ratio <b>3 tall : 1 dwarf</b> (1)."),
  ("b)", "A woman who is a carrier of colour blindness (X<sup>C</sup>X<sup>c</sup>) marries a colour-blind man (X<sup>c</sup>Y). (i) Draw a Punnett square. (ii) What percentage of their daughters are colour-blind?", 3, "", 50, "(i) Gametes X<sup>C</sup>, X<sup>c</sup> &times; X<sup>c</sup>, Y gives X<sup>C</sup>X<sup>c</sup>, X<sup>c</sup>X<sup>c</sup>, X<sup>C</sup>Y, X<sup>c</sup>Y (2). (ii) Daughters: X<sup>C</sup>X<sup>c</sup> (carrier) and X<sup>c</sup>X<sup>c</sup> (colour-blind) &rarr; <b>50 %</b> (1)."),
  ("c)", "A diploid cell of an animal has 12 chromosomes. How many chromosomes will be present in (i) each daughter cell after mitosis, (ii) each gamete after meiosis?", 1, "", 14, "(i) <b>12</b> (ii) <b>6</b> (0.5 mark each)."),
  ("d)", "Give TWO differences between mitosis and meiosis.", 2, "", 24, "Mitosis: 1 division, 2 identical diploid cells, in body cells. Meiosis: 2 divisions, 4 different haploid cells, in germ cells, with crossing over. (any two, 1 mark each)"),
  ("e)", "Explain how meiosis produces genetic variation.", 1, "", 14, "Crossing over in prophase I and random (independent) assortment of homologous chromosomes give different combinations of alleles in each gamete."),
 ],
 9: [
  ("a)", "In an industrial area the percentage of dark peppered moths changed as shown.<br><table class='tab' style='width:auto'><tr><th>Year</th><th>1850</th><th>1870</th><th>1890</th><th>1910</th></tr><tr><th>Dark moths (%)</th><td>5</td><td>25</td><td>60</td><td>85</td></tr></table>(i) State the trend.", 1, "", 14, "The percentage of dark moths <b>increased</b> steadily (5 % to 85 %)."),
  ("", "(ii) Explain the trend using natural selection.", 3, "", 36, "Soot darkened the tree trunks (1). Dark moths were better camouflaged and were eaten less by birds, so more survived and reproduced (1). They passed the dark allele to offspring, so its frequency increased (1)."),
  ("b)", "Two populations of squirrels were separated by a newly formed river. Name the type of isolation and explain how it can lead to a new species.", 3, "", 36, "<b>Geographic isolation</b> (1). No gene flow; mutations and different selection pressures make the populations different (1) until they can no longer interbreed = speciation (1)."),
  ("c)", "In a population, the frequency of the recessive allele (q) is 0.4. Calculate the frequency of the dominant allele (p) and of heterozygous individuals.", 2, "", 24, "p = 1 &minus; 0.4 = <b>0.6</b> (1); 2pq = 2 &times; 0.6 &times; 0.4 = <b>0.48</b> (1)."),
  ("d)", "Name ONE invasive plant in Bhutan and state ONE problem it causes.", 1, "", 14, "Lantana camara / crofton weed (Ageratina) / polka dot plant / Mikania &mdash; crowds out native plants and reduces pasture and crop yield."),
 ],
}
