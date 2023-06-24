from random import sample, randrange, randint

AllTraits = {'Animal enthusiast': [], 'Art lover': [], 'Bookworm': [], 'Bro': [], 'Cat lover': [], 'Child of the islands': [], 'Child of the ocean': [],
           'Creative': [], 'Dance machine': [], 'Dog lover': [], 'Erratic': [], 'Geek': [], 'Genius': [], 'Green fiend': [], 'High maintenance': [],
             'Jealous': [], 'Lactose intolerant': [], 'Music lover': [], 'Perfectionist': [], 'Recycle disciple': [], 'Self-absorbed': [], 'Self-assured': [],
               'Vegetarian': [],"Active":["Lazy"],"Adventurous":["Lazy"],"Clumsy":["Maker"],"Goofball":["Snob"],"Insider":["Loner"],"Kleptomaniac":["Good"],
               "Loves outdoors":["Sqeamish"],"Loyal":["Noncommittal"],"Materialistic":["Freegan"],"Overachiever":["Lazy"],"Paranoid":["Outgoing"],
               "Romantic":["Unflirty"],"Unflirty":["Romantic"],"Ambitious":["Freegan", "Lazy"],"Cheerful":["Gloomy", "Hot-headed"],"Evil":["Childish", "Good"],
               "Family-oriented":["Hates children", "Noncommittal"],"Foodie":["Freegan", "Glutton"],"Glutton":["Foodie", "Squeamish"],
               "Hates children":["Childish", "Family-oriented"],"Hot-headed":["Cheerful", "Gloomy"],"Maker":["Clumsy", "Lazy"],"Mean":["Good", "Proper"],"Neat":["Lazy", "Slob"],
               "Noncommittal":["Family-oriented", "Loyal"],"Proper":["Mean", "Slob"],"Socially awkward":["Outgoing", "Party Animal"],"Childish" :["Evil", "Hates children", "Snob"],
               "Gloomy" :["Cheerful", "Hot-headed", "Party animal"],"Good" :["Evil", "Kleptomaniac", "Mean"],"Loner" :["Insider", "Outgoing", "Party animal"],
               "Outgoing": ["Loner", "Paranoid", "Socially awkward"],"Party animal": ["Gloomy", "Loner", "Socially awkward"],"Slob" :["Neat", "Proper", "Squeamish"],
               "Snob" :["Childish", "Freegan", "Goofball"],"Squeamish":["Freegan", "Glutton", "Loves outdoors", "Slob"],
               "Freegan":["Ambitious", "Foodie", "Materialistic", "Snob", "Squeamish"],"Lazy":["Active", "Adventurous", "Ambitious", "Maker", "Neat", "Overachiever"]}

Jobs = ["Astronaut", "Athlete","Criminal","Culinary","Business","Babysit","Barista","Fast Food Employee","Manual Worker","Retail Employee","Diver","Fisherman","Lifeguard",
        "Entertainer","Freelancer","Painter","Secret Agent","Style Influencer","Tech Guru","Author","Critic","Politician","Social Media","Education","Engineer","Law",
        "Civil Designer","Actor","Detective","Doctor","Scientist","Conservationist","Gardener","Army","Salary"]

#The "AllTraits" dictionary contains all the traits for the sims 4 and the values are lists of any traits that conflict

class TraitsClass:
    

    def __init__(self,ListTraits,Jobs):
        self.ListTraits = ListTraits
        self.Jobs = Jobs  

    def PickTraits(self):
        Picked = []
        while len(Picked) != 3: #Iterates though the dictionary while "Picked" length isnt over 3 
            x = sample( sorted(self.keys()), 1 ) #selects random Key from the trait dictionary, this was kind of frustrating to get the way I wanted 
            if x in Picked:
                pass
            else:
                if Picked == []:
                    Picked.append(x[0])
                    continue
                else:
                    for i in Picked: # Checks to make sure selected key isn't in "Picked" or is the value for any element in "Picked" compared to the dictionary
                        if x in self[i]:
                            continue
                        else:
                            pass
                    Picked.append(x[0])
        return Picked
    
    def PickJob(self): #selects random element from the Job list
        return self[randrange(len(self))]
    
    def NumberOfSims(self,x,y): # formats the output for the random number of sims selected
        Number = randint(3,9)
        Household = ""

        for i in range(Number):
            Traits = "Traits: "+", ".join(TraitsClass.PickTraits(x))
            Job = "Job: " + TraitsClass.PickJob(y)
            Household +=f"\n{Traits}\n{Job}\n"

        return Household
    




