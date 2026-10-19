"""ICT Model Set 2: questions and answer key."""
from ictm_util import run, code, ic, out, xl
import ictm_figs as F

CODE = "BCSE/ICT/MODEL-2"

SC = xl([["Student", "Marks"], ["Dema", 40], ["Kinley", 60], ["Lhamo", 80], ["Jigme", 20]])

C7 = "print(2 ** 3 + 10 % 4)"
C8 = '''for i in range(3):
    for j in range(2):
        print("*", end="")
    print()'''
C9 = '''count = 0
while count < 3:
    print(count, end=" ")
    count += 1'''
C10 = '''name = "karma dorji"
print(name.title())'''
C11 = '''nums = [5, 10, 15, 20, 25]
print(nums[-3:])'''
C12 = '''s = {1, 2, 2, 3, 3, 3}
print(len(s))'''
C13 = '''d = {"x": 10, "y": 20}
print(d.get("z", 0))'''
C14 = '''def sq(n):
    return n * n
print(sq(sq(2)))'''
for c, a in ((C7, "10"), (C8, "**\n**\n**"), (C9, "0 1 2"), (C10, "Karma Dorji"), (C11, "[15, 20, 25]"), (C12, "3"), (C13, "0"), (C14, "16")):
    assert run(c).strip() == a, (c, run(c))

# (question, [A,B,C,D], answer letter, reason, figure)
MCQS = [
 ("A cloud that combines a private cloud with a public cloud is called a", ["hybrid cloud.", "personal cloud.", "local cloud.", "closed cloud."], "A", "Private + public = hybrid cloud.", ""),
 ("Which Google Workspace tool is the best for collecting answers to a class survey online?", ["Google Slides", "Google Forms", "Google Calendar", "Google Meet"], "B", "Google Forms makes online surveys and records the responses in a sheet.", ""),
 ("Which Creative Commons licence lets others change and share your work, but only if the new work uses the <b>same licence</b>?", ["CC BY-ND", "CC BY-NC", "CC BY-SA", "CC0"], "C", "SA = ShareAlike: derivative works must carry the same licence.", ""),
 ("Which is the correct APA 7 reference for a book? (Italics are not shown.)", ["Wangchuk, T. (2020). Rivers of the Himalaya. Royal Press.", "Tenzin Wangchuk, 2020, Rivers Of The Himalaya, Royal Press", "(2020) Wangchuk T. Rivers of the Himalaya: Royal Press", "Rivers of the Himalaya. Wangchuk, T. Royal Press. 2020."], "A", "APA 7: Surname, Initial. (Year). Title in sentence case. Publisher.", ""),
 ("Study the sheet. What is the value of <code>=AVERAGE(B2:B5)</code>?", ["40", "50", "60", "200"], "B", "(40 + 60 + 80 + 20) &divide; 4 = 50.", SC),
 ("Which chart is the best to show how one student&rsquo;s marks <b>changed over five exams</b>?", ["Pie chart", "Line chart", "Column chart of one exam", "Table only"], "B", "A line chart shows a trend over time.", ""),
 ("What is the value printed by this statement?" + code(C7), ["8", "9", "10", "14"], "C", "2 ** 3 = 8 and 10 % 4 = 2, so 8 + 2 = 10.", ""),
 ("Which output does this program produce?" + code(C8), ["One row of six stars", "Three rows, each with two stars", "Two rows, each with three stars", "Six rows, each with one star"], "B", "The outer loop runs 3 times; each time the inner loop prints 2 stars, then print() starts a new line.", ""),
 ("What is the output of the program?" + code(C9), ["0 1 2", "1 2 3", "0 1 2 3", "3"], "A", "count = 0, 1, 2 are printed; when count becomes 3 the condition is false.", ""),
 ("What is the output of the program?" + code(C10), ["karma dorji", "KARMA DORJI", "Karma Dorji", "Karma dorji"], "C", "title() makes the first letter of every word a capital.", ""),
 ("What is the output of the program?" + code(C11), ["[5, 10, 15]", "[15, 20, 25]", "[10, 15, 20]", "[20, 25]"], "B", "nums[-3:] takes the last three items.", ""),
 ("What is the output of the program?" + code(C12), ["6", "5", "3", "2"], "C", "A set keeps only unique values: {1, 2, 3}.", ""),
 ("What is the output of the program?" + code(C13), ["Error", "None", "0", "20"], "C", "The key &ldquo;z&rdquo; is missing, so get() returns the default value 0.", ""),
 ("What is the output of the program?" + code(C14), ["4", "8", "16", "32"], "C", "sq(2) = 4, then sq(4) = 16.", ""),
 ("Which loop correctly draws a square with the turtle <code>t</code>?", ["for i in range(4): t.forward(100); t.left(90)", "for i in range(3): t.forward(100); t.left(90)", "for i in range(4): t.forward(100); t.left(60)", "for i in range(5): t.forward(100); t.left(72)"], "A", "A square has 4 equal sides and 90&deg; turns.", ""),
]

FILL = [
 ("In a ______ cloud, resources are owned by a provider and shared among many users over the internet.", "public"),
 ("The Excel function that counts the cells that meet a given condition is ______.", "COUNTIF"),
 ("The Python keyword used to define a function is ______.", "def"),
 ("The ______ statement is used to leave a loop immediately.", "break"),
 ("A ______ in Python stores data as key&ndash;value pairs.", "dictionary"),
]
TF = [
 ("Google Forms can be used to collect responses online.", "TRUE"),
 ("A work in the public domain can be used freely without permission.", "TRUE"),
 ("In Python the index of the first item of a list is 1.", "FALSE"),
 ("A set can store duplicate values.", "FALSE"),
 ("A recursive function must have a base case.", "TRUE"),
]

SHEET = xl([["Name", "English", "Maths", "Total", "Result"], ["Dema", 62, 70, "", ""], ["Kinley", 35, 48, "", ""], ["Lhamo", 80, 91, "", ""], ["Jigme", 55, 40, "", ""]])

D3C = '''for i in range(1, 4):
    for j in range(i):
        print(i, end=" ")
    print()'''
S4A = '''stock = {"rice": 20, "dal": 12}
stock["oil"] = 8
stock["rice"] -= 5
del stock["dal"]
print(stock)
print(len(stock))'''
S4B = '''text = "python programming"
print(text.count("g"))
print(text.find("pro"))
print(text[::-1])'''
S4C = '''A = {2, 4, 6, 8}
B = {4, 8, 10}
print(A | B)
print(A & B)
print(A - B)'''
F5B = '''def mystery(a, b=3):
    return a * b + 1
print(mystery(2))
print(mystery(2, 5))
print(mystery(b=4, a=1))'''
assert run(F5B).split() == ["7", "11", "5"]
Q6B = '''import turtle
t = turtle.Turtle()
for i in range(___):
    t.forward(___)
    t.right(___)'''
Q6A = '''n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")'''
assert run(Q6A, ["-5"]).endswith("Negative\n")
Q5C = '''def sum_to(n):
    if n == 1:
        return 1
    return n + sum_to(n - 1)

print(sum_to(5))'''
assert run(Q5C).strip() == "15"
Q5A = '''def interest(p, r, t):
    return p * r * t / 100

print(interest(5000, 8, 2))'''
assert run(Q5A).strip() == "800.0"

Q7 = '''menu = {"momo": 60, "tea": 15, "noodles": 80, "juice": 30}
total = 0

print("Menu:", list(menu.keys()))
item = input("Enter item (or done): ").lower()
while item != "done":
    if item in menu:
        qty = int(input("Quantity: "))
        while qty <= 0:
            qty = int(input("Quantity must be positive. Quantity: "))
        total = total + menu[item] * qty
    else:
        print("Item not on the menu")
    item = input("Enter item (or done): ").lower()

discount = 0
if total > 200:
    discount = total * 10 / 100

print("Total:", total)
print("Discount:", discount)
print("Amount to pay:", total - discount)'''
TEST7 = run(Q7, ["momo", "3", "pizza", "tea", "0", "2", "done"])
assert "Amount to pay: 189.0" in TEST7 or "Amount to pay: 189" in TEST7, TEST7

QB = {
 2: [
  ("a)", "Differentiate between a <b>public cloud</b> and a <b>private cloud</b> on <b>two</b> points.", 3, "", 28,
   "Any two points [1&frac12; each]: owner &ndash; public: a provider (e.g. Google, Amazon); private: one organisation. Users &ndash; public: many users share the resources; private: only that organisation. Cost &ndash; public: pay for what is used, cheap to start; private: costly to set up and maintain. Security/control &ndash; private gives more control; public less."),
  ("b)", "State <b>one</b> risk of storing data in the cloud and one way of reducing it.", 2, "", 22,
   "Risk [1]: data can be hacked or leaked / service may be unavailable without internet / provider may lose data. Reduction [1]: use strong passwords and two-step verification / keep a backup copy / set correct sharing permissions."),
  ("c)", "Study the sheet. Total = English + Maths. The result is &ldquo;Pass&rdquo; when the total is 100 or more, otherwise &ldquo;Fail&rdquo;.<br>" + SHEET + "<br>Write the Excel formula for (i) <b>D2</b>; (ii) <b>E2</b> using IF; (iii) the highest English mark; (iv) the number of students who passed (use the Result column).", 5, "", 40,
   "(i) <code>=B2+C2</code> [1]; (ii) <code>=IF(D2&gt;=100,&quot;Pass&quot;,&quot;Fail&quot;)</code> [2: IF with condition 1, both results 1]; (iii) <code>=MAX(B2:B5)</code> [1]; (iv) <code>=COUNTIF(E2:E5,&quot;Pass&quot;)</code> [1] = 2 (Dema 132 and Lhamo 171 pass; Kinley 83 and Jigme 95 fail)."),
 ],
 3: [
  ("a)", "Write the APA 7 reference for this book: author <b>Karma Phuntsho</b>; year <b>2013</b>; title <b>The History of Bhutan</b>; publisher <b>Random House India</b>.", 3, "", 20,
   "Phuntsho, K. (2013). <i>The history of Bhutan</i>. Random House India. &mdash; surname and initial [1]; year in brackets [1]; title in italics and sentence case, then publisher [1]."),
  ("b)", "Explain <b>two</b> responsibilities of a good digital citizen.", 2, "", 22,
   "Any two [1 each]: be respectful and kind online (no cyber-bullying); protect your privacy and passwords; give credit and avoid plagiarism; check facts before sharing; follow copyright and licence rules; do not share others&rsquo; photos without permission."),
  ("c)", "Write the output of the program.<br>" + code(D3C), 3, "", 28,
   "The outer loop gives i = 1, 2, 3 and the inner loop prints i exactly i times on the same line [2]. Output [1]:" + out(run(D3C).replace(" \n", " \n"))),
  ("d)", "State the difference between the <code>break</code> and <code>continue</code> statements.", 2, "", 22,
   "<code>break</code> ends the whole loop at once and the program goes to the next statement after the loop [1]. <code>continue</code> skips the rest of the current turn only and starts the next turn of the loop [1]."),
 ],
 4: [
  ("a)", "Write the output of the program.<br>" + code(S4A), 4, "", 26,
   "rice becomes 15 (20 &minus; 5), oil is added, dal is deleted [2]. Output [2]:" + out(run(S4A))),
  ("b)", "Write the output of each <code>print</code> statement.<br>" + code(S4B), 3, "", 22,
   "count(&ldquo;g&rdquo;) = 2 [1]; find(&ldquo;pro&rdquo;) = 7 (the index where &ldquo;pro&rdquo; starts in &ldquo;programming&rdquo;) [1]; reversed text [1]:" + out(run(S4B))),
  ("c)", "Write the output of the program.<br>" + code(S4C), 3, "", 22,
   "Union, intersection, difference [1 each]:" + out(run(S4C))),
 ],
 5: [
  ("a)", "Write a function <code>interest(p, r, t)</code> that <b>returns</b> the simple interest (p &times; r &times; t &divide; 100). Then show a statement that calls it to print the interest on Nu 5000 at 8% for 2 years.", 3, "", 36,
   code(Q5A) + "def with 3 parameters [1]; correct return expression [1]; correct call/print (800.0) [1]."),
  ("b)", "Write the output of the program.<br>" + code(F5B), 3, "", 22,
   "mystery(2) = 2 &times; 3 + 1 = 7; mystery(2, 5) = 2 &times; 5 + 1 = 11; mystery(b=4, a=1) = 1 &times; 4 + 1 = 5. Output (1 mark each):" + out(run(F5B))),
  ("c)", "Write a <b>recursive</b> function <code>sum_to(n)</code> that returns the sum of the first n natural numbers (1 + 2 + &hellip; + n). Show the call for n = 5 and its output.", 4, "", 44,
   code(Q5C) + "base case n == 1 [1]; recursive call with n &minus; 1 [1]; adding n to the call [1]; output 15 [1]."),
 ],
 6: [
  ("a)", "Study the flowchart. (i) What is printed when <i>n</i> = 7, &minus;3 and 0? (ii) Write the Python program for the flowchart using <code>if &ndash; elif &ndash; else</code>.", 6, F.fig_sign(), 50,
   "(i) 7 &rarr; Positive; &minus;3 &rarr; Negative; 0 &rarr; Zero [2]. (ii)" + code(Q6A) + "input with int [1]; if n &gt; 0 [1]; elif n &lt; 0 [1]; else Zero [1]."),
  ("b)", "Complete the program so that the turtle draws a regular pentagon with sides of 80 steps.<br>" + code(Q6B), 2, "", 16,
   "range(<b>5</b>), forward(<b>80</b>), right(<b>72</b>) &mdash; a pentagon has 5 sides and the exterior angle is 360 &divide; 5 = 72&deg; [&frac12;, &frac12;, 1]."),
  ("c)", "Give the result of: (i) <code>not True or False</code> &nbsp; (ii) <code>(5 &gt; 2) and (4 &lt; 1)</code> &nbsp; (iii) <code>7 % 2 == 1 or 1 &gt; 2</code>", 2, "", 16,
   "(i) False; (ii) False; (iii) True. [1 for two correct, 2 for all three]"),
 ],
 7: [
  ("", "A school canteen keeps its menu in a <b>dictionary</b>: momo Nu 60, tea Nu 15, noodles Nu 80, juice Nu 30. Write a Python program that:<br>(a) stores the menu in a dictionary [2]<br>(b) repeatedly asks for the item (type <i>done</i> to stop); if the item is in the menu, asks for the quantity (must be above 0) and adds the cost to the total, otherwise prints &ldquo;Item not on the menu&rdquo; [5]<br>(c) gives a <b>10% discount</b> if the total is more than Nu 200 [1]<br>(d) prints the total, the discount and the amount to pay [2]", 10, "", 135,
   code(Q7) + "Sample run (inputs momo, 3, pizza, tea, 0, 2, done): " + out(TEST7) +
   "Marking: (a) dictionary with 4 correct pairs [2]. (b) while loop until &ldquo;done&rdquo; [1], <code>in menu</code> test [1], quantity validation [1], cost = price &times; quantity added to total [1], else message [1]. (c) if total &gt; 200 then 10% [1]. (d) three correct prints [2]. Accept any correct program."),
 ],
}
