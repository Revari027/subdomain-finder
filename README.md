# 🔍 Subdomain Finder

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A sleek and simple command-line tool to find subdomains — via **passive** (CRT.SH) or **brute-force** using custom wordlists.

> Built by `caramell_revv` – Universitas Negeri Jakarta

---

## ✨ Features

- 🚀 Passive subdomain enumeration via [crt.sh](https://crt.sh)
- 🧠 Brute-force subdomain using wordlists
- 📊 Beautiful terminal UI using `rich`
- 🧾 Save results to file
- 🖥️ Cross-platform (Windows & Linux)

---

## 🧰 Requirements

- Python 3.9+
- `pip install` dependencies:

```bash
pip install -r requirements.txt
```
## 📦 Installation
```bash
git clone https://github.com/Revari027/subdomain-finder.git
cd subdomain-finder
python -m venv .venv
.venv\Scripts\activate    # ⬅️ Windows
# source .venv/bin/activate  ⬅️ Linux/MacOS
pip install -r requirements.txt
```

## 💻 Usage
```bash
python finder.py
```

## 🔧 What You'll Be Asked
1. Enter target domain (e.g., example.com)

2. Choose scan mode:
   - passive → automatic enumeration via crt.sh
   - brute   → manual scan using your own wordlist

3. (Optional) Save the results to a file

## 📸 CLI Preview
![Gambar WhatsApp 2025-07-23 pukul 20 52 33_1d053787](https://github.com/user-attachments/assets/b9d0320c-7072-44ea-8b81-0e74cf26265e)

## 📁 Example Wordlist
Put your wordlists at wordlists/ folder:
```bash
wordlists/subdomains.txt
```
Example content:
```bash
www
mail
ftp
admin
webmail
dev
```
## 🙋 Author

    👤 Revario Sayiddina Al Habsy
    📍 Universitas Negeri Jakarta
    🔗 GitHub: @Revari027
    
## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests are welcome! If you'd like to contribute ideas, improvements, or features, feel free to open an issue or PR.
