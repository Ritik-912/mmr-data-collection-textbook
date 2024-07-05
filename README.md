# PDF Collection for Multimodal and Reasoning Tasks

This repository is dedicated to collecting PDFs from the National Digital Library of India (https://ndl.iitkgp.ac.in/) for use in multimodal and reasoning tasks. The process involves multiple steps and scripts, running on both Windows and Linux machines, to ensure the accurate and comprehensive collection of PDF URLs and their subsequent downloads.

## Repository Overview

The repository contains the following scripts and their respective purposes:

1. **link_scrapper.py**: Scrapes initial PDF viewer links and saves them.
2. **download_link_collector.py**: Collects exact PDF URLs from the viewer pages.
3. **missing_url.py**: Identifies missed URLs during the scraping process.
4. **download_missed_links_collector.py**: Collects remaining missed PDF URLs.
5. **total_download_url.py**: Aggregates all PDF download URLs.
6. **downloader.py**: Downloads the PDFs using the collected URLs.
7. **excepted_downloads.sh**: Attempts to download PDFs that initially failed.

## Detailed Process

### 1. Scraping PDF Viewer Links

- **Script**: [link_scrapper.py](link to file)
- **Environment**: Windows 11
- **Description**: Utilizes Selenium with Firefox browser to open the browsing page on the NDLI website and scrolls to load all the PDF viewer links.
- **Output**: `scrapped_url.csv` containing the initial list of PDF viewer links.

### 2. Collecting Exact PDF URLs

- **Script**: [download_link_collector.py](link to file)
- **Environment**: Linux
- **Description**: Extracts the exact PDF URLs from the viewer pages.
- **Output**: 
  - `download_url.csv`: Contains 1961 PDF links.
  - `error_download_links.csv`: Contains 7 error links.

### 3. Identifying Missed URLs

- **Script**: [missing_url.py](link to file)
- **Environment**: Linux
- **Description**: Identifies URLs that were missed during the initial collection.
- **Output**: `missed_url.csv` containing 36 missed URLs.

### 4. Collecting Remaining Missed Links

- **Script**: [download_missed_links_collector.py](link to file)
- **Environment**: Linux
- **Description**: Collects the remaining missed PDF URLs.
- **Output**: 
  - `remaining_download_url.csv`
  - `error_download_links(1).csv`

### 5. Aggregating All Download URLs

- **Script**: [total_download_url.py](link to file)
- **Environment**: Linux
- **Description**: Aggregates all PDF download URLs into a single file.
- **Output**: `total_download_url.csv`

### 6. Downloading PDFs

- **Script**: [downloader.py](link to file)
- **Environment**: Linux
- **Description**: Downloads the PDFs using the URLs in `total_download_url.csv`.
- **Output**: 
  - `excepted_download.csv` for links that caused exceptions during download.
  - `excepted_downloads.sh` script was used to attempt re-downloads, but all of them had connection timeout errors.

### Final Output

After completing the above steps, we successfully downloaded 1881 PDFs. 

### Future Work

The next step involves extracting questions from these PDFs for the multimodal and reasoning tasks.

---

Please ensure that you have the necessary dependencies installed and configured before running the scripts by installing libraries in `requirements.txt`.

For any queries or contributions, feel free to open an issue or submit a pull request.

+------------+      +-------------------------+      +----------------------+
|            | ---> | link_scrapper.py        | ---> | scrapped_url.csv     |
|   Start    |      +-------------------------+      +----------------------+
|            | 
+------------+
                   +-------------------------+      +----------------------+
                   | download_link_collector | ---> | download_url.csv     |
                   | .py                     |      | error_download_links |
                   +-------------------------+      +----------------------+

                   +-------------------------+      +----------------------+
                   | missing_url.py          | ---> | missed_url.csv       |
                   +-------------------------+      +----------------------+

                   +-------------------------+      +----------------------+
                   | download_missed_links   | ---> | remaining_download_url|
                   | _collector.py           |      | .csv                 |
                   +-------------------------+      | error_download_links |
                                                    | (1).csv              |
                                                    +----------------------+
                   +-------------------------+      +----------------------+
                   | total_download_url.py   | ---> | total_download_url   |
                   +-------------------------+      | .csv                 |
                                                    +----------------------+
                   +-------------------------+      +----------------------+
                   | downloader.py           | ---> | excepted_download    |
                   +-------------------------+      | .csv                 |
                                                    +----------------------+
                   +-------------------------+      +----------------------+
                   | excepted_downloads.sh   | ---> | Connection timeout   |
                   +-------------------------+      | errors               |
                                                    +----------------------+
                   +-------------------------+      
                   | Final Output: 1881 PDFs | 
                   | Downloaded             | 
                   +-------------------------+   

                   +-------------------------+      
                   | Future Work: Extract    | 
                   | Questions from PDFs     | 
                   +-------------------------+ 
