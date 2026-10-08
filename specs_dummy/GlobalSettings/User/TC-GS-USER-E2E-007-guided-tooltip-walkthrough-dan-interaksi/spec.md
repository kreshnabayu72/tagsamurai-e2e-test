---
id: TC-GS-USER-E2E-007-guided-tooltip-walkthrough-dan-interaksi
title: "Guided Tooltip walkthrough 5 step, kontrol navigasi, a11y keyboard, dan replay"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-29
  - TC-GS-USER-30
  - TC-GS-USER-31
  - TC-GS-USER-32
  - TC-GS-USER-33
  - TC-GS-USER-34
  - TC-GS-USER-35
  - TC-GS-USER-36
  - TC-GS-USER-37
  - TC-GS-USER-38
  - TC-GS-USER-39
  - TC-GS-USER-40
coverage:
  web: automated
---

# Guided Tooltip walkthrough 5 step, kontrol navigasi, a11y keyboard, dan replay

## Prerequisites

- Login sebagai user yang belum pernah menyelesaikan walkthrough Guided Tooltip
- Berada di halaman Global Settings > User > User List

## Test Steps

### Walkthrough 5 Step

1. Buka halaman User List, verifikasi popover Guided Tooltip terbuka otomatis pada Step 1 (Search)
2. Verifikasi teks instruksi Step 1, lalu klik tombol '[Next]'
3. Verifikasi popover berpindah ke Step 2 (Filter), lalu klik '[Next]'
4. Verifikasi popover berpindah ke Step 3 (Download), lalu klik '[Next]'
5. Verifikasi popover berpindah ke Step 4 (Changelog), lalu klik '[Next]'
6. Verifikasi popover berpindah ke Step 5 (Column Visibility), lalu klik '[Back]' untuk kembali ke Step 4
7. Klik '[Next]' kembali ke Step 5, lalu klik '[Done]'
8. Verifikasi popover tertutup dan state panduan tersimpan sebagai selesai

### Replay dan Aksesibilitas Keyboard

9. Klik ikon [?] pada breadcrumb untuk memicu replay Guided Tooltip
10. Verifikasi tooltip kembali terbuka di Step 1
11. Tekan tombol Esc pada keyboard, verifikasi tooltip langsung tertutup (exit tanpa selesai)
12. Fokuskan keyboard (Tab) ke tombol '[+ User]' dan ikon Table Tools, verifikasi indikator focus ring tampil jelas dan tooltip terbuka via keyboard

## Notes

- Menggabungkan 12 test case granular (TC-GS-USER-29 s.d. TC-GS-USER-40).
