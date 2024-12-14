import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def test_notebook():
    """Test that the Jupyter notebook runs without errors."""
    with open("your_notebook.ipynb") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})
        print("Notebook executed successfully.")
    except Exception as e:
        assert False, f"Error occurred while running the notebook: {e}"
