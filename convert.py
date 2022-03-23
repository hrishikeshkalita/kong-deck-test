import os
import yaml
from pathlib import Path

directory = "config-files"
kong = {'_format_version': '1.1','consumers':[],'services':[],'plugins':[]}

statefilename = 'kong.yaml'
statefilepath = Path('./'+statefilename)
statefilepath.touch(exist_ok=True)


for file in os.listdir(directory):
    if(file.endswith(".yaml")):
        with open(os.path.join(directory,file),'r') as f:
            devfilecontent = yaml.full_load(f)
            try:
                if(devfilecontent['consumers']):
                    for consumer in devfilecontent['consumers']:
                        kong['consumers'].append(consumer)
            except KeyError:
                print("Ok! No Consumers present.")
            except:
                print("Some other error")
            try:
                if(len(devfilecontent['services']) != 0):
                    for service in devfilecontent['services']:
                        kong['services'].append(service)
            except KeyError:
                print("Ok! No Services present.")
            except:
                print("Some other error")
            try:
                if(len(devfilecontent['plugins']) != 0):
                    for plugin in devfilecontent['plugins']:
                        kong['plugins'].append(plugin)
            except KeyError:
                print("Ok! No Plugins present.")
            except:
                print("Some other error")
            
with open(statefilename,'w+') as f:
    yaml.dump(kong,f)
