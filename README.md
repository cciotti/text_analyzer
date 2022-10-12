# Text Analyzer 

A simple program to analyze text sequences. The code uses a Python library called [NLTK](https://www.nltk.org) for processing, extracting, and counting of sequences (n-grams). I chose this library as I've worked with it quite a bit over the last few years and found it to be both useful and interesting. I also have a bit of coursework in the area of Data Science. 

## Up and Running

- Tools Required
    - [Docker](https://docs.docker.com/engine/reference/run/)
    - GNU `make` (I have 3.81 locally but any modern version should work)
        - You don't technically need make, you can look at the Makefile and run the commands manually if you wish
    
This is a Python project and to make it easy to run locally without installing any extraneous programs or packages, there is a Dockerfile available. This will make interacting with the program simple. You can build the Docker image by typing `make docker`. You will then have an image called `text_analyzer:latest` on your system. You can run `docker run text_analyzer:latest` and you'll get a demo of the program in 
 action. If you want to interact with the CLI, you'll need to use the Docker image interactively. Please follow these steps.

```shell
docker run -it --entrypoint bash text_analyzer:latest
# You can use stdin, pass some files, or do both
cat tests/test_data.txt | python main.py samples/*.txt
```

If you want to supply your own directory of documents, you'll have to alter the Docker command slightly. 

```shell
docker run -it --entrypoint bash -v /path/to/your/data:/data text_analyzer:latest
python main.py /data/*.txt
```

### Running the Tests

If you want to run the tests, you'll need to use the Docker image interactively. Please follow these steps.

```shell
docker run -it --entrypoint bash text_analyzer:latest
make test
# If you want to see a coverage report
make coverage
```

### Configuration

This project uses a tool called [Dynaconf](https://www.dynaconf.com) to externalize configuration data. I've used for several years, and it's quite useful. One of the interesting features is it allows you to override configuration values with environment variables. If you look at `analyzer/config.py` you'll see when instantiating the object I pass `envvar_prefix="C_VAR"`. Using this prefix along with the name of a config value you can override it. For example, in `analyzer/settings.toml` you'll see the default value of `ngram_size` is `3`. If you want to override that default, you simply export an environment variable called `C_VAR_ngram_size` set to whatever value you want. 

### Logging

The Python logger is off by default when running in the Docker container. There is an issue with the order of the logs and print statements that I didn't have time to figure out. This only happens when not running interactively. If, when you're using the CLI you want the logs export an environment variable like this: `export LOGGING_ENABLED="true"`. If you want debug logs (there are only a couple), export another environment variable like this: `export DEBUG_ENABLED="true"`.    

#### A note about the Makefile

If you were running this on your local system, you would need to interact with the Makefile a little more, and I encourage you to have a look at it. But, for simplicity, I install the dependencies at Docker build-time.

## Next Steps

Software is never finished, only abandoned. Or so the old saying goes. There are a number of things I would like to do to enhance this project.

- Additional tooling
    - [pre-commit](https://pre-commit.com)
    - [flake8](https://flake8.pycqa.org/en/latest/)
    - [pylint](https://pylint.pycqa.org/en/latest/)
    - [click](https://click.palletsprojects.com/en/8.1.x/)
    
- Additional features
    - Sentiment analysis
    - Alternate tokenizers
    - Analyze and label parts of text (classification)
    - Graphing relationships in the text
  
- Nicer output





  


