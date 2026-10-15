# マザーズバッグ モデル撮影 2026 ／ 写真・動画 使用同意

2026年10月27日（火）に実施する KABAG マザーズバッグのモデル撮影で使う、写真・動画の使用同意フォーム一式です。

## 回答フォーム（Google フォーム）

https://docs.google.com/forms/d/e/1FAIpQLSfuLosPhaxA4shbx-BveXnNJvT4NUB9M-lr8MriT_UmE3tL0g/viewform

- 回答は ellgrun のアカウントの Google フォームに保存されます。
- 回答項目：保護者のお名前／Instagram のアカウント名／お子さまの呼び名と年齢／アカウント紹介の可否／使用への同意（チェック）。

## ファイル一覧

| ファイル | 内容 |
| --- | --- |
| `consent-print-sheet.html` | 撮影当日の受付で使う A4 印刷用シート（QRコード入り）。ブラウザで開いて印刷、または PDF 保存してください。 |
| `consent-print-sheet.pdf` | 上記の PDF 版。 |
| `consent-form-qr.svg` | 回答フォームの QRコード（ベクター・印刷向け）。 |
| `consent-form-qr.png` | 回答フォームの QRコード（PNG）。 |
| `generate-qr.py` | QRコードを再生成するスクリプト。 |

## 撮影当日の流れ（スタッフ用）

1. 各組の撮影を始める前に、保護者の方へ印刷用シートをお渡し／ご提示します。
2. その場でスマートフォンから QRコードを読み取り、フォームに回答してもらいます。
3. 送信されたことを確認してから撮影に入ってください。

## 写真・動画を使わせていただく場所

- 商品ページ
- SNS（Instagram・TikTok・YouTube・LINE など）
- ネット広告
- 店頭 POP・販売店向け資料
- ※ 使用期間の期限は設けていません。

## QRコードの再生成

```
pip install segno
python generate-qr.py
```
