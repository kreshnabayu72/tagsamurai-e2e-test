---
id: TC-GS-DIV-E2E-023-edit-division-happy-path-rename-dan-update-code
title: "Penyuntingan Divisi Sukses: Perubahan Name Ter-trim dan Pembaruan Code"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-35
  - TC-GS-DIV-195
  - TC-GS-DIV-225
  - TC-GS-DIV-265
coverage:
  web: automated
---

# Penyuntingan Divisi Sukses: Perubahan Name Ter-trim dan Pembaruan Code

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data divisi 'Legal' (Code 'LOG')

## Test Steps

1. Buka modal Edit pada baris divisi 'Legal'
2. Ubah Division Name menjadi ada spasi di awal dan akhir: '   Legal Affairs   '
3. Ubah Code menjadi: 'LGST'
4. Klik ganda dengan cepat tombol '[Save]' untuk menguji guard double-click
5. Verifikasi hanya 1 request update yang diproses oleh server
6. Verifikasi toast sukses muncul: 'Success, division has been updated.'
7. Verifikasi modal Edit menutup secara otomatis
8. Verifikasi baris pada tabel utama terbarukan menampilkan Name 'Legal Affairs' (spasi bersih) dan Code 'LGST'

## Notes

- Membuktikan fungsionalitas edit normal, auto-trim, dan pembaruan kode divisi (division.md §9.2 [F-DIV-03]).
