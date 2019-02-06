# Pandas Presentation

This repository was designed to act as an hour session to a [local data science meetup](). This notebook has sections that are intended to be read, without any user interaction, and other sections that challenge the user to use Pandas to solve specific problems. My hope is that people will break up into groups and work together on one laptop to go through each cell, this way the more experienced individuals will be able to help the less experienced.

## Sections

I've broken up the notebook into four sections

1. Instantiation: Which simply goes over different ways to create a series or data frame object. This is purposefully basic to illustrate how there are many ways to import your data.
2. Accessing Data: Which walks through different operations you can apply on a data frame. There is no coherent big picture in this section and simply walks through some useful commands.
3. Working With A Dataset: This is the main section of this notebook. We'll be using the Titanic training data set as a source of data to explore. Some of the python code will be provided, while other pieces will be blank and ask you to figure out how to complete each task.
4. `eval` and `query`: We'll walk through the usages of these two performant methods.
5. Challenges: If you're experienced with Pandas or just want to work through problems, skip to this section.

## Installation Instructions

This Jupyter Notebook was written using Python 3. I've saved all the dependencies in a `requirements.txt` file. I use the follow steps to get Jupyter up and running. If you have better or simpler instructions, please let me know.

1. Clone this repository to your local computer. You can do this with any GUI tool of your choice, or use the following command in terminal:

  `$ git clone https://github.com/GregHilston/ds_pandas_presentation.git`

2. Create a virtual environment. This is to ensure that the dependencies that I've defined for this project never interact or cause issues with other projects you might have:

  `$ venv venv`

3. Activate the virtual environment. This is to ensure all dependencies you install, are being installed to your newly created virtual environment and not your global space.

 `$ source venv/bin/activate`

4. Install the dependencies. You won't be able to run the notebook or any of the code without the code that this project depends on.

 `$ pip3 install -r requirements.txt`

5. _This step might be optional. To be honest, my entire laptop's Python setup it botched. I'd try skipping this step at first and coming back to it if you can't get the notebook to run._
  
  Create a new kernel:

  `$ python3 -m ipykernel install --user --name ds_pandas_presentation`

6. At this point, you should be able to run the notebook. 

  `$ jupyter lab`

## Improvements?

If there's something I can improve, please either reach out to me, or feel free to submit a pull request.

Additionally, if you have completed the notebook in the allotted time, feel free to come up with your own challenges and let me know about them or submit a pull request to [here]() and I'll gladly add them!