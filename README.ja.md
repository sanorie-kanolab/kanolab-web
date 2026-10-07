[English](README.md)

# kanolab-web

加納研究室（滋賀大学教育学部 科学コミュニケーション研究室）のウェブサイトです。GitHub Pages で公開します。

内容は、研究室の Google Sites 統合制作マニュアル（PAGE 01〜26、日英）に基づきます。ビルド不要の静的 HTML/CSS で構成しています。

## 構成

マニュアルの全26ページを日本語・英語で公開しています。

| 日本語 | English | 内容 |
|--------|---------|------|
| `index.html` | `en/index.html` | ホーム（PAGE 01） |
| `research/`（`inclusive-steam/`、`traditional-knowledge/`、`responsible-ai/`、`projects/`、`outputs/`） | `en/research/…` | 研究（PAGE 02〜12） |
| `unesco-chair/` | `en/unesco-chair/` | ユネスコチェア（PAGE 13） |
| `workshops/`（`workshop-archive/`） | `en/workshops/…` | ワークショップ（PAGE 14〜15） |
| `games-books/`（`games/`、`books/`） | `en/games-books/…` | ゲーム教材・書籍（PAGE 16〜18） |
| `people/` | `en/people/` | メンバー（PAGE 19） |
| `join/`（`phd/`、`jsps/`、`collaboration/`） | `en/join/…` | 研究室に参加（PAGE 20〜23） |
| `media/`、`contact/`、`access/` | `en/media/` ほか | SNS・メディア、問い合わせ、アクセス（PAGE 24〜26） |
| `assets/style.css` | | 共通スタイル |

URL パスは、マニュアルに記載された各ページの「推奨パス」に従っています。リンクはすべて相対パスなので、プロジェクト URL（`/kanolab-web/`）でも独自ドメインでも動作します。
日本語ページ `X/index.html` には、対応する英語ページ `en/X/index.html` があります。

## ローカルでの確認

```sh
python3 -m http.server 8000
# http://localhost:8000/ を開く
```

## 進捗

- 完了：全26ページ（日本語・英語）。文章とリンクはマニュアルに基づく。
- 公開前に確定が必要な箇所は黄色（`<mark class="todo">`）で表示：問い合わせ・申込フォームの URL（無効化した「準備中」ボタン）、ワークショップのイベント情報、メンバー名、ユネスコチェアの日付など。`grep -rl 'class="todo"' .` で探せます。
- 画像（ヒーロー・カード）：写真が未提供のため未配置
