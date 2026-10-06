---
id: TC-GS-DIV-E2E-014-create-division-code-auto-generate-inisial
title: "Pembuatan Divisi Baru dengan Code Dikosongkan Menghasilkan Auto-Generate Inisial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-260
coverage:
  web: automated
---

# Pembuatan Divisi Baru dengan Code Dikosongkan Menghasilkan Auto-Generate Inisial

## Prerequisites

- Login sebagai Role: Total Control
- Nama divisi 'Human Capital' belum terdaftar

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Ketik Division Name: 'Human Capital'
3. Biarkan field Code benar-benar kosong (tanpa live preview kode sebelum submit)
4. Klik tombol '[Submit]'
5. Verifikasi muncul toast sukses 'Success, division has been created.'
6. Cari baris 'Human Capital' pada tabel utama
7. Verifikasi kolom Code terisi otomatis dengan string 'HC' (hasil inisial tiap kata sesuai algoritma F-DIV-09)

## Notes

- Menguji implementasi algoritma auto-generate token inisial DIV-LOGIC-04 / division.md §9.2 [F-DIV-09].
