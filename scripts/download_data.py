import os
import subprocess

DATA_DIR = "data/raw"
DATASET = "thoughtvector/customer-support-on-twitter"


def download_dataset():
    """
    Download the Customer Support on Twitter dataset using the Kaggle API.
    Requires Kaggle credentials (kaggle.json).
    """

    try:
        subprocess.run(
            [
                "kaggle",
                "datasets",
                "download",
                "-d",
                DATASET,
                "-p",
                DATA_DIR,
                "--unzip",
            ],
            check=True,
        )
        print("Dataset downloaded and extracted successfully.")

    except FileNotFoundError:
        print("Error: Kaggle CLI not installed.")
        print("Install it with: pip install kaggle")

    except subprocess.CalledProcessError:
        print("Error: Dataset download failed.")
        print("Make sure Kaggle API credentials are configured.")


if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    download_dataset()