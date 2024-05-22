#### Navigation
- [General](#General)
- [Nvidia](#Nvidia)
- [Git](#Git)
- [Python](#Python) 
- [Selenium](#Selenium)
- [NVM](#NVM)
- [MongoDB](#MongoDB)
- [Links](#Links)

![joshua-coleman-kFRKvJQtNHg-unsplash](https://github.com/KIlian42/Cheatsheet/assets/57774167/81efef7e-409f-4ee1-9c45-eae36f1f02d6)

# General

### Environment variables
Set environment variale
> Mac
```
export MYVARIABLE=123
echo $MYVARIABLE
```

### Test API with CURL

##### GET request
```
curl http://example.com
```

##### POST request
```
curl -X POST "http://example.com/api/endpointname" -H "accept": "application/json" -H "Content-Type: application/json" -d '{"parameter1": "Content of parameter1", "parameter2": "Content of parameter2"}'
```

##### End running process
> Mac
```
sudo lsof -i :8000
sudo kill -9 68102
```

##### Make folder, make file & delete file/folder
> Mac
```
mkdir myfolder
touch myfile.txt
rm -r myfolder myfile.txt
```

##### Vim & Nano
> Mac
```
vim myfile.txt
nano myfile.txt
```

##### Vue Git & Cloudflare deployment
Tips:<br />
Vue: When creating a new Git repo for a Vue project not forgot to push also hidden files (to view them press "Comman+Shift+."). Otherwise git clone & npm install will fail when setting up the project.<br /><br />
Cloudflare deployment:<br />
1. Just pushing updates to Git will trigger automatically the cloudbuild in Cloudflare. Expect logs in left menu tab under Workers&Pages to see if the deployment progress fails. Copy the new url endpoint (i.e. "....pages.dev"). <br />
2. Click in the left menu tab "Websites" (first tab) and choose website (middle). Click in left menu tab "DNS". Replace the new url endpoint in the DNS configuration file. 

# Nvidia

1. T4 -> 16 GB vram <br />
2. V100 -> 16 GB vram <br />
3. L2, L4 -> 24 GB vram <br />
4. RTX Quadro 8000 -> (24, 48) GB vram <br />
5. A100, H100 -> (40, 80) GB vram <br />

# Git
##### Help
```
git --help
```

##### Create branch
```
git branch "…"
git checkout -b "…"
```

##### See status
```
git status
```

##### Add all changes for next commit
```
git add *
```

##### Commit changes
```
git commit -m "First commit"
```

##### Add tag
```
git tag -a v0.1.0 -m "v0.1.0“
```

##### Push/Pull commit
```
git push
git pull
```

##### Revert all changes
```
git reset --hard HEAD
```

##### Switch branch
```
git switch "Name of branch"
git checkout "Name of branch or document/script"
```

##### Show Git history
```
git log
git log --oneline
git log --pretty=format:"%h - %an, %ar : %s"
git log --graph --decorate --oneline
```

##### Stash changes
```
git stash
git stash pop 
git stash apply (stash stays accessable accross branches)
git stash save "Add a description here"
git stash list
git stash apply stash@{0}
```

##### Merge branch
Assuming you are currently in the main branch and you want to merge the feature branch into your main branch
```
git merge feature_branch
git pull feature_branch
```

##### Delete branch
Local branch (-d safe delete, -D force delete)
```
git branch -d feature-branch
git branch -D feature-branch
```
Remote branch
```
git push origin --delete feature-branch
```

##### Clone repository
```
git clone name_of_repository
```

# Python

### Docstring template

```
"""
Description:
----
Description of function. This is '''bold'''. This is ''italic''.

Args:
----
    parameter1 (list): A list of data.
    parameter2 (str): A string describing the data.

Returns:
----
    variable1 (list): Edited list.

Raises:
----
    KeyError: Raises an exception.
```

### Pip

```
pip install --upgrade pip
```
##### Install virtualenv
```
pip install virtualenv
```

> Mac
```
python3.11 -m venv .venv
source .venv/bin/activate
deactivate
pip install -r requirements.txt
```

> Windows
```
py -3.11 -m venv .venv
.venv\Scripts\activate.bat
.venv\Scripts\deactivate.bat
pip install -r requirements.txt
```

### Poetry
...

### Formatting

###### Notice: In Python 2 a "coding: utf-8" should be added to the beginning of a script.

##### Ruff

```
pip install ruff
```
```
ruff format .
ruff check . --fix --select I
```

### Arguments

```
import argparse
parser = argparse.ArgumentParser(description="Some description")
parser.add_argument('-d','--dir',type=str,default='training2017',help='The directory of the dataset')
parser.add_argument('-t','--test_set',type=float,default=0.2,help='The percentage of test set')
args = parser.parse_args()
my_function(args.dir, test=args.test_set)
```

### Warnings, logging, error handling and testing

##### Ignore warnings
```
import warnings
warnings.filterwarnings("ignore")
```

##### Logging
```
import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger_module1 = logging.getLogger('module1')
logger_module1.setLevel(logging.INFO)
logger_module2 = logging.getLogger('module2')
logger_module2.setLevel(logging.WARNING)
logger_module1.error("An error occurred: %s", str(e), exc_info=True)
logger_module2.error("An error occurred: %s", str(e), exc_info=True)
```

##### Error handling
```
try:
	assert …
except Exception as e:
	raise(e)
```
For more, see: https://docs.python.org/3/library/exceptions.html

##### Testing
```
pip install pytest
```
All tests are within /tests directory <br />
conftest.py defines @fixtures
```
assert x
```

### Imports and pathes

##### Imports
Imports within submodules always are resolved from the working direction of the executed main script. Submodules only know files within the working direction of the main executed script or within the same folder. To extend the path knowledge from parent folders of the submodule, do the following:
```
pip install path
```
```
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
import ..
```
directory.parent -> folder of current file <br />
directory.parent.parent -> parent folder


More: https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import
```
import sys
sys.path.append("..")
```
##### Join path file (relative pathes)

File opening works different than imports, since the relative file reading path starts only from the working direction of the project .venv folder. Also, do not add "/" at the beginning of the relative path, otherwise the path will not get resolved. A better way to open files is by (also here do not use "/" to join the second path):

```
import os
current_path = os.getcwd() # or os.path.dirname(os.path.abspath(__file__))
file_name = „src/folderX/file.txt“
full_file_path = os.path.join(current_path, file_name)
full_file_path = os.path.join(os.getcwd(), file_name)
```

##### Working direction
```
import os
print(os.getcwd()) # Working direction (project .venv folder)
print(os.path.dirname(os.path.abspath(__file__))) # Working direction (current script folder)
```

### Files

##### Delete file if exist
```
import os
if os.path.exists(file_path):
	os.remove(file_path)
```

##### Open file
```
f = open("file.txt", "r", encoding="utf-8")
data = f.readlines()
f.close()
```

##### Write file
```
f = open("file.txt", "w", encoding="utf-8")
f.writelines(data)
# f.write(data)
f.close()
```

##### Write file "with open“
```
with open('file.txt', 'w', encoding='utf-8') as file:
    file.writelines(html_content)
```

##### Iterate through files in folder
```
import os
directory = 'src/dataset‘
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
```

### JSON

##### Load file into dict
```
import json
with open(file_path, 'r') as file:
	data = json.load(file)
```

##### Load string into dict
```
import json
data = json.loads(str)
```

##### Save list as JSON
```
with open('json_file.json', 'w') as file:
        json.dump(json_list, file, indent=2)
```

### List

##### Process list (inline)
```
lst = [x+x for x in lst]
```

##### Map list
```
data = list(map(lambda x: x.replace("\n", ""), data))
```

##### Join list
```
joined_lst = '; '.join(lst)
```

##### Transpose list
```
data = [list(row) for row in zip(*data)]
```

##### Overlap of two lists
```
set = set(lst1).intersection(lst2)
if set:
	…
```

##### Sort nested list
```
combined = list(zip(lst1, lst2))
combined.sort(key=lambda x: x[1])
lst1, lst2 = zip(*combined)
lst1 = list(lst1)
lst2 = list(lst2)
```

##### Shuffle nested list
```
import random
combined = list(zip(X, Y, Z))
random.shuffle(combined)
X, Y, Z = zip(*combined)
X = list(X)
Y = list(Y)
Z = list(Z)
```

##### Count unique values in list
```
from collections import Counter
count = Counter(lst)
print(count)
```

##### Extract unique values from list
```
Ist = list(set(lst))
```

##### Count double values in one list
```
from collections import Counter
count = Counter(Ist)
doubles_count = {item: c for item, c in count.items() if c > 1}
```

##### Get double values in two lists
```
doubles = [item for item in list1 if item in list2]
```

### Queue
```
import queue
q = queue.Queue()
q.qsize()
q.put()
q.get()
```

### Pandas

###### Note: Pandas is slower, but a powerful tool.

##### Read csv
```
df = pd.read_csv(file_path, delimiter=";")
```
##### Drop nan
```
df.dropna(inplace=True)
```
##### Iterate rows and columns
```
for index, row in df.iterrows():
	column1_value = row["Column1“]
   	column2_value = row["Column2“]
```
```
for column in df.columns:
    print(column, df[column].head()) 
for column_name, data in df.items():
    print(column_name, data.head())  # Example operation
```
##### Access row 3 and column 2 with iloc
```
third_row_value = df.iloc[2, 1]
```

### Time and TQDM

##### Pause
```
import time
time.sleep(2)
```

##### Measure time
```
from datetime import datetime
start=datetime.now()
print(f"Duration: {datetime.now()-start}")
```

##### TQDM
```
from tqdm import tqdm
for i in tqdm(lst):
    ...
for index, row in enumerate(tqdm()): # (for enumerate)
    ...
```

##### TQDM (manually update)
```
pbar = tqdm(total=total_number, desc="Load data")
loop:
	pbar.update(1)
```

### Multithreading and Multiprocessing
##### Multiprocessing
Count CPUs
```
import os
num_cores = os.cpu_count()
print("Number of CPUs:", num_cores)
```

```
import multiprocessing
from tqdm import tqdm

def extract_features(input_list, list_index, new_shared_list, lock):
    for x in tqdm(input_list, desc=f“Process {list_index}", position=list_index, leave=False):
        try:
		new_value … do something …
                with lock:
                    new_shared_list.extend(new_value)
        except Exception as e:
            pass

manager = multiprocessing.Manager()
all_features = manager.list()
lock = manager.Lock()
num_processes = 4 # multiprocessing.cpu_count()

processes = []
for sublist_index in range(num_processes):
	p = multiprocessing.Process(target=extract_features, args=(lst[list_index], list_index, new_lst, lock))
        processes.append(p)
        p.start()

for process in processes:
        process.join()
```

### Regex

##### Remove multiple whitespaces
```
new_text = re.sub(" +", " ", text)
```

##### Remove special characters except a-z, A-Z and whitespace
```
new_text = re.sub("[^a-zA-ZäöüÄÖÜß ]", "", text)
```

# Selenium

##### Tips:
- Avoid getting blocked -> download pages 
- Lazy loading -> scroll to bottom
- Iframes -> driver.switch_to.frame("iframeClassOrID")
- https://medium.com/@pankaj_pandey/web-scraping-using-python-for-dynamic-web-pages-and-unveiling-hidden-insights-8dbc7da6dd26
- https://pypi.org/project/selenium-stealth/

```
pip install selenium
```

##### Save and load html file:
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

page = ""
driver.get(page)
html_content = driver.page_source
with open("src/data/example.html", "w", encoding="utf-8") as file:
	file.write(html_content)
driver.get("file:/Users/kiliankramer/Desktop/example.html")
```

##### Close driver
```
driver.close() # closes current window
driver.quit() # shuts down driver
```

##### Wait for input
```
If driver.find_element("XPATH", "//*[@id="L2AGLb"]"):
	input("CAPTCHA…")
```
##### Accept cookies
```
driver.find_element("path", "//*[@id="L2AGLb"]").click()
```

##### Find elements
```
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, "//div[@class='link-text padding-s ng-binding ng-scope']") # <- best
driver.find_element("id", "anyIDname")
driver.find_element(By.ID, "anyIDname")
driver.find_element(By.CLASS_NAME, "anyCLASSname")
(By.tagname, "p")
```

##### Interact with element
```
element.send_keys("input")
element.click()
```

##### Get div itself
```
inner_html = element.get_attribute("innerHTML") # string
outer_html = element.get_attribute("outerHTML") # string
inner_html = element.text
id = element.get_attribute("id")
```

##### Some helper queries
```
from selenium.webdriver.common.by import By
element = driver.find_element() and element.find_element() is also possible:
all_elements = driver.find_elements(By.XPATH, "//*")
parent_element = element.find_element(By.XPATH, "..")
child_element = element.find_element(By.XPATH, "./*") # Finds first child element -> find_elements() would fine all child elements of a specific HTML tag
ancestor_element = element.find_element(By.XPATH, "./preceding::*[1]")
successor_element = element.find_element(By.XPATH, "./following::*[1]")
```

# NVM
Node Version Manager
```
brew install nvm
source $(brew --prefix nvm)/nvm.sh
nvm install 18
nvm install 21
nvm list
nvm use 18
nvm version
```

# MongoDB

##### List, start and stop MongoDB instances
```
brew services list
brew services start mongodb/brew/mongodb-community@5.0
brew services stop mongodb/brew/mongodb-community@5.0
```

##### Start MongoDB shell
```
mongosh
mongosh "mongodb://localhost:27017"
quit
```

##### MongoDB shell commands
```
show dbs
use tutorial
db.dropDatabase('tutorial')
db.createCollection('products')
show collections
db.dropCollection('products')
```

# Links

##### LLM leaderboards
https://artificialanalysis.ai <br />
https://chat.lmsys.org/?leaderboard <br />
https://huggingface.co/spaces/mteb/leaderboard <br />

##### Dataset sources
https://huggingface.co/datasets <br />
https://www.kaggle.com/datasets <br />
https://commoncrawl.org <br />
https://dumps.wikimedia.org


##### Further links
https://vast.ai <br />
https://groq.com <br />
https://ollama.com <br />
https://github.com/settings/personal-access-tokens  <br />
see: https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#:~:text=creating%20GitHub%20Apps.%22-,Creating%20a%20personal%20access%20token,Click%20Generate%20new%20token. <br />