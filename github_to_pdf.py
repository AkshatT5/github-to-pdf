import os
import shutil
from git import Repo
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
import html
import textwrap

print("Script is starting")

EXCLUDED_EXTENSIONS = {
    '.pdf', '.md', '.txt', '.log',
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot',
    '.csv', '.tsv', '.xls', '.xlsx', '.doc', '.docx',
    '.zip', '.tar', '.gz', '.rar'
}

EXCLUDED_DIRECTORIES = {
    'node_modules', 'dist', 'build', '.git', '.github', '.idea', '.vscode',
    'test', 'tests', 'docs', 'images', 'img', 'assets'
}

ALWAYS_INCLUDE_FILES = {
    'package.json', 'package-lock.json', 'yarn.lock', 'tsconfig.json', 'babel.config.js', 'webpack.config.js'
}

def clone_repo(repo_url, local_path):
    print(f"Cloning {repo_url} to {local_path}")
    if os.path.exists(local_path):
        print(f"Directory {local_path} already exists. Removing it...")
        shutil.rmtree(local_path)
    Repo.clone_from(repo_url, local_path)
    print("Clone complete")

def should_include_file(file_path):
    file_name = os.path.basename(file_path)
    if file_name in ALWAYS_INCLUDE_FILES:
        return True
    _, ext = os.path.splitext(file_path)
    if ext.lower() in EXCLUDED_EXTENSIONS:
        return False
    parts = file_path.split(os.sep)
    for part in parts:
        if part.lower() in EXCLUDED_DIRECTORIES:
            return False
    return True

def get_file_contents(file_path):
    print(f"Reading file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return html.escape(file.read())
    except UnicodeDecodeError:
        return "[File content could not be decoded as UTF-8]"

def wrap_text(text, width=80):
    wrapped_lines = []
    for line in text.split('\n'):
        wrapped_lines.extend(textwrap.wrap(line, width=width) or [''])
    return '\n'.join(wrapped_lines)

def create_pdf(repo_path, pdf_path):
    print(f"Creating PDF: {pdf_path}")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=0.5*inch, rightMargin=0.5*inch, topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    story = []

    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=8,
        leading=10,
        alignment=TA_LEFT,
        leftIndent=0,
        rightIndent=0,
    )

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d.lower() not in EXCLUDED_DIRECTORIES]
        for file in files:
            file_path = os.path.join(root, file)
            if not should_include_file(file_path):
                continue
            relative_path = os.path.relpath(file_path, repo_path)
            print(f"Adding file to PDF: {relative_path}")
            story.append(Paragraph(f"<b>{relative_path}</b>", styles['Heading2']))
            story.append(Spacer(1, 12))
            content = get_file_contents(file_path)
            wrapped_content = wrap_text(content)
            story.append(Preformatted(wrapped_content, code_style))
            story.append(Spacer(1, 12))

    doc.build(story)
    print("PDF creation complete")

def cleanup_old_pdfs(directory='.'):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf') and filename.startswith('repository_contents'):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                print(f"Deleted old PDF: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {str(e)}")

def main():
    print("Entering main function")
    try:
        cleanup_old_pdfs()
        repo_url = input("Enter the GitHub repository URL: ")
        print(f"Repository URL entered: {repo_url}")
        local_path = "./temp_repo"
        pdf_path = "repository_contents.pdf"
        print("Cloning repository...")
        clone_repo(repo_url, local_path)
        print("Generating PDF...")
        create_pdf(local_path, pdf_path)
        print("Cleaning up...")
        shutil.rmtree(local_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Calling main function")
    main()

print("Script has finished")