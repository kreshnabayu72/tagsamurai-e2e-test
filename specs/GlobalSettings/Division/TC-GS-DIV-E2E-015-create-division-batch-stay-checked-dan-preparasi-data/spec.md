---
id: TC-GS-DIV-E2E-015-create-division-batch-stay-checked-dan-preparasi-data
title: "Pembuatan Batch Divisi Menggunakan Checkbox Stay on This Form"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-25
  - TC-GS-DIV-26
coverage:
  web: automated
---

# Pembuatan Batch Divisi Menggunakan Checkbox Stay on This Form

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Ketik Division Name: 'Marketing'
3. Centang checkbox 'Stay on this form after submitting'
4. Klik tombol '[Submit]'
5. Verifikasi muncul toast sukses 'Success, division has been created.'
6. Verifikasi modal Create Division TETAP terbuka, input form ter-reset kosong kembali, dan checkbox 'Stay on this form' tetap dalam kondisi tercentang
7. Ketik Division Name: 'Operations'
8. Klik tombol '[Submit]'
9. Verifikasi toast sukses muncul kembali dan form tetap terbuka dalam keadaan bersih
10. Ketik Division Name: 'Human Resources 2' (divisi aman tanpa referensi user)
11. Hapus centang pada checkbox 'Stay on this form after submitting'
12. Klik tombol '[Submit]'
13. Verifikasi toast sukses muncul dan modal Create Division kini menutup otomatis
14. Verifikasi ketiga baris divisi ('Marketing', 'Operations', 'Human Resources 2') tampil pada tabel utama

## Notes

- Data divisi yang dibuat di sini digunakan untuk variasi pencarian, penyaringan, dan pengujian bulk delete.
