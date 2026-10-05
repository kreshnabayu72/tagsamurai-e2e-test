---
id: TC-GS-ACTLOG-E2E-006-hover-tooltip-toolbar-dan-teks-terpotong
title: "Hover tooltip pada icon table tools dan teks lengkap untuk nama yang terpotong"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-18
  - TC-GS-ACTLOG-19
coverage:
  web: automated
---

# Hover tooltip pada icon table tools dan teks lengkap untuk nama yang terpotong

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control
- Terdapat entri dengan User bernama panjang pada Tab Session dan Modified By bernama panjang pada Tab User Action

## Test Steps

### Tab Session
1. Buka Tab Session
2. Arahkan kursor ke icon Search pada toolbar dan verifikasi tooltip "Search" muncul
3. Arahkan kursor ke icon Filter pada toolbar dan verifikasi tooltip "Filter" muncul
4. Arahkan kursor ke icon Download pada toolbar dan verifikasi tooltip "Download" muncul
5. Arahkan kursor ke header kolom Actions (⋯) dan verifikasi tooltip "Setup column" muncul
6. Arahkan kursor ke nama user yang terpotong pada kolom User
7. Verifikasi tooltip menampilkan nama lengkap user secara utuh tanpa terpotong
### Tab User Action
8. Klik tab "User Action"
9. Arahkan kursor ke nama admin yang terpotong pada kolom Modified By
10. Verifikasi tooltip menampilkan nama lengkap admin secara utuh tanpa terpotong

## Notes

- Tooltip nama terpotong memastikan keterbacaan penuh identitas aktor tanpa merusak kerapian layout tabel.
