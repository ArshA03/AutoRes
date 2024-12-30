# AutoRes: Automated Resume Refinement and Tailoring

AutoRes is a Python-based automation tool designed to help users tailor their resumes for specific job descriptions. Leveraging AI-powered natural language processing and semantic similarity techniques, AutoRes simplifies the process of refining resumes, extracting key insights from job descriptions, and generating a polished, job-specific resume in just a few steps.

---

## 🌟 Features

- **AI-Powered Resume Tailoring**: Automatically rewrite your resume's experience and project sections using keywords from the job description.
- **Job Description Analysis**: Extract essential keywords, required skills, and peer-reviewed best practices from any job description.
- **Resume Scoring and Matching**: Identify the best-matching resume from a library using semantic similarity.
- **Doc to Text Conversion**: Seamlessly convert `.docx` files to `.txt` for processing.
- **Streamlined Output**: Generate tailored resumes in both text and PDF formats.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Necessary Python packages (install using the `pyproject.toml` file)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AutoRes.git
   cd AutoRes
   ```

2. Install dependencies:
   ```bash
   pip install poetry
   poetry install
   ```

3. Configure your environment:
   - Create a `.env` file in the root directory.
   - Add your API key for OpenRouter:
     ```
     API_KEY=your_openrouter_api_key
     ```

---

## 📂 Directory Structure

Here's an overview of the project layout:

```plaintext
ArshA03-AutoRes/
├── sample_input2.yaml       # Example YAML input for generating resumes
├── tests/                   # Test scripts and resources
│   ├── resources/           # Test data including sample resumes and job descriptions
│   ├── res_score/           # Utility scripts for resume scoring
├── src/AutoRes/             # Main application logic
│   ├── resources/           # Input and output data folders
│   ├── res_score/           # Core modules for resume processing
│   ├── main.py              # Entry point for the application
├── .github/                 # GitHub configuration files
├── .devcontainer/           # Development container configuration
├── pyproject.toml           # Project dependencies and configuration
├── README.md                # Project documentation
```

---

## ✨ Usage

### 1. Analyze a Job Description
Analyze and extract keywords from a job description using the following script:
```python
from src.AutoRes.main import analyze_job_description

job_description = "path_to_job_description.txt"
analyze_job_description(job_description)
```

### 2. Match the Best Resume
Use the following function to find the best-matching resume:
```python
from src.AutoRes.main import find_best_resume

best_resume, similarity_score = find_best_resume("path_to_resumes_folder", "path_to_job_description.txt")
```

### 3. Tailor Your Resume
Tailor your resume to the job description with:
```python
from src.AutoRes.main import tailor_resume

tailor_resume("best_matching_resume.txt")
```

### 4. Convert `.docx` Files to `.txt`
Easily convert Word documents to text:
```python
from src.AutoRes.res_score.doctxt import doctxt

doctxt("input.docx", "output.txt")
```

---

## 🛠️ Tools and Technologies

- **Programming Languages**: Python
- **Key Libraries**:
  - `sentence-transformers` for semantic similarity
  - `scikit-learn` for machine learning utilities
  - `spire-doc` for document parsing
  - `requests` for API communication
  - `dotenv` for environment variable management
- **API Integration**: OpenRouter for AI-driven text processing

---

## 📑 Example Files

### sample_input2.yaml
A YAML template for creating structured resumes with metadata.

### Job Description Examples
Stored in `src/AutoRes/resources/texts/jd.txt`, these files serve as inputs for testing the job description analysis feature.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 📧 Contact

For inquiries or support, reach out to:

- **Author**: Ash Afshar  
- **Email**: arsha03@outlook.com  
- **GitHub**: [@ArshA03](https://github.com/ArshA03)
- **LinkedIn**: [Ash Afshar](https://www.linkedin.com/in/ash-afshar/)

---

## 📝 Acknowledgments

- Inspired by modern resume refinement techniques and AI-driven career solutions.
- Special thanks to all contributors and testers for improving this tool.
