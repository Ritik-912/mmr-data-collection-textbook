# PDF Collection for Multimodal and Multilingual Reasoning Tasks

This repository is dedicated to collecting PDFs from the National Digital Library of India (https://ndl.iitkgp.ac.in/) for use in multimodal and multilingual reasoning tasks. The process involves multiple steps and scripts, running on both Windows and Linux machines, to ensure the accurate and comprehensive collection of PDF URLs and their subsequent downloads.

## Repository Overview

The repository contains the following scripts and their respective purposes:

1. **link_scrapper.py**: Scrapes initial PDF viewer links and saves them.
2. **download_link_collector.py**: Collects exact PDF URLs from the viewer pages.
3. **missing_url.py**: Identifies missed URLs during the scraping process.
4. **downloader.py**: Downloads the PDFs using the collected URLs.

## Detailed Process

### 1. Scraping PDF Viewer Links

- **Script**: [link_scrapper.py](https://github.com/Ritik-912/mmr-data-collection/blob/main/link_scrapper.py)
- **Environment**: Windows 11
- **Description**: Utilizes Selenium with Firefox browser to open the browsing page on the NDLI website and scrolls to load all the PDF viewer links.
- **Output**: [scrapped_url.csv](https://github.com/Ritik-912/mmr-data-collection/blob/main/scrapped_url.csv) containing the initial list of PDF viewer links.

### 2. Collecting Exact PDF URLs

- **Script**: [download_link_collector.py](https://github.com/Ritik-912/mmr-data-collection/blob/main/download_link_collector.py)
- **Environment**: Windows 11
- **Description**: Extracts the exact PDF URLs from the viewer pages.
- **Output**: 
  - [download_url.csv](https://github.com/Ritik-912/mmr-data-collection/blob/main/download_url.csv): Contains 1961 PDF links.
  - [error_download_links.csv](https://github.com/Ritik-912/mmr-data-collection/blob/main/error_download_links.csv): Contains 7 error links.

### 3. Identifying Missed URLs

- **Script**: [missing_url.py](https://github.com/Ritik-912/mmr-data-collection/blob/main/missing_url.py)
- **Environment**: Windows 11
- **Description**: Identifies URLs that were missed during the initial collection.
- **Output**: [missed_url.csv](https://github.com/Ritik-912/mmr-data-collection/blob/main/missed_url.csv) containing 36 missed URLs.

### 4. Collecting Remaining Missed Links

- **Manually**: Added the missed link using MS Excel in [download_url.csv](https://github.com/Ritik-912/mmr-data-collection/blob/main/download_url.csv)
- **Environment**: Windows 11
- **Description**: Collects the remaining missed PDF URLs.

### 5. Downloading PDFs

- **Script**: [downloader.py](https://github.com/Ritik-912/mmr-data-collection/blob/main/downloader.py)
- **Environment**: Linux
- **Description**: Downloads the PDFs using the URLs in `total_download_url.csv`.
- **Output**: 
  - [excepted_download.csv](https://github.com/Ritik-912/mmr-data-collection/blob/main/excepted_downloads.csv) for links that caused exceptions during download.
  - [excepted_downloads.sh](https://github.com/Ritik-912/mmr-data-collection/blob/main/excepted_downloads.sh) script was used to attempt re-downloads, but all of them had connection timeout errors.

### Final Output

After completing the above steps, we successfully downloaded 1836 PDFs. 

### Future Work

The next step involves extracting questions from these PDFs for the multimodal and multilingual reasoning tasks.

---

Please ensure that you have the necessary dependencies installed and configured before running the scripts by installing libraries in [windows_requirements.txt](https://github.com/Ritik-912/mmr-data-collection/blob/main/windows_requirements.txt) and [linux_requirements.txt](https://github.com/Ritik-912/mmr-data-collection/blob/main/linux_requirements.txt).

For any queries or contributions, feel free to open an issue or submit a pull request.
___

### Flow Diagram:




```

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
                   | downloader.py           | ---> | excepted_download    |
                   +-------------------------+      | .csv                 |
                                                    +----------------------+
                   +-------------------------+      
                   | Final Output: 1881 PDFs | 
                   | Downloaded              | 
                   +-------------------------+   

                   +-------------------------+      
                   | Future Work: Extract    | 
                   | Questions from PDFs     | 
                   +-------------------------+ 
```
