---
title: "How to count number of words in a pdf file from Linux cli"
date: 2023-09-05T04:30:03+00:00
# weight: 1
# aliases: ["/first"]
# tags: ["first"]
author: "Me"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
# description: "Desc Text."
# canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
categories:
    - Development
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
# editPost:
#     URL: "https://github.com/<path_to_repo>/content"
#     Text: "Suggest Changes" # edit text
#     appendFilePath: true # to append file path to Edit link
---

### Using `pdftotext`:

1. **Installation**:
    - If it's not installed, you'll need to install the `poppler-utils` package which includes `pdftotext`.
    ```
    sudo apt install poppler-utils
    ```
    or
    ```
    yum install poppler-utils
    ```
    depending on your distribution.

2. **Usage**:
    - Once installed, you can convert a PDF to text and then count the words as follows:
    ```
    pdftotext input.pdf - | wc -w
    ```
    Here, `input.pdf` is your source PDF file, and `wc -w` counts the number of words. The `-` in `pdftotext` specifies that the output should be sent to stdout, which is then piped into `wc`.

### Using `pdfgrep`:

1. **Installation**:
    - Install `pdfgrep` using your package manager:
    ```
    sudo apt install pdfgrep
    ```
    or
    ```
    yum install pdfgrep
    ```

2. **Usage**:
    - `pdfgrep` is generally used for pattern matching, but you can use it to match any word characters and pipe them to `wc -w` like this:
    ```
    pdfgrep -o '\w+' input.pdf | wc -w
    ```
    This might be slower and is generally more useful when you're looking for specific words.

### Using Python with PyPDF2:

You can also create a small Python script to do the job using the `PyPDF2` library.

1. **Installation**:
    - Install PyPDF2 using pip:
    ```
    pip install PyPDF2
    ```

2. **Usage**:
    - Here's a simple Python script you could use:

    ```python
    import PyPDF2

    def count_words_in_pdf(file_path):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)
            total_words = 0
            for i in range(reader.numPages):
                page = reader.getPage(i)
                text = page.extractText()
                total_words += len(text.split())
        return total_words

    if __name__ == "__main__":
        file_path = "input.pdf"
        print(count_words_in_pdf(file_path))
    ```

    Save this script, make it executable, and run it. It will read `input.pdf` and print out the number of words.

### Using `pdf2txt.py` from the `pdfminer` suite:

1. **Installation**:
    - You can install `pdfminer` like this:
    ```
    pip install pdfminer.six
    ```

2. **Usage**:
    ```
    pdf2txt.py input.pdf | wc -w
    ```
    This command will convert the PDF to text and pipe it to `wc` to count the words.

### Performance Considerations:

- **Accuracy**: Not all methods have the same level of accuracy. Text layout in PDFs can be complicated, and the above methods might not capture all the nuances.
  
- **Speed**: Native CLI tools like `pdftotext` and `pdfgrep` are generally faster compared to Python-based solutions, which have to spin up a Python interpreter.

- **Complexity**: `pdftotext` and `pdfgrep` are easier to use for simple tasks, but Python-based solutions offer more flexibility and control.

- **Portability**: The CLI tools depend on certain packages that need to be installed, but a Python script could be more portable, especially if you're going to run it on different systems.

The method you choose will likely depend on your specific requirements. If you just need a quick and dirty solution, `pdftotext` piped into `wc` is easy and effective. For more complex requirements, such as handling multiple PDFs, incorporating additional logic, or even using more advanced text analysis techniques (like natural language processing), you might want to look at Python-based solutions. These provide the building blocks to craft a tailored solution that could evolve with your needs. The elegance of the Linux command line is that it offers a wide range of tools that can be combined in an almost infinite number of ways to solve problems both big and small. This toolbox gets even more powerful when you integrate it with scripting languages like Python, enabling you to tackle not just text-processing tasks but a multitude of other challenges as well.