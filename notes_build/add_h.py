import re, pathlib
ROOT = pathlib.Path(__file__).parent

def append_to(fname, title_substr, html):
    p = ROOT / "parts" / fname
    s = p.read_text(encoding="utf-8")
    i = s.index(title_substr)
    j = s.index("</div>\n</section>", i)
    s = s[:j] + html + "\n" + s[j:]
    p.write_text(s, encoding="utf-8")

ADD = {}

ADD[("h_01_early.html", "Indus Valley Civilisation")] = '''
<h3>Main sites</h3>
<table class="tbl"><tr><th>Site</th><th>Known for</th></tr>
<tr><td>Harappa (Punjab)</td><td>first site found (1921); granaries, workers&rsquo; quarters; gave the civilisation its name</td></tr>
<tr><td>Mohenjo-daro (Sindh)</td><td>&ldquo;mound of the dead&rdquo;; <b>Great Bath</b>, large granary, best-planned streets</td></tr>
<tr><td>Lothal (Gujarat)</td><td><b>dockyard</b>, bead-making, sea trade</td></tr>
<tr><td>Kalibangan (Rajasthan)</td><td>ploughed field, fire altars</td></tr>
<tr><td>Dholavira (Gujarat)</td><td>stepped water reservoirs &mdash; water conservation</td></tr>
<tr><td>Rakhigarhi (Haryana)</td><td>one of the largest Indus sites</td></tr></table>
<h3>Feature &rarr; why it mattered</h3>
<table class="tbl"><tr><th>Feature</th><th>Benefit</th></tr>
<tr><td>Grid streets</td><td>easy movement, orderly growth</td></tr>
<tr><td>Fire-baked bricks</td><td>strong, flood-resistant houses</td></tr>
<tr><td>Covered drains</td><td>clean streets, fewer diseases</td></tr>
<tr><td>Great Bath / wells</td><td>water supply, ritual bathing</td></tr>
<tr><td>Granary</td><td>food storage for the city</td></tr>
<tr><td>Seals and weights</td><td>trade, ownership, fair measures</td></tr>
<tr><td>Dockyard</td><td>sea trade (with Mesopotamia)</td></tr></table>
<h3>Likely questions</h3>
<ul>
<li><b>Why is it called an urban civilisation?</b> planned cities, writing (seals), specialised crafts, trade and public works.</li>
<li><b>Causes of decline:</b> river shifting/drying, floods, climate change, fall in trade.</li>
<li><b>Link to Bhutan today:</b> grid planning in Thimphu, covered drains, waste bins, nature worship, meditation tradition.</li>
</ul>'''

ADD[("h_01_early.html", "Vedic Religion")] = '''
[[fig:vedic_to_buddha|Why new religions arose in the 6th century BCE.]]
<h3>Vedic religion vs Buddhism</h3>
<table class="tbl"><tr><th></th><th>Vedic</th><th>Buddhism</th></tr>
<tr><td>Worship</td><td>nature gods; fire sacrifice (yajna)</td><td>no creator god; meditation, ethics</td></tr>
<tr><td>Priests</td><td>Brahmins essential</td><td>monks (Sangha); no priest needed</td></tr>
<tr><td>Animals</td><td>sacrificed</td><td>non-violence (<i>ahimsa</i>)</td></tr>
<tr><td>Society</td><td>caste (varna) by birth</td><td>equality; all castes join the Sangha</td></tr>
<tr><td>Aim</td><td>wealth, victory, heaven</td><td>end of suffering (nirvana)</td></tr></table>
<h3>Four holy places &amp; Three Jewels</h3>
<table class="tbl"><tr><th>Place</th><th>Event</th></tr>
<tr><td>Lumbini</td><td>birth</td></tr><tr><td>Bodh Gaya</td><td>Enlightenment</td></tr><tr><td>Sarnath</td><td>First Sermon</td></tr><tr><td>Kushinagar</td><td>Mahaparinirvana</td></tr></table>
<p><b>Three Jewels:</b> the Buddha, the Dharma (teachings), the Sangha (community of monks).</p>
<h3>Buddhism in Bhutan</h3>
<ul>
<li><b>7th century:</b> Tibetan king <b>Songtsen Gampo</b> built Kyichu (Paro) and Jampa (Bumthang) temples.</li>
<li><b>8th century (746):</b> <b>Guru Rinpoche</b> came to Bumthang (Sindhu Raja) and spread Vajrayana.</li>
<li><b>1616:</b> the Zhabdrung made <b>Drukpa Kagyu</b> the state religion.</li>
</ul>
</ul>'''.replace("</ul>\n</ul>", "</ul>")

ADD[("h_01_early.html", "The Age of Exploration")] = '''
<h3>Who did what</h3>
<table class="tbl"><tr><th>Explorer</th><th>Country</th><th>Achievement</th></tr>
<tr><td>Prince Henry the Navigator</td><td>Portugal</td><td>sponsored voyages and navigation school</td></tr>
<tr><td>Bartolomeu Dias</td><td>Portugal</td><td>rounded the Cape of Good Hope, 1488</td></tr>
<tr><td>Christopher Columbus</td><td>Spain</td><td>reached the Americas, 1492</td></tr>
<tr><td>Vasco da Gama</td><td>Portugal</td><td>sea route to India (Calicut), 1498</td></tr>
<tr><td>Pedro Cabral</td><td>Portugal</td><td>reached Brazil, 1500</td></tr>
<tr><td>Ferdinand Magellan</td><td>Spain</td><td>expedition that first circled the globe, 1519&ndash;22</td></tr>
<tr><td>Cortes / Pizarro</td><td>Spain</td><td>conquered the Aztec (1521) / Inca (1530s) empires</td></tr></table>
<h3>Effects: positive and negative</h3>
<table class="tbl"><tr><th>Positive</th><th>Negative</th></tr>
<tr><td>global trade and cultural links (globalisation)</td><td>conquest and colonisation</td></tr>
<tr><td>exchange of crops (potato, maize, tomato) and animals</td><td>slave trade of Africans</td></tr>
<tr><td>better maps and scientific knowledge</td><td>diseases such as smallpox killed natives</td></tr>
<tr><td>new foods, goods and ideas spread</td><td>loss of native cultures and land</td></tr></table>'''

ADD[("h_01_early.html", "Colonialism")] = '''
<h3>Cause and effect</h3>
<table class="tbl"><tr><th>Event</th><th>Effect</th></tr>
<tr><td>Plassey 1757</td><td>Company controls Bengal politics</td></tr>
<tr><td>Diwani 1765</td><td>right to collect revenue; drain of wealth</td></tr>
<tr><td>Subsidiary Alliance (Wellesley)</td><td>princes lose independence</td></tr>
<tr><td>Doctrine of Lapse (Dalhousie)</td><td>states annexed; discontent</td></tr>
<tr><td>Revolt of 1857</td><td>Crown rule from 1858</td></tr>
<tr><td>Partition of Bengal 1905</td><td>Swadeshi movement</td></tr>
<tr><td>Jallianwala Bagh 1919</td><td>mass anger; non-cooperation (1920&ndash;22)</td></tr>
<tr><td>Salt March 1930; Quit India 1942</td><td>mass civil disobedience &rarr; freedom 1947</td></tr></table>'''

ADD[("h_02_hist_zhab.html", "Historiography, Oral History")] = '''
<h3>Oral history vs oral tradition</h3>
<table class="tbl"><tr><th></th><th>Oral history</th><th>Oral tradition</th></tr>
<tr><td>Meaning</td><td>memories of events a person lived</td><td>stories, songs, customs passed through generations</td></tr>
<tr><td>Time</td><td>recent past</td><td>long past</td></tr>
<tr><td>Collected by</td><td>interviews and recordings</td><td>listening, repetition, performance</td></tr>
<tr><td>Example</td><td>an elder describing a flood</td><td>folk tale of a place, ballads, proverbs</td></tr></table>
<h3>Sources of history</h3>
<ul><li><b>Primary:</b> treaties, diaries (Turner), letters, inscriptions, photos. <b>Secondary:</b> textbooks, later studies.</li><li><b>Types:</b> written, archaeological, oral, visual.</li></ul>
<h3>Why study history?</h3>
<ul><li>learn from the past; build identity; understand cause and effect; respect other cultures.</li></ul>'''

ADD[("h_02_hist_zhab.html", "Zhabdrung")] = '''
<h3>Zhabdrung&rsquo;s achievements</h3>
<table class="tbl"><tr><th>Area</th><th>What he did</th></tr>
<tr><td>Political</td><td>unified valleys; Choe-sid government; 3 regions under Poenlops</td></tr>
<tr><td>Military</td><td>repelled Tibetan&ndash;Mongol invasions (1634, 1639, 1644)</td></tr>
<tr><td>Religious</td><td>Drukpa Kagyu as state religion; monastic body under the Je Khenpo</td></tr>
<tr><td>Legal</td><td>Kathrim; spiritual and secular law</td></tr>
<tr><td>Cultural</td><td>Driglam Namzha, dzong architecture, festivals, Dzongkha</td></tr></table>
<h3>Dzongs: why they matter</h3>
<table class="tbl"><tr><th>Dzong</th><th>Founded</th></tr>
<tr><td>Simtokha</td><td>1629 (first dzong)</td></tr><tr><td>Punakha</td><td>1637</td></tr><tr><td>Wangdue Phodrang</td><td>1638</td></tr></table>
<p>A dzong is a <b>fortress, monastery and administrative centre</b> in one: it defended the valley, held monks and officials, and hosted tshechus &mdash; the visible sign of <b>Choe-sid</b>.</p>'''

ADD[("h_02_hist_zhab.html", "Bhutan &amp; British India")] = '''
[[fig:duar_war|The Duar War: cause-and-effect chain.]]
<h3>Likely questions</h3>
<ul>
<li><b>Causes of the Duar War:</b> border disputes and raids in the Duars; British wish for the fertile Duars (revenue, tea, route to Tibet); the failed Eden mission.</li>
<li><b>Effects of Sinchula:</b> Bhutan lost the Duars and Dewangiri (about a fifth of its land) but gained a yearly payment and peace.</li>
<li><b>Why did the British support Ugyen Wangchuck?</b> He proved a skilled mediator in 1904; he later became the stable ruler of a united Bhutan (1907).</li>
</ul>'''

ADD[("h_03_kings.html", "The Monarchy")] = '''
<h3>The Third King: modernisation</h3>
<table class="tbl"><tr><th>Year</th><th>Step</th></tr>
<tr><td>1953</td><td>National Assembly (Tshogdu) set up</td></tr>
<tr><td>1956</td><td>land reform; serfdom abolished</td></tr>
<tr><td>1961</td><td>First Five Year Plan; Thimphu capital</td></tr>
<tr><td>1968</td><td>High Court and Council of Ministers</td></tr>
<tr><td>1971</td><td>Bhutan joins the United Nations</td></tr></table>
<h3>Fourth King: reign in brief</h3>
<ul>
<li><b>1972:</b> ascends the throne at 16. <b>1974:</b> coronation.</li>
<li><b>1981 / 1991:</b> Dzongkhag and Gewog development committees (DYT, GYT).</li>
<li><b>1998:</b> hands over executive power to the Council of Ministers.</li>
<li><b>2001&ndash;05:</b> Constitution drafted. <b>2003:</b> Operation All Clear. <b>2006:</b> abdication.</li>
</ul>'''

ADD[("h_03_kings.html", "The Fifth Druk Gyalpo")] = '''
<h3>Key dates</h3>
<table class="tbl"><tr><th>Date</th><th>Event</th></tr>
<tr><td>21 Feb 1980</td><td>birth</td></tr>
<tr><td>31 Oct 2004</td><td>installed as Trongsa Poenlop</td></tr>
<tr><td>9 Dec 2006</td><td>becomes Fifth Druk Gyalpo</td></tr>
<tr><td>2008</td><td>coronation (Punakha and Thimphu)</td></tr>
<tr><td>13 Oct 2011</td><td>royal wedding, Punakha Dzong</td></tr>
<tr><td>17 Dec 2019</td><td>Gyalsung announced</td></tr>
<tr><td>2024</td><td>first Gyalsung batch</td></tr></table>'''

ADD[("h_04_constitution.html", "Constitution, GNH")] = '''
<h3>Articles to know</h3>
<table class="tbl"><tr><th>Art.</th><th>Subject</th></tr>
<tr><td>1</td><td>The Kingdom</td></tr><tr><td>2</td><td>Institution of Monarchy</td></tr><tr><td>3</td><td>Spiritual heritage</td></tr><tr><td>4</td><td>Culture</td></tr><tr><td>5</td><td><b>Environment</b></td></tr><tr><td>6</td><td>Citizenship</td></tr><tr><td>7</td><td>Fundamental rights</td></tr><tr><td>8</td><td>Fundamental duties</td></tr><tr><td>9</td><td>Principles of State policy (GNH)</td></tr></table>
<h3>Roles of the Druk Gyalpo</h3>
<ul><li>Head of State; <b>symbol of unity</b> of the Kingdom and people; Supreme Commander of the armed forces; protector of all religions; may grant amnesty (acts above party politics).</li></ul>'''

ADD[("h_04_constitution.html", "Civil Society")] = '''
<h3>Examples of CSOs</h3>
<table class="tbl"><tr><th>CSO</th><th>Focus</th></tr>
<tr><td>RENEW</td><td>women, victims of abuse</td></tr><tr><td>Bhutan Kidney Foundation</td><td>kidney patients</td></tr><tr><td>Tarayana</td><td>rural poverty alleviation</td></tr><tr><td>RSPN</td><td>nature conservation</td></tr></table>
<p><b>Community vitality</b> is one of the nine GNH domains: trust, volunteering and mutual help (self-help, <i>woola</i>).</p>'''

for (f, t), html in ADD.items():
    append_to(f, t, html)
print("ok")
