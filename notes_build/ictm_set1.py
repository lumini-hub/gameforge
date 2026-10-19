"""ICT Model Set 1: questions and answer key."""
from ictm_util import run, code, ic, out, xl
import ictm_figs as F

CODE = "BCSE/ICT/MODEL-1"

MARKS = xl([["Name", "Section", "Marks"], ["Pema", "A", 72], ["Sonam", "B", 58], ["Dechen", "A", 91], ["Karma", "B", 45], ["Tashi", "A", 66], ["Yangchen", "B", 80]])

C7 = '''x = 7
y = 2
print(x // y, x % y)'''
C8 = '''for i in range(2, 10, 3):
    print(i, end=" ")'''
C9 = '''n = 1
while n < 20:
    n = n * 2
    if n > 10:
        break
print(n)'''
C10 = '''s = "Thimphu"
print(s[1:4], s[-1])'''
C11 = '''marks = [40, 55, 70]
marks.append(85)
marks.pop(0)
print(len(marks), marks[0])'''
C12 = '''fruit = {"apple": 30, "pear": 45}
fruit["pear"] = 50
fruit["plum"] = 20
print(len(fruit), fruit["pear"])'''
C13 = '''def power(b, e=2):
    return b ** e
print(power(3), power(2, 3))'''
C14 = '''a = 5
b = 10
print(a > 3 and not b < 8)'''
C15 = '''def f(n):
    if n == 0:
        return 1
    return n * f(n - 1)
print(f(4))'''
for c, a in ((C7, "3 1"), (C8, "2 5 8 "), (C9, "16"), (C10, "him u"), (C11, "3 55"), (C12, "3 50"), (C13, "9 8"), (C14, "True"), (C15, "24")):
    assert run(c).strip() == a.strip(), (c, run(c))

# (question, [A,B,C,D], answer letter, reason, figure)
MCQS = [
 ("Which of the following is an example of Software as a Service (SaaS)?", ["Google Docs", "Amazon EC2 virtual server", "Google App Engine", "A school&rsquo;s own data centre"], "A", "Google Docs is software used through a browser: SaaS. EC2 is IaaS and App Engine is PaaS.", ""),
 ("A school keeps student records on a cloud that only the school can use, hosted in its own building. This is a", ["public cloud.", "private cloud.", "hybrid cloud.", "community cloud."], "B", "A cloud used by one organisation only is a private cloud.", ""),
 ("A photograph is shared under the Creative Commons licence <b>CC BY-ND</b>. You are allowed to", ["change the photograph and claim it as your own.", "share the photograph unchanged and give credit to the creator.", "sell edited copies without credit.", "use it only if you pay the creator."], "B", "BY = give credit; ND = no derivatives, so it can be shared but not changed.", ""),
 ("Which is the correct APA 7 in-text citation for a <b>direct quotation</b> from page 14 of a 2022 work by Dorji?", ["(Dorji, 2022, p. 14)", "(Dorji 2022 14)", "(2022, Dorji, p.14)", "Dorji (p. 14, 2022)"], "A", "APA 7 direct quote: (Author, year, p. page).", ""),
 ("Study the spreadsheet. What is the result of <code>=SUMIF(B2:B7,&quot;B&quot;,C2:C7)</code>?", ["183", "209", "133", "3"], "A", "Section B marks are 58 + 45 + 80 = 183.", MARKS),
 ("Which chart is the most suitable to show the <b>share</b> of each subject in a student&rsquo;s total marks?", ["Pie chart", "Line chart", "Scatter plot", "Histogram"], "A", "A pie chart shows parts of a whole.", ""),
 ("What is the output of the program?" + code(C7), ["3.5 1", "3 1", "3 3.5", "4 1"], "B", "7 // 2 = 3 (floor division) and 7 % 2 = 1 (remainder).", ""),
 ("What is the output of the program?" + code(C8), ["2 5 8", "2 5 8 11", "3 6 9", "2 3 4 5 6 7 8 9"], "A", "range(2, 10, 3) gives 2, 5, 8.", ""),
 ("What is printed by the program?" + code(C9), ["8", "10", "16", "32"], "C", "n becomes 2, 4, 8, 16; 16 &gt; 10 so the loop breaks and 16 is printed.", ""),
 ("What is the output of the program?" + code(C10), ["Thi u", "him u", "him p", "hi u"], "B", "s[1:4] = &ldquo;him&rdquo; (indexes 1, 2, 3); s[-1] = &ldquo;u&rdquo;.", ""),
 ("What is the output of the program?" + code(C11), ["4 40", "3 55", "3 40", "4 55"], "B", "After append the list has 4 items; pop(0) removes 40, leaving [55, 70, 85].", ""),
 ("What is the output of the program?" + code(C12), ["2 45", "3 45", "3 50", "2 50"], "C", "pear is changed to 50 and plum is added, so there are 3 keys.", ""),
 ("What is the output of the program?" + code(C13), ["9 8", "9 6", "6 8", "3 3"], "A", "power(3) uses e = 2 &rarr; 9; power(2, 3) = 2<sup>3</sup> = 8.", ""),
 ("What does the following print?" + code(C14), ["True", "False", "Error", "None"], "A", "a &gt; 3 is True; b &lt; 8 is False, so not False is True; True and True = True.", ""),
 ("What is the output of the program?" + code(C15), ["10", "12", "24", "120"], "C", "f(4) = 4 &times; 3 &times; 2 &times; 1 &times; f(0) = 24.", ""),
]

FILL = [
 ("______ as a Service (IaaS) gives users virtual servers, storage and networks on rent.", "Infrastructure"),
 ("In an APA reference list the entries are arranged in ______ order of the authors&rsquo; surnames.", "alphabetical"),
 ("The built-in Python function that returns the number of items in a list is ______.", "len()"),
 ("A ______ is an unordered collection of unique items written inside curly brackets.", "set"),
 ("The keyword used to skip the rest of the current loop turn and go to the next turn is ______.", "continue"),
]
TF = [
 ("Data saved in the cloud can be opened from any device that has an internet connection.", "TRUE"),
 ("The items of a tuple can be changed after the tuple is created.", "FALSE"),
 ("Using a protected photograph without permission or credit when its licence does not allow it is copyright infringement.", "TRUE"),
 ("In a flowchart, a parallelogram is used for input and output.", "TRUE"),
 ("The Excel formula =AVERAGE(B2:B7) only adds the values and does not divide.", "FALSE"),
]

SHEET2 = xl([["Code", "Item", "Price (Nu)", "Qty sold", "Amount (Nu)"], [101, "Notebook", 30, 12, ""], [102, "Pen", 10, 40, ""], [103, "Ruler", 15, 8, ""], [104, "Bag", 450, 2, ""], ["", "Total", "", "", ""]])

D3 = '''total = 0
for n in range(1, 8):
    if n % 3 == 0:
        continue
    total += n
print("Total:", total)'''
A3 = run(D3)
assert A3.strip() == "Total: 19"

S4A = '''word = "Bhutan Today"
print(word.upper())
print(word[0:6])
print(len(word))
print(word.replace("Today", "Now"))'''
S4B = '''colours = ["red", "green", "blue"]
colours.insert(1, "yellow")
colours.remove("blue")
colours.sort()
print(colours)'''
S4C = '''a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a & b)
print(a | b)'''

F5C = '''def total(n):
    if n == 1:
        return 1
    return n + total(n - 1)
print(total(4))'''

Q6C = '''total = 0
i = 1
while i <= 9:
    total = total + i
    i = i + 2
print(total)'''
assert run(Q6C).strip() == "25"

Q7 = '''n = int(input("Number of books borrowed (1-5): "))
while n < 1 or n > 5:
    print("Invalid. Enter a number from 1 to 5.")
    n = int(input("Number of books borrowed (1-5): "))

fines = []
for i in range(1, n + 1):
    days = int(input("Days kept for book " + str(i) + ": "))
    if days > 14:
        fine = (days - 14) * 2
    else:
        fine = 0
    fines.append(fine)

total = 0
for i in range(len(fines)):
    print("Book", i + 1, "fine: Nu", fines[i])
    total = total + fines[i]

if total == 0:
    print("No fine to pay")
else:
    print("Total fine: Nu", total)'''
TEST7 = run(Q7, ["7", "3", "10", "20", "15"])
assert "Total fine: Nu 14" in TEST7, TEST7

QB = {
 2: [
  ("a)", "Name the <b>three</b> cloud service models and give one example of each.", 3, "", 28,
   "IaaS &ndash; Infrastructure as a Service, e.g. Amazon EC2 / virtual servers [1]; PaaS &ndash; Platform as a Service, e.g. Google App Engine [1]; SaaS &ndash; Software as a Service, e.g. Google Docs, Gmail [1]. (Accept any correct example.)"),
  ("b)", "Explain <b>two</b> ways in which a class can benefit from using Google Docs or Google Slides for a group project.", 2, "", 24,
   "Any two, 1 mark each: several students can edit the same file <b>at the same time</b> from different places; changes are <b>saved automatically</b> and the version history lets them go back; <b>comments and suggestions</b> let members give feedback; the file can be <b>shared by link</b> with view/comment/edit rights; no need to email copies."),
  ("c)", "The sheet below records the sales of a school shop. Write the Excel formula or function for each.<br>" + SHEET2 +
         "<br>(i) the amount in <b>E2</b> (price &times; quantity sold) <br>(ii) the total of the Amount column in <b>E6</b><br>(iii) the price of the item with code 103, using VLOOKUP <br>(iv) the largest quantity sold", 4, "", 38,
   "(i) <code>=C2*D2</code> (= 360) [1]; (ii) <code>=SUM(E2:E5)</code> (= 1780) [1]; (iii) <code>=VLOOKUP(103,A2:C5,3,FALSE)</code> (= 15) [1]; (iv) <code>=MAX(D2:D5)</code> (= 40) [1]. Amounts: 360, 400, 120, 900."),
  ("d)", "Which chart would you choose to show the <b>amount</b> earned from each item, and why?", 1, "", 16,
   "Column (bar) chart [&frac12;]: it lets the amounts of the four items be compared easily [&frac12;]. (A pie chart is also accepted if the reason is given.)"),
 ],
 3: [
  ("a)", "Define <b>plagiarism</b>. Write <b>two</b> ways to avoid it.", 3, "", 28,
   "Plagiarism is using another person&rsquo;s words, ideas or work and presenting it as your own without giving credit [1]. Avoid it by: writing in your own words and <b>citing the source</b> [1]; putting quotation marks around copied words and adding a reference list [1]; asking permission / using work with a suitable licence."),
  ("b)", "What do the Creative Commons symbols <b>BY</b> and <b>NC</b> mean?", 2, "", 18,
   "BY (Attribution) &ndash; users must give credit to the creator [1]. NC (Non-Commercial) &ndash; the work may not be used for profit [1]."),
  ("c)", "Write the Python <b>data type</b> of each value: (i) <code>17</code> &nbsp; (ii) <code>3.14</code> &nbsp; (iii) <code>&quot;Bhutan&quot;</code> &nbsp; (iv) <code>False</code>", 2, "", 16,
   "(i) int  (ii) float  (iii) str (string)  (iv) bool (Boolean) &mdash; &frac12; mark each."),
  ("d)", "Write the output of the program and show how the value of <code>total</code> changes.<br>" + code(D3), 3, "", 40,
   "n takes 1, 2, 3, 4, 5, 6, 7. Multiples of 3 (3 and 6) are skipped by <code>continue</code>. total = 1 &rarr; 3 &rarr; 7 &rarr; 12 &rarr; 19 [2]. Output: " + out(A3) + "[1]"),
 ],
 4: [
  ("a)", "Write the output of each <code>print</code> statement.<br>" + code(S4A), 4, "", 30,
   "Output [1 each]:" + out(run(S4A))),
  ("b)", "Write the output of the program.<br>" + code(S4B), 3, "", 22,
   "insert &rarr; ['red', 'yellow', 'green', 'blue']; remove &rarr; ['red', 'yellow', 'green']; sort &rarr; alphabetical [2]. Output:" + out(run(S4B)) + "[1]"),
  ("c)", "Write the output of the first two <code>print</code> statements. Then say what happens when <code>t[1] = 25</code> is executed for the tuple <code>t = (10, 20, 30)</code>.<br>" + code(S4C), 3, "", 28,
   "a &amp; b is the intersection and a | b is the union: " + out(run(S4C)) + "[2] <code>t[1] = 25</code> gives a <b>TypeError</b> because a tuple is immutable (its items cannot be changed) [1]."),
 ],
 5: [
  ("a)", "Differentiate between a <b>parameter</b> and an <b>argument</b>.", 2, "", 22,
   "A parameter is the variable named in the function definition (<code>def area(l, w)</code>) [1]; an argument is the actual value passed when the function is called (<code>area(5, 3)</code>) [1]."),
  ("b)", "Write a function <code>grade(marks)</code> that <b>returns</b> &ldquo;Distinction&rdquo; if marks are 75 or more, &ldquo;Pass&rdquo; if marks are 40 to 74, and &ldquo;Fail&rdquo; otherwise.", 4, "", 52,
   code('''def grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"''') + "def line and colon [1]; first condition and return [1]; elif for 40&ndash;74 [1]; else Fail [1]."),
  ("c)", "Trace the recursive function and write its output.<br>" + code(F5C), 3, "", 30,
   "total(4) = 4 + total(3) = 4 + (3 + total(2)) = 4 + 3 + (2 + total(1)) = 4 + 3 + 2 + 1 [2]. Output: <b>10</b> [1]."),
  ("d)", "Why must every recursive function have a <b>base case</b>?", 1, "", 16,
   "The base case is the condition that stops the function from calling itself; without it the recursion never ends and causes a RecursionError (stack overflow) [1]."),
 ],
 6: [
  ("a)", "Name the flowchart symbol used for (i) start or stop, (ii) a decision, (iii) input or output, (iv) a process.", 2, "", 20,
   "(i) terminator / oval (rounded rectangle); (ii) diamond; (iii) parallelogram; (iv) rectangle &mdash; &frac12; mark each."),
  ("b)", "Study the flowchart. What is printed at the end?", 2, F.fig_sum_odd(), 14,
   "sum = 0, i = 1: i = 1, 3, 5, 7, 9 are added (the loop stops when i = 11): 1 + 3 + 5 + 7 + 9 = <b>25</b> [2]."),
  ("c)", "Write a Python program for the flowchart using a <code>while</code> loop.", 3, "", 36,
   code(Q6C) + "initialise sum and i [1]; <code>while i &lt;= 9</code> with the two updates inside [1]; <code>print(total)</code> after the loop [1]."),
  ("d)", "Give the result (True or False) of: (i) <code>8 &gt; 5 and 3 &gt; 7</code> &nbsp; (ii) <code>not (4 == 4) or 2 &lt; 3</code> &nbsp; (iii) <code>10 % 3 == 1</code>", 3, "", 18,
   "(i) False (True and False); (ii) True (False or True); (iii) True (10 % 3 = 1) &mdash; 1 mark each."),
 ],
 7: [
  ("", "A school library charges a late fine of <b>Nu 2 per day</b> for every day a book is kept for <b>more than 14 days</b>. Write a Python program that:<br>(a) asks for the number of books borrowed and keeps asking until the number is from 1 to 5 [3]<br>(b) for each book, asks for the days kept, calculates the fine and stores the fines in a list [4]<br>(c) prints the fine for each book, then the total fine, or &ldquo;No fine to pay&rdquo; if the total is 0 [3]", 10, "", 130,
   code(Q7) + "Sample run (inputs 7, 3, 10, 20, 15): " + out(TEST7) +
   "Marking: (a) input and conversion to int [1], while loop with the condition <code>n &lt; 1 or n &gt; 5</code> [1], message and re-input [1]. (b) empty list [1], for loop over the books [1], correct fine <code>(days - 14) * 2</code> only when days &gt; 14 [1], append to list [1]. (c) loop to print each fine [1], total [1], if/else for &ldquo;No fine&rdquo; [1]. Accept any correct program."),
 ],
}
