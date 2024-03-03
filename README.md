<div align="center">
  
# Resume-Parser
</div>
A  comprehensive resume parser, capable of extracting detailed information from resumes in various formats (PDF, LATEX, HTML, DOC, etc.). The parser accurately classify text into distinct sections (e.g., education, work experience, skills) and sequence them based on dates, where available. Also standardize different job titles and occupations against the O*NET database, ensuring a consistent taxonomy across parsed resumes and implement an advanced feature that mines detailed skills and competencies from project descriptions and position roles within the resume, highlighting the candidate's specific abilities and expertise and can extract skills from resume and predict what skills it can have based on projects and jobs.
<br>
<div align="center">

# How does it work?
</div>

The Resume Matcher takes your resume as input, parses them using Python, and with various libraries and models, analyse all your resume and providing you with detailed information, section classification, job extraction, skill extraction and prediction with json file format.

The process is as follows:

1. **Parsing**: The system uses Python to parse both your resume.

2. **Classification into different section**: The tool uses python script to extract the details with their classes and extract them from your resume. The sections includes e.g.,  Name, email, education, work experience, skills.

3. **Job extraction**: The tool enables to extract job title from input resume and matches with the existing O*NET database.
   
4. **Skill extraction and prediction**: It also extract the skill from the resume as it contains projects and jobs and also accourding to it, it can predict the skills that user have. This can be done using the dataset that we have created and trained a model to predict skills.
<br>

<div align="center">

## How to install

</div>

Follow these steps to run the application.

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/PrinceNasit/Resume-Parser.git
   ```

3. Navigate to the project directory:
   ```bash
   cd your-repository
   ```

3. Install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Prepare Data:
   Place your resumes in any format (e.g., PDF, DOCX, LATEX, HTML)  in the current folder. Remove any existing content in this folder.
    
5. Run the project:
   Open the ResumeRevealer.ipynb file in Jupyter Notebook or JupyterLab.
   Run all the cells and you will get your output .txt file.

Python version is 3.11.4.

You can download dataset from given link : [Dataset](https://drive.google.com/drive/folders/1Pko8-of2G0smNEGJUq7I2oInJ2-C-ufn?usp=sharing)
