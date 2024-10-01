import song

def test_song():
    assert song.song() == _EXPECTED_DEFAULT_SONG

def test_None_animals():
    assert song.song(None) == _EXPECTED_DEFAULT_SONG

def test_one_animal():
    assert song.song(["6"]) == """There was an old lady who swallowed a 6...
...She's dead, of course!"""

def test_one_different_animal():
    assert song.song(["Foo"]) == """There was an old lady who swallowed a Foo...
...She's dead, of course!"""

def test_two_animal():
    assert song.song(["5", "6"]) == """There was an old lady who swallowed a 5.
I don't know why she swallowed a 5 - perhaps she'll die!

There was an old lady who swallowed a 6...
...She's dead, of course!"""

def test_three_animal():
    assert song.song(["4", "5", "6"]) == """There was an old lady who swallowed a 4.
I don't know why she swallowed a 4 - perhaps she'll die!

There was an old lady who swallowed a 5;
That wriggled and wiggled and tickled inside her.
She swallowed the 5 to catch the 4;
I don't know why she swallowed a 4 - perhaps she'll die!

There was an old lady who swallowed a 6...
...She's dead, of course!"""

def WIPtest_four_animal():
    assert song.song(["3", "4", "5", "6"]) == """There was an old lady who swallowed a 4.
I don't know why she swallowed a 4 - perhaps she'll die!

There was an old lady who swallowed a 5;
That wriggled and wiggled and tickled inside her.
She swallowed the 5 to catch the 4;
I don't know why she swallowed a 4 - perhaps she'll die!

There was an old lady who swallowed a 6...
...She's dead, of course!"""

def test_empty_list_of_animals():
    assert song.song([]) == ""

_EXPECTED_DEFAULT_SONG = """There was an old lady who swallowed a fly.
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a spider;
That wriggled and wiggled and tickled inside her.
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a horse...
...She's dead, of course!"""
