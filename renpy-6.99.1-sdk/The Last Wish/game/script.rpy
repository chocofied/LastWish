# You can place the script of your game in this file.

# BG IMAGES
# You can declare an image to be used later by typing "image", the type, then the name of the image, and set it equal to the address of the image in the directory.
image black = "backgrounds/blackout.png"
image white = "backgrounds/whiteout.png"
# TODO: replace ice palace bg's with self-made ones
image ice palace = "backgrounds/ice_palace.png"
image ice hw 1 = "backgrounds/ice_hallway1.jpg"
image ice hw 2 = "backgrounds/ice_hallway2.jpg"
image mirror room = "backgrounds/mirror_room.jpeg"

# SPRITES
# main character
# none yet

# CHARACTER DECLARATIONS
# the first argument is the name of the character, that will show up above their speech box.
# the second is how fast the text types into the speech box.
# I don't remember perfectly, but I think the last argument allows for the name to be in the separate box above the speech box. 

# TODO: make the character names different colors?

# anonymous character (unknown name)
define a = Character('?????',
                    what_slow_cps = 20,
                    show_two_window = True)
# main character
define p = Character('Beauty',
                    what_slow_cps = 20,
                    show_two_window = True)
# narrator text
define n = Character(None,
                    what_slow_cps = 10)

# The game starts here. Is it possible to have this play before the title screen?
label start:

# scene (name of image) will put that image on the background
    scene black
    # this command will pause the text before starting to type it.
    pause(.5)
    # note the "a" before the text. The a defined above will "speak" this text.
    a "This can't be real...{w=.5} This can't be the end."
    a "All we wanted was to find our love...{w=.5} to achieve our dreams..."
    a "To live our happily ever after..!{w=.5} We won't let it end."
    a "We'll try again. Please...{w=.5} Grant us this last wish!"
    
    scene white
    # this command dissolves the white bg into the white bg.
    with Dissolve(3)
    n "You can have your chance. We'll give you the opportunity to change that fate."
    n "But in exchange.{w=.5}.{w=.5}."

    scene black
    with Dissolve(.1)
    scene white
    with Dissolve(.1)
    scene black
    with Dissolve(1)
    scene white
    with Dissolve(.1)
    scene black
    with Dissolve(1)
    scene white
    with Dissolve(3)
    
    # the w's are manual pauses within the text.
    pause(1)
    n "I want to help them find their happily ever after. To do that, I need to.{w=.5}.{w=.5}."
# each n advances to the next text box.
    
# Alternatively, this could be called scene 1 or tutorial something else. Consider moving the code for this secene to a separate file later.
label regain_consciousness:
    # TODO: replace this background with an original background
    scene black
    with Dissolve(3)
    
    pause(1)
    n "I blinked awake."
    
    return
