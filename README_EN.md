# Automatic Installation Tool for Bug Bounty Tools

`Translated by google.`

Este README está disponível em outros idiomas:
- [Português](README.md)

This tool automates the installation of several tools used in _bug bounty_ and _pentesting_. The script checks if the tools are already installed on the system and, if not, automatically installs them, including the necessary dependencies.

## Installed Tools

The installed tools are organized into the following categories:

### 1. Reconnaissance Tools

- **Amass**: Powerful tool for subdomain reconnaissance and network mapping.
- **Assetfinder**: Tool for finding subdomains associated with a domain using multiple online sources.
- **Subfinder**: Subdomain enumeration tool with support for a variety of sources.
- **Chaos**: Domain enumeration tool from ProjectDiscovery's Chaos service.
- **Hakrawler**: A simple web crawler used for discovering hidden endpoints on websites.
- **Httpx**: Fast and configurable URL scanner, supports header capture, HTTP status validation, and more.
- **Gau**: Gathers archived URLs from the Wayback Machine, Common Crawl, and others for security analysis.
- **Waybackurls**: Collects URLs archived by the Wayback Machine to perform tests on old content. 
- **DNSgen**: Generates subdomain variations from a domain, useful for discovering subdomains by mutation.
- **GetJS**: Tool for extracting links from JavaScript files and identifying possible interesting endpoints.
- **Hakrevdns**: Tool for performing _reverse DNS lookup_, allowing the discovery of hosts from IP addresses.
- **Haktldextract**: Tool for extracting TLDs (top-level domains) and SLDs (second-level domains) from URLs.
- **Cariddi**: Fast web crawler with support for vulnerability detection and data exfiltration from URLs.
- **Naabu**: Fast port scanner that uses the `libpcap-dev` package to perform scans.

### 2. Fuzzing Tools

- **Ffuf**: Fast fuzzing tool, excellent for finding hidden directories and files in web applications.
- **Bhedak**: Automation tool for fuzzing, useful for discovering security vulnerabilities.
- **Qsreplace**: Utility for replacing query string parameters in URLs, very useful in fuzzing tests.
- **Dalfox**: Tool for discovering XSS vulnerabilities in web applications, ideal for security testing.

### 3. Vulnerability Detection Tools

- **Dalfox**: Tool for discovering XSS vulnerabilities in web applications.
- **Jaeles**: Automation framework for security testing with support for attack customization.
- **SQLMap**: Powerful tool for automating SQL injection tests and exploiting related flaws.
- **Airixss**: XSS scanner that automatically tests applications for Cross-Site Scripting vulnerabilities.
- **Shuffledns**: Fast tool for resolving subdomains that uses multiple sources and resolvers.

### 4. Notification and Automation Tools

- **Notify**: Tool for personalized notifications, ideal for integrating with security tools and receiving alerts.
- **Rush**: Tool for parallel execution of commands with resource limit control, ideal for large-scale automation.

### 5. Other Useful Tools

- **Anew**: Utility for manipulating lists, adds new entries without duplicating them.
- **Freq**: Tool for analyzing HTTP response frequencies, useful for identifying anomalous patterns in large sets of responses.
- **Gowitness**: Takes screenshots of web pages, collects information and generates reports. 
- **Goop**: Utility for parsing Go.mod files, useful for managing dependencies in Go projects.
- **Haklistgen**: Generates custom wordlists for brute force attacks based on various techniques.
- **Unfur**: Utility for parsing URLs and extracting useful components.
- **Page-fetch**: Utility for scraping web page content, useful for further analysis.
- **Cf-check**: Checks if an IP address is protected by Cloudflare.
- **Hednsextractor**: Tool for extracting DNS information from HTTP headers.

## Requirements

Before running the script, make sure you have the following dependencies installed:

- **Python 3**: The script uses Python to execute some commands.
- **Git**: Required to clone tool repositories.
- **Go**: Some tools need to be installed via `go install`. 
- **Apt**: The script uses `apt` to install some dependencies and tools.

## Installation

### 1. Cloning the repository

First, clone this repository to your system:

```bash
git clone https://github.com/DavidJovino/bugbounty_installers.git
cd bugbounty_installers
```

2. Running the installation script

Run the `install_tools.py` script to automatically install the tools:

```bash
python3 install_tools.py
```

3. Setting environment variables for Go

If you haven't already set up the environment for Go, the script automatically adds the following environment variables to your shell configuration file (`~/.bashrc` or `~/.zshrc`):

```bash
export GOROOT=/usr/lib/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```

After executing the script, run the command below to load the new environment variables:

```bash
source ~/.bashrc
# or if using Zsh
source ~/.zshrc
```

4. Tools that require dependencies

For some tools, the script also automatically installs the necessary dependencies. For example, for **Naabu**, the script ensures that the `libpcap-dev` package is installed.

### Usage

After running the installation script, the tools will be available on your system. You can use them directly in the terminal, for example:

```bash
amass enum -d example.com
subfinder -d example.com
naabu -host example.com
```

How it Works

1. The script checks if the tools are already installed on the system.
2. If a tool is not installed, the script automatically downloads and installs it.
3. The script also installs any necessary dependencies (such as `libpcap-dev` for Naabu).
4. Go tools are installed in the `$GOPATH/bin` directory.

Adding New Tools

If you want to add new tools to the automatic installation list, edit the `tools` dictionary in the `install_tools.py` file as follows:

```python
tools = {
"NewTool": {"check": lambda: is_go_tool_installed("newtool"), "install": lambda: install_go_program("NewTool", "github.com/example/newtool")},
}
```
Just add the new tool as per the example above, specifying how to check for installation and how to proceed to install it.
Contributing

Contributions are welcome! If you want to add new features or fix bugs, please follow the steps below:

1. *Fork* this repository.
2. Create a *branch* for your feature (`git checkout -b my-feature`).
3. *Commit* your changes (`git commit -m 'Add new feature'`).
4. Push the *branch* to your repository (`git push origin my-feature`).
5. Open a *pull request*.