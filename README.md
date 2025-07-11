# 📸 Instagram Post Uploader via Streamlit

This is a simple Streamlit app that allows you to upload images to your Instagram account directly from a browser interface.

## 🚀 Features

* Login with Instagram credentials
* Upload image files (`.jpg`, `.jpeg`, `.png`)
* Add a caption to your post
* Upload the post to Instagram with one click
* Simple, responsive UI with progress and status feedback

## 🛠️ Requirements

* Python 3.7+
* [Streamlit](https://streamlit.io)
* [instagrapi](https://github.com/adw0rd/instagrapi)

## 📦 Installation

```bash
git clone https://github.com/your-username/instagram-uploader-streamlit.git
cd instagram-uploader-streamlit
pip install -r requirements.txt
```

**requirements.txt**

```txt
streamlit
instagrapi
```

## ▶️ Usage

```bash
streamlit run app.py
```

Then open the provided `localhost` link in your browser.

## 🖼️ How It Works

1. Enter your Instagram **username** and **password**.
2. Upload an image.
3. Write your caption.
4. Click **"Post to Instagram"**.
5. The app logs in and uploads your post.

## ⚠️ Important Notes

* Instagram may temporarily block or challenge suspicious login attempts (2FA, challenge required, etc.).
* This tool uses the unofficial `instagrapi` client, which may not always be reliable due to API changes.
* Always follow Instagram’s community guidelines and terms of service.

## 📁 File Structure

```
📁 instagram-uploader-streamlit/
│
├── app.py               # Streamlit app code
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 📌 Disclaimer

This project is for **educational purposes only**. Use it responsibly and at your own risk.

---

