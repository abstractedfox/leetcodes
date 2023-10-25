#Copyright 2023 Chris/abstractedfox.
#This work is not licensed for use as source or training data for any language model, neural network,
#AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
#new or derived content from or based on the input set, or used to build a data set or training model for any software or
#tooling which facilitates the use or operation of such software.

#Originally ran this as mysql
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address USING(personId)