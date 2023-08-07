# The script of the game goes in this file.

# Declare characters used by this game. 

define mc1 = Character ("[mcname]")
define mc2 = Character("[mcname]", color= "#FFC0CB")
define narrator = Character("Narrator", color= "#FFFFFF")
define mc3 = Character("Jeff", color="#008000")

# create integer values 
default addiction = -3
default money = 3

#create ending scenes

# game start.

label start:

 
# create name and chose character 

    scene bg room with dissolve
    play music "Forgotten Memories.mp3"
    narrator "What is your name"
    $ mcname = renpy.input("")
    show mc1 happy at left
    mc1 "32 years ago i was born in a small town in the the middle of nowhere not ammounting to much this is a story of how addiction ruined my life"
    mc1 "no connection to any real events person etc"

    scene bg couch with dissolve
    show mc1 happy at right with moveinleft
    narrator " your friend loaned you money for food to help ease the burden with your financial situation you promise him you will pay him back as soon as you can however"
    menu:
        "Go to the bar":
            $ addiction = addiction + 1
            jump choseAlcohol
        "Go to the casino ":
            $ addiction = addiction +1
            $ money = money -1
            jump choseGamble
# create regular scenes
#game path
label choseAlcohol:
    scene bg bar with dissolve
    show mc1 sad 
    narrator"Despite spending nearly all of your money on booze The emptiness you feel due to your financial situation doesnt fade"
    menu:
        "spend the rest and go hungry for the week":
            $ addiction = addiction +2
            scene bg couch with dissolve
            show mc1 sad at left with moveinright
            narrator " You arrive back at your house regretting you descision"
            narrator "a week goes by and your friend asks if you want to go to the bar and watch the game this sunday"
            menu:
                "Go":
                    scene bg bar
                    $ money = money -1
                    $ addiction = addiction +1
                    narrator "After throwing the party you wake up feeling out of it and it's noticable at your job"
                    scene bg job with dissolve
                    show mc1 sad at left with moveinright
                    show mc3 angry at right with moveinleft
                    mc3 "im afraid i have to let you go"
                    scene bg bar with dissolve 
                    narrator "to cope with you loss of job you turned to drinking up until you panic when bills are due in 2 weeks"
                    menu:
                        "sell some funiture to make up for your loss":
                            $money = money-1
                            narrator "your hot water piped burst"
                            menu:
                                "sell some funiture to make up for your loss":
                                    $money = money -2
                                    narrator"your phone reached eol"
                                    menu:
                                        "drink your problems away":
                                            $addiction = 3
                                        "go to the casino":
                                            jump choseGamble
                                        
                                "drink your problems away":
                                    $addiction = 3
                                "go to the casino":
                                    jump choseGamble

                        "mix alcohol with something strong":
                            $ addiction = 3

                "Throw a game night party at your house instead":
                    scene bg roomNight
                    $ addiction +2
                    narrator "After throwing the party you wake up feeling out of it and it's noticable at your job"
                    scene bg job with dissolve
                    show mc1 sad at left with moveinright
                    show mc3 angry at right with moveinleft
                    mc3 "im afraid i have to let you go"
                    scene bg bar with dissolve 
                    narrator "to cope with you loss of job you turned to drinking up until you panic when bills are due in 2 weeks"
                    menu:
                        "Look for a new job":
                            narrator"your addiction causes you go inbetween jobs spending all your money on booze until life catches up with and all your bills are well overdue"
                            $money = 0
                            $addiction = 3
                        "mix alcohol with something strong":
                            $ addiction = 3
        # selling furniture financial crisis route            
        "sell some furniture to recoup your loss":
            $ addiction = 0
            $ money = money - 1
            scene bg room with dissolve
            narrator "a week goes by and your friend asks if you want to go to the bar and watch the game this saturday"
            menu:
                "Go":
                    scene bg bar
                    $ money = money -1
                    $ addiction = addiction +1
                    narrator ""

                "Throw a game night party at your house instead":
                    scene bg roomNight
                    $ addiction +2
                    $ money = money - 1
                    narrator "you take out an extra loan in order to pay for new furniture that you previously sold"
                    narrator "After throwing the party you wake up feeling out of it and it's noticable at your job"
                    scene bg job with dissolve
                    show mc1 sad at left with moveinright
                    show mc3 angry at right with moveinleft
                    mc3 "im afraid i have to let you go"
                    scene bg bar with dissolve 
                    narrator "to cope with you loss of job you turned to drinking up until you panic when bills are due in 2 weeks"
                    # to much debt from alchohol financial crisis
                    menu:
                        "Sell more items":
                            $ money = money -1
                            $ addiction = addiction +2
                            narrator "whatever you had left wasnt enough causing you to take out more loans"
                            menu: 
                                "ask the bank":
                                    narrator "your loan was not granted"
                                    menu:
                                        "call a friend":
                                            narrator "after multiple months going through this cycle your friend eventually distances themself from you"
                                            $ addiction  = 3
                                            $ money = 0
    jump checkEnding
#game path
label choseGamble:
    scene bg casino with dissolve 
    show mc1 sad at right with moveinleft
    narrator "you won a couple yet you lost more leaving you in a bit more debt"
    show mc3 happy at left with moveinright
    mc3 "You look down why not buy this rabbit foot for better luck"
    menu:
        #depression route
        "Yes":
            $money = money +2
            narrator" The rabbit foot actually worked and you won the jackpot"
            scene bg fancyRoom with dissolve
            narrator"You won 3 more jackpots and became filthy rich"
            scene depress2 with dissolve 
            narrator "life was going great"
            scene bg friends
            narrator "you made new friends"
            scene bg party
            narrator "and had lots of fun until"
            scene bg blackScreen 
            show mc1 happy at left with moveinright
            mc1 "I lost all of my money!"
            scene bg casino with dissolve
            play music "sadbackground.mp3"
            narrator "you try again recalling the rabbit foot you were given before"
            narrator "but it was no use"
            hide mc1 happy
            show mc1 sad at left with moveinright
            narrator "you suffered loss"
            narrator "after loss"
            narrator "after loss"
            narrator"you eventually stopped but it was too late although you werent poor anymore by anymeans you werent well off mentally due to your relationships hygiene motivation etc taking a hit after repeated losses"

        #financial crisis route
        "no":
            $money = money-2
            narrator "you opt to get a loan from an even shadier guy"
            show mc1 happy at right with moveinleft
            mc1 "I won"
            narrator "after winning the first time you decide to play again unfortunately that luck ran out this time leaving you with nothing but your house "
            menu:
                "bet your assets":
                    jump lostEverything


    jump checkEnding
# create ending scenes
label checkEnding:
    if addiction == 3 and money <= 0:
        jump financialCrisis
    elif addiction == 3:
        jump overdose
    else:
        jump depression

label financialCrisis:
    scene bg blackScreen with dissolve
    narrator "Your addiction caused you to run out of money"
    narrator "Nearly all of you possesions were reposessed"
    scene bg lostPossession  with dissolve
    narrator "as you can see addictions cause people financial situations to decline as they lose their jobs and/or neglect to pay their bills in order to engage in their addiction"
    narrator "Be sure to check the about section in the main menu for credits"
    return

        
label overdose: 
    scene bg ambulance with dissolve

    narrator "Your addiction caused you to overdose"
    scene bg hospital with dissolve
    narrator "as drug/alchol addictions progress many people turn to higher doses or expiriment by trying out nor or mixing with new drugs"
    narrator "All of these carry the risk of severe ailments or death"
    narrator "be sure to check the about section in the main menu for credits"
    return

label depression:
    scene bg blackScreen with dissolve
    narrator "You have spiraled into depression"
    scene bg messyRoom with dissolve
    narrator "addictions can cause you to neglect relationships hygine and other daily activities leading to depression"
    narrator "be sure to check the about section in the main menu"
    return
label lostEverything:
    play music "sadbackground.mp3"
    scene bg lostEverything
    narrator "Unable to support youself betting away your last penny you find yourself without a stable shelter"
    show mc1 sad at left with moveinright
    narrator "forcing you to move multiple times due to making enemies with local homeless people from bets until eventually you decide to far away"
    scene bg outOftown with dissolve 
    show mc1 sad at left with moveinright
    narrator "out of town"
    scene bg desert with dissolve
    show mc1 sad at left with moveinright
    narrator "in the desert"
    scene bg outOfTown2 with dissolve
    show mc1 sad at left with moveinright
    narrator "until finally you settled down in an abandoned ruin where you spend the rest of you days in exile away from financial troubles"
    narrator "gambling is a dangerous activity that can leave you in financial ruin "
    narrator "be sure to the about section for credits"
    return