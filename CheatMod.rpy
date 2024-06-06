screen CheatMenu():
    tag menu
        
    vbox:
        yalign 0.0
        xfill True

    hbox:
        textbutton "Lily":
            action IncrementVariable(lp, 1)