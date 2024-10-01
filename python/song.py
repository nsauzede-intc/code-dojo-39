def song(animals = None):
    if animals == None:
        return f"""{_INIT_PHRASE} fly.
I don't know why she swallowed a fly - perhaps she'll die!

{_INIT_PHRASE} spider;
That wriggled and wiggled and tickled inside her.
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

{_INIT_PHRASE} bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

{_INIT_PHRASE} cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

{_INIT_PHRASE} dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

{_INIT_PHRASE} cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

{_INIT_PHRASE} horse...
...She's dead, of course!"""
    else:
        song = ""

        if len(animals) == 0:
            return song
        
        if(len(animals) > 1):
            song += _get_first_paragraph(animals[0])

        song += _get_last_paragraph(animals[-1])

        return song

def _get_first_paragraph(animal):
    return f"""{_INIT_PHRASE} {animal}.
I don't know why she swallowed a {animal} - perhaps she'll die!

"""

def _get_last_paragraph(animal):
    return f"""{_INIT_PHRASE} {animal}...
...She's dead, of course!"""

_INIT_PHRASE = "There was an old lady who swallowed a"

def main():
    print(song())
