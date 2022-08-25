class PlanetaryData:
    
    def __init__(self):#intializer method
        self.storage={}
    
    def createdatastructer(self):# to hold the values
        noofplanets=int(input())#to take no of planets
        for i in range(noofplanets):
            planet=input()#to take input of the planet name
            atmosphericgases=[str(i) for i in input().split()]# to store atmospheric gases
            Moons=int(input())# to hold no.of moons
            Rings=input("enter input as  Yes or No")# to hold cboolean value for rings 
            planetinfo={}# to store planet info
            planetinfo['atmosphericgases']=atmosphericgases
            planetinfo['moons']=Moons
            planetinfo['rings']=Rings
            self.storage[planet]=planetinfo# used dictionary to store values  key will be name of planet and value for that key will be information ofthat particular plannet
        return self.storage
    def countofmoons(self):# method to get no of moons of planets which has rings
        count=0
        for planet,stats in self.storage.items():
            if stats['rings']=='Yes':
                count+=stats['moons']
        return count
    
    def foundonmaxplanets(self):# to retreieve most common gases in planets
         list_gases=[]
        for values in self.storage.values():
            gas=values['atmosphericgases']
            for i in gas:
                list_gases.append(i)
        maxi=Counter(list_gases)
        item=0
        tup=None
        for items,values in maxi.items():
            if values>item:
                item=values
                tup=((items,values))
        print(tup[0])
      

solarsystem=PlanetaryData()# created a instance to parent class
print(solarsystem.createdatastructer())# method to store data
solarsystem.countofmoons()# method to retrive moons
solarsystem.foundonmaxplanets()#  Method to retrieve gas found in maximum of planets
