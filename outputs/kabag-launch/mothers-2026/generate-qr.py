#!/usr/bin/env python3
"""回答フォームの QRコードを再生成するスクリプト。"""
import segno

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfuLosPhaxA4shbx-BveXnNJvT4NUB9M-lr8MriT_UmE3tL0g/viewform"


def main():
    qr = segno.make(FORM_URL, error="h")
    qr.save("consent-form-qr.svg", scale=10, border=2)
    qr.save("consent-form-qr.png", scale=10, border=2)
    print("Generated consent-form-qr.svg and consent-form-qr.png")


if __name__ == "__main__":
    main()
