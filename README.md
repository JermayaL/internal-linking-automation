# internal-linking-automation
Automate Internal Linking With Python
&nbsp;
This script was rewritten from an existing script of Jonathan Boshoff: https://jonathanboshoff.com/automate-internal-linking-with-python/.

**The difference: His script is run with Google Colab. This script has been rewritten for use in any IDE.**

Commands (based on the article of Jonathan Boshoff you have do steps 3.
I used Pycharm and Python. Be sure you have both an IDE as Pycharm and Python installed on your computer.

Pycharm: https://www.jetbrains.com/pycharm/download/?section=mac
Python: https://www.python.org/downloads/

Installed above correctly?
Make sure you have your own API key from Google Console Cloud and create your own Search Engine.

https://programmablesearchengine.google.com/
https://console.cloud.google.com/

**Commands**
<ol>
  <li>Follow step 3 carefully.</li>
  <li>Download Pycharm and Python</li>
  <li>Create a project in Pycharm and drag the input.csv and main.py into the project</li>
  <li>Go below to 'Terminal' and typ: pip install -r requirements.txt</li>
  <li>Make sure the input.csv itself is populated with your own URLs and keywords</li>
  <li>Now you could run the script by: python main.py</li>
</ol>

**Why create my own search engine?**
It allows you to bypass restrictions. Google doesn't like it when people scrape search results, and you can get quickly blocked. But if you register your own search engine, you can overcome this restriction.
