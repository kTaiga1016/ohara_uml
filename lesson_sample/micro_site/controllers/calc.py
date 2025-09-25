from utils import parse_post, render_template

def calc(environ):
    result = None
    method = environ["REQUEST_METHOD"]
    a = b = ""
    if method == "POST":
        data = parse_post(environ)
        a = data.get("a", [""])[0]
        b = data.get("b", [""])[0]
        try:
            result = int(a) + int(b)
        except Exception:
            result = "Invalid input"
    result_block = f"<p>答え: {result}</p>" if result is not None else ""
    return render_template(
        "boundaries/calc.html",
        a=a,
        b=b,
        result_block=result_block
    )