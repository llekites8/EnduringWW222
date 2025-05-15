from drafter import *
from dataclasses import dataclass
import random
@dataclass
class State:
    name:str
    score:int
    lunch:str
    
    
@route
def index(state:State)-> Page:
    return Page(state,[
        "Enduring World War II Impact",
        Button("Begin",german)
        ])
@route
def begin(state:State)-> Page:
    return Page(state,[
        "Please enter your name",
        TextBox("name", "Name"),
        Button("Continue", bfbegin1)
        ])
@route
def bfbegin1(state:State, name:str)-> Page:
    state.name = name
    return begin1(state)

@route
def begin1(state:State)-> Page:
    return Page(state,[
        "Hello " + state.name + ", please choose a side of the war.",
        Button("Germany", german),
        ])

@route
def german(state:State)->Page:
    return Page(state,[
        "You have been put into the German army for World War 2.\nUnbelievably, this also puts you in the position of being Hitler's right hand man.",
        "ALSO unbelievably, you are Jewish!",
        "In this game you must attempt to assassinate Hitler while maintaing your secret identity.",
        Button("Attempt to Assassinate Him", kill)
        ])
@route
def kill(state:State)->Page:
    return Page(state,[
        "As a devout Jew, Hitler stands against everything you stand for and you are aware he is trying to eradicate Jews\n",
        "You have decided to take it into your own hands to try and assassinate Hitler when he least expects it\n",
        "You hatch a masterplan to accomplish this goal and end Hitler's reign for all\n",
        Button("Continue", plan)
        ])
@route
def plan(state:State)->Page:
    x = random.randint(1,3)
    if x ==1:
        return Page(state,[
            "You have decided to assassinate Hitler while he is eating breakfast.\n",
            "As his right hand man (or woman) you must decide what to make him for breakfast",
            Button("Feed him Breakfast", breakfast)
            ])
    elif x == 2:
        return Page(state,[
            "You have decided to assassinate Hitler while he is eating lunch.\n",
            "As his right hand man (or woman) you must decide what to make him for lunch.",
            Button("Make him Lunch", lunch)
            ])
    elif x ==3:
        return Page(state,[
            "You have decided to assassinate Hitler while he is eating dinner.\n",
            "As his right hand man (or woman) you must decide what to make him for dinner",
            Button("Make him Dinner", dinner)
            ])
@route
def breakfast(state:State)->Page:
    y = random.randint(1,3)
    if y == 1:
        return Page(state,[
            "You're first order of business to make this plan successful is to put laxatives in his morning coffee.\n",
            "Hitler has put a lock on all cuboards in his house and in order to get the ingredients you need you must answer the questions correctly.\n",
            "The lock on the cuboard with the laxatives asks you:\n 'What year did the Holocaust Begin?",
            Button("1938", q2b),
            Button("1939", q2b),
            Button("1933", right),
            Button("1934", q2b)
            ])
    elif y == 2:
        return Page(state,[
            "You're first order of business is to undercook Hitler's morning scrapple.\n",
            "This could potentially give him salmonella and would end his reign.\n",
            "However you must answer this question to undercook his scrapple.\n",
            "What estimated portion of the Jewish Population were murdered during the Holocaust?",
            Button("1/6", q2b),
            Button("1/4",q2b),
            Button("2/5", q2b),
            Button("1/3", right)
            ])
    elif y == 3:
        return Page(state,[
            "In order to assassinate Hitler, you must feed him something scalding hot.\n",
            "In order to heat up something to that level of heat, you must answer a question first.\n",
            "What were the other two camps at the Auschwitz complex in Austria?\n",
            Button("Birkenau and Monowitz", right),
            Button("Birkenau and Frounler", q2b),
            Button("Monowitz and Bourstler", q2b),
            Button("Bourstler and Frounler", q2b)
            ])
        
@route
def right(state:State)->Page:
    state.score = 1
    return q2b(state)
@route
def q2b(state:State)->Page:
    if state.score == 1:
        return Page(state,[
            "Nice Job!\nYou were able to complete the first part of your plan!\n",
            "You apologize to Hitler for your silly mistake as he looks at you furiously.\n",
            "The next step of your plan involves getting Hitler while he cleans himself up from the mess you have caused.",
            Button("Conitnue", nextpart)
            ])
    elif state.score == 0:
        return Page(state,[
            "Ouch not quite!\n",
            "Hitler has become suspicious of your devious activity and is on to you.\n",
            "If you answer two more questions incorrectly, Hitler will have to replace you, which will expose your Jewish ties.\n",
            "The next part of your plan involves fooling Hitler while he cleans himself up for the day in the bathroom.\n",
            Button("Continue", nextpart)
            ])
@route
def nextpart(state:State)->Page:
    z = random.randint(1,3)
    if z == 1:
        return Page(state,[
            "You plan to attack Hitler while he is combing his mustahce.\n",
            "You have put poisonous Nair (No-hair) in his mustache concotion so that he not only loses his mustache but it will also poison him.\n",
            "However, in order for this to work you must answer this question:\n",
            "How many children died during the Holocaust?",
            Button("1.3 million", wrong2),
            Button("800,000", wrong2),
            Button("1.1 million", right2),
            Button("900,000", wrong2)
            ])
    elif z== 2:
        return Page(state,[
            "You plan to attack Hitler while he is combing his mustahce.\n",
            "You have put poisonous Nair (No-hair) in his mustache concotion so that he not only loses his mustache but it will also poison him.\n",
            "However, in order for this to work you must answer this question:\n",
            "When did the Holocaust technically end?",
            Button("May 8th, 1945", right2),
            Button("May 8th, 1944", wrong2),
            Button("April 18th, 1945", wrong2),
            Button("April 18th, 1944", wrong2)
            ])
    elif z == 3:
        return Page(state,[
            "You plan to attack Hitler while he is combing his mustahce.\n",
            "You have put poisonous Nair (No-hair) in his mustache concotion so that he not only loses his mustache but it will also poison him.\n",
            "However, in order for this to work you must answer this question:\n",
            "What were Jewish prisoners called?\n",
            Button("Prisoners", wrong2),
            Button("Gefangener", wrong2),
            Button("Häftling", wrong2),
            Button("Sonderkommando", right2)
            ])
@route
def right2(state:State)-> Page:
    state.score += 3
    return wrong2(state)
@route
def wrong2(state:State)->Page:
    if state.score ==4:
        return Page(state,[
            "Nice job!\nYou have successfully completed the second part of your plan!\n",
            "Hitler is growing increasingly suspicious but you once again manage to play it off as a mistake.\n",
            "The final part of your plan involves getting Hitler while he is at his most vulnerable...\n",
            "While he is listening to his morning Jazz!\n",
            "In order to do this, you must answer not one, but two questions correctly out of a possible three questions.",
            Button("Continue", four)
            ])
    elif state.score == 3:
        return Page(state,[
            "Nice job!\nYou have successfully completed the second part of your plan!\n",
            "Hitler is growing increasingly suspicious but you once again manage to play it off as a mistake.\n",
            "The final part of your plan involves getting Hitler while he is at his most vulnerable...\n",
            "While he is listening to his morning Jazz!\n",
            "In order to do this, you must answer not one, not two, but three questions correctly out of a possible four questions.",
            Button("Continue", four)
            ])
    elif state.score == 0 or state.score == 1:
        return Page(state,[
            "Oh no!\nYou have failed the second part of the plan and Hitler is very suspcious of you.\n",
            "In order to fool Hitler and succeed in the final part of your plan, that is -- get him while he's listening to Jazz-\nYou must answer four out of a possible five questions correctly.\n",
            Button("Continue", four)
            ])
    
@route
def four(state:State)->Page:
    if state.score == 4:
        return Page(state,[
            "Since you have gotten both questions right so far, you only have to correctly answer two out of three questions in order to kill Hitler while he listens to Jazz.\n",
            "Your first question is: \nWhich concentration camp recorded the most Jewish deaths outside of Auschwitz?\n",
            Button("Dachau", wrong3),
            Button("Bergen-Belsen", wrong3),
            Button("Majdanek", right3)
            ])
    if state.score == 3 or state.score == 1:
        return Page(state,[
            "Since you have only answered one question correctly, you must answer correctly answer three out of a possible four questions in order to kill Hitler while he listens to Jazz.\n",
            "Your first question is: \nWhich concentration camp recorded the most Jewish deaths outside of Auschwitz?\n",
            Button("Dachau", wrong3),
            Button("Bergen-Belsen", wrong3),
            Button("Majdanek", right3)
            ])
    if state.score == 0:
        return Page(state,[
            "Since you haven't answered any questions correctly, you must correctly answer four out of a possible five questions in order to kill Hitler while he listens to Jazz.\n",
            "Your first question is: \nWhich concentration camp recorded the most Jewish deaths outside of Auschwitz?\n",
            Button("Dachau", wrong3),
            Button("Bergen-Belsen", wrong3),
            Button("Majdanek", right3)
            ])
    
@route
def right3(state:State)->Page:
    if state.score ==1:
        state.score =3
    state.score += 2
    return wrong3(state)
@route
def wrong3(state:State)->Page:
    if state.score == 2 or state.score == 5 or state.score == 6:
        return Page(state,[
            "One down!\nYou're next question is:\n",
            "What day did Germany invade Poland and officially start World War II?",
            Button("September 1st, 1939", right4),
            Button("September 2nd 1939", wrong4),
            Button("September 3rd 1939", wrong4)
            ])
    else:
        return Page(state,[
            "You're next question is:\n",
            "What day did Germany invade Poland and officially start World War II?",
            Button("September 1st, 1939", right4),
            Button("September 2nd 1939", wrong4),
            Button("September 3rd 1939", wrong4)
            ])
    
@route
def right4(state:State)->Page:
    state.score += 7
    return wrong4(state)

@route
def wrong4(state:State)->Page:
    if state.score ==13:
        return done(state)
    elif state.score == 12 or state.score ==6 or state.score == 11:
        return Page(state,[
            "One left!",
            "You're final question is:\nWhat was the first concentration camp called?",
            Button("Bergen-Belsen", wrong5),
            Button("Dachau", right5),
            Button("Flossenburg", wrong5)
            ])
    elif state.score == 5 or state.score == 10 or state.score == 9:
        return Page(state,[
            "Two left!",
            "You're next question is:\nWhat was the first concentration camp called?",
            Button("Bergen-Belsen", wrong5),
            Button("Dachau", right5),
            Button("Flossenburg", wrong5)
            ])
    elif state.score == 2 or state.score ==7:
        return Page(state,[
            "You will need to answer the final three questions correctly.\n",
            "You're next question is:\nWhat was the first concentration camp called?",
            Button("Bergen-Belsen", wrong5),
            Button("Dachau", right5),
            Button("Flossenburg", wrong5)
            ])
    else:
        return youvebeenkilled(state)
    
@route
def right5(state:State)->Page:
    if state.score ==12  or state.score ==11  or state.score ==6 :
        return done(state)
    else:
        state.score += 6
    return wrong5(state)

@route
def wrong5(state:State)->Page:
    if state.score == 5 or state.score == 10 or state.score == 6 or state.score == 2 or state.score ==7:
        return youvebeenkilled(state)
    if state.score == 18:
        return done(state)
    elif state.score == 15 or state.score == 12 or state.score == 16 or state.score ==11:
        return Page(state,[
            "One left!\n Your final question is:\nWhat year did your boss, Hitler, become chancellor of Germany?\n",
            Button("1934", wrong6),
            Button("1933", done),
            Button("1932", wrong6),
            Button("1931", wrong6)
            ])
    elif state.score == 8 or state.score ==9 or state.score == 13:
        return Page(state,[
            "Two left!\nYour next question is:\nWhat year did you boss, Adolf Hitler, become the chancellor of Germany?\n",
            Button("1934", wrong6),
            Button("1933", right6),
            Button("1932", wrong6),
            Button("1931", wrong6)
            ])
    
@route
def right6(state:State)->Page:
    if state.score == 8 or state.score ==9 or state.score == 13:
        state.score += 100
    return wrong6(state)

@route
def wrong6(state:State)->Page:
    if state.score == 8 or state.score ==9 or state.score == 13 or state.score == 12 or state.score == 11 or state.score == 6:
        return youvebeenkilled(state)
    elif state.score == 108 or state.score == 109 or state.score == 113 or state.score == 15:
        return Page(state,[
            "Here is your final question!\n",
            "What was the act passed in Germany that gave Hitler absolute power over Germany?",
            Button("The Power Act", youvebeenkilled),
            Button("The Enabling Act", done),
            Button("The Authoritarian Act", youvebeenkilled),
            Button("The Control Act", youvebeenkilled)
            ])
@route
def youvebeenkilled(state:State)->Page:
    return Page(state,[
        "OH NOOO!\n",
        "Hitler caught on to your plan and attacked you before you were able to properly take him out for good.",
        "He sentenced you to a concentration camp where he said you will serve out the rest of your days."
        ])

@route
def done(state:State)->Page:
    return Page(state,[
        "You're plan worked!",
        "You were able to succesfully take out Hitler while he was listening to his morning Jazz.\n",
        "You did this by blasting a music type you invented called 'Heavy Metal' and this startled him so much he passed away on the spot.",
        "Hooray!",
        ])
#############################################################################################

@route
def lunch(state:State)->Page:
    return Page(state,[
        "Your first order of business in your masterplan is to decide what to cook Hitler for lunch.\n",
        "However, each choice you make will require you to corretly answer questions along the way.\n",
        "With that in mind, what will you decide to cook Hitler for lunch?",
        TextBox("lunch", "Lunch"),
        Button("Continue", lunch2)
        ])
@route
def lunch2(state:State, lunch:str)->Page:
    state.lunch = lunch
    return lunch3(state)
@route
def lunch3(state:State)->Page:
    return Page(state,[
        "You have decided to make Hitler " + state.lunch + " for lunch.\n",
        "However, before you give it to him, you plan on sprinkling in some slices of a carolina reaper pepper.",
        "In order to do so, you must first answer this question:\n",
        "What percentage of the German population were Jews when the Holocaust first began?",
        Button("10%",wrrong),
        Button("5%", wrrong),
        Button(">1%", rright)
        ])
@route
def rright(state:State)->Page:
    state.score += 100
    return wrrong(state)

@route
def wrrong(state:State)->Page:
    if state.score == 100:
        return Page(state,[
            "Nice Job! You were able to make Hitler's food super hot and he rushed to the bathroom to throw up.\n"
            "If you hurry quickly enough, you will be able to lock the door so he cannot use the bathroom.\n"
            "But to do so, you must answer this question:\nDid the Nazi's come to power legally?",
            Button("Yes", rright2),
            Button("No", wwrong2)
            ])
    else:
        return Page(state,[
            "OH NO!\nHitler caught you trying to put a carolina reaper in his " + state.lunch + " and got furious at you.\n",
            "He said if he catches you again that you're toast.\nLuckily for you, in Hitler's rage, he got very sick and rushed to the bathroom.",
            "If you answer this next question correctly, you'll be able to lock the door so that he cannot use the bathroom.\n"
            "Did the Nazi's come to power legally?",
            Button("Yes", rright2),
            Button("No", wwrong2)
            ])
@route
def rright2(state:State)->Page:
    state.score += 1000
    return wwrong2(state)
@route
def wwrong2(state:State)->Page:
    if state.score == 0:
        return youvebeenkilled2(state)
    elif state.score == 100:
        return Page(state,[
            "Oh No!\nYou weren't able to lock the door in time and Hitler noticed you were trying to lock him out.\n",
            "While on the toilet, he scolds you for your inadequacy and says that if it happens again you'll be yesterdays news.\n",
            "You regain your bearings and realize that Hitler is still eating lunch and you still have time to sabotage his meal.\n",
            "Your next plan of action is to break one of the legs off of his chair so that when he sits he will fall off.\n",
            "In order to do this, you must answer this next question correctly:\nWho else did the Nazi's target in terms of extermination?",
            Button("Homosexuals", wwrong3),
            Button("Poles", wwrong3),
            Button("Physically disabled", wwrong3),
            Button("All of the above", rright3)
            ])
    elif state.score == 1100 or state.score == 1000:
        return Page(state,[
            "Nice Job!\n Hitler was locked out of the bathroom and had an accident outside the bathroom on his expensive carpet.\n",
            "He was upset at you but understands things happen. He told you he is going to change and come back to finish his meal.\n",
            "While he is gone, you plan to break one of the legs off of his chair so that when he sits he will fall.\n",
            "In order to do this, you must answer this next question correctly:\nWho else did the Nazi's target in terms of extermination?",
            Button("Homosexuals", wwrong3),
            Button("Poles", wwrong3),
            Button("Physically disabled", wwrong3),
            Button("All of the above", rright3)
            ])
    
@route
def rright3(state:State)->Page:
    state.score += 10000
    return wwrong3(state)

@route
def wwrong3(state:State)->Page:
    if state.score == 100 or state.score == 1000:
        return youvebeenkilled2(state)
    elif state.score == 10100 or state.score == 11100 or state.score == 11000:
        return Page(state,[
            "You did it!\nHitler fell out of his chair when he sat down and hurt his tailbone. He is befuddled at how the chair lost its leg and complains to you.\n",
            "Hitler tells you to call the doctor so that he can get a shot in his rump to soothe the swelling.\n",
            "When the doctor arrives, you hatch a plan to secretly steal the needle the doctor will use to stop the swelling, and replace it with a drug that will take Hitler out",
            "However, in order to do so, you must answer this question correctly:\nWhat set of laws excluded Jewish people from public life?",
            Button("Anti Laws", wwrong4),
            Button("Nuremburg Laws", rright4),
            Button("Exlcusion Laws", wwrong4)
            ])
    elif state.score ==1100:
        return Page(state,[
            "When Hitler returned to the kitchen, he chose to sit in a different seat and did not even notice the broken chair.\n",
            "It wasn't until later when he dropped his apple onto the chair that he noticed the broken leg. He scrutinized you for this and said if he sees you slip like this again you will be punished.\n",
            "While Hitler is explaining all of this to you, a bee flies through the kitchen sink window and stings Hitler right on top of his nose.\n",
            "Hitler tells you to call the doctor so that the doctor can give him a needle to soouth the swelling. However you see this as an opportunity to fill the needle with poison and finally kill Hitler.\n",
            "However, in order to do so, you must answer this question correctly:\nWhat set of laws excluded Jewish people from public life?",
            Button("Anti Laws", youvebeenkilled2),
            Button("Nuremburg Laws", rright4),
            Button("Exlcusion Laws", youvebeenkilled2)
            ])
@route
def rright4(state:State)->Page:
    state.score += 100000
    return wwrong4(state)

@route
def wwrong4(state:State)->Page:
    if state.score == 10100:
        return youvebeenkilled2(state)
    else:
        return Page(state,[
            "The doctor finally arrived with the needle to soothe Hitler's swelling, while the two were discussing price, you switched the needles.\n",
            "You then gave the doctor a needle containing a lethal dose of fentanyl. When the doctor used the needle, it essentially euthanized Hitler and he passed away on the spot.\n",
            "Congratulations! Germany is now free from Hitler's reign thanks to your quick thinking and expertise!"
            ])
@route
def youvebeenkilled2(state:State)->Page:
    return Page(state,[
        "Hitler has had enough of your shenanigans and calls in a backup right-hand-man to replace you.\n",
        "He then sends you off to a concentration camp where he says you will live out the rest of your days.\n",
        "You failed."
        ])
    
##############################################################
    
@route
def dinner(state:State)->Page:
    return Page(state,[
        "You decide that you will kill Hitler during his dinner time meal.\n",
        "You decide that your first order of business will be to spill Hitler's hot soup all over him.\n",
        "Hitler asked you to prepare some chicken noodle soup for his dinner time meal. While walking over to him with his soup, you work up the courage to spill it on him.\n"
        "However, in order to complete this successfully, you must answer this question correctly:\nWhat does the term, 'Night of Broken Glass' refer to?",
        Button("Kristallnacht", rrright),
        Button("Crystallnacht", wwwrong),
        Button("Krystallnacht", wwwrong),
        ])
@route
def rrright(state:State)->Page:
    state.score += 100
    return wwwrong(state)
@route
def wwwrong(state:State)->Page:
    if state.score == 100:
        return Page(state,[
            "You successfully spilled the hot soup all over Hitler's lap. Hitler cries out in agony and rushes to the freezer to grab some ice and then to his bedroom for a spare change of clothes.\n",
            "While Hitler is changing, you begin to plan the next part of your elaborate scheme.\nYou plan to put olive oil all over the floor so that when Hitler returns he will slip and fall.\n",
            "However, to do this properly, you must answer this next question properly:\nHow many Jews died during death marches?",
            Button("90k", wrongg),
            Button("95k",wrongg),
            Button("100k",rightt)
            ])
    else:
        return Page(state,[
            "Oh No!\nYou missed Hitler's lap and spilled the soup all over the floor. Hitler is furious but you explain that it was just a mistake.\n",
            "Hitler runs out of the room to grab a towel to clean it up and curses you up and down letting you know that if you slip again he will replace you.\n",
            "While Hitler is gone grabbing the towel, you begin to plan the next part of your elaborate scheme.\nYou plan to put olive oil all over the floor so that when Hitler returns he will slip and fall.\n",
            "However, to do this properly, you must answer this next question properly:\nHow many Jews died during death marches?",
            Button("90k", wrongg),
            Button("95k",wrongg),
            Button("100k",rightt)
            ])
@route
def rightt(state:State)->Page:
    state.score += 1000
    return wrongg(state)

@route
def wrongg(state:State)->Page:
    if state.score == 0:
        return youvebeenkilled3(state)
    elif state.score == 1000 or state.score == 1100:
        return Page(state,[
            "Success!\nWhen Hitler came back into the kitchen to finish eating his dinner he slipped all over the olive oil and fell hurting his head in the process.\n",
            "You tell him it was an accident and you must have cleaned up the excess soup a little too well. He believes but says he must grab an ice pack for his new headache.\n",
            "While he is gone, you decide to heat up his milk so that it is chunky.\n",
            "However, to do this successfully, you must answer this question correctly:\n 'What year did the Holocaust Begin?",
            Button("1938", wrongg2),
            Button("1939", wrongg2),
            Button("1933", rightt2),
            Button("1934", wrongg2)
            ])
    elif state.score == 100:
        return Page(state,[
            "Hitler catches you putting olive oil all over the floor and demands to know what you're up to.\n",
            "While you escape by telling him you're cleaning, he tells you that another error like this will ship you off to a concentration camp quicker than you can say concentration camp.\n",
            "While Hitler goes to throw away the towel, you decide to heat up his milk and make it chunky.\n",
            "However, to do this successfully, you must answer this question correctly:\n 'What year did the Holocaust Begin?",
            Button("1938", wrongg2),
            Button("1939", wrongg2),
            Button("1933", rightt2),
            Button("1934", wrongg2)
            ])
@route
def rightt2(state:State)->Page:
    state.score +=10000
    return wrongg2(state)

@route
def wrongg2(state:State)->Page:
    if state.score == 100:
        return youvebeenkilled3(state)
    elif state.score == 1000 or state.score == 1100:
        return Page(state,[
            "Oh no! Hitler caught you while you were attempting to heat up his milk. You told his it was to soothe his nerves but he doesn't buy it.\n",
            "He says if you mess up again you again, you will be replaced.\nWhile you couldn't spoil his milk in time, you decided to unbolt the fan from the ceiling so that if Hitler were to turn it on, it would fall off on top of him.\n",
            "However, to do that in time while Hitler dumps out his milk, you must answer this question correctly:\n",
            "How many children died during the Holocaust?",
            Button("1.3 million", wrongg3),
            Button("800,000", wrongg3),
            Button("1.1 million", rightt3),
            Button("900,000", wrongg3)
            ])
    else:
        return Page(state,[
            "You were able to successfully spoil Hitler's milk and he got very sick when he drank it.\nHe rushed to the sink to spit it all out.\n",
            "While he is busy spitting out the milk, you decide to to unbolt the fan from the ceiling so that if Hitler were to turn it on, it would fall off on top of him.\n",
            "However, to do that in time while Hitler spits out his milk, you must answer this question correctly:\n",
            "How many children died during the Holocaust?",
            Button("1.3 million", wrongg3),
            Button("800,000", wrongg3),
            Button("1.1 million", rightt3),
            Button("900,000", wrongg3)
            ])
    
@route
def rightt3(state:State)->Page:
    state.score = 0
    return wrongg3(state)

@route
def wrongg3(state:State)->Page:
    if state.score == 1000 or state.score == 1100:
        return youvebeenkilled3(state)
    elif state.score != 0:
        return Page(state,[
            "While you were not able to completely dismantle the ceiling fan, you got pretty close, if you can cause one more distraction without getting caught you might be able to full dismantle it.\n",
            "You decided that the best choice would be to start a small fire in the room adjacent to the kitchen. This would not only get Hilter out of the kitchen, but he would turn the fan on when he comes back in.\n",
            "However, you must first answer this question to start the small fire out of a couple of dry sticks and paper:\n",
            "How many incarceration cites did the Nazi's construct?",
            Button("28k", youvebeenkilled3),
            Button("35k", youvebeenkilled3),
            Button("44k", rightt4),
            Button("56k", youvebeenkilled3)
            ])
    elif state.score == 0:
        return Page(state,[
            "You were able to successfully dismantle the fan from the ceiling! Now all you have to do is turn it on once Hitler retakes his seat.\n",
            "However, in order for that to happen you must successfully answer this last question. If you do not, you will get caught and sent away.\n",
            "What day is international Holocaust Rememberance Day?",
            Button("August 29th", youvebeenkilled3),
            Button("August 24th", youvebeenkilled3),
            Button("January 25th", youvebeenkilled3),
            Button("January 27th", doneski)
            ])
    
@route
def rightt4(state:State)->Page:
    return(state,[
        "You were able to successfully start the fire. Hitler began to smell smoke from the other room and rushed in to see what the problem was.\n",
        "While he was gone, you finished dismantling the fan from the ceiling, now all you need to do it turn it on when Hitler returns so that it falls on him and cuases his demise.\n",
        "In order for this to happen properly, you must answer this final question correctly. Answering this incorrectly, would result in Hitler catching on to your plan and removing you.\n",
        "Your final question is: How many people, total including those that weren't Jewish, were estimated to have been killed during the Holocaust?",
        Button("10 million", youvebeenkilled3),
        Button("11 million", doneski),
        Button("12 million", youvebeenkilled),
        Button("13 million", youvebeenkilled)
        ])

@route
def doneski(state:State)->Page:
    return Page(state,[
        "You did it!!\nWhen Hitler returned to his seat to continue his meal, you flicked on the fan switch and the fan came tumbling down taking him out.\n",
        "You have successfully defeated Hitler and ended his reign!!\nCongratulations!!"
        ])
    
@route
def youvebeenkilled3(state:State)->Page:
    return Page(state,[
        "OH NO! Hitler caught you while you were attempting to execute your plan.\n",
        "He called in his guards and they held you down while he told you you'd be shipped off to a concentration camp for your crimes against the Nazi regime.\n",
        "You lose."
        ])
    

            
        
        
        
        
    

    
        
        
            
        
    
            
    






    

    
        
        
        
        
        
        
        
        
        
        

start_server(State("no",0, "no"))
