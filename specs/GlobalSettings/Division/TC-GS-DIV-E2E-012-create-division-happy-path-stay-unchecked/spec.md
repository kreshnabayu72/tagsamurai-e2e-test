---
id: TC-GS-DIV-E2E-012-create-division-happy-path-stay-unchecked
title: "Pembuatan Divisi Baru Sukses dengan Auto-Trim dan Stay Unchecked"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-21
  - TC-GS-DIV-24
  - TC-GS-DIV-193
coverage:
  web: automated
---

# Pembuatan Divisi Baru Sukses dengan Auto-Trim dan Stay Unchecked

## Prerequisites

- Login sebagai Role: Total Control
- Nama divisi 'Finance' belum ada di sistem

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Ketik nama divisi dengan spasi di awal dan akhir: '   Finance   '
3. Biarkan field Code kosong dan pastikan checkbox 'Stay on this form after submitting' tidak dicentang
4. Klik ganda dengan cepat tombol '[Submit]' untuk menguji guard double-click
5. Verifikasi hanya 1 request pembuatan yang diproses oleh sistem
6. Verifikasi toast notifikasi sukses muncul dengan teks 'Success, division has been created.'
7. Verifikasi modal Create Division menutup secara otomatis
8. Verifikasi baris baru 'Finance' muncul pada tabel utama dengan nama yang telah ter-trim bersih tanpa spasi tambahan

## Notes

- Menguji pembersihan spasi otomatis (trim) dan perilaku form menutup saat Stay Unchecked (division.md §9.2 [F-DIV-02]).
