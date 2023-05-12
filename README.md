# News Links Emailer

This program emails you 20 different news links about the topic you want. It uses the [News API](https://newsapi.org/) to fetch news articles from different sources. The default topic is "Tesla", but you can specify any topic you want. The program is set up to run every 24 hours with the help of Pythonanywhere.com.

## Getting Started

### Prerequisites

Before running this program, you need to have a News API key. You can get a free key by signing up [here](https://newsapi.org/register). 

### Installing

1. Clone this repository or download the ZIP file and extract its contents.
2. Install the required packages by running `pip install -r requirements.txt`.

### Running the Program

1. Set your News API key to the varable named api_key.
2. In `main.py`, set the `topic` variable to the topic you want to get news about. If you don't specify a topic, the default is "Tesla".
3. In `send_email.py`, set the sender's and receiver's email variables to the email addresses you want to use for sending and receiving emails.
4. Run `main.py` to fetch news articles and send an email with links to those articles. 

### Running the Program on Pythonanywhere.com

1. Create an account on [Pythonanywhere.com](https://www.pythonanywhere.com/).
2. Upload your code to Pythonanywhere.com using their file browser.
3. Set your News API key as an environment variable by going to the "Consoles" tab and running the command `export api_key = your_api_key`.
4. Go to the "Tasks" tab and set up a new task to run `main.py` once a day.
5. Set up your email credentials in the same way as described in the previous section.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
