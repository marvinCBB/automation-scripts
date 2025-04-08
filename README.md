# Wikipedia Data Fetcher and Renamer

This Python automation script fetches content from a list of Wikipedia pages, saves each page's text to a file, analyzes word frequency, and renames the file using the most common word in the content (excluding stop words). 

After renaming, all files are sorted by size, and a numeric index is added as a prefix to each filename. This ensures files are clearly organized in order of content length.

## 🚀 Features

- Scrapes and saves Wikipedia pages as `.txt` files
- Analyzes each file for word frequency and renames it using the most common word
- Adds a numerical prefix to each file name based on its size
- Outputs a clean, sorted list of files

## 🛠 Requirements

- Python 3.x
- Required packages:
  - `requests`
  - `beautifulsoup4`

You can install them with:

```bash
pip install requests beautifulsoup4
```

## 📦 How to Use

1. Clone the repository:
```bash
git clone https://github.com/marvinCBB/automation-scripts.git
```

2. Navigate into the project folder:
```bash
cd automation-scripts
```

3. Run the script:
```bash
python wikipedia_fetcher.py
```

You can customize the list of Wikipedia pages directly inside the script.

## 👨‍💻 Author

**marvinCBB**  
Freelance automation & coding enthusiast  
Follow me on GitHub: [github.com/marvinCBB](https://github.com/marvinCBB)
