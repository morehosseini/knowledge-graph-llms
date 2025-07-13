# Semantic Mapping of AI-Related Job Competencies in Construction: A Knowledge Graph Analysis

[![DOI](https://img.shields.io/badge/DOI-10.xxxx%2Fxxxxxx-blue)](https://doi.org/10.xxxx/xxxxxx)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/morehosseini/knowledge-graph-llms/blob/main/notebooks/)

## Overview

This repository contains the complete codebase and methodology for the research paper "Semantic Mapping of AI-Related Job Competencies in Construction: A Knowledge Graph Analysis" by Dr. M. Reza Hosseini from The University of Melbourne.

### Key Contributions
- **Novel Methodology**: First systematic application of knowledge graph methodology to AI workforce analysis in construction
- **Automated Pipeline**: LLM-powered knowledge extraction from job postings data
- **Network Analysis**: Comprehensive analysis of AI role interconnections and competency patterns
- **Practical Insights**: Evidence-based guidance for workforce development and career pathways

## Quick Start

### Option 1: Google Colab (Recommended)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/morehosseini/knowledge-graph-llms/blob/main/notebooks/01_data_preprocessing.ipynb)

### Option 2: Local Setup

~~~
# Clone the repository
git clone https://github.com/morehosseini/knowledge-graph-llms.git
cd knowledge-graph-llms

# Create conda environment
conda env create -f environment.yml
conda activate knowledge-graph-llms

# Or use pip
pip install -r requirements.txt

# Start Jupyter
jupyter notebook notebooks/
~~~

## Repository Structure

~~~
├── data/                     # Sample and processed data
├── notebooks/               # Jupyter notebooks for analysis pipeline
├── src/                     # Source code modules
│   ├── data_processing/     # Data preprocessing utilities
│   ├── knowledge_extraction/ # LLM-based extraction tools
│   ├── graph_analysis/      # Network analysis functions
│   └── visualization/       # Plotting and visualization tools
├── results/                 # Generated figures and metrics
├── docs/                    # Documentation and guides
└── paper/                   # Paper manuscript and supplementary materials
~~~

## Key Findings

🔍 **87.5%** of AI roles exist in an interconnected competency network  
📊 **Data Engineer** emerges as the key bridge role (not Data Scientist)  
💬 **Communication skills** are more central than technical skills for career mobility  
📈 Construction shows **12.3% annual growth** in AI recruitment (4x other industries)

## Methodology

1. **Data Collection**: 283 AI-related job postings from major construction companies (Australia/New Zealand, 2021–2025)
2. **Knowledge Extraction**: Automated LLM-based entity and relationship extraction
3. **Graph Construction**: NetworkX-based knowledge graph with 2,362 nodes and systematic refinement
4. **Network Analysis**: Centrality metrics, clustering analysis, and pathway identification

## Data Usage & Privacy

- Raw job posting data not included due to licensing restrictions
- Sample synthetic data provided for demonstration
- Original Lightcast data available with appropriate licensing
- All personal information anonymized

## Citation

~~~
@article{hosseini2025semantic,
  title={Semantic Mapping of AI-Related Job Competencies in Construction: A Knowledge Graph Analysis},
  author={Hosseini, M. Reza},
  institution={The University of Melbourne},
  year={2025},
  doi={10.xxxx/xxxxxx}
}
~~~

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Dr. M. Reza Hosseini**  
Senior Lecturer in Construction Technology  
Faculty of Architecture, Building and Planning  
The University of Melbourne  
📧 reza.hosseini@unimelb.edu.au  
🌐 [University Profile](https://findanexpert.unimelb.edu.au/profile/xxxxx)

## Acknowledgments

- Lightcast for providing labor market analytics data  
- OpenAI for LLM capabilities  
- The University of Melbourne for research support

> **Warning:** The notebooks and graph files here may not reflect the final, revised versions used in the study.
