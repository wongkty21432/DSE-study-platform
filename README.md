# DSE-study-platform
DSE 文憑試學習平台。自適應題庫練習 + 完整學習指南，支援多科目、雙語切換、進度追蹤與 Best 5 預測。

## 科目

| 科目 | 題庫 | 學習指南 |
|------|:--:|:--:|
| 資訊及通訊科技 (ICT) | 76 題 (中文) | 8 課題 |
| 化學 (Chemistry) | 427 題 (英文) | 13 課題 |
| 其餘 16 科 | 即將推出 | — |

## 進度

### 已完成
- [x] 平台主頁 (科目選擇、註冊登入)
- [x] ICT 題庫 (76 題，中英雙語，自適應難度)
- [x] ICT 學習指南 (8 課題，含程式範例)
- [x] CHEM 題庫 (427 題，英文)
- [x] CHEM 學習指南 (13 課題)
- [x] 用戶帳號系統 (註冊/登入/MySQL 儲存)
- [x] 進度頁面 (Best 5 預測、圓餅圖、課題掌握度)
- [x] 題目管理工具 (CRUD)
- [x] Python 題目處理工具
- [x] 雙語切換 (中/英，URL 參數)
- [x] 設置頁面 (選修科選擇、預計等級)

### 未完成
- [ ] CHEM 題庫中文化
- [ ] CHEM 學習指南中文化
- [ ] ICT 學習指南英文化 (內容部分)
- [ ] 生物 (Biology)
- [ ] 物理 (Physics)
- [ ] 經濟 (Economics)
- [ ] 企業、會計與財務概論 (BAFS)
- [ ] 中國歷史 (Chinese History)
- [ ] 歷史 (History)
- [ ] 地理 (Geography)
- [ ] 視覺藝術 (Visual Arts)
- [ ] 體育 (Physical Education)
- [ ] 旅遊與款待 (Tourism & Hospitality)
- [ ] 數學延伸單元一 (M1)
- [ ] 數學延伸單元二 (M2)
- [ ] 英國語文 (English Language)
- [ ] 中國語文 (Chinese Language)
- [ ] 數學 (Mathematics)
- [ ] 公民與社會發展 (CSD)
- [ ] 管理員後台 (用戶管理)
- [ ] 手機適配優化
- [ ] GitHub Pages 部署
- [ ] 自動化題目匯入 (從 PDF 擷取)
- [ ] 單元測試

## 快速開始

### 1. 直接使用 (離線)

打開 `index.html` 即可瀏覽科目，進入題庫練習。進度儲存在瀏覽器 IndexedDB。

### 2. 完整部署 (含帳號系統)

需要 XAMPP (Apache + MySQL)。

```bash
# 複製到 XAMPP
cp -r DSE-study-platform /c/xampp/htdocs/

# 啟動 XAMPP (Apache + MySQL)

# 初始化資料庫
# 瀏覽器打開 http://localhost/dse-ict-api/setup.php

# 打開平台
# http://localhost/dse-study-platform/
```

預設管理員帳號：`admin` / `admin123`

### 3. GitHub Pages

前端可以部署到 GitHub Pages。API 需要自建伺服器或使用 ngrok 暴露本機 XAMPP。

## 目錄結構

```
DSE-study-platform/
├── index.html              # 主頁 (科目選擇 + 註冊登入)
├── progress.html           # 學習進度 (Best 5 + 圖表)
├── ict/
│   ├── quiz-bank.html      # ICT 題庫
│   ├── study-guide.html    # ICT 學習指南
│   ├── questions-ict.json  # 題目資料
│   └── admin.html          # 題目管理工具
├── chem/
│   ├── quiz-bank.html      # CHEM 題庫
│   └── study-guide.html    # CHEM 學習指南
└── api/                    # (在 XAMPP: dse-ict-api/)
    ├── config/
    │   ├── database.php
    │   └── schema.sql
    ├── login.php
    ├── register.php
    ├── save-progress.php
    ├── get-progress.php
    ├── session.php
    └── setup.php
```

## 新增科目

1. 在 `index.html` 的 Electives 區域加入科目卡片
2. 建立 `subject/quiz-bank.html` 和 `subject/study-guide.html`
3. 題庫格式參考 `ict/questions-ict.json`
4. 在 `progress.html` 的 `SUB` 物件加入課題名稱
5. API 的 `subject` 欄位會自動區分科目

## 技術棧

- 前端：HTML/CSS/JS (Vanilla)
- 資料庫：IndexedDB (本地) + MariaDB/MySQL (雲端)
- API：PHP 8.0+ (PDO)
- 伺服器：XAMPP (Apache)
