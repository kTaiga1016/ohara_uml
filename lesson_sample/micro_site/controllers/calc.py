from utils import parse_post, render_template

def calc(environ):
    result = None
    method = environ["REQUEST_METHOD"]
    set_first_value = set_second_value = ""
    if method == "POST":
        data = parse_post(environ)
        set_first_value = data.get("a", [""])[0]
        set_second_value = data.get("b", [""])[0]
        try:
            result = int(set_first_value) + int(set_second_value)
        except Exception:
            result = "Invalid input"
    result_block = f"<p>答え: {result}</p>" if result is not None else ""
    return render_template(
        "boundaries/calc.html",
        set_first_value=set_first_value,
        set_second_value=set_second_value,
        result_block=result_block
    )