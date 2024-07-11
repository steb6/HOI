import requests
import os

def check_url_exists(url):
    """Check if the URL exists."""
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking URL {url}: {e}")
        return False

def download_file(url, download_folder='downloads'):
    """Download the content from the URL."""
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = os.path.join(download_folder, url.split('/')[-1])
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url}, status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def main(urls):
    for url in urls:
        if check_url_exists(url):
            download_file(url)
        else:
            print(f"URL does not exist: {url}")

if __name__ == "__main__":
    # Example list of URLs
    urls = [
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject1_rgbd_images.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject3_rgbd_images.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject4_rgbd_images.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject5_rgbd_images.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/humanactivities/data/README_images.txt",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject1_rgbd_rawtext.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject3_rgbd_rawtext.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject4_rgbd_rawtext.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/web3/CAD-120/data/Subject5_rgbd_rawtext.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/humanactivities/data/README_raw.txt",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/humanactivities/data/Subject1_annotations.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/humanactivities/data/Subject3_annotations.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/humanactivities/data/Subject4_annotations.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/humanactivities/data/Subject5_annotations.tar.gz",
        "https://web.archive.org/web/20200728130201/http://pr.cs.cornell.edu/humanactivities/data/README_annotations.txt",
    ]
    main(urls)