def song(animals = None):
    if animals == None:
        return f"""{_INIT_PHRASE} fly.
{_get_recurrent_question("fly")}

{_INIT_PHRASE} spider;
{_WIGGLE_PHRASE}
She swallowed the spider to catch the fly;
{_get_recurrent_question("fly")}

{_INIT_PHRASE} bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
{_get_recurrent_question("fly")}

{_INIT_PHRASE} cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
{_get_recurrent_question("fly")}

{_INIT_PHRASE} dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
{_get_recurrent_question("fly")}

{_INIT_PHRASE} cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
{_get_recurrent_question("fly")}

{_INIT_PHRASE} horse...
{_END_PHRASE}"""
    else:
        song = ""

        if len(animals) == 0:
            return song
        
        if(len(animals) > 1):
            song += _get_first_paragraph(animals[0])

        previous_animal = animals[0]
        for animal in animals[1:-1]:
            song += _get_middle_paragraph(previous_animal, animal)
            previous_animal = animal

        song += _get_last_paragraph(animals[-1])

        return song

def _get_first_paragraph(animal):
    return f"""{_INIT_PHRASE} {animal}.
{_get_recurrent_question(animal)}

"""

def _get_middle_paragraph(previous_animal, animal):
    return f"""{_INIT_PHRASE} {animal};
{_WIGGLE_PHRASE}
She swallowed the {animal} to catch the {previous_animal};
{_get_recurrent_question(previous_animal)}

"""

def _get_last_paragraph(animal):
    return f"""{_INIT_PHRASE} {animal}...
{_END_PHRASE}"""

def _get_recurrent_question(animal):
    return f"I don't know why she swallowed a {animal} - perhaps she'll die!"

_INIT_PHRASE = "There was an old lady who swallowed a"
_WIGGLE_PHRASE = "That wriggled and wiggled and tickled inside her."
_END_PHRASE = "...She's dead, of course!"

def main():
    print(song())
