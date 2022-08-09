
guests = ['james cagney','john wayne','jimmy stewart']
print(guests[0].title(),',would you please join me for dinner tonight?')
print(guests[1].title(),',would you please join me for dinner tonight?')
print(guests[2].title(),',would you please join me for dinner tonight?')

#john wayne can't come, invite james dean instead
print("\nguests[1].title()",',is unable to make dinner tonight.')
del guests[1]
guests.append('james dean')
print(guests)
print(guests[0].title(),',would you please join me for dinner tonight?')
print(guests[1].title(),',would you please join me for dinner tonight?')
print(guests[2].title(),',would you please join me for dinner tonight?')

print("\nguests[0].title()","I found a bigger table so we have room for more!")
print(guests[1].title(),"I found a bigger table so we have room for more!")
print(guests[2].title(),"I found a bigger table so we have room for more!")

guests.insert(0,'james coburn')
guests.insert(2,'james bond')
guests.append('james brown')

print("\nguests[0].title()",',join me for dinner.')
print(guests[1].title(),',join me for dinner.')
print(guests[2].title(),',join me for dinner.')
print(guests[3].title(),',join me for dinner.')
print(guests[4].title(),',join me for dinner.')
print(guests[5].title(),',join me for dinner.')

print("\nThe big table will not be here in time.")

popped_guests = guests.pop()
print(guests)
print(popped_guests.title(),",the big table won't arrive in time. We have to cancel our dinner plans.")
popped_guests = guests.pop()
print(popped_guests.title(),",the big table won't arrive in time. We have to cancel our dinner plans.")
popped_guests = guests.pop()
print(popped_guests.title(),",the big table won't arrive in time. We have to cancel our dinner plans.")
popped_guests = guests.pop()
print(popped_guests.title(),",the big table won't arrive in time. We have to cancel our dinner plans.")

print(f"\n{guests[0].title()}","you are still invited to our more intimate dinner.")
print(guests[1].title(),"you are still invited to our more intimate dinner.")

print(len(guests))#prints number of guests


