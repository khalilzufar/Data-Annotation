# Kuta Beach Reviews Sentiment Analysis & Data Labeling 🏖️📝

## Overview 🌟
This project focuses on executing a rigorous human-in-the-loop data annotation pipeline on raw text reviews collected from Google Maps for Pantai Kuta (Kuta Beach), Bali, Indonesia. The core purpose is to build a high-quality, human-validated baseline dataset to support comparative studies between multilingual and Indonesian-specific transformer models (such as `mBERT` vs `IndoBERT`) in understanding casual real-world text[cite: 1]. 

The project pipeline covers:
- 🧑‍💻 Data Ingestion
- 🧹 Heuristic Language Filtering
- 🔍 Strict Boundary Classification
- 📊 Human-in-the-Loop Evaluation

By labeling and validating informal expressions, structural internet slang, and mixed-language tokens, this project provides a clean, golden-standard dataset optimized for localized NLP model training[cite: 1].

## Objectives 🎯
- Clean and filter a raw multi-language dataset to strictly isolate native and colloquial Indonesian text[cite: 1].
- Establish a consistent rule-based annotation schema (Taxonomy Framework) for human evaluation[cite: 1].
- Audit and document textual data mappings with contextual linguistic justifications to prevent model drift.

## Dependencies ⚙️
- ![Python](https://github.com/user-attachments/assets/efbcb388-ef93-4ed9-b571-cd79647f8e59)
- ![Jupyter Notebook](https://github.com/user-attachments/assets/34ef0fd4-6bdb-42f4-98a1-000efe2e47f1)

## Libraries & Tools 📚
- **Data Manipulation & Regex Operations:**
  - Pandas
- **Interactive Annotation Interface:**
  - Standard OS & Built-in CLI IO Modules

## How to Use 🛠️
1. **Clone this repository:**
```bash
   git clone [https://github.com/khalilzufar/Data-Annotation.git](https://github.com/khalilzufar/Data-Annotation.git)
   ```
2. Navigate to the Project Directory: Change your current directory to the cloned repository folder:
   ```bash
   cd Data-Annotation
   ```
3. Run the Data Filtering Notebook: Open Jupyter Notebook to view the ingestion script:
   ```bash
   jupyter notebook data_annotator.ipynb
   ```
4. Launch the Interactive Annotation Script: Execute the Python CLI interface via terminal to start or resume the checkpoint-based annotation system:
   ```bash
   python annotate.py
   ```
   
## Target Dataset Distribution 📈
Post-evaluation metrics for the human-annotated 200 rows baseline sample:
- **Label 2 (Positive Sentiment):** 142 Rows (71.0%)
- **Label 1 (Neutral / Mixed Sentiment):** 35 Rows (17.5%)
- **Label 0 (Negative Sentiment):** 23 Rows (11.5%)

## Author ✍️
**Khalil Zufar**

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khalil-zufar/)
