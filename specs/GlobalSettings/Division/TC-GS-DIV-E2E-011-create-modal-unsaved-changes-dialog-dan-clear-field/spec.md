---
id: TC-GS-DIV-E2E-011-create-modal-unsaved-changes-dialog-dan-clear-field
title: "Pembersihan Form via `[Clear Field]` dan Dialog Konfirmasi Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-27
  - TC-GS-DIV-190
  - TC-GS-DIV-191
coverage:
  web: automated
---

# Pembersihan Form via `[Clear Field]` dan Dialog Konfirmasi Unsaved Changes

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Ketik 'Divisi Sementara' pada Division Name dan 'TEMP' pada Code
3. Klik tombol '[Clear Field]' pada footer modal
4. Verifikasi seluruh input teks pada field Name dan Code menjadi kosong kembali, border error bersih, dan modal Create Division TETAP terbuka tanpa dialog peringatan
5. Ketik kembali teks 'Data Kotor' pada Division Name
6. Klik icon close '[✕]' pada header modal atau klik area backdrop luar
7. Verifikasi muncul dialog konfirmasi peringatan 'Unsaved Changes' dengan deskripsi 'You have unsaved changes. Are you sure you want to leave?' serta tombol '[Stay]' dan '[Leave]'
8. Klik tombol '[Stay]'
9. Verifikasi dialog Unsaved Changes tertutup dan modal Create Division tetap terbuka mempertahankan teks 'Data Kotor'
10. Klik kembali icon '[✕]' dan klik tombol '[Leave]'
11. Verifikasi dialog dan modal Create Division tertutup penuh

## Notes

- Tombol [Clear Field] dilarang memicu dialog Unsaved Changes sesuai protokol interaksi division.md §4.4 item 3.
