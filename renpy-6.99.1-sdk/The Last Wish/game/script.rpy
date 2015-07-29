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
# each new line advances to the next text box.
    
# Alternatively, this could be called scene 1 or tutorial something else. Consider moving the code for this secene to a separate file later.
label regain_consciousness:
    define o = Character('Old Merchant',
                    what_slow_cps = 20,
                    show_two_window = True)
    define lol = Character('Weird Cat Guy',
                    what_slow_cps = 20,
                    show_two_window = True)
    image village = "backgrounds/cobblestone_village.jpg"
    # TODO: replace this background with an original background
    scene black
    with Dissolve(3)
    
    pause(1)
    n "I wake up, as if from a dream."
    
    scene village
    with Dissolve(2)
    
    a "What was that dream? Who was that voice? What were they talking about?"
    
    n "My neck hurts from having slept in an awkward position for too long.
       I slowly sit upright, wincing as the wooden crate I'm sitting on creaks under my weight."
    n "A yawn escapes my lips; how long have I been asleep?"
    
    o "Hello, Miss!"
    
    n "I turn at the sound of a croaky voice. 
       An old man stands looking at me from behind a stall. 
       There are some gears, tools, and other odd bits laid out on the table, apparently for sale."
    
    a "Yes?"
    
    o "You've been sleeping on that box for a while now. Aren't you uncomfortable?
        What's a decent young girl like you doing, napping in a place like this?
        You should hurry home before it gets dark."
    
    a "Oh..."
    
    n "That's when I notice that the sun has nearly set. 
        A mellow orange has bathed the red cobblestone bricks of the road in a soft hue of harvest wheat. 
        Yes, it's time I should be heading home. Mom is probably worried."
    
    a "Hm?"
    n "That's odd. My mind is drawing a blank. 
        I can't seem to remember what my house looks like, let alone how to get there, or even what my mom looks like."
    n "Do I even have a 'home' to head back to?"
    a "Sir, do you know how long I've been asleep?"
    o "I'd say it hasn't been more than an hour or so. Seems like you were pretty tired, eh?"
    a "I guess so."
    n "Tired? 
       Well, I suppose that's the only explanation for why I fell asleep sitting on this splintering little box in the middle of a street. 
       With a grimace, I stand up, stretch my arms over my head, and begin walking down the street."
    a "Goodbye, mister. I hope your sales go well."
    o "Hope you have a nice evening, too. Heading back home?"
    a "No. There's something I must do."
    
    n "The merchant blinks, but makes no further comment and turns his attention to a customer approaching his wares.
       I continue to walk away without a backwards glance, my footsteps strangely sure, my eyes focused on an impending destination."
    n "The streets are beginning to quiet down. Slowly, the last few people disappear down shaded alleyways and closing doors.
       A distant knolling bell announces the evening lull."
    n "Ding! ... Dong! ... Ding!"
    # add bell sounds
    
    n "From the far left, a cheery voice halts you mid-step."
    lol "Hey there, Ace of Spades."
    
    n "I glance over in the direction of the voice. A distinct sound of purring greets my ears."
    
    lol "So, Ace of Spades, Spade of all Aces, how are you feeling today?"
    
    return
