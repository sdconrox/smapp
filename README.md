# SMAPP (Spam App)

**Disclaimer: This script is for educational and ethical cybersecurity research purposes only. Do not use it to attack or disrupt any unauthorized system or service.**

## Overview

`smapp.py` is a Python script that generates and submits randomized fake login data to a target URL, simulating form submissions through proxies with randomized user agents. This tool can be useful for:

- Testing how a web form handles spam/fake data.
- Overwhelming phishing pages with bogus credentials to reduce the likelihood of successful credential theft.
- Demonstrating the importance of bot protection and CAPTCHA.

Despite the commits being recent, this was written years ago without the help of an LLM.

## Features

- Random email and password generation using the [`Faker`](https://faker.readthedocs.io/en/master/) library.
- Random User-Agent spoofing.
- Proxy rotation using the [pubproxy.com](https://pubproxy.com/) API.
- Configurable number of submissions (`smapps`), proxy request iterations, and proxy list limits.
- Verbose logging to stdout.

## Requirements

- Python 3.6+
- `requests`
- `faker`

Install dependencies via pip:

```bash
pip install -r requirements.txt
```

Contents of requirements.txt:

    requests
    faker

## Installation

1. Clone the repo.
1. Build the wheel:

        python -m build --wheel

1. Install with pip:

        pip install dist/smapp-0.1.0-py3-none-any.whl

## Usage

```bash
python smapp.py -u https://example.com/login -s 25 -i 2 -l 15
```

### Arguments

Argument             | Description                                        | Default                   |
|--------------------|----------------------------------------------------|---------------------------|
-u, --url            | Target URL to send fake form data to               | https://httpbin.org/post  |
-s, --smapps         | Number of fake submissions to send                 | 10                        |
-i, --iterator-range | Number of times to fetch proxy lists from pubproxy | 1                         |
-l, --list-limit     | Number of proxies to request per iteration         | 10                        |


### Example

```bash
python smapp.py -u https://phishy-site.com/login -s 100 -i 5 -l 10
```

This sends 100 fake login submissions using proxies from 5 separate proxy list fetches, each returning 10 proxies.

## Ethical Use

This script is designed to target malicious phishing pages and should only be used against systems you own or have explicit permission to test. Misuse of this script may be illegal and unethical.

Author: Shane Conroy
License: MIT (modify as needed)
