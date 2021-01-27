# points-card-reloader

Reload your Optimum Card offers using Python, Selenium WebDriver, and Firefox.

## Installation and Configuration

Instructions are for a Linux environment.

1. Ensure python 3.7 or higher is installed.

2. Install the prerequisite packages:
    
    `python -m pip install selenium`
    
    `python -m pip install keyring`
    
3. Download [Firefox](https://www.mozilla.org/en-US/firefox/linux/) 
and [Geckodriver](https://github.com/mozilla/geckodriver/releases).  

4. Clone this repository to a location on your machine.

5. Securely store your Optimum login information in your local keyring.
    
    For example, on Debian Linux 10, run `seahorse` to launch the Passwords and Keys utility.
    
    Create a new password, name it `optimum-card`.
    
    Enter the email address and password associated with your Optimum account and save. 

6. In the project repository, edit `config.json`

    Set the paths to your firefox and geckodriver binaries.
    
    Set the path where you want the script to log to.
    
    `application_name` must match the name of the password entry in your keyring, e.g. `optimum-card`.
    
    `user_name` must match the username in the `optimum-card` password entry, 
    i.e. the email address used to log into your Optimum account.
    
## Running the Script

Run the script: `python reload-card.py`

The script will log in, view the offers page, thereby loading the week's offers,
and write the points balance to the log.

The script does not log credentials.  
The script sets the Geckodriver log level to error which does not log sendkeys.    

View the log: `tail -n 10 reload-points-log.txt`

A successful run will have log prints like the following:

```
2021-01-27 14:46:30.386224:Preparing options, capabilities, and profile
2021-01-27 14:46:30.451071:Instantiating webdriver
2021-01-27 14:46:39.380743:Visiting landing page
2021-01-27 14:46:39.383522:Visiting login page
2021-01-27 14:46:56.500674:Visiting offers page
2021-01-27 14:47:08.381080:Points available: 166,146
2021-01-27 14:47:09.735988:Signed out
2021-01-27 14:47:13.027270:Quit driver
```