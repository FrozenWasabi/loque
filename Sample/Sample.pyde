from Images import loadImageNames
from Images import loadImages
add_library('minim')
minim = Minim(this)

def setup():
    global imageList, imageListNames, fileName 
    global screen, homeBounds, textBounds, infoBounds, textA, textB, textANum, textBNum, textPast, textOrder, myFont
    global allBoundaries, whichBoundary, numBoundaries
    global bubbleX, bubbleY, textBubble
    global musicbackground
    global goodbad, score, convoEnd
    
    size(540,960)
    
    musicbackground = minim.loadFile("music.mp3")
    musicbackground.loop()
    
    screen = 0
    scrollNum = 0
    score = 0
    convoEnd = False
        
    myFont = createFont("Calibri", 20)
    textFont(myFont)
    
    fileName = "ImageNames.txt"
    imageListNames = loadImageNames(fileName)
    imageList = loadImages(imageListNames)
    
    imageList[3].resize(435, 60)
    imageList[4].resize(435, 60)
    
    allBoundaries = []
    whichBoundary = -1
    numBoundaries = len(allBoundaries)
    
    homeBounds = []
    homeY = 480
    homeW = 0
    
    textBounds = [[[26, 26], [66, 66]]]
    textY = 642
    textW = 0
    
    infoBounds = [[[26, 26], [66, 66]], [[60, 853], [480, 923]]]
    
    for i in range(3):
        homeY = 480 + homeW + 37*i
        textY = 642 + textW + 22*i
        
        homeBounds.append([[84, homeY], [458, 96+homeY]])
        textBounds.append([[60, textY], [480, 70+textY]])
        
        homeW += 96
        textW += 70
        
    textANum = 1
    textBNum = 0
    
    textA = [["Hi, how are you?"], 
             ["I'm doing good! Nice to talk to someone today.", "... Pardon? Love your enthusiasm", "Oh... that doesn't go with the spirit of the website."],
             ["I love to travel, is there anywhere you want to visit"],
             ["Oh yes I have, the atmosphere was lovely.", "I see... ", "Well, it's never too late to start"],
             ["I love them! They're so adorable and fluffy.", "Sorry? I'm not comfortable answering that...", "Hello? It's rude to leave people on read."],
             ["I see...", "Yeah, we have so much in common", "Hmm, you don't see that interested"],
             ["What's your favourite genre of books or tv shows?"],
             ["Eh? That's kinda off-putting...", "Mhm fantasy is always interesting.", "Huh? Sorry? That was random"],
             ["Its pretty rainy today", "...I see", "You forgot who I am? I wasn't important enough? I see."],
             ["Out of curiosity, what's your favourite food?"],
             ["Hm you might what to avoid that", "Good to know. Your favourite food tho?", "Oh yess. That's delicious, especially when fresh."]]

    textB = [["Great! What about you?", " Yaaa, I know righttt", "I don't talk to strangers."],
             ["I want to visit Paris. Have you been before? ", "Traveling is so boring.", "I haven't really thought about it."],
             ["Do you like dogs?", "Where do you live?", "..."],
             ["I hate em", "Mhm I totally agree. They're soo cute", "Ya"],
             ["Horror, I like to watch people die...", " I love fantasy.", "Have you been fishing?"],
             ["How's the weather today?", "Don't talk to me", "Who are you again?"],
             ["Definitely battery acid. You should try sometime", "I like to sleep", "Mm, sushi is by far my favourite."]]
    
    goodbad = [[1,0,0], [1,0,0], [1,0,0], [0,1,0], [0,1,0], [1,0,0], [0,0,1]]
    
    
    textOrder = [1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 0]
    
    bubbleX = 40
    bubbleY = 430
    
    textPast = [textA[0][0]]
    textBubble = imageList[3]
    
    image(imageList[0], 0, 0)

def draw():
    global imageList, imageListNames, fileName 
    global screen, homeBounds, textBounds, textA, textB, textANum, textBNum, textPast, textOrder, myFont
    global allBoundaries, whichBoundary, numBoundaries
    global bubbleX, bubbleY, textBubble
    global score, goodbad, convoEnd
                
    fill(255)
    textSize(20)
    textAlign(CENTER)
    
    if screen == 0:
        image(imageList[0], 0, 0)
        
        allBoundaries = homeBounds
        
        if whichBoundary == 0:
            screen = 1
        elif whichBoundary == 1:
            screen = 2
        elif whichBoundary == 2:
            delay(250)
            exit()
        
    elif screen == 1:
        image(imageList[1], 0, 0)
        
        if textOrder[textANum + textBNum] == 1 or convoEnd == True:
            allBoundaries = [[[26, 26], [66, 66]]]
        else:
            allBoundaries = textBounds
        
        if textOrder[textANum + textBNum] == 2 and whichBoundary == -1 and convoEnd != True:

            for i in range(len(textB[textBNum])):
                textSize(20)
                text(textB[textBNum][i], width/2-10, textBounds[i+1][0][1]+(textBounds[i+1][1][1]-textBounds[i+1][0][1])*3/5)    

        if whichBoundary == 0:
            screen = 0
        elif whichBoundary == 1 or whichBoundary == 2 or whichBoundary == 3:
            
            if textOrder[textANum + textBNum] == 2:
                
                if whichBoundary == 1:
                    if goodbad[textBNum][0] == 0:
                        score += 1
                    textPast.append(textB[textBNum][whichBoundary-1])
                    textBNum += 1
                  
                    if textANum + textBNum == 7:
                        textOrder.insert(8, 2)
                        textOrder.insert(9, 1)    
                               
                elif whichBoundary == 2:
                    if goodbad[textBNum][1] == 0:
                        score += 1
                    textPast.append(textB[textBNum][whichBoundary-1])
                    textBNum += 1
                  
                elif whichBoundary == 3:
                    if goodbad[textBNum][2] == 0:
                        score += 1
                    textPast.append(textB[textBNum][whichBoundary-1])
                    textBNum += 1
                  
                if textANum + textBNum == 7 and (whichBoundary == 2 or whichBoundary == 3):
                    textA.pop(5)
                    textB.pop(3)
                
        bubbleY = 430
        for i in range(len(textPast)-1, -1, -1):

            if textOrder[i] == 1:
                bubbleX = 40
                textBubble = imageList[3]
            elif textOrder[i] == 2:
                bubbleX = 65
                textBubble = imageList[4]
            
            if bubbleY >= 110:
                delay(100)
                image(textBubble, bubbleX, bubbleY)
                
                textSize(16)
                if textOrder[i] == 1 or textOrder[i] == 0:
                    text(textPast[i], 248+bubbleX, bubbleY+36)
                elif textOrder[i] == 2:
                    text(textPast[i], 188+bubbleX, bubbleY+36)
                
                bubbleY -= 80

        if textOrder[textANum + textBNum] == 1 and convoEnd != True:
            if score == 3:
                textPast.append("Uh I uh needa go somewhere bye")
                allBoundaries = [[[26, 26], [66, 66]]]
                convoEnd = True
            else:
                if len(textA[textANum]) == 3:
                    textPast.append(textA[textANum][whichBoundary-1])
                else:
                    textPast.append(textA[textANum][0])
            
            if textOrder[textANum + textBNum + 1] == 0:
                textPast.append("Thanks for chatting with me!")
                allBoundaries = [[[26, 26], [66, 66]]]
                convoEnd = True

            textANum += 1
    
    elif screen == 2:
        image(imageList[2], 0, 0)
        allBoundaries = infoBounds
        
        if whichBoundary == 0:
            screen = 0
        elif whichBoundary == 1:
            screen = 1
                 
    whichBoundary = -1

def mouseReleased(): #FOR RECTANGLES
    global allBoundaries, whichBoundary, numBoundaries
    global sound
    
    validLocation = False
    for i in range(len(allBoundaries)):        
        validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
        validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
        validLocation = validXRange and validYRange
        if validLocation:
            sound = minim.loadFile("click.mp3")
            sound.play()
            whichBoundary = i
            break
