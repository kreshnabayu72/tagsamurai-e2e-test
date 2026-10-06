---
id: TC-GS-DIV-E2E-027-delete-single-screening-cancel-dan-double-submit
title: "Screening Dialog Konfirmasi Delete Single, Pembatalan `[Cancel]`, dan Double-Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-41
  - TC-GS-DIV-44
  - TC-GS-DIV-45
coverage:
  web: automated
---

# Screening Dialog Konfirmasi Delete Single, Pembatalan `[Cancel]`, dan Double-Submit

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Terdapat data divisi aman 'Finance'

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik icon row action (⋯) pada baris 'Finance' lalu klik 'Delete'
3. Verifikasi dialog konfirmasi bahaya 'Delete Division' (severity danger) muncul
4. Verifikasi body dialog menampilkan bullet '• Finance' dan kalimat 'Are you sure you want to delete it? This action cannot be undone.'
5. Verifikasi tombol aksi memuat '[Cancel]' (variant text) dan '[Delete]' (variant filled danger)
6. Klik tombol '[Cancel]' atau tekan tombol Escape
7. Verifikasi dialog tertutup dan baris 'Finance' tetap ada di tabel tanpa perubahan
8. Buka kembali dialog Delete pada baris 'Finance'
9. Klik ganda dengan cepat tombol '[Delete]'
10. Verifikasi sistem hanya memproses 1 request penghapusan tanpa menyebabkan error double-submit

## Notes

- Format dialog konfirmasi hapus single mengacu pada division.md §4.2d Dialog 1.
