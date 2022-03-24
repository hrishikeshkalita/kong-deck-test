import os
import yaml
import logging
from pathlib import Path

version = '1.1'
directory = "config-files"
kong = {'_format_version': version,'consumers':[],'services':[],'plugins':[],'upstreams':[]}

statefilename = 'kong.yaml'
statefilepath = Path('./'+statefilename)
statefilepath.touch(exist_ok=True)


for path, subdirs, files in os.walk(directory):
    for file in files:
        if(file.endswith(".yaml")):
            with open(os.path.join(path,file),'r') as f:
                devfilecontent = yaml.full_load(f)
                try:
                    if(devfilecontent['consumers']):
                        for consumer in devfilecontent['consumers']:
                            kong['consumers'].append(consumer)
                except KeyError:
                    logging.info("No consumers present in "+file)
                except Exception as e:
                    logging.error("Error in "+file+" -> "+str(e))
                try:
                    if(len(devfilecontent['services'])):
                        for service in devfilecontent['services']:
                            kong['services'].append(service)
                except KeyError:
                    logging.info("No Services present in "+file)
                except Exception as e:
                    logging.error("Error in "+file+" -> "+str(e))
                try:
                    if(len(devfilecontent['plugins'])):
                        for plugin in devfilecontent['plugins']:
                            kong['plugins'].append(plugin)
                except KeyError:
                    logging.info("No Plugins present in "+file)
                except Exception as e:
                    logging.error("Error in "+file+" -> "+str(e))
            
with open(statefilename,'w+') as f:
    yaml.dump(kong,f)
