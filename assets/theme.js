/**
 * ライト／ダークテーマの切り替え。
 * - 初回は OS の設定（prefers-color-scheme）に従う。
 * - ヘッダーのボタンで切り替え、選択は localStorage に保存する。
 * - 保存値は <head> 内で読み込んだ時点で適用し、表示のちらつきを防ぐ。
 */
(function () {
  "use strict";

  var STORAGE_KEY = "kanolab-theme";
  var THEMES = ["light", "dark"];
  var root = document.documentElement;
  var isJapanese = (root.getAttribute("lang") || "ja") === "ja";
  var darkQuery = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

  function readStored() {
    try {
      var value = localStorage.getItem(STORAGE_KEY);
      return THEMES.indexOf(value) >= 0 ? value : null;
    } catch (e) {
      return null; // プライベートモード等で使えない場合
    }
  }

  function writeStored(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (e) {
      // 保存できなくても動作には影響しない
    }
  }

  function currentTheme() {
    var attr = root.getAttribute("data-theme");
    if (THEMES.indexOf(attr) >= 0) return attr;
    return darkQuery && darkQuery.matches ? "dark" : "light";
  }

  // 保存済みの選択を描画前に適用する
  var stored = readStored();
  if (stored) root.setAttribute("data-theme", stored);

  function updateButton(button) {
    var dark = currentTheme() === "dark";
    // ボタンは「切り替え先」を示す
    button.textContent = dark ? "☀" : "☾";
    button.setAttribute("aria-pressed", dark ? "true" : "false");
    var label = dark
      ? (isJapanese ? "ライトモードに切り替え" : "Switch to light mode")
      : (isJapanese ? "ダークモードに切り替え" : "Switch to dark mode");
    button.setAttribute("aria-label", label);
    button.setAttribute("title", label);
  }

  document.addEventListener("DOMContentLoaded", function () {
    var button = document.querySelector(".theme-toggle");
    if (!button) return;
    updateButton(button);

    button.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      writeStored(next);
      updateButton(button);
    });

    // 手動選択がない間は OS 設定の変更に追従する
    if (darkQuery && darkQuery.addEventListener) {
      darkQuery.addEventListener("change", function () {
        if (!readStored()) updateButton(button);
      });
    }
  });
})();
