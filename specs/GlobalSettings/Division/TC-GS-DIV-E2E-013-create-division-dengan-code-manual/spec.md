---
id: TC-GS-DIV-E2E-013-create-division-dengan-code-manual
title: "Pembuatan Divisi Baru Sukses dengan Input Code Manual"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-259
coverage:
  web: automated
---

# Pembuatan Divisi Baru Sukses dengan Input Code Manual

## Prerequisites

- Login sebagai Role: Total Control
- Nama divisi 'Logistics' dan Code 'LOG' belum ada di sistem

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Ketik Division Name: 'Logistics'
3. Ketik Code secara manual: 'LOG'
4. Klik tombol '[Submit]'
5. Verifikasi muncul toast sukses 'Success, division has been created.' dan modal menutup
6. Cari baris 'Logistics' pada tabel utama
7. Verifikasi kolom Name menampilkan 'Logistics' dan kolom Code menampilkan 'LOG'

## Notes

- Memvalidasi penyimpanan nilai Code manual yang ditentukan pengguna (division.md §4.2c).
