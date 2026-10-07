---
id: TC-GS-ACTLOG-E2E-008-guided-tooltip-walkthrough
title: "Siklus Lengkap Guided Tooltip Walkthrough, Navigasi Tombol, Overlay, dan Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-18
  - TC-GS-ACTLOG-19
  - TC-GS-ACTLOG-20
  - TC-GS-ACTLOG-21
  - TC-GS-ACTLOG-22
  - TC-GS-ACTLOG-23
coverage:
  web: automated
---

# Siklus Lengkap Guided Tooltip Walkthrough, Navigasi Tombol, Overlay, dan Keyboard

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Flag profil pengguna 'guided_tooltip_seen_gs-activity-log' bernilai false (belum pernah melihat onboarding)

## Test Steps

### Kunjungan Pertama & Auto-Trigger
1. Buka halaman Global Settings > Activity Log.
2. Verifikasi walkthrough otomatis terbuka menyorot tab Session dan User Action (Step 1 of 2).
3. Verifikasi Title Step 1 adalah 'Two Kinds of Activity' dan Description 'Switch tabs to review sign-in activity or data changes.'.
4. Verifikasi tombol [Back] tidak ditampilkan pada Step 1.
5. Klik tombol [Next].
6. Verifikasi walkthrough berpindah ke Step 2 of 2 menyorot icon Filter di toolbar.
7. Verifikasi Title Step 2 adalah 'Narrow Down the Log' dan Description 'Narrow down the log to find specific entries. Available filters depend on the tab you are on.'.
8. Verifikasi tombol utama berubah menjadi [Done].
9. Klik tombol [Done].
10. Verifikasi walkthrough tertutup dan flag 'guided_tooltip_seen_gs-activity-log' tersimpan sebagai true.
11. Navigasi ke modul lain lalu kembali ke Activity Log, verifikasi walkthrough tidak muncul otomatis.
### Manual Replay & Navigasi Fleksibel
12. Klik tombol [?] di header halaman.
13. Verifikasi walkthrough terbuka kembali mulai dari Step 1.
14. Klik [Next], lalu klik [Back], verifikasi kembali ke Step 1.
15. Klik [?] lagi, lalu klik tombol [Skip], verifikasi walkthrough langsung tertutup.
16. Buka kembali walkthrough via [?], klik area overlay gelap di luar elemen sorotan, verifikasi walkthrough tertutup.
17. Buka kembali walkthrough via [?], ubah ukuran jendela browser (resize), verifikasi walkthrough tertutup otomatis.
### Kontrol Aksesibilitas Keyboard
18. Buka walkthrough via tombol [?].
19. Tekan tombol Enter pada keyboard, verifikasi maju ke Step 2.
20. Tekan tombol Panah Kiri (←), verifikasi mundur ke Step 1.
21. Tekan tombol Panah Kanan (→), verifikasi maju ke Step 2.
22. Tekan tombol Esc, verifikasi walkthrough tertutup secara aman.

## Notes

- Guided Tooltip memberikan orientasi dua langkah kepada pengguna mengenai pemisahan log sesi vs aksi mutasi.
