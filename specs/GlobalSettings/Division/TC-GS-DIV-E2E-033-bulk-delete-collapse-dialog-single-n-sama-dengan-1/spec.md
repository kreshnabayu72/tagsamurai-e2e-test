---
id: TC-GS-DIV-E2E-033-bulk-delete-collapse-dialog-single-n-sama-dengan-1
title: "Penyederhanaan Dialog Bulk Delete Menjadi Dialog Single Saat N=1 (Aman vs In-Use)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-257
  - TC-GS-DIV-258
coverage:
  web: automated
---

# Penyederhanaan Dialog Bulk Delete Menjadi Dialog Single Saat N=1 (Aman vs In-Use)

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat 1 divisi aman 'Finance' dan 1 divisi in-use 'Human Resources'

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Centang HANYA 1 baris divisi aman 'Finance' melalui checkbox baris
3. Klik tombol '[Delete]' pada Bulk Action Bar
4. Verifikasi dialog konfirmasi otomatis collapse ke format Single (Dialog 1): judul singular 'Delete Division' (bukan 'Delete Divisions'), 1 bullet '• Finance', dan teks 'Are you sure you want to delete it? This action cannot be undone.'
5. Tutup dialog konfirmasi tersebut dan batalkan seleksi
6. Centang HANYA 1 baris divisi in-use 'Human Resources'
7. Klik tombol '[Delete]' pada Bulk Action Bar
8. Verifikasi dialog otomatis collapse ke dialog blocker Single (Dialog 2): judul 'Cannot Delete Data', 1 bullet '• Human Resources — still in use', dan tombol tunggal '[OK]' (bukan format kelompok campuran bulk)

## Notes

- Memvalidasi aturan kolaps dialog N=1 sesuai klarifikasi prd-conventions.md §7 dan division.md §4.2d.
