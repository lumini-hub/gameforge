#!/usr/bin/env python3
"""Builds a mock BCSE Class X Physics paper (exam format) and its marking scheme as PDFs."""
import subprocess, pathlib, html
import physics_figs as pf
from physics_figs import T, L, R, C, P, poly, wave

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
CODE = "BCSE/22-1/MOCK"


def svg(w, h, body, width=None):
    return f'<svg viewBox="0 0 {w} {h}" width="{width or w}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Serif, Times New Roman, serif">{pf.DEFS}{body}</svg>'


# ------------------------------------------------------------------ figures
def fig_rule():
    b = [R(30, 60, 360, 14, "#e0c9a6", "#333", 1.5)]
    for k in range(11):
        x = 30 + k * 36
        b.append(L(x, 60, x, 66, "#333", 1))
    for cm in (0, 20, 40, 60, 80, 100):
        b.append(T(30 + cm * 3.6, 92, str(cm), 10))
    b.append(poly([(210, 74), (198, 100), (222, 100)], "#bbb", "#333", 1.5)); b.append(T(210, 114, "pivot", 10))
    b.append(L(66, 30, 66, 60, "#b3261e", 2.4, arrow=True)); b.append(T(66, 22, "6 N", 11))
    b.append(L(282, 74, 282, 108, "#1b3a6b", 2.4, arrow=True)); b.append(T(282, 122, "W", 11))
    b.append(T(210, 40, "Uniform metre rule, pivoted at the 50 cm mark", 11))
    return svg(420, 130, "".join(b), 330)


def fig_vi3():
    b = []
    gx, gy, gw, gh = 50, 15, 190, 140
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#000", 1.4, arrow=True)); b.append(L(gx, gy + gh, gx, gy - 6, "#000", 1.4, arrow=True))
    b.append(T(gx + gw, gy + gh + 15, "Current (I)", 10, anchor="end")); b.append(T(18, gy + 70, "Voltage (V)", 10, rot=-90))
    for name, x2, y2, tx in (("P", 120, 22, 124), ("Q", 170, 40, 174), ("R", 205, 95, 208)):
        b.append(L(gx, gy + gh, x2 + gx - 40 + 0, gy + y2, "#000", 2)); b.append(T(x2 + gx - 36, gy + y2 - 3, name, 12, anchor="start", weight="bold"))
    return svg(260, 190, "".join(b), 230)


def fig_vi2():
    b = []
    gx, gy, gw, gh = 50, 15, 190, 140
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#000", 1.4, arrow=True)); b.append(L(gx, gy + gh, gx, gy - 6, "#000", 1.4, arrow=True))
    b.append(T(gx + gw, gy + gh + 15, "I (A)", 10, anchor="end")); b.append(T(18, gy + 70, "V (V)", 10, rot=-90))
    # X: through (2 A, 8 V): 1 A = 40px, 1 V = 10px
    b.append(L(gx, gy + gh, gx + 160, gy + gh - 80, "#000", 2)); b.append(T(gx + 164, gy + gh - 84, "X", 12, anchor="start", weight="bold"))
    b.append(P(f"M{gx},{gy + gh} Q{gx + 40},{gy + gh - 10} {gx + 70},{gy + gh - 50} T{gx + 130},{gy + 8}", "none", "#000", 2)); b.append(T(gx + 134, gy + 8, "Y", 12, anchor="start", weight="bold"))
    for I in (1, 2, 3, 4):
        b.append(L(gx + I * 40, gy + gh, gx + I * 40, gy + gh + 4, "#000", 1)); b.append(T(gx + I * 40, gy + gh + 15, str(I), 9))
    for V in (4, 8, 12):
        b.append(L(gx, gy + gh - V * 10, gx - 4, gy + gh - V * 10, "#000", 1)); b.append(T(gx - 7, gy + gh - V * 10 + 3, str(V), 9, anchor="end"))
    b.append(L(gx + 80, gy + gh, gx + 80, gy + gh - 40, "#000", 1, dash="3 3")); b.append(L(gx, gy + gh - 40, gx + 80, gy + gh - 40, "#000", 1, dash="3 3"))
    return svg(260, 190, "".join(b), 230)


def fig_wire():
    b = []
    for k in range(4):
        y = 30 + k * 34
        b.append(L(30, y, 270, y, "#444", 1.4, arrow=True))
    b.append(T(30, 18, "Magnetic field", 10, anchor="start"))
    b.append(C(150, 80, 14, "#fff", "#000", 2)); b.append(C(150, 80, 3, "#000", "#000"))
    b.append(T(150, 118, "wire (current flows out of the page, towards you)", 10))
    return svg(300, 130, "".join(b), 300)


def fig_wave():
    b = [L(20, 70, 300, 70, "#888", 1, dash="3 3"), P(wave(20, 300, 70, 38, 1.5), "none", "#000", 2.2)]
    b.append(T(78, 22, "P", 11, weight="bold")); b.append(T(160, 122, "Q", 11, weight="bold")); b.append(T(222, 22, "R", 11, weight="bold"))
    b.append(C(77, 32, 2.5, "#000", "#000")); b.append(C(163, 108, 2.5, "#000", "#000")); b.append(C(250, 32, 2.5, "#000", "#000"))
    return svg(320, 135, "".join(b), 300)


def fig_cones():
    b = []
    b.append(poly([(40, 100), (100, 100), (70, 40)], "#ddd", "#000", 2)); b.append(T(70, 118, "X", 12, weight="bold"))
    b.append(poly([(190, 100), (220, 100), (205, 55)], "#ddd", "#000", 2).replace("190,100 220,100 205,55", "175,100 235,100 205,40")); b.append(T(205, 118, "Y", 12, weight="bold"))
    b.append(poly([(330, 80), (390, 80), (360, 20)], "#ddd", "#000", 2).replace("330,80 390,80 360,20", "320,100 400,95 340,45")); b.append(T(360, 118, "Z", 12, weight="bold"))
    b.append(L(20, 100, 440, 100, "#000", 1.5))
    return svg(460, 128, "".join(b), 360)


def fig_cone_rest():
    """three pictures for Q2(c): cone on its base, on its tip, on its side"""
    b = [L(15, 100, 435, 100, "#000", 1.5)]
    b.append(poly([(30, 100), (100, 100), (65, 30)], "#eee", "#000", 2))
    b.append(poly([(190, 40), (240, 40), (215, 98)], "#eee", "#000", 2).replace("190,40 240,40 215,98", "180,20 250,20 215,98"))
    b.append(poly([(330, 100), (420, 100), (330, 72)], "#eee", "#000", 2).replace("330,100 420,100 330,72", "320,68 425,100 320,100"))
    return svg(450, 112, "".join(b), 380)


# ------------------------------------------------------------------ helpers
def box(h, marks_col=True, w_marks="20mm"):
    return f'<table class="box"><tr><td style="height:{h}mm"></td>{"<td class=m style=width:" + w_marks + "></td>" if marks_col else ""}</tr></table>'


def part(label, text, marks=None, fig="", h=None, indent=0):
    mk = f"[{marks}]" if marks else ""
    out = f'<div class="part" style="margin-left:{indent}mm"><div class="lab">{label}</div><div class="txt">{text}</div><div class="mk">{mk}</div></div>'
    if fig:
        out += f'<div class="fig" style="margin-left:{14 + indent}mm">{fig}</div>'
    if h:
        out += box(h)
    return f'<div class="blk">{out}</div>'


def mcq(label, text, opts, fig=""):
    o = "".join(f'<div class="opt"><span>{l}</span><span>{t}</span></div>' for l, t in zip("ABCD", opts))
    f = f'<div class="fig" style="margin-left:14mm">{fig}</div>' if fig else ""
    return f'<div class="blk mcq"><div class="part"><div class="lab">{label}</div><div class="txt">{text}</div></div>{f}<div class="opts">{o}</div></div>'


# ------------------------------------------------------------------ Section A content
MCQS = [
    ("The SI unit of the moment of a force is", ["N", "N m", "N/m", "J/s"], "B", "Moment = force &times; distance, so the unit is N m.", ""),
    ("A body is in stable equilibrium if, when it is slightly displaced, its centre of gravity", ["rises and the body returns to its original position.", "falls and the body moves further away.", "stays at the same height and the body stays in the new position.", "moves outside the base and the body topples."], "A", "Stable equilibrium: C.G. rises and the body returns.", ""),
    ("The uniform metre rule in the figure is balanced at the 50 cm mark by a 6 N force at the 10 cm mark. What is the weight W hung at the 70 cm mark?", ["4 N", "6 N", "9 N", "12 N"], "D", "6 &times; 40 = W &times; 20 &rArr; W = 12 N.", fig_rule()),
    ("Which of the following objects has the greatest stability?", ["A tall, narrow cylinder standing on its end", "A short cone with a wide base", "A cone balanced on its tip", "A tall box with a narrow base"], "B", "Low C.G. and a wide base give the greatest stability.", ""),
    ("If the distance between two masses is halved, the gravitational force between them becomes", ["half", "double", "four times", "one quarter"], "C", "F &prop; 1/r&sup2;: (1/&frac12;)&sup2; = 4.", ""),
    ("A stone is dropped from a cliff. Neglecting air resistance, its speed after 3 s is (g = 10 m/s&sup2;)", ["10 m/s", "20 m/s", "30 m/s", "45 m/s"], "C", "v = g t = 10 &times; 3 = 30 m/s.", ""),
    ("A parachutist falls at terminal velocity. At this stage", ["the weight is greater than the air resistance.", "the weight is equal to the air resistance.", "the air resistance is zero.", "the acceleration is 10 m/s&sup2;."], "B", "Terminal velocity: drag = weight, net force zero.", ""),
    ("A force of 50 N moves an object 4 m in the direction of the force. The work done is", ["12.5 J", "54 J", "100 J", "200 J"], "D", "W = F d = 50 &times; 4 = 200 J.", ""),
    ("A crane lifts a 500 kg load through 10 m in 20 s. The power developed is (g = 10 m/s&sup2;)", ["250 W", "2500 W", "5000 W", "50 000 W"], "B", "W = 500 &times; 10 &times; 10 = 50 000 J; P = 50 000 / 20 = 2500 W.", ""),
    ("A machine takes in 500 J of energy and gives out 400 J of useful energy. Its efficiency is", ["20 %", "80 %", "100 %", "125 %"], "B", "400 / 500 &times; 100 = 80 %.", ""),
    ("A force of 200 N acts on an area of 0.5 m&sup2;. The pressure is", ["100 Pa", "250 Pa", "400 Pa", "1000 Pa"], "C", "P = F/A = 200 / 0.5 = 400 Pa.", ""),
    ("In a hydraulic machine a force of 20 N acts on a piston of area 2 cm&sup2;. The large piston has an area of 40 cm&sup2;. The force on the large piston is", ["20 N", "40 N", "200 N", "400 N"], "D", "F<sub>2</sub> = 20 &times; 40/2 = 400 N.", ""),
    ("The pressure at a point in a liquid depends on", ["the shape of the container.", "the depth and the density of the liquid.", "the area of the surface of the liquid.", "the volume of the liquid only."], "B", "P = &rho; g h.", ""),
    ("How much heat is needed to raise the temperature of 3 kg of water by 10 &deg;C? (c = 4200 J/kg&deg;C)", ["12 600 J", "42 000 J", "126 000 J", "420 000 J"], "C", "Q = 3 &times; 4200 &times; 10 = 126 000 J.", ""),
    ("Equal amounts of heat are supplied to equal masses of four liquids. Which liquid shows the smallest rise in temperature?", ["Liquid A, c = 2100 J/kg&deg;C", "Liquid B, c = 2400 J/kg&deg;C", "Liquid C, c = 3400 J/kg&deg;C", "Liquid D, c = 4200 J/kg&deg;C"], "D", "&Delta;T = Q/mc: the largest c gives the smallest rise.", ""),
    ("While ice is melting at 0 &deg;C, the heat supplied", ["raises the temperature of the ice.", "raises the temperature of the water.", "changes the state without a change in temperature.", "is lost to the surroundings."], "C", "Latent heat of fusion: temperature stays constant.", ""),
    ("The graph shows the V&ndash;I relationship for three conductors P, Q and R. Which conductor has the greatest resistance?", ["P", "Q", "R", "All have the same resistance"], "A", "Resistance = V/I = slope; P is the steepest.", fig_vi3()),
    ("A 12 &Omega; resistor is connected across a 36 V supply. The current through it is", ["0.33 A", "3 A", "24 A", "432 A"], "B", "I = V/R = 36/12 = 3 A.", ""),
    ("The heat produced in a 5 &Omega; resistor carrying a current of 2 A for 10 s is", ["20 J", "100 J", "200 J", "400 J"], "C", "H = I&sup2;Rt = 4 &times; 5 &times; 10 = 200 J.", ""),
    ("Fleming's left-hand rule is used to find the direction of", ["the induced current in a generator.", "the force on a current-carrying conductor in a magnetic field.", "the magnetic field around a straight wire.", "the heat produced in a conductor."], "B", "Left hand = motor effect (force).", ""),
    ("A transformer has 100 turns in the primary and 500 turns in the secondary. If the input voltage is 20 V, the output voltage is", ["4 V", "20 V", "100 V", "2500 V"], "C", "V<sub>s</sub> = 20 &times; 500/100 = 100 V.", ""),
    ("Which of the following electromagnetic waves has the shortest wavelength?", ["Microwaves", "Infrared", "X-rays", "Gamma rays"], "D", "Gamma rays have the shortest wavelength.", ""),
    ("Which of the following is a longitudinal wave?", ["Light", "Sound", "X-ray", "Radio wave"], "B", "Sound is made of compressions and rarefactions.", ""),
    ("An alpha particle consists of", ["1 proton and 1 neutron.", "2 protons and 2 neutrons.", "1 electron.", "a high-energy electromagnetic wave."], "B", "An alpha particle is a helium nucleus.", ""),
    ("When uranium-238 (<sup>238</sup><sub>92</sub>U) emits an alpha particle, the daughter nucleus is", ["<sup>234</sup><sub>90</sub>Th", "<sup>234</sup><sub>92</sub>U", "<sup>238</sup><sub>93</sub>Np", "<sup>236</sup><sub>90</sub>Th"], "A", "A &minus; 4 = 234, Z &minus; 2 = 90.", ""),
]
ROM = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv"]

FILL = [
    ("The turning effect of a force about a point is called the ______________.", "moment (torque)"),
    ("At terminal velocity the net force acting on a falling body is ______________.", "zero"),
    ("Heat always flows from a body at a higher temperature to a body at a ______________ temperature.", "lower"),
    ("The direction of the induced current in a conductor is given by Fleming's ______________ rule.", "right-hand"),
    ("The radiation which has the highest penetrating power is ______________.", "gamma radiation (rays)"),
]
TF = [
    ("A couple produces a net force on a body.", "FALSE"),
    ("The pressure at a point in a liquid acts in all directions.", "TRUE"),
    ("The resistance of a wire increases when its length is increased.", "TRUE"),
    ("Radio waves travel faster than gamma rays in a vacuum.", "FALSE"),
    ("The red shift of light from distant galaxies shows that the universe is expanding.", "TRUE"),
]
MATCH_A = ["Unit of power", "Device that changes an alternating voltage", "Heat absorbed in melting at constant temperature", "A vehicle that moves over the surface of Mars", "Ray deflected towards the positive plate"]
MATCH_B = ["latent heat", "watt", "beta rays", "rover", "transformer", "alpha rays", "joule"]
MATCH_ANS = ["b", "e", "a", "d", "c"]

# ------------------------------------------------------------------ Section B content (parts with answers)
# each question: list of (label, text, marks, fig, box_height_mm, answer_html)
QB = {
    2: [
        ("a)", "A uniform plank 4 m long is pivoted at its centre. A boy weighing 300 N sits 1.5 m from the pivot. Where should a girl weighing 450 N sit to balance the plank?", 2, "", 60,
         "Clockwise = anticlockwise: 300 &times; 1.5 = 450 &times; d &rArr; d = 450/450 = <b>1.0 m</b> from the pivot on the other side (the girl sits nearer the pivot)."),
        ("b)", "State TWO conditions for a body to be in equilibrium.", 1, "", 25, "(1) The net (resultant) force is zero. (2) The net moment about any point is zero (clockwise moments = anticlockwise moments)."),
        ("c)", "Three pictures of the same cone resting on a table are shown. Name the type of equilibrium of each and give a reason.", 2, fig_cone_rest(), 40,
         "<b>Cone on its base:</b> stable equilibrium (C.G. rises when tilted, the cone returns). <b>Cone on its tip:</b> unstable equilibrium (C.G. falls when displaced, it moves further). <b>Cone on its side:</b> neutral equilibrium (C.G. stays at the same height, it stays in the new position)."),
        ("d)", "A table lamp with a wide, heavy base is difficult to topple. Explain.", 1, "", 30, "The heavy wide base keeps the centre of gravity low and gives a large base area, so the line of gravity stays inside the base even when the lamp is tilted."),
        ("e)", "Which produces the greater moment about the pivot: 20 N acting at 0.30 m or 15 N acting at 0.50 m? Show your calculation.", 2, "", 50,
         "Moment 1 = 20 &times; 0.30 = 6 N m. Moment 2 = 15 &times; 0.50 = 7.5 N m. The <b>15 N force at 0.50 m</b> gives the greater moment."),
        ("f)", "Turning a tap is an example of a couple. Why?", 2, "", 40, "Two equal, opposite parallel forces act on the opposite sides of the tap handle; the net force is zero but they give a turning effect (moment = F &times; distance between the forces) &mdash; a couple."),
    ],
    3: [
        ("a)", "A ball is dropped from rest from the top of a tower and takes 4 s to reach the ground. Take g = 10 m/s&sup2;. Calculate (i) the velocity of the ball just before it hits the ground and (ii) the height of the tower.", 2, "", 65,
         "(i) v = g t = 10 &times; 4 = <b>40 m/s</b>. (ii) h = &frac12; g t&sup2; = 0.5 &times; 10 &times; 16 = <b>80 m</b>."),
        ("b)", "Explain why a feather and a coin fall at the same rate in a vacuum but not in air.", 2, "", 45, "In a vacuum only gravity acts, so both have the same acceleration g. In air the feather's large surface area gives a large air resistance compared with its weight, so it falls more slowly than the coin."),
        ("c)", "Calculate the gravitational force between a 5 kg mass and an 8 kg mass placed 0.4 m apart. (G = 6.67 &times; 10<sup>&minus;11</sup> N m&sup2; kg<sup>&minus;2</sup>)", 2, "", 65,
         "F = G m<sub>1</sub>m<sub>2</sub>/r&sup2; = 6.67 &times; 10<sup>&minus;11</sup> &times; 5 &times; 8 / (0.4)&sup2; = 6.67 &times; 10<sup>&minus;11</sup> &times; 40 / 0.16 = <b>1.67 &times; 10<sup>&minus;8</sup> N</b>."),
        ("d)", "State the law of conservation of energy.", 1, "", 25, "Energy can neither be created nor destroyed; it can only be changed from one form to another (the total energy stays constant)."),
        ("e)", "A girl of mass 60 kg climbs a flight of stairs 3 m high in 6 s. Calculate the power she develops. (g = 10 m/s&sup2;)", 2, "", 65, "Work = m g h = 60 &times; 10 &times; 3 = 1800 J. Power = W/t = 1800/6 = <b>300 W</b>."),
        ("f)", "Give ONE way in which a household can improve its energy efficiency.", 1, "", 25, "Use LED lamps / 5-star appliances, insulate the walls and roof, switch off unused appliances (any one)."),
    ],
    4: [
        ("a)", "In a hydraulic jack the small piston has an area of 4 cm&sup2; and a force of 50 N is applied to it. The large piston has an area of 80 cm&sup2;. Calculate the force on the large piston and name the principle used.", 2, "", 65,
         "F<sub>2</sub> = F<sub>1</sub> &times; A<sub>2</sub>/A<sub>1</sub> = 50 &times; 80/4 = <b>1000 N</b>. Principle: <b>Pascal's law</b> (pressure is transmitted equally through an enclosed liquid)."),
        ("b)", "A sharp knife cuts better than a blunt one. Explain.", 1, "", 25, "For the same force the sharp edge has a very small area, so the pressure (P = F/A) is large."),
        ("c)", "A rectangular tank with a base 2 m &times; 1.5 m contains water to a depth of 2 m. Calculate (i) the pressure at the bottom and (ii) the force on the base. (density of water = 1000 kg/m&sup3;, g = 10 m/s&sup2;)", 2, "", 70,
         "(i) P = &rho; g h = 1000 &times; 10 &times; 2 = <b>20 000 Pa</b>. (ii) F = P &times; A = 20 000 &times; (2 &times; 1.5) = <b>60 000 N</b>."),
        ("d)", "Calculate the heat needed to raise the temperature of 0.5 kg of water from 20 &deg;C to 70 &deg;C. (c = 4200 J/kg&deg;C)", 2, "", 60, "Q = m c &Delta;T = 0.5 &times; 4200 &times; 50 = <b>105 000 J</b>."),
        ("e)", "1 kg of water at 90 &deg;C is mixed with 2 kg of water at 15 &deg;C in an insulated container. Calculate the final temperature.", 2, "", 70,
         "Heat lost = heat gained: 1 &times; c &times; (90 &minus; T) = 2 &times; c &times; (T &minus; 15) &rArr; 90 &minus; T = 2T &minus; 30 &rArr; 3T = 120 &rArr; <b>T = 40 &deg;C</b>."),
        ("f)", "Why is water used as a coolant in car radiators?", 1, "", 25, "Water has a high specific heat capacity, so it absorbs a large amount of heat from the engine for a small rise in its temperature."),
    ],
    5: [
        ("a)", "The graph shows the V&ndash;I graphs for two wires X and Y. Which wire obeys Ohm's law? Use the graph to calculate the resistance of that wire.", 2, fig_vi2(), 50,
         "<b>Wire X</b> obeys Ohm's law (straight line through the origin). From the graph, V = 8 V when I = 2 A, so R = V/I = 8/2 = <b>4 &Omega;</b>."),
        ("b)", "A 60 W lamp is connected to a 240 V supply. Calculate (i) the current through the lamp and (ii) its resistance.", 2, "", 60, "(i) I = P/V = 60/240 = <b>0.25 A</b>. (ii) R = V/I = 240/0.25 = <b>960 &Omega;</b>."),
        ("c)", "The filament of a lamp glows but the connecting wires stay cool although the same current flows through both. Explain.", 1, "", 30, "The filament has a much higher resistance (thin tungsten wire), so more heat is produced in it (H = I&sup2;Rt)."),
        ("d)", "Calculate the heat produced in a 20 &Omega; resistor carrying a current of 3 A for 5 s.", 2, "", 55, "H = I&sup2;Rt = 3&sup2; &times; 20 &times; 5 = 9 &times; 100 = <b>900 J</b>."),
        ("e)", "State TWO factors which affect the resistance of a wire.", 1, "", 25, "Length, cross-sectional area, material, temperature (any two)."),
        ("f)", "Explain why electricity is transmitted over long distances at a very high voltage.", 2, "", 45, "For a given power P = V I, a higher voltage gives a smaller current. The heat loss I&sup2;R in the transmission lines is then much smaller, so less energy is wasted."),
    ],
    6: [
        ("a)", "A straight wire carrying a current out of the page lies in a magnetic field directed from left to right as shown. State the direction of the force on the wire and name the rule you used.", 2, fig_wire(), 40,
         "Using <b>Fleming's left-hand rule</b>: first finger = field (to the right), second finger = current (out of the page); the thumb points <b>upwards (towards the top of the page)</b>, so the force on the wire is upward."),
        ("b)", "Name ONE way of increasing the emf produced by a generator.", 1, "", 25, "Rotate the coil faster, or use a stronger magnet, or use more turns on the coil, or a larger coil (any one)."),
        ("c)", "A transformer has 400 turns in the primary coil and 100 turns in the secondary coil. The input is 240 V and 0.5 A. Assuming the transformer is 100 % efficient, calculate (i) the output voltage and (ii) the output current.", 3, "", 75,
         "(i) V<sub>s</sub> = V<sub>p</sub> &times; N<sub>s</sub>/N<sub>p</sub> = 240 &times; 100/400 = <b>60 V</b>. (ii) V<sub>p</sub>I<sub>p</sub> = V<sub>s</sub>I<sub>s</sub> &rArr; I<sub>s</sub> = 240 &times; 0.5 / 60 = <b>2 A</b>. (It is a step-down transformer.)"),
        ("d)", "Why does a transformer not work with a direct current (DC) supply?", 1, "", 25, "A DC gives a steady magnetic flux; there is no change of flux in the core, so no emf is induced in the secondary coil."),
        ("e)", "State TWO differences between an AC generator and a DC generator.", 2, "", 45, "AC generator: <b>slip rings</b>; output <b>alternates</b> in direction. DC generator: <b>split-ring commutator</b>; output flows in <b>one direction</b>."),
        ("f)", "The core of a transformer is made of laminated iron sheets. Why?", 1, "", 25, "Lamination reduces eddy currents, so less energy is wasted as heat in the core."),
    ],
    7: [
        ("a)", "An FM radio station broadcasts at a frequency of 100 MHz. Calculate the wavelength of the wave. (speed of radio waves = 3 &times; 10<sup>8</sup> m/s)", 2, "", 55, "&lambda; = c/f = 3 &times; 10<sup>8</sup> / (100 &times; 10<sup>6</sup>) = <b>3 m</b>."),
        ("b)", "The figure shows a wave. Identify the distance between P and R and the distance from Q to the dotted line. Is it a transverse or a longitudinal wave?", 2, fig_wave(), 40,
         "P to R is one complete <b>wavelength</b>; the distance from Q to the dotted line is the <b>amplitude</b>. The vibration is perpendicular to the direction of travel, so it is a <b>transverse</b> wave."),
        ("c)", "Why is infrared radiation used in a TV remote control? State ONE limitation.", 2, "", 45, "It carries signals over a short range and does not pass through to other rooms or interfere with other devices. Limitation: it travels in straight lines, so the path must not be blocked (line of sight)."),
        ("d)", "State ONE harmful effect of ultraviolet radiation on the human body.", 1, "", 25, "Skin burns / skin cancer / eye damage (any one)."),
        ("e)", "State ONE advantage of digital signals over analogue signals.", 1, "", 25, "Digital signals are less affected by noise and can be regenerated without loss (any one: easier to store, process, or secure)."),
        ("f)", "A person in a valley behind a hill can hear a radio broadcast but cannot see the transmitter. Explain.", 2, "", 45, "Radio waves have a long wavelength, comparable to the hill, so they diffract around it (and can be reflected by the ionosphere). Light has a very short wavelength and does not diffract noticeably around the hill."),
    ],
    8: [
        ("a)", "Complete the equation for the decay of radium: <sup>226</sup><sub>88</sub>Ra &rarr; X + <sup>4</sup><sub>2</sub>He", 1, "", 25, "X = <b><sup>222</sup><sub>86</sub>Rn</b> (A = 226 &minus; 4 = 222; Z = 88 &minus; 2 = 86)."),
        ("b)", "A lead nucleus <sup>214</sup><sub>82</sub>Pb emits a beta particle. Write the nuclear equation.", 2, "", 45, "<sup>214</sup><sub>82</sub>Pb &rarr; <b><sup>214</sup><sub>83</sub>Bi + <sup>0</sup><sub>&minus;1</sub>e</b> (mass number unchanged, atomic number increases by 1)."),
        ("c)", "Name the radiation with (i) a charge of +2 and (ii) no charge and the greatest penetrating power.", 2, "", 40, "(i) <b>Alpha particles</b>. (ii) <b>Gamma rays</b>."),
        ("d)", "State ONE safety precaution when handling a radioactive source in a laboratory.", 1, "", 25, "Use long tongs and keep the source in a lead-lined box (or wear protective clothing / keep the exposure time short)."),
        ("e)", "Why is gamma radiation used to sterilise surgical instruments?", 1, "", 25, "Gamma rays are highly penetrating and kill bacteria even inside sealed packets, without heating the instruments."),
        ("f)", "Differentiate between an orbiter and a rover.", 2, "", 50, "<b>Orbiter:</b> goes into orbit around a planet and studies it from above for a long time. <b>Rover:</b> lands and moves over the surface, collecting soil and rock samples."),
        ("g)", "What does the cosmological red shift tell us about the universe?", 1, "", 25, "The wavelengths of light from distant galaxies are stretched, so the galaxies are moving away: the universe is expanding."),
    ],
    9: [
        ("a)", "Suggest TWO features that would make a school hostel in a cold place energy efficient.", 2, "", 45, "Thick insulated walls and roof; double-glazed windows; large south-facing windows for sunlight; draught-proof doors; solar water heater (any two)."),
        ("b)", "A car of mass 1000 kg moves at 20 m/s. Calculate its kinetic energy. How much work must the brakes do to stop it?", 2, "", 60, "KE = &frac12; m v&sup2; = 0.5 &times; 1000 &times; 400 = <b>200 000 J</b>. Work done by the brakes = change in KE = <b>200 000 J</b>."),
        ("c)", "Should Bhutan install more solar power plants? Justify with TWO reasons.", 2, "", 45, "Yes. (1) Hydropower is low in winter, solar is strong then, so it improves energy security. (2) Solar is clean and renewable and reduces imports."),
        ("d)", "A boy of mass 40 kg stands on both feet. The total area of contact is 0.04 m&sup2;. Calculate the pressure he exerts on the ground. (g = 10 m/s&sup2;)", 2, "", 60, "F = 40 &times; 10 = 400 N; P = F/A = 400/0.04 = <b>10 000 Pa</b>."),
        ("e)", "A tall bookshelf is usually fixed to the wall. Why is this necessary?", 1, "", 25, "It has a high centre of gravity and a narrow base, so it can easily topple; fixing it to the wall prevents the line of gravity leaving the base."),
        ("f)", "State ONE advantage and ONE limitation of a flyby mission such as Voyager 2.", 1, "", 30, "Advantage: needs little fuel and can visit several planets. Limitation: collects data only for a short time (it does not orbit or land)."),
    ],
}

# check the marks total
for q, parts in QB.items():
    assert sum(p[2] for p in parts) == 10, (q, sum(p[2] for p in parts))

CSS = """
@page { size: A4; margin: 17mm 17mm 26mm 17mm;
  @bottom-left { content: "%CODE%\\A Copyright Reserved"; white-space: pre; font: italic bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; vertical-align: top; width: 40%; }
  @bottom-center { content: " "; border-top: 3px double #000; width: 20%; }
  @bottom-right { content: "Page " counter(page) " of " counter(pages); font: bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; text-align: right; vertical-align: top; width: 40%; } }
html { font-family: "Liberation Serif", "Times New Roman", serif; font-size: 11pt; line-height: 1.3; color: #000; }
body { margin: 0; }
h2.sec { text-align: center; font-size: 12pt; margin: 0 0 1mm; }
.sub { text-align: center; margin: 0 0 5mm; }
.q { font-weight: bold; margin: 4mm 0 2mm; display: flex; justify-content: space-between; }
.part { display: flex; margin: 1.5mm 0; }
.part .lab { width: 14mm; flex: none; }
.part .txt { flex: 1; text-align: justify; }
.part .mk { width: 12mm; flex: none; text-align: right; font-weight: bold; }
.dir { font-weight: bold; text-align: justify; }
.blk { break-inside: avoid; margin-bottom: 1mm; }
.opts { margin-left: 14mm; margin-bottom: 3mm; }
.opt { display: flex; gap: 6mm; } .opt span:first-child { width: 6mm; }
.fig { margin: 1mm 0 2mm; }
table.box { width: 100%; border-collapse: collapse; margin: 1.5mm 0 2.5mm; }
table.box td { border: 1px solid #000; padding: 0; }
table.tab { width: 100%; border-collapse: collapse; margin: 1.5mm 0 3mm; }
table.tab td, table.tab th { border: 1px solid #000; padding: 2mm 2mm; vertical-align: top; text-align: left; font-weight: normal; }
table.tab td.m { width: 20mm; }
table.tab td.a { width: 22mm; }
.rough { break-before: page; text-align: center; font-weight: bold; }
.key td, .key th { font-size: 9.8pt; }
.key table.tab td { vertical-align: top; }
""".replace("%CODE%", CODE)


def paper_html():
    h = []
    h.append('<h2 class="sec">SECTION A [40 MARKS]</h2><div class="sub">ANSWER <b>ALL</b> QUESTIONS</div>')
    h.append('<div class="q"><span>Question 1</span><span>[25]</span></div>')
    h.append('<div class="part"><div class="lab">a)</div><div class="txt dir">Directions: For each question, there are four alternatives A, B, C and D. Choose the correct alternative and circle it. Do not circle more than ONE alternative. If there are more than one choice circled, NO score will be awarded.</div></div>')
    for r, (text, opts, ans, why, fg) in zip(ROM, MCQS):
        h.append(mcq(r + ".", text, opts, fg))
    # fill in
    h.append('<div class="blk"><div class="part"><div class="lab">b)</div><div class="txt">Fill in the blanks by writing suitable word/s.</div><div class="mk">[5]</div></div>')
    h.append('<table class="tab">' + "".join(f'<tr><td style="width:12mm">{ROM[i]}.</td><td>{t}</td><td class="m"></td></tr>' for i, (t, a) in enumerate(FILL)) + "</table></div>")
    h.append('<div class="blk"><div class="part"><div class="lab">c)</div><div class="txt">State whether the following statements are <b>TRUE</b> or <b>FALSE</b>.</div><div class="mk">[5]</div></div>')
    h.append('<table class="tab">' + "".join(f'<tr><td style="width:12mm">{ROM[i]}.</td><td>{t}</td><td class="a"></td><td class="m"></td></tr>' for i, (t, a) in enumerate(TF)) + "</table></div>")
    h.append('<div class="blk"><div class="part"><div class="lab">d)</div><div class="txt">Match each item under <b>Column A</b> with the most appropriate item in <b>Column B</b>. Write the correct alphabet in the space provided under the ‘<b>ANSWER</b>’ column.</div><div class="mk">[5]</div></div>')
    rows = []
    for i in range(7):
        a = f'<td class="a" style="height:11mm">{ROM[i] + "." if i < 5 else ""}</td><td>{ROM[i] + ". " + MATCH_A[i] if i < 5 else ""}</td>'
        rows.append(f'<tr>{a}<td>{"abcdefg"[i]}. {MATCH_B[i]}</td><td class="m"></td></tr>')
    h.append('<table class="tab"><tr><th class="a" style="text-align:center">Answer</th><th style="text-align:center">Column A</th><th style="text-align:center">Column B</th><th class="m"></th></tr>' + "".join(rows) + "</table></div>")
    # section B
    h.append('<div style="break-before:page"></div><h2 class="sec">SECTION B [60 MARKS]</h2><div class="sub">ATTEMPT <b>ANY SIX</b> QUESTIONS</div>')
    for q, parts in QB.items():
        h.append(f'<div class="q" style="justify-content:flex-start;break-after:avoid"><span>Question {q}</span></div>')
        for (lab, text, marks, fig, bh, ans) in parts:
            h.append(part(lab, text, marks, fig, bh))
    h.append('<div class="rough">Rough Work</div>')
    h.append('<div class="rough" style="break-before:page">Rough Work</div>')
    return "<!doctype html><html><head><meta charset=utf-8><style>" + CSS + "</style></head><body>" + "".join(h) + "</body></html>"


def key_html():
    h = [f'<h2 class="sec">MARKING SCHEME &mdash; {CODE}</h2><div class="sub">Class X Physics &middot; Mock Paper (for self-checking)</div>', '<div class="key">']
    h.append('<h3>Section A &mdash; Q1(a) Multiple choice (1 mark each)</h3><table class="tab"><tr><th style="width:12mm">No.</th><th style="width:14mm">Answer</th><th>Reason</th></tr>')
    for r, (t, o, a, why, fg) in zip(ROM, MCQS):
        h.append(f"<tr><td>{r}.</td><td><b>{a}</b></td><td>{why}</td></tr>")
    h.append("</table>")
    h.append('<h3>Q1(b) Fill in the blanks (1 mark each)</h3><table class="tab">' + "".join(f"<tr><td style='width:12mm'>{ROM[i]}.</td><td><b>{a}</b></td></tr>" for i, (t, a) in enumerate(FILL)) + "</table>")
    h.append('<h3>Q1(c) True / False (1 mark each)</h3><table class="tab">' + "".join(f"<tr><td style='width:12mm'>{ROM[i]}.</td><td><b>{a}</b></td></tr>" for i, (t, a) in enumerate(TF)) + "</table>")
    h.append('<h3>Q1(d) Matching (1 mark each)</h3><table class="tab"><tr>' + "".join(f"<td>{ROM[i]}. &rarr; <b>{MATCH_ANS[i]}</b></td>" for i in range(5)) + "</tr></table>")
    h.append("<h3>Section B (10 marks per question)</h3>")
    for q, parts in QB.items():
        h.append(f"<h4>Question {q}</h4><table class='tab'><tr><th style='width:12mm'>Part</th><th style='width:12mm'>Marks</th><th>Answer and working</th></tr>")
        for (lab, text, marks, fig, bh, ans) in parts:
            h.append(f"<tr><td>{lab}</td><td>{marks}</td><td>{ans}</td></tr>")
        h.append("</table>")
    h.append('<p><b>Marking guide:</b> award marks for the correct formula, substitution and final answer with unit (for calculations: 1 mark for method, 1 mark for the answer with unit in 2-mark parts). Accept g = 9.8 m/s&sup2; with correspondingly adjusted answers.</p></div>')
    return "<!doctype html><html><head><meta charset=utf-8><style>" + CSS.replace('@bottom-left { content: "' + CODE + '\\A Copyright Reserved";', '@bottom-left { content: "' + CODE + ' - Marking scheme\\A Copyright Reserved";') + ".key h3{font-size:12pt;margin:5mm 0 1.5mm} .key h4{font-size:11pt;margin:4mm 0 1mm}</style></head><body>" + "".join(h) + "</body></html>"


def render(html_text, name):
    f = ROOT / f"{name}.html"
    f.write_text(html_text, encoding="utf-8")
    pdf = ROOT / f"{name}.pdf"
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{f}"], check=True, stderr=subprocess.DEVNULL)
    return pdf


if __name__ == "__main__":
    print(render(paper_html(), "BCSE_Physics_Mock_Paper"))
    print(render(key_html(), "BCSE_Physics_Mock_Marking_Scheme"))
