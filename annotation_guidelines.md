# Annotation Guidelines: Localized Kuta Beach Review Sentiment Analysis

## 1. Project Objective
The purpose of this project is to create a high-quality, human-validated gold-standard dataset from unmoderated public Google Maps reviews for Pantai Kuta, Bali. This taxonomy framework ensures that manual annotation remains highly consistent, objective, and adaptive to informal Indonesian syntax, internet slang, and multi-language tourist expressions.

## 2. Taxonomy & Labeling Schema
Annotators must evaluate each review based on its linguistic context and assign exactly one of the following numerical tokens:

### 🟩 Label 2: Positive Sentiment
* **Definition:** The text expresses clear satisfaction, admiration, praise, or an explicit recommendation.
* **Edge Case Handling:** If a review contains minor descriptive facts but the overall emotional valence is highly enthusiastic, it must be labeled as `2`.
* **Example:** *"Tempat favorit akuu 🤭"*

### 🟨 Label 1: Neutral / Mixed Sentiment
* **Definition:** The text is strictly informative (factual/objective descriptions without emotional attachment) OR contains an even balance of positive and negative remarks (conflicting metrics).
* **Edge Case Handling:** Reviews that acknowledge scenic beauty but pair it with strong operational caveats (e.g., traffic, mild crowding) must be assigned to `1`.
* **Example:** *"Tempat mantai terkenal di bali. Sayang kemarin ngga lihat sunsetnya karena agak berawan. Cukup ramai disini."*

### 🟥 Label 0: Negative Sentiment
* **Definition:** The text conveys explicit dissatisfaction, irritation, environmental complaints, infrastructure failures, or safety warnings.
* **Edge Case Handling:** Sarcastic comments that use praise words superficially but conclude with a major failure must be strictly evaluated as `0`.
* **Example:** *"suasana nya aja enak kalo sore datang pas siang puanasss..."* (Focuses heavily on physical discomfort).

## 3. Data Quality Assurance (QA) Metrics
To maintain data integrity and prevent model drift, a script-based boundary check is executed post-annotation to ensure zero null records and restrict values strictly to the integer domain of `{0, 1, 2}`.