[English](README.md)

# kanolab-web

加納研究室（滋賀大学教育学部 科学コミュニケーション研究室）のウェブサイトです。GitHub Pages で公開します。

内容は、研究室の Google Sites 統合制作マニュアル（PAGE 01〜26、日英）に基づきます。ビルド不要の静的 HTML/CSS で構成しています。

## 構成

| パス | 内容 |
|------|------|
| `index.html` | 日本語ホーム（PAGE 01） |
| `en/index.html` | 英語ホーム（PAGE 01） |
| `assets/style.css` | 共通スタイル |

リンクはすべて相対パスなので、プロジェクト URL（`/kanolab-web/`）でも独自ドメインでも動作します。
日本語ページ `X/index.html` には、対応する英語ページ `en/X/index.html` を置きます。

## ローカルでの確認

```sh
python3 -m http.server 8000
# http://localhost:8000/ を開く
```

## 進捗

- 完了：ホーム（日本語・英語）
- 未作成：ナビゲーションから参照している他のページ（`research/`、`unesco-chair/`、`workshops/`、`games-books/`、`people/`、`join/`、`media/`、`contact/`、`access/` とその下位ページ）
- 画像（ヒーロー・カード）：写真が未提供のため未配置
