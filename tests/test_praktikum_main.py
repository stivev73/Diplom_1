import runpy


def test_main_module_entrypoint(capsys):
    runpy.run_module("praktikum.praktikum", run_name="__main__")
    out = capsys.readouterr().out
    assert "Price:" in out
