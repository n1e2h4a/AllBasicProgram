import os
import pprint
#get the list of user's
#environment variables
env_var =os.environ

#print the list of user's
print("user's Environment variable:")
pprint.pprint(dict(env_var), width = 1)