---
id: TC-GS-USER-E2E-004-screening-row-action-overlay-dan-toggle-status
title: "Screening overlay row action menu (⋯) dan visual toggle Active"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-24
  - TC-GS-USER-26
  - TC-GS-USER-27
  - TC-GS-USER-28
coverage:
  web: automated
---

# Screening overlay row action menu (⋯) dan visual toggle Active

## Prerequisites

- Login sebagai Role: Total Control
- Pre-setup User tersedia (memuat user aktif dan user dengan pending email)

## Test Steps

### Visual State Toggle Active

1. Buka Global Settings > User > User List
2. Amati kolom Active pada baris user aktif, verifikasi toggle berwarna hijau saat ON dan abu-abu netral saat OFF

### Overlay Row Action Menu

3. Klik ikon menu (⋯) pada baris user normal (Dewi Lestari)
4. Verifikasi menu popover menampilkan opsi: 'Detail', 'Edit', 'Resend Activation Email' (atau sesuai kondisi status), dan 'Delete'
5. Klik area di luar popover untuk menutup menu
6. Temukan baris Rina Putri (berstatus Pending Email Confirmation), klik menu (⋯)
7. Verifikasi opsi 'Resend Confirmation Email' tampil kondisional di dalam menu
8. Klik opsi 'Detail' dari menu (⋯) tersebut, verifikasi aplikasi berpindah ke halaman Detail Rina Putri

## Notes

- Menggabungkan 4 test case granular (TC-GS-USER-24 s.d. TC-GS-USER-28).
