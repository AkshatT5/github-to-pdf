## GitHub Repo to PDF

This Python script allows you to generate a PDF document from a GitHub repository, including syntax highlighting for code files. It's a useful tool for code review, documentation, or offline reading of repository contents.

****Features****

- Clones a GitHub repository
- Generates a PDF with repository contents
- Implements syntax highlighting for code files
- Includes a table of contents for easy navigation
- Allows customization of included/excluded files and directories
- Provides a progress bar for visual feedback during PDF generation

****Installation****

1. Clone this repository:
   ```bash
   git clone https://github.com/AkshatT5/github-to-pdf.git
   cd github-to-pdf
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv github_to_pdf_env
   source github_to_pdf_env/bin/activate  # On Windows, use github_to_pdf_env\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

****Usage****

Run the script from the command line:
```bash
python github_to_pdf.py [REPO_URL] [OPTIONS]
```
If you don't provide a REPO_URL, the script will prompt you to enter one.

****Options****

- `--include-dirs`: Additional directories to include (space-separated)
- `--include-files`: Additional files to include (space-separated)
- `--include-extensions`: Additional file extensions to include (space-separated)
- `--max-file-size`: Maximum file size to include in bytes (default: 100000)

****Example****

```bash
python github_to_pdf.py https://github.com/username/repo --include-dirs extra_dir1 extra_dir2 --include-files important.txt --include-extensions .cfg --max-file-size 200000
```

****Customization****

You can customize the script by modifying the following variables in the `github_to_pdf.py` file:

- `EXCLUDED_EXTENSIONS`: File extensions to exclude
- `EXCLUDED_DIRECTORIES`: Directories to exclude
- `ALWAYS_INCLUDE_FILES`: Files to always include, even if in excluded directories

****Contributing****

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

****License****

This project is licensed under the MIT License - see the LICENSE file for details.

****Acknowledgments****

- GitPython for Git repository handling
- ReportLab for PDF generation
- Pygments for syntax highlighting
- tqdm for the progress bar

****Contact****

Akshat Tiwari - akshattiwariat@gmail.com  
Project Link: [GitHub Repository](https://github.com/AkshatT5/github-to-pdf)
