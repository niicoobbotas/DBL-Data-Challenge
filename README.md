# DBL-Data-Challenge
# filtering the useless information from the data
To run the script, you must have Python 3 installed. You also need to install the `tqdm` library for the progress bar. You can install `tqdm` by running:

pip install tqdm

(Mac users may need to use pip3 install tqdm if pip does not work.)

The folder structure should be organized as follows:

Project Folder/
├── README.md
├── filter_uselessinfo.py
├── data/
│    └── (All your input JSON files here)
├── datacleaned_tweets/ (This will be created automatically)

Inside the `filter_uselessinfo.py` script, make sure the folder paths are set correctly.

For Mac users, use:

json_dir_path = "/Users/your-username/Desktop/data"
output_dir_path = "/Users/your-username/Desktop/datacleaned_tweets"

For Windows users, use:

json_dir_path = "C:\\Users\\your-username\\Desktop\\data"
output_dir_path = "C:\\Users\\your-username\\Desktop\\datacleaned_tweets"

(Replace `your-username` with your actual computer username. On Windows, remember to use double backslashes `\\`.)

To run the script:

For Mac users, open Terminal and run:

cd ~/Desktop/data
python3 filter_uselessinfo.py

For Windows users, open Command Prompt (CMD) and run:

cd Desktop\data
python filter_uselessinfo.py

After running, the cleaned tweets will be saved into the `datacleaned_tweets/` folder. Each output `.json` file corresponds to one processed input file. Only tweets containing airline names are retained.

If some JSON files are invalid or corrupted, the script automatically skips them and continues. The script also displays a real-time progress bar using the `tqdm` library.
