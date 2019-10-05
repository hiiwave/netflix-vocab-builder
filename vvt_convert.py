import click
from pathlib import Path
import re


@click.command()
@click.argument('vtt_files', nargs=-1)
@click.option('-o', '--output', default='converted.txt')
def cli(vtt_files, output):
    result = [transform(Path(v).read_text(errors='ignore')) for v in vtt_files]
    result = '\n\n'.join(result)
    Path(output).write_text(result)
    print('Created ' + output)


def transform(full_text: str) -> str:
    paragraphs = full_text.split('\n\n')
    ret = []
    for para in paragraphs[4:]:
        parsed = _parse_para(para)
        ret.append(parsed)
    ret = '\n'.join(ret)
    ret = remove_format(ret)
    return ret


def remove_format(s: str) -> str:
    """Remove the formatting tags
    
    >>> remove_format("<i>Baby, don't get hooked on me</i>")
    "Baby, don't get hooked on me"

    >>> remove_format('<c.white><c.mono_sans> SO NO ONE TOLD YOU</c.mono_sans></c.white>')
    'So no one told you'

    """
    for matched in re.findall(r'\<\/?[^<>]*\>', s):
        s = s.replace(matched, '')
    s = s.strip().capitalize()
    return s


def _parse_para(para: str) -> str:
    ret = '\n'.join(para.strip().split('\n')[2:])
    return ret


if __name__ == '__main__':
    cli()
