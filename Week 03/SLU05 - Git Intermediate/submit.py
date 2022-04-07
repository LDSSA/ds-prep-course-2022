import requests

import click
from nbgrader import utils
from traitlets.config import Config
import nbconvert
import nbformat

###############################################################################
# Grading
###############################################################################

def grade(nb):
    total_score = 0
    max_total_score = 0
    for cell in nb.cells:
        if utils.is_grade(cell):
            score, max_score = utils.determine_grade(cell)
            total_score += score
            max_total_score += max_score

    return total_score, max_total_score

def execute(notebook, timeout=None, allow_errors=True):
    c = Config()
    c.NotebookExporter.preprocessors = [
        "nbconvert.preprocessors.ClearOutputPreprocessor",
        "nbconvert.preprocessors.ExecutePreprocessor",
    ]
    c.ExecutePreprocessor.allow_errors = allow_errors
    if timeout:
        c.ExecutePreprocessor.timeout = timeout

    exporter = nbconvert.NotebookExporter(config=c)
    notebook, _ = exporter.from_notebook_node(notebook)

    return nbformat.reads(notebook, as_version=nbformat.NO_CONVERT)

def get_grade(notebook_path='Exercise notebook.ipynb'):
    '''Gets the grade for the given notebook.'''
    notebook = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
    notebook = execute(notebook)
    total_score, max_score = grade(notebook)

    return total_score

###############################################################################
# Submitting
###############################################################################

def submit(learning_unit: int, exercise_notebook: int, slackid: str, score: float) -> None:
    '''
    Submits the notebook.

    Parameters:
        url: like "https://sub-nb-grades-collector.herokuapp.com/submit"
        learning_unit: like 0
        exercise_notebook: like 0
        slackid: like "UTS63FC02"
        score: like 16.0
    '''
    data = {
        "learning_unit": learning_unit,
        "exercise_notebook": exercise_notebook,
        "slackid": slackid,
        "score": score,
    }
    response = requests.post('https://prep-course-portal.ldsacademy.org/submissions/', json=data)
    print('Success' if response.ok else 'Whoopsie Daisy', response.text)

@click.command()
@click.option('--notebook_name', default='Exercise notebook.ipynb')
@click.option('--learning_unit', help='learning_unit: like 0', required=True)
@click.option('--exercise_notebook', default=1, help='exercise_notebook: like 1')
@click.option('--slackid', help='slackid: like "UTS63FC02"', required=True)
def grade_submit(notebook_name: str = 'Exercise notebook.ipynb', **kwargs) -> None:
    '''
    Grades the notebook and submits the grade to the prep course portal.

    Parameters:
        notebook_name: the name of the exercise notebook
        slackid: like "UTS63FC02"
        score: like 16.0
    '''
    # TODO change once we releace most recent verion of ldsagrader to pip
    # from ldsagrader import notebook_grade
    # notebook_grade(notebook=notebook_name, checksum=None, timeout=None)['total_score']
    kwargs['score'] = get_grade(notebook_name)
    submit(**kwargs)

if __name__ == '__main__':
    grade_submit()