
# Impression Network Analysis

This repository contains the Python implementation and analysis of an **Impression Network**, derived from a dataset representing the relationships among students. The project explores various social network metrics and features using directed graphs and algorithms.

## Problem Statement

The task is to analyze the provided impression network dataset (shared as a Google Sheet) by conducting the following experiments:
1. **Top Leader Identification**  
   Choose the top leader by running a **random walk with teleportation** on the graph.
2. **Missing Links Recommendation**  
   Use a matrix-based method to predict missing edges in the graph, as explained in the class.
3. **Creative Problem Proposal and Solution**  
   Propose and solve a brand-new problem using the dataset, showcasing creativity and novel applications.

## Project Overview

The project involves:
1. Graph construction from the dataset.
2. Implementation of algorithms to solve the three tasks:
   - **Random Walk with Teleportation** for leader identification.
   - **Linear Regression on Adjacency Matrix Rows** to recommend missing links.
   - **Custom Problem**: Analyze graph metrics like **Assortativity**, **Mutuality**, and **Closeness Centrality** to derive insights on the network's structure.

## Files in the Repository

- `Q1.py`: Implements:
  - Directed graph creation.
  - Graph visualization using Matplotlib.
  - Random walk with teleportation to identify the top leaders in the impression network.
- `Q2.py`: Contains the implementation for:
  - Conversion of the graph to an adjacency matrix.
  - Missing link detection using a combination of linear regression and PageRank scores.
- `Q3.py`: Implements:
  - Assortativity analysis (connections between similar nodes).
  - Mutuality computation (reciprocated edges in the network).
  - Closeness centrality ranking to measure node influence.
- `Project_2___2023CSB1140.pdf`: Detailed project documentation, including problem statement, methodologies, pseudo-codes, and results.

## Dependencies

To run the code, ensure the following Python libraries are installed:
- `networkx`
- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

Install them via pip:
```bash
pip install networkx pandas numpy matplotlib scikit-learn
```

## Dataset

The dataset is in CSV format, exported from the provided Google Sheet. It contains nodes (student identifiers) and their relationships. Update the file path in the scripts before execution.

## Running the Code

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Place the `ImpressionNetwork.csv` file in the same directory.
3. Execute the scripts:
   - For top leader identification: `python Q1.py`
   - For missing links recommendation: `python Q2.py`
   - For assortativity, mutuality, and centrality analysis: `python Q3.py`

## Results

### Top Leader Identification
Using a random walk with teleportation:
- The top leader identified is `2023CSB1091`.
- The algorithm prints the top 5 leaders in descending order of influence.

### Missing Links Recommendation
The matrix-based method identifies approximately 3900–4500 missing links depending on the dataset and threshold. These edges are recommended based on linear regression scores or PageRank-based heuristics.

### Custom Problem: Graph Metrics Analysis
1. **Assortativity**:  
   - 72.89% of edges connect nodes of the same branch.  
2. **Mutuality**:  
   - There are 1204 reciprocated edges (double-sided connections).  
3. **Closeness Centrality**:  
   - The top 10 nodes ranked by closeness centrality include `2023CSB1091`, highlighting its central role in the network.

## Deliverables

- **Code**: All Python scripts (`Q1.py`, `Q2.py`, `Q3.py`) are provided for reproducibility.
- **Latex Report**: A concise report explaining the methodology and results (to be added to the repository).
- **Video Presentation**: A summary video showcasing the problem, approach, and results (to be submitted).

## References

1. [NetworkX Documentation](https://networkx.org/documentation/stable/reference/index.html)
2. [Scikit-Learn Documentation](https://scikit-learn.org/stable/documentation.html)
3. [Social Network Analysis - Wikipedia](https://en.wikipedia.org/wiki/Social_network_analysis)
4. [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## License

This project is licensed under the MIT License. See `LICENSE` for details.
