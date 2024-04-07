
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def inform_error(msg):
    console.print(msg, style='bold red on black')

def greeting(msg):
    md = Markdown(msg)
    console.print(md)


def ask(msg, justify='left', width=None):
    if width is None: width = len(msg)
    # console.print(msg, justify=justify, width=width, end=' ')
    msg = msg.ljust(width)
    answer = console.input(f"[bold]{msg}[/] >> ").strip()
    return answer


def ask4int(msg, justify='left', width=None, default=None):
    answer = ask(msg, justify=justify, width=width)
    result = None
    if not answer.isdigit():
        if ask4YesOrNo("A resposta deve ser um número intereiro. Deseja repetir?"):
            answer = ask4int(msg, justify=justify, width=width)
    try:
        result = int(answer)
    except ValueError:
        inform_error(f"Não foi possível entender a sua resposta: {answer}")
        if type(default, int):
            result = default
    return result


def ask4float(msg, justify='left', width=None):
    answer = ask(msg, justify=justify, width=width)
    result = None
    try:
        result = float(answer)
    except ValueError:
        inform_error(f"Não foi possível entender a sua resposta: {answer}")
    return result


def ask4option(msg, options, default=None, justify='left', width=None):
    finalmsg = f"**{msg}**\n"
    if not isinstance(options, (list, tuple)):
        raise TypeError("Options must be a list or tuple")

    for i, t in enumerate(options, start=1):
        finalmsg += f"{i}. {t}\n"

    md = Markdown(finalmsg)
    console.print(md)
    answer = ask("", justify=justify, width=width)

    if answer in options:
        return answer
    elif answer.isdigit():
        index = int(answer) - 1
        if index >= 0 and index < len(options):
            return options[index]

    inform_error(f"Não foi possível entender a sua resposta: {answer}")


def ask4YesOrNo(msg, default=False, justify='left', width=None):
    answer = ask(f"{msg}\n[s\\n]",justify=justify, width=width)
    positive = {'yes', 'y', '1', 'yep', 'sim', 's'}
    negative = {'no', 'not', "don't", '0', '2', 'nao', 'não', 'n'}
    if answer.lower() in positive:
        return True
    elif answer.lower() in negative:
        return False
    else:
        inform_error(f"Não foi possível entender a sua resposta: {answer}")

    return default


def ask4date(msg, default=None, justify='left', width=None):
    answer = ask(msg, justify=justify, width=width)
    return answer