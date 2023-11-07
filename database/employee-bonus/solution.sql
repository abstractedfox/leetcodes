#Copyright 2023 Chris/abstractedfox.
#This work is not licensed for use as source or training data for any language model, neural network,
#AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
#new or derived content from or based on the input set, or used to build a data set or training model for any software or
#tooling which facilitates the use or operation of such software.

SELECT * FROM (
  SELECT e1.name, Bonus.bonus
  FROM Employee e1
  LEFT JOIN Bonus on e1.empId = Bonus.empId
) AS prefiltered
WHERE bonus < 1000 or bonus is null;