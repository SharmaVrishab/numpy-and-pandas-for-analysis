# NumPy & Pandas for Data Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)

A comprehensive collection of Python scripts and Jupyter notebooks designed to help beginners and intermediate users master **NumPy** and **Pandas** for practical data analysis. This repository focuses on hands-on examples covering array manipulation, data cleaning, transformation, and exploration — perfect for building a strong foundation in data science workflows.

## 📚 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Learning Path](#learning-path)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

## ✨ Features

### NumPy
- **Array Creation**: Multiple methods for creating arrays (zeros, ones, random, ranges)
- **Mathematical Operations**: Element-wise operations, linear algebra, statistics
- **Indexing & Slicing**: Advanced indexing techniques and boolean masking
- **Broadcasting**: Understanding and applying NumPy's broadcasting rules
- **Vectorization**: Writing efficient, loop-free code
- **Performance**: Comparison with Python lists and optimization techniques

### Pandas
- **Data Structures**: Working with **Series** and **DataFrames**
- **I/O Operations**: Reading/writing data (CSV, Excel, JSON, SQL, Parquet)
- **Data Cleaning**: Handling missing values (`NaN`, `None`), duplicates, and outliers
- **Data Transformation**: Applying functions, mapping values, encoding categorical data
- **Filtering & Selection**: Boolean indexing, query methods, loc/iloc
- **Grouping & Aggregation**: GroupBy operations, pivot tables, crosstabs
- **Time Series**: Working with datetime objects and time-based indexing
- **Combining Data**: Merging, joining, concatenating, and appending datasets
- **Visualization**: Basic plotting with Pandas built-in methods

## 🚀 Installation

Ensure you have **Python 3.8 or higher** installed. You can check your version with:

```bash
python --version
```

### Option 1: pip (Recommended)

Install the required packages using pip:

```bash
pip install numpy pandas jupyter matplotlib seaborn
```

### Option 2: conda

If you're using Anaconda or Miniconda:

```bash
conda create -n data-analysis python=3.10
conda activate data-analysis
conda install numpy pandas jupyter matplotlib seaborn
```

### Option 3: Clone and Install

Clone this repository and install dependencies:

```bash
git clone https://github.com/yourusername/numpy-and-pandas-for-analysis.git
cd numpy-and-pandas-for-analysis
pip install -r requirements.txt
```

## 🎯 Quick Start

Launch Jupyter Notebook to start exploring:

```bash
jupyter notebook
```

Then open any of the notebooks in the `notebooks/` directory to begin learning.

### Your First NumPy Array

```python
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # [2 4 6 8 10]
```

### Your First Pandas DataFrame

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)
print(df)
```

## 🗺️ Learning Path

### Beginner Track
1. **NumPy Basics** - Arrays, indexing, basic operations
2. **Pandas Introduction** - Series, DataFrames, basic operations
3. **Data Loading** - Reading CSV/Excel files
4. **Data Cleaning** - Handling missing values and duplicates

### Intermediate Track
5. **Advanced NumPy** - Broadcasting, vectorization, linear algebra
6. **Data Transformation** - Applying functions, groupby operations
7. **Data Merging** - Joins, concatenation, combining datasets
8. **Time Series Analysis** - DateTime operations and resampling

### Advanced Track
9. **Performance Optimization** - Memory management and speed improvements
10. **Real-World Projects** - Complete data analysis workflows

## 💡 Examples

### Example 1: Array Operations with NumPy

```python
import numpy as np

# Create a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Statistical operations
print(f"Mean: {matrix.mean()}")
print(f"Standard Deviation: {matrix.std()}")
print(f"Column sums: {matrix.sum(axis=0)}")
```

### Example 2: Data Cleaning with Pandas

```python
import pandas as pd

# Load data
df = pd.read_csv('datasets/sample_data.csv')

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Filter data
filtered_df = df[df['Age'] > 25]
```

### Example 3: GroupBy and Aggregation

```python
# Group by category and calculate statistics
summary = df.groupby('Category').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Profit': 'sum'
})
print(summary)
```

## 🎓 Learning Objectives

By working through this repository, you'll be able to:

- ✅ Understand NumPy's array-based computing and its advantages over Python lists
- ✅ Perform efficient mathematical and statistical operations on large datasets
- ✅ Master Pandas for real-world data wrangling and exploration
- ✅ Confidently clean, transform, and analyze tabular data
- ✅ Handle missing data and outliers effectively
- ✅ Combine data from multiple sources using various join operations
- ✅ Create meaningful aggregations and summaries of complex datasets
- ✅ Work with time series data and perform temporal analysis
- ✅ Apply common data analysis workflows used in industry and research
- ✅ Write efficient, vectorized code for better performance

## 🤝 Contributing

Contributions are welcome! 🎉

We appreciate contributions of all kinds, including:

- 🐛 Bug reports and fixes
- 📝 Documentation improvements
- ✨ New examples and tutorials
- 💡 Feature suggestions
- 📊 Additional datasets

### How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 📚 Resources

### Official Documentation
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Jupyter Documentation](https://jupyter.org/documentation)

### Recommended Reading
- [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### Community
- [Stack Overflow - NumPy](https://stackoverflow.com/questions/tagged/numpy)
- [Stack Overflow - Pandas](https://stackoverflow.com/questions/tagged/pandas)
- [r/datascience](https://www.reddit.com/r/datascience/)

## 🌟 Acknowledgments

Special thanks to the NumPy and Pandas development teams for creating these incredible tools that power data science workflows worldwide.

---

⭐ If you find this repository helpful, please consider giving it a star!

**Happy Learning! 📊🐍**
