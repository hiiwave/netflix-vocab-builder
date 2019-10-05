from vvt_convert import cli, convert
from click.testing import CliRunner
from pathlib import Path


def test_cli():
    sample_vtt = (Path(__file__).parent / 'sample1.vtt').as_posix()
    print(sample_vtt)
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, [sample_vtt])
        assert result.exit_code == 0
        assert result.output == 'Created converted.txt\n'
        assert Path('converted.txt').exists()


def test_convert():
    textin = (Path(__file__).parent / 'sample1.vtt').read_text(errors='ignore')
    textout = (Path(__file__).parent / 'converted1.txt').read_text(errors='ignore')
    assert convert(textin) == textout