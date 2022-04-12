import sklearn as pk
#print(pk.__version__)
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())
#through below we can import datamembers of another file
import example_file
print(example_file.x)
#basically above ex is used when we are trying to implement
#different codes from different files
example_file.fun("ankur")