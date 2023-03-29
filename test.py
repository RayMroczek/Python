#importing packages
import pandas as pd

#create a data frame from scratch.
data_dict = {
    "schools": ["a", "b", "c"],
    "students": [91, 800, 705]
}

print(data_dict)

data4 = pd.DataFrame(data_dict)
print(data4)
