from madlib_cli import __version__
from madlib_cli.madlib import *
import os.path

def test_version():
    assert __version__ == '0.1.0'


def test_read_template():
    madlib('/home/emad/madlib-cli/madlib_cli/madlib_template.txt', 'y')
    with open('/home/emad/madlib-cli/madlib_cli/madlib_template_result.txt','r') as c:
        line_test = c.read()
        assert line_test == "Make Me A Video Game!\n\nI the  and   have 's  sister and plan to steal her  !\n\nWhat are a  and backpacking  to do? Before you can help , you'll have to collect the   and   that open up the  worlds connected to A  Lair. There are   and   in the game, along with hundreds of other goodies for you to find."
    assert os.path.exists('/home/emad/madlib-cli/madlib_cli/madlib_template_result.txt')


def test_parse():
    madlib('/home/emad/madlib-cli/madlib_cli/madlib_template.txt', 'y')
    assert "Make Me A Video Game!\n\nI the  and   have 's  sister and plan to steal her  !\n\nWhat are a  and backpacking  to do? Before you can help , you'll have to collect the   and   that open up the  worlds connected to A  Lair. There are   and   in the game, along with hundreds of other goodies for you to find."


def test_merge():
    actual = madlib(['game','name','sily','badly','go','sleep','tea','play','write','do','samer','ssd','world','ball','fan','sing','play','wrote','pay','nice','eminem','concare'])
    expected = "Make Me A Video Game!\n\nI the game and name sily have badlygo's sleep sister and plan to steal her tea play!\n\nWhat are a write and backpacking do to do? Before you can help samer, you'll have to collect the ssd world and ball fan that open up the sing worlds connected to A play Lair. There are wrote pay and nice eminem in the game, along with hundreds of other goodies for you to find."
    assert actual == expected