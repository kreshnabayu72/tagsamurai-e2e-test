---
id: TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke
title: "Validasi Field Name: Wajib Diisi, Batas 120 Karakter, Duplikat Debounce, Keystroke Emoji, dan Re-check Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-19
  - TC-GS-DIV-20
  - TC-GS-DIV-22
  - TC-GS-DIV-23
  - TC-GS-DIV-192
  - TC-GS-DIV-276
coverage:
  web: automated
---

# Validasi Field Name: Wajib Diisi, Batas 120 Karakter, Duplikat Debounce, Keystroke Emoji, dan Re-check Submit

## Prerequisites

- Login sebagai Role: Total Control
- Telah terdapat data divisi bernama 'Finance' di sistem

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Biarkan field Division Name kosong lalu klik tombol '[Submit]'
3. Verifikasi muncul pesan error inline 'Name must not be empty' dan modal tetap terbuka
4. Ketik teks sebanyak 121 karakter pada field Division Name
5. Verifikasi input terpotong tepat pada 120 karakter dan/atau muncul pesan error inline 'Max. 120 characters'
6. Coba masukkan karakter emoji pada field Division Name melalui keyboard / paste
7. Verifikasi karakter emoji terfilter langsung saat mengetik (keystroke block) dan jika lolos ke submit ditolak validasi 'Name contains invalid characters'
8. Ketik nama divisi 'finance' (huruf kecil, menyamai divisi 'Finance' yang sudah ada) tanpa memindahkan kursor
9. Tunggu jeda debounce ~500ms dan verifikasi muncul pesan error inline 'Name already exists'
10. Klik tombol '[Submit]' pada form
11. Verifikasi server melakukan re-check atomik saat submit, mengembalikan error duplicate 409, form tetap terbuka, dan tombol submit kembali aktif

## Notes

- Validasi duplikat nama bersifat case-insensitive per entitas sesuai division.md §6 dan §9.9.
