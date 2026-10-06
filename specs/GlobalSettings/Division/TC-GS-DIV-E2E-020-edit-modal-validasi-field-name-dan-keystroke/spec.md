---
id: TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke
title: "Validasi Field Name Edit: Required, Batas 120 Karakter, Duplikat Debounce, Keystroke Emoji, dan Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-33
  - TC-GS-DIV-36
  - TC-GS-DIV-213
  - TC-GS-DIV-214
  - TC-GS-DIV-222
  - TC-GS-DIV-226
coverage:
  web: automated
---

# Validasi Field Name Edit: Required, Batas 120 Karakter, Duplikat Debounce, Keystroke Emoji, dan Submit

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia divisi target 'Legal' dan divisi lain 'Finance'

## Test Steps

1. Buka modal Edit pada baris divisi 'Legal'
2. Hapus seluruh teks pada field Division Name hingga kosong lalu klik '[Save]'
3. Verifikasi muncul pesan error inline 'Name must not be empty' dan modal tetap terbuka
4. Ketik teks melebihi 120 karakter dan verifikasi batas input terpotong tepat pada 120 karakter
5. Coba masukkan karakter emoji pada field Division Name
6. Verifikasi karakter emoji terblokir langsung saat mengetik (keystroke filter) atau ditolak error 'Name contains invalid characters'
7. Ketik nama divisi yang menyamai divisi lain: 'finance' (case-insensitive)
8. Tunggu jeda debounce ~500ms dan verifikasi muncul inline error 'Name already exists'
9. Klik tombol '[Save]' dan verifikasi re-check atomik server menolak perubahan dengan error duplicate, data tidak tersimpan, dan modal tetap terbuka

## Notes

- Menerapkan Prinsip Simetri Create/Edit validation rule division.md §9.9.
