import nbformat
import pytest
import os

def test_notebook():
    """Test that the Jupyter notebook can be opened."""
    notebook_path = "Final Project Code0.ipynb"

    # Check if the notebook exists
    if not os.path.exists(notebook_path):
        pytest.fail(f"Notebook file {notebook_path} not found.")

    try:
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)
        print("Notebook opened successfully.")
    except Exception as e:
        pytest.fail(f"Error occurred while opening the notebook: {e}")
