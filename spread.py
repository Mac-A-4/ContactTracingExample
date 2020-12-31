
people = [
    "Malcolm",
    "Suporn",
    "Izzy",
    "Shivani",
    "David",
    "Tom Hanks",
    "Rita Wilson"
]

"""
    https://image.prntscr.com/image/MZaQTm1cSoyxWFnlHxrv6w.png
"""

adjacency = [
    [ 0, 1, 0, 0, 1, 0, 0 ],
    [ 1, 0, 1, 1, 1, 0, 0 ],
    [ 0, 1, 0, 1, 0, 0, 0 ],
    [ 0, 1, 1, 0, 0, 0, 0 ],
    [ 1, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 1 ],
    [ 0, 0, 0, 0, 0, 1, 0 ]
]

"""
    Given the name of a person, get their index in the people list.
    The index is used to access the information contained within the adjacency matrix.
    person -> string    : The name of the person in question.
    return -> int       : The index of the person.
"""
def personIndex(person):
    return people.index(person)

"""
    Given the name of a person, get a list of those who the person is directly connected to.
    person -> string    : The name of the person in question.
    return -> list      : A list of names, those connected to the person.
"""
def personFriends(person):
    index = personIndex(person) #get the index of the given person
    row  = adjacency[index] #get the matrix row describing the connections of the given person
    output = [] #empty output list
    for i in range(0, len(row)): # for (int i = 0; i < row.size(); ++i) for those who know c++
        if row[i] == 1: #if the given person is connected to the current person we are checking
            output.append(people[i]) #add that person's name to the output
    return output

"""
    Given the name of a person, get a list of those who that person is indirectly connected to.
    person -> string    : The name of the person in question.
    return -> list      : A list of names, containing the names of those connected to the person, be it indirectly or not.
"""
def personNetwork(person):
    output = []
    def recursiveTraverse(p): #nested function, recursively visits all connected people based on an origin person
        nonlocal output #allow this function to modify the output variable (because it belongs to a different function)
        for e in personFriends(p): #for every friend of the given person
            if e not in output: #if we have not already visited this person
                output.append(e) #add the person to the list
                recursiveTraverse(e) #visit this person's friends as well
    recursiveTraverse(person) #invoke the recurvie function with the root person
    return output

"""
    Determines who could possibly be affected, given the name of patient zero, the origin.
    p0 -> string    : The name of patient zero, guaranteed to be member of the people list.
    return -> list  : The list of names of those who could possibly be affected (nonzero chance).
"""
def spread(p0):
    return personNetwork(p0) #those who could be affected are either directly or indirectly connected to p0

"""

We know that, in this example network, there are two distinct groups.
One contains Malcolm, Suporn, Izzy, Shivani, and David. Everyone in this
group knows each other either directly or indirectly. The other one 
contains Tom Hanks and his wife Rita. Nobody in the first group knows 
either Tom Hanks or his wife, so there are no connections between these 
groups. In graph theory, these would be called connected components.

This iteration of the contact tracing program is basic in that it only 
gives a binary (yes or no) answer to whether or not someone has a nonzero 
chance of being affected. This program could be improved in the future by
weighting different relationships, i.e. certain relationships are closer
than others, and being able to model the probability of spread based on 
the strength or closeness of relationships is more useful than simply 
discovering who resides in which connected components.

"""