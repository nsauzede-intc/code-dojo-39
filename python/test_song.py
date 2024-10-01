import song

def test_song():
    assert song.song() == _EXPECTED_DEFAULT_SONG

def test_None_animals():
    assert song.song(None) == _EXPECTED_DEFAULT_SONG

def test_one_animal():
    assert song.song(["Wailord"]) == """There was an old lady who swallowed a Wailord...
...She's dead, of course!"""

def test_one_different_animal():
    assert song.song(["Foo"]) == """There was an old lady who swallowed a Foo...
...She's dead, of course!"""

def test_two_animal():
    assert song.song(["Gyarados", "Wailord"]) == """There was an old lady who swallowed a Gyarados.
I don't know why she swallowed a Gyarados - perhaps she'll die!

There was an old lady who swallowed a Wailord...
...She's dead, of course!"""

def test_three_animal():
    assert song.song(["Charizard", "Gyarados", "Wailord"]) == """There was an old lady who swallowed a Charizard.
I don't know why she swallowed a Charizard - perhaps she'll die!

There was an old lady who swallowed a Gyarados;
That wriggled and wiggled and tickled inside her.
She swallowed the Gyarados to catch the Charizard;
I don't know why she swallowed a Charizard - perhaps she'll die!

There was an old lady who swallowed a Wailord...
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
