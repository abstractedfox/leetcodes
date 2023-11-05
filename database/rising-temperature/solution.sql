#Copyright 2023 Chris/abstractedfox.
#This work is not licensed for use as source or training data for any language model, neural network,
#AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
#new or derived content from or based on the input set, or used to build a data set or training model for any software or
#tooling which facilitates the use or operation of such software.

SELECT id 
FROM Weather 
WHERE temperature > (
    SELECT temperature 
    FROM Weather as Compare 
    WHERE Compare.recordDate = Weather.recordDate - INTERVAL 1 DAY
    AND Compare.temperature < Weather.Temperature
)
