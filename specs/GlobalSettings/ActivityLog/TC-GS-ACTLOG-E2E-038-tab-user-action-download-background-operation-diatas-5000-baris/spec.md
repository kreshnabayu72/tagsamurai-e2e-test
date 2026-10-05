---
id: TC-GS-ACTLOG-E2E-038-tab-user-action-download-background-operation-diatas-5000-baris
title: "Tab User Action: Download log >5.000 baris memicu operasi background, toast persiapan, dan notifikasi in-app"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-199
coverage:
  web: automated
---

# Tab User Action: Download log >5.000 baris memicu operasi background, toast persiapan, dan notifikasi in-app

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan hasil filter aktif melebihi 5.000 baris

## Test Steps

1. Buka Tab User Action dengan hasil data >5.000 baris
2. Klik icon Download lalu pilih opsi "CSV"
3. Verifikasi toast "Preparing your export. We'll notify you when it's ready." segera muncul
4. Verifikasi operasi dialihkan ke background task
5. Verifikasi notifikasi in-app muncul saat file ekspor selesai diproses dengan masa simpan file 24 jam

## Notes

- File hasil operasi background export tersimpan dan dapat diunduh ulang selama 24 jam.
