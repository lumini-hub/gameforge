"""Biology Model Set 2: content and answer key."""
import model_figs as F

CODE = "BCSE/22-3/MODEL-2"

MCQS = [
 ("Prokaryotic cells differ from eukaryotic cells because prokaryotic cells", ["have a nucleus.", "lack membrane-bound organelles.", "are larger.", "have chloroplasts."], "B", "Prokaryotes have no nucleus or membrane-bound organelles (DNA lies in the nucleoid).", ""),
 ("Red blood cells were placed in three solutions as shown. Which beaker contains a solution that is hypertonic to the cells?", ["Beaker X", "Beaker Y", "Beaker Z", "None of them"], "A", "In X the cells have shrunk, so water left by osmosis: the solution is hypertonic.", F.tonicity()),
 ("Which process needs ATP?", ["Osmosis", "Simple diffusion", "Active transport", "Facilitated diffusion"], "C", "Active transport moves substances against the gradient using ATP.", ""),
 ("The figure shows a chloroplast. In which part does the light reaction take place?", ["A", "B", "C", "D"], "A", "A = grana (thylakoids), B = stroma, C = oxygen released, D = glucose.", F.chloroplast()),
 ("The raw materials of the light reaction are", ["carbon dioxide and ATP.", "water and light.", "glucose and oxygen.", "NADPH and ATP."], "B", "Light energy splits water in the light reaction.", ""),
 ("Which hormone can be sprayed to stop potatoes from sprouting in storage?", ["Gibberellin", "NAA (auxin)", "Ethylene", "Cytokinin"], "B", "NAA prevents early sprouting.", ""),
 ("Which hormone is used to ripen fruits early?", ["Ethylene", "2,4-D", "Abscisic acid", "Gibberellin"], "A", "Ethylene promotes fruit ripening.", ""),
 ("Which statement about the phloem is correct?", ["Its cells are dead.", "It carries water only.", "It carries sugars in both directions.", "Its walls contain lignin."], "C", "Phloem carries sucrose up and down to wherever it is needed.", ""),
 ("After a ring of bark is removed from a stem, the stem swells above the ring because", ["water collects there.", "sugars cannot move down past the ring.", "minerals collect there.", "the xylem is blocked."], "B", "The phloem is cut, so sugars from the leaves accumulate above the gap.", ""),
 ("Pancreatic juice contains enzymes that digest", ["only starch.", "only protein.", "starch, protein and fat.", "only fat."], "C", "Pancreatic amylase, trypsin and lipase digest all three.", ""),
 ("In the figure, which letter shows the organ that makes bile?", ["A", "B", "C", "D"], "A", "A = liver, B = stomach, C = pancreas, D = small intestine.", F.digestive()),
 ("The final product of carbohydrate digestion that is absorbed in the small intestine is", ["maltose.", "glucose.", "amino acids.", "fatty acids."], "B", "Maltose is changed to glucose by maltase.", ""),
 ("A person with gallstones that block the bile duct has difficulty digesting", ["starch.", "proteins.", "fats.", "vitamins."], "C", "Without bile, fats are not emulsified.", ""),
 ("Which blood group is the universal donor?", ["AB", "A", "B", "O"], "D", "Group O red cells have no A or B antigens.", ""),
 ("The plasma of a person of blood group O contains", ["anti-A only.", "anti-B only.", "anti-A and anti-B.", "no antibodies."], "C", "Group O has both antibodies and no antigens.", ""),
 ("Phagocytosis in blood is carried out by", ["platelets.", "red blood cells.", "white blood cells.", "plasma."], "C", "White blood cells engulf pathogens.", ""),
 ("Which substance is completely reabsorbed in the kidneys of a healthy person?", ["Glucose", "Urea", "Salts", "Water"], "A", "All the glucose is reabsorbed in the PCT; urea is not.", ""),
 ("In the human kidney, filtration of blood takes place in the", ["loop of Henle.", "glomerulus and Bowman's capsule.", "distal convoluted tubule.", "collecting duct."], "B", "High pressure in the glomerulus forces the filtrate into the capsule.", ""),
 ("The figure shows a reflex arc. Which letter represents the motor neuron?", ["A", "B", "C", "D"], "D", "A = receptor, B = sensory neuron, C = spinal cord, D = motor neuron, E = effector.", F.reflex()),
 ("Crossing over occurs during", ["prophase I.", "metaphase I.", "anaphase II.", "telophase I."], "A", "Homologous chromosomes pair and exchange segments in prophase I.", ""),
 ("The figure shows a cell in division. The phase shown is", ["metaphase I.", "metaphase II.", "metaphase of mitosis.", "prophase I."], "A", "Homologous pairs (bivalents) line up at the equator: metaphase I.", F.metaphase1()),
 ("A heterozygous tall plant (Tt) is crossed with a dwarf plant (tt). The percentage of tall offspring is", ["0 %", "25 %", "50 %", "100 %"], "C", "Tt &times; tt gives 1 Tt : 1 tt = 50 % tall.", ""),
 ("A woman who is a carrier of haemophilia marries a normal man. The chance that a son is haemophilic is", ["0 %", "25 %", "50 %", "100 %"], "C", "Half of the sons receive the X chromosome with the haemophilia allele.", ""),
 ("Which is an example of geographic isolation?", ["Two plant species flower in different seasons.", "A river splits a squirrel population.", "Birds with different courtship calls.", "Species living in different habitats of the same area."], "B", "A physical barrier (river) separates the populations.", ""),
 ("Bhutan is part of the biodiversity hotspot called the", ["Western Ghats.", "Eastern Himalaya.", "Sundaland.", "Madagascar."], "B", "The Eastern Himalaya hotspot includes Bhutan, Nepal and north-east India.", ""),
]

FILL = [
 ("The enzyme that digests protein in the stomach is ____________.", "pepsin"),
 ("The plant hormone ____________ closes stomata during drought.", "abscisic acid"),
 ("A trait that shows only when two copies of the recessive allele are present is called a ____________ trait.", "recessive"),
 ("The use of microorganisms to clean up pollution is called ____________.", "bioremediation"),
 ("The structure in the prokaryotic cell where the DNA is found is the ____________.", "nucleoid"),
]
TF = [
 ("Mitochondria are absent in prokaryotic cells.", "TRUE"),
 ("In active transport substances move from a region of low concentration to high concentration.", "TRUE"),
 ("The dark reaction takes place in the grana.", "FALSE"),
 ("Gene flow increases the differences between populations.", "FALSE"),
 ("Lantana camara is an invasive plant in Bhutan.", "TRUE"),
]
MATCH_A = ["Breaks fats into tiny droplets", "Site of filtration in the nephron", "Crossing over of chromosomes", "A small group starts a new population", "Hormone that ripens fruits"]
MATCH_B = ["Prophase I", "Bile", "Glomerulus", "Ethylene", "Founder effect", "Stroma", "Loop of Henle"]
MATCH_ANS = ["b", "c", "a", "e", "d"]

QB = {
 2: [
  ("a)", "The figure shows a plant cell that was placed in a strong salt solution.<br>(i) Name the parts A and C.", 1, F.plasmolysis(), 14, "A = <b>cell wall</b>; C = <b>vacuole</b> (0.5 mark each)."),
  ("", "(ii) Name the process that caused the change and state what fills the space B.", 1, "", 14, "<b>Osmosis</b> (plasmolysis); space B is filled with the outside (salt) solution."),
  ("", "(iii) What would happen to this cell if it was then placed in pure water?", 1, "", 14, "Water enters by osmosis, the vacuole swells and pushes the membrane against the wall; the cell becomes turgid again (deplasmolysis)."),
  ("b)", "Give TWO differences between active transport and facilitated diffusion.", 2, "", 24, "Active transport: against the gradient, uses ATP, carrier (pump) proteins. Facilitated diffusion: down the gradient, no ATP, uses channel/carrier proteins. (any two, 1 mark each)"),
  ("c)", "Dry raisins placed in water become swollen after a few hours. Explain.", 2, "", 24, "Raisins contain a concentrated sugar solution, so water is hypotonic to them (1). Water enters by osmosis through the semipermeable skin and the raisins swell (1)."),
  ("d)", "Draw a labelled diagram of a prokaryotic cell. Label the part that is not found in eukaryotic cells.", 3, "", 60, "Rod/oval cell with cell wall, cell membrane, cytoplasm, ribosomes, plasmid, flagellum (2); <b>nucleoid</b> (DNA region with no nuclear membrane) labelled clearly (1)."),
 ],
 3: [
  ("a)", "A student measured the number of oxygen bubbles released by pondweed in 5 minutes at different carbon dioxide concentrations.<br><table class='tab' style='width:auto'><tr><th>NaHCO<sub>3</sub> (g/100 ml)</th><th>0</th><th>0.2</th><th>0.4</th><th>0.6</th><th>0.8</th></tr><tr><th>Bubbles in 5 min</th><td>6</td><td>20</td><td>34</td><td>40</td><td>40</td></tr></table>Plot a graph of the results.", 3, "", 70, "x-axis: sodium hydrogen carbonate (g/100 ml); y-axis: number of bubbles in 5 min, with scale and units (1); points plotted correctly (1); smooth curve rising then flat, with title (1)."),
  ("b)", "Name the independent and dependent variables.", 1, "", 14, "Independent: <b>CO<sub>2</sub> concentration (NaHCO<sub>3</sub>)</b>; dependent: <b>number of bubbles (rate of photosynthesis)</b>."),
  ("c)", "State a conclusion from the results.", 1, "", 14, "As CO<sub>2</sub> concentration rises the rate increases up to 0.6 g/100 ml, after which it stays constant (another factor limits)."),
  ("d)", "Suggest TWO ways a farmer can improve the yield of tomatoes in a greenhouse using the knowledge of photosynthesis.", 2, "", 24, "Keep the temperature near the optimum (30&ndash;35 &deg;C); give enough light (transparent roof / lamps); raise CO<sub>2</sub>; water regularly. (any two)"),
  ("e)", "What is the role of water in the light reaction?", 1, "", 14, "Water is <b>split (photolysis)</b> to give hydrogen for NADPH and oxygen as a by-product."),
  ("f)", "Explain why photosynthesis stops at night even though the dark reaction does not need light.", 2, "", 24, "At night the light reaction stops, so no ATP and NADPH are made (1). The dark reaction depends on these products and soon runs out of them (1)."),
 ],
 4: [
  ("a)", "A ring of bark was removed from the stem of a woody plant. Draw a diagram to show the result after some months and explain.", 3, "", 50, "Swelling above the ring, no swelling below (1, labelled). Phloem was removed so sugars from the leaves cannot move down (1). Xylem is intact, water still moves up (1)."),
  ("b)", "Why are leaves called a source and roots a sink?", 2, "", 24, "Leaves make sugar by photosynthesis in excess of their needs and export it (source) (1). Roots use or store the sugar (sink) (1)."),
  ("c)", "State THREE differences between xylem and phloem.", 3, "", 36, "Xylem: water and minerals, dead cells, upward only. Phloem: sugars, living cells, both directions, needs ATP. (any three)"),
  ("d)", "Give TWO uses of auxin in farming.", 2, "", 24, "NAA stops early fruit drop / sprouting of potatoes; helps cuttings to make roots; 2,4-D kills broad-leaved weeds. (any two)"),
 ],
 5: [
  ("a)", "Study the figure of the human digestive system. Name the parts A, B, C and D.", 2, F.digestive(), 24, "A = liver; B = stomach; C = pancreas; D = small intestine (0.5 mark each)."),
  ("b)", "Where is bile stored and what is its function?", 2, "", 24, "Stored in the <b>gall bladder</b> (1); <b>emulsifies fats</b> and makes the food alkaline (1)."),
  ("c)", "Explain what would happen to digestion if the pancreatic duct was blocked.", 2, "", 24, "Pancreatic amylase, trypsin and lipase cannot reach the small intestine (1), so digestion of starch, proteins and fats is reduced (1)."),
  ("d)", "State TWO habits that improve digestion.", 2, "", 24, "Chew food thoroughly; eat at regular times; exercise regularly; drink water; eat fibre (any two)."),
  ("e)", "Why is chewing important?", 2, "", 24, "Chewing breaks food into small pieces, increasing the surface area for enzymes (1) and mixes it with saliva containing amylase (1)."),
 ],
 6: [
  ("a)", "State ONE function each of red blood cells, white blood cells and platelets.", 3, "", 36, "RBC: carry oxygen (haemoglobin); WBC: defend the body / phagocytosis; platelets: help clotting. (1 mark each)"),
  ("b)", "A man of blood group AB needs a blood transfusion. Which groups can he receive and why?", 2, "", 24, "A, B, AB and O (1). AB has no anti-A or anti-B in the plasma, so no clumping occurs (1)."),
  ("c)", "The table shows the concentration (g/100 ml) of some substances in the glomerular filtrate and in urine.<br><table class='tab' style='width:auto'><tr><th></th><th>Glucose</th><th>Urea</th><th>Protein</th></tr><tr><td>Filtrate</td><td>0.10</td><td>0.03</td><td>0</td></tr><tr><td>Urine</td><td>0</td><td>2.00</td><td>0</td></tr></table>Explain the differences for glucose and urea.", 3, "", 36, "Glucose is completely reabsorbed in the PCT, so none is in urine (1). Urea is not reabsorbed while water is, so its concentration is much higher in urine (1). Some urea is also secreted (1)."),
  ("d)", "What would happen if a person did not make enough ADH?", 2, "", 24, "Less water is reabsorbed in the collecting duct (1), so a large volume of dilute urine is passed and the person becomes dehydrated (1)."),
 ],
 7: [
  ("a)", "(i) Trace the pathway of a reflex when a person steps on a sharp pin.", 2, "", 24, "Receptor (skin) &rarr; sensory neuron &rarr; interneuron in spinal cord &rarr; motor neuron &rarr; effector (leg muscle) &rarr; leg is withdrawn."),
  ("", "(ii) Why is the brain not needed for the first response?", 1, "", 14, "The spinal cord processes the signal so the response is quick."),
  ("b)", "Give TWO differences between a reflex action and a voluntary action.", 2, "", 24, "Reflex: involuntary, fast, spinal cord, no thinking, e.g. blinking. Voluntary: controlled by the brain, slower, e.g. writing. (any two)"),
  ("c)", "How is the human nervous system similar to a computer? Give TWO points.", 2, "", 24, "Receptors/sensors give input; brain/CPU processes; effectors/monitor give output; electrical signals; memory/storage. (any two)"),
  ("d)", "State THREE harmful effects of anabolic steroids.", 3, "", 36, "Infertility, irregular periods, liver and heart damage, high blood pressure, mood swings, aggression, depression (any three)."),
 ],
 8: [
  ("a)", "The figure shows a family in which haemophilia occurs.<br>(i) Write the genotype of I-2 and II-3.", 1, F.pedigree(), 14, "I-2 = X<sup>H</sup>X<sup>h</sup> (carrier); II-3 = X<sup>h</sup>Y (0.5 mark each)."),
  ("", "(ii) From whom did II-3 inherit the haemophilia allele? Explain.", 2, "", 24, "From his <b>mother (I-2)</b> (1). A son receives his X chromosome from his mother and the Y chromosome from his father (1)."),
  ("b)", "Two heterozygous tall pea plants (Tt) are crossed. Draw a Punnett square and give the genotypic and phenotypic ratios.", 3, "", 50, "Gametes T, t &times; T, t gives TT, Tt, Tt, tt (1). Genotypic ratio 1 TT : 2 Tt : 1 tt (1). Phenotypic ratio 3 tall : 1 dwarf (1)."),
  ("c)", "Explain how meiosis keeps the chromosome number the same from one generation to the next.", 2, "", 24, "Meiosis halves the number in gametes (1); fertilisation restores the diploid number in the zygote (1)."),
  ("d)", "A cell has 14 chromosomes. How many are present in each cell after (i) mitosis, (ii) meiosis?", 1, "", 14, "(i) 14 (ii) 7 (0.5 mark each)."),
  ("e)", "Why are the daughter cells formed by mitosis identical?", 1, "", 14, "The DNA is copied exactly and each chromatid is shared equally between the two cells; no crossing over."),
 ],
 9: [
  ("a)", "The graph shows the population of an animal before and after hunting began.<br>(i) Name the effect that reduced the genetic variation of the survivors.", 1, F.bottleneck(), 14, "<b>Bottleneck effect</b> (genetic drift)."),
  ("", "(ii) Explain the effect on the genetic diversity of the population.", 2, "", 24, "Only a few individuals survive, so many alleles are lost (1). The population becomes less variable and is less able to adapt to disease or change (1)."),
  ("b)", "A river divides a bird population into two. Name the type of isolation and explain how it can lead to speciation.", 3, "", 36, "<b>Geographic isolation</b> (1). No gene flow; mutation, natural selection and drift act differently on each population (1) until they cannot interbreed (1)."),
  ("c)", "What is an invasive species? Give ONE example from Bhutan and ONE effect on the ecosystem.", 3, "", 36, "A non-native species that spreads quickly and harms native species (1). Example: Lantana camara / crofton weed / polka dot plant (1). Effect: crowds out native plants, reduces biodiversity or crop yield (1)."),
  ("d)", "State ONE way Bhutan conserves its biodiversity.", 1, "", 14, "60 % forest cover for all time in the Constitution; protected areas and biological corridors; hunting ban; community forests (any one)."),
 ],
}
