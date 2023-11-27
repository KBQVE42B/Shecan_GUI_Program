import pickle
# serializing or marshaling

activef = open('active.dat', 'wb')
active = True

data = pickle.dump(active, activef)