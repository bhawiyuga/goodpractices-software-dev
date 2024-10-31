---
marp: true
theme: gaia
paginate: true
---

# Good Scientific Software Development with Python

Adhitya Bhawiyuga

---

# Agenda

1. Existing Issues in Scientific Software Development
2. Reproducibility
3. Documentation
4. Modularity
5. Testing

---

# Existing Issues in Scientific Software Development

---

## Common Problems

- Lack of version control
- Poor documentation
- Inconsistent coding styles
- Difficulty in reproducing results
- Insufficient testing

---

## Consequences of Poor Practices

- Wasted time and resources
- Difficulty in collaboration
- Errors in research findings
- Challenges in peer review
- Obstacles to building upon previous work

---

# Reproducibility

---

## Code Repository

- Use version control (e.g., Git)
- Host on platforms like GitHub, GitLab, or Bitbucket
- Commit frequently with meaningful messages

---

## Project Structure

```
my_project/
├── src/
│   └── my_module/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_core.py
├── docs/
├── data/
├── notebooks/
├── README.md
├── requirements.txt
└── setup.py
```

---

## Specify Dependencies

- Use virtual environments (venv, conda)
- Specify dependencies in `requirements.txt` or `pyproject.toml`
- Consider using package manager like `pip`, `uv`, `conda`

---

## Packaging and Delivery

- Create a `setup.py` file
- Use `setuptools` for packaging
- Publish to PyPI or use private repositories

---


## Other Notes for Reproducibility

- Document your work
- Use Docker for containerization if needed
- Implement Continuous Integration (CI)

---

# Documentation

---

## Documentation: Key to Reproducibility

- Crucial for understanding and reproducing scientific software
- Helps future you, collaborators, and other researchers
- Various types serve different purposes

---

## Types of Documentation

1. README.md
2. In-line comments
3. Docstrings
4. API documentation
5. User guides and tutorials

---

## README.md

- Project's front page
- Includes:
  - Project description
  - Installation instructions
  - Basic usage examples
  - Links to more detailed documentation
- Example: https://github.com/geopandas/geopandas

---

## In-line Comments

- Explain complex or non-obvious code
- Use sparingly for clarity, not for every line

Example:

```python
def calculate_entropy(data):
    data = np.array(data) 
    # Calculate probability distribution
    unique, counts = np.unique(data, return_counts=True)
    prob_dist = counts / len(data)
    # Apply Shannon entropy formula: -sum(p * log2(p))
    entropy = -np.sum(prob_dist * np.log2(prob_dist))
    return entropy
```
---

## Docstrings

- Describe purpose, parameters, and return values of functions/classes
- Follow conventions (e.g., NumPy style, Google style)

---

## Docstring Example (NumPy style)

```python
def calculate_mean_temperature(temperatures):
    """
    Calculate the mean temperature from a list of temperatures.

    Parameters
    ----------
    temperatures : list of float
        A list of temperature measurements in Celsius.

    Returns
    -------
    float
        The mean temperature.

    Raises
    ------
    ValueError
        If the input list is empty.
    """
    if not temperatures:
        raise ValueError("Temperature list is empty")
    return sum(temperatures) / len(temperatures)
```

---

## API Documentation

- Comprehensive reference for all public modules, classes, and functions
- Often generated automatically (e.g., using `Sphinx`)
- Includes:
  - Function signatures
  - Detailed descriptions
  - Usage examples
- Example: https://geopandas.org/en/latest/docs/reference.html

---

## User Guides and Tutorials

- Provide in-depth explanations and examples
- Can include:
  - Step-by-step tutorials
  - Explanation of underlying algorithms
  - Best practices for using the software
  - Common use cases and examples

---

## Documentation Best Practices

- Evolutive process
- Use clear, concise language
- Include examples
- Explain the "why" not just the "what"
- Use automated tools (e.g., Sphinx, MkDocs) for generation and hosting

---

# Modularity

---

## Breaking Down Complex Functions (Before)

```python
def complex_analysis(data):
    # 100 lines of code doing everything
    pass
```

---

## Breaking Down Complex Functions (After)

```python
def preprocess_data(data):
    # ...

def analyze_data(processed_data):
    # ...

def visualize_results(analysis_results):
    # ...

def complex_analysis(data):
    processed_data = preprocess_data(data)
    results = analyze_data(processed_data)
    visualize_results(results)
    return results
```

---

## Benefits of Modularity

- Improved readability
- Easier maintenance
- Reusable components
- Simplified testing

---

# Testing

---

## Unit Testing in Python

- Use the `unittest` module or `pytest`
- Test individual functions and classes
- Aim for high test coverage

---

## Example: Unit Test

```python
import unittest
from my_module.core import add_numbers

class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

---

## Test-Driven Development (TDD)

1. Write a failing test
2. Write minimal code to pass the test
3. Refactor the code
4. Repeat

---

# Conclusion

- Addressing existing issues improves the quality and reliability of scientific software
- Reproducibility ensures your work can be verified and built upon
- Modularity improves code quality and maintainability
- Testing helps catch bugs early and ensures code reliability

---

# Questions?

Thank you for attending!