class goa:
    names=""
    drinks=""
    def party(self):
        print("Lets party...")
    def beach(self):
        print("Enjoy a walk at the beach")

ramesh=goa()
suresh=goa()

ramesh.name="Ramesh"
suresh.name="Suresh"

ramesh.drink="Yes"
suresh.drink="No"

print(ramesh.name)
print("Drink: ",ramesh.drink)
print(suresh.name)
print("Drink: ",suresh.drink)

ramesh.party()
suresh.beach()