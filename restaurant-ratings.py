# your code goes here
with open("scores.txt") as restaurant_ratings:

    restaurant_dict = {}

    for line in restaurant_ratings:
        line = line.rstrip().split(":")
        name, rating = line

        restaurant_dict[name] = rating

    restaurant_alpha = sorted(restaurant_dict)

    for restaurant in restaurant_alpha:
        print "Restaurant %s is rated at %s." % (restaurant, restaurant_dict[restaurant])

restaurant_ratings.closed