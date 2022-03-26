# So you want to log things, do you? 
This toolbox is here so you can copy paste silly boilerplate code into your app, and not have to worry about updating it because its just gonna get replaced if it breaks.

## Why?
I find the logging module in python to be somewhat confusing on one point:
loggers inheret based on their names, within a dotted hierarchical structure... 
Meaning, submodules need to know whom their parent is, if you want the submodule name to also be in the name of the logger.
But apparently, you don't need that: you only really need root.
So the reccomendation in standardlib is a bit nonsensical, it claims that a good practice is to initiate loggers like: 
```log = logging.getLogger(__name__)```
But if you do that in your submodules, they would all need special formatters and stuff!

## okay... How?
Instructions are in the code, but basically. keep the logger name root for all and setup formatting and handlers in a seperate module that you import only once. 
Oh and importing to an underscore keeps pylint happy: ```import package.custom_logger as _```

Whatever formatting and special things you want to do, you can do in there. Keep all the dirty logger stuff in one location. 
