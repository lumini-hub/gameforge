"""Helpers shared by the ICT model-paper content files."""
import io, contextlib, html, builtins


def run(code, inputs=()):
    """Run a snippet of Python and return what it printed (used so answer keys are always right)."""
    it = iter(inputs)
    out = io.StringIO()
    env = {"__name__": "__main__"}
    real_input = builtins.input
    builtins.input = lambda prompt="": (print(prompt, end=""), next(it))[1]
    try:
        with contextlib.redirect_stdout(out):
            exec(code, env)
    finally:
        builtins.input = real_input
    return out.getvalue()


def code(s):
    """Format a code block for the question paper or key."""
    return '<pre class="code">' + html.escape(s.strip("\n")) + "</pre>"


def ic(s):
    return "<code>" + html.escape(s) + "</code>"


def out(s):
    """Output block for the answer key."""
    return '<pre class="code out">' + html.escape(s.rstrip("\n")) + "</pre>"


def xl(rows, widths=None, caption=""):
    """A spreadsheet picture: column letters, row numbers and cell values."""
    n = len(rows[0])
    letters = "ABCDEFGH"[:n]
    h = '<table class="xl"><tr><th></th>' + "".join(f"<th>{c}</th>" for c in letters) + "</tr>"
    for i, r in enumerate(rows, 1):
        cells = "".join(f"<td{' class=\"hd\"' if i == 1 else ''}>{html.escape(str(c)) if c != '' else '&nbsp;'}</td>" for c in r)
        h += f"<tr><th>{i}</th>{cells}</tr>"
    return h + "</table>"
