def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %r cheeses!" % cheese_count
    print "You have %r boxes of crackers!" %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
  
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(5 + 5, 20 + 30)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amoutn_of_cheese + 100, amount_of_crackers + 1000)


#this is my own function that gives a presentation of any person, then I use it to present myself

def presenting_oneself(first_name, last_name, age, current_city):
   print "My name is %r %r, I am %r years old, I live in %r." % (first_name, last_name, age, current_city)
   

presenting_oneself('Giuseppe', 'De Santis', '27', 'Edinburgh')

