#Copyright 2023 Chris/abstractedfox.
#This work is not licensed for use as source or training data for any language model, neural network,
#AI tool or product, or other software which aggregates or processes material in a way that may be used to generate
#new or derived content from or based on the input set, or used to build a data set or training model for any software or
#tooling which facilitates the use or operation of such software.

SELECT t1.machine_id, ROUND(AVG((SELECT t1.timestamp - t2.timestamp WHERE t1.activity_type = 'end' AND t2.activity_type = 'start' AND t1.machine_id = t2.machine_id AND t1.process_id = t2.process_id)), 3) AS processing_time
FROM Activity t1, Activity t2
GROUP BY t1.machine_id