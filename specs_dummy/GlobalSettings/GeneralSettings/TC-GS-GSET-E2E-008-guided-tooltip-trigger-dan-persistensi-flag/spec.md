---
id: TC-GS-GSET-E2E-008-guided-tooltip-trigger-dan-persistensi-flag
title: "Guided Tooltip: trigger kunjungan pertama, penutupan dengan/tanpa simpan flag, dan klik overlay"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-14
  - TC-GS-GSET-17
  - TC-GS-GSET-146
  - TC-GS-GSET-147
coverage:
  web: automated
---

# Guided Tooltip: trigger kunjungan pertama, penutupan dengan/tanpa simpan flag, dan klik overlay

## Prerequisites

- Login sebagai Role: Total Control dengan akun baru; flag `guided_tooltip_seen_gs-general-settings` belum ada
- User berada di Global Settings
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Trigger Kunjungan Pertama dan Skip

1. Buka Global Settings > General Settings
2. Verifikasi walkthrough otomatis muncul dari Step 1 pada kunjungan pertama
3. Klik `[Skip]`
4. Verifikasi walkthrough tertutup dan flag `seen` tersimpan
5. Keluar ke menu lain lalu buka kembali Global Settings > General Settings
6. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### Tutup Tanpa Simpan Flag: Navigasi Keluar

7. Login ulang dengan akun baru berflag `seen` belum ada, buka Global Settings > General Settings
8. Saat Step 1 tampil, navigasi ke Global Settings > Activity Log
9. Verifikasi walkthrough tertutup saat navigasi keluar tanpa menyimpan flag `seen`
10. Kembali ke Global Settings > General Settings
11. Verifikasi walkthrough muncul lagi otomatis dari Step 1

### Tutup Tanpa Simpan Flag: Resize Viewport

12. Gunakan akun baru berflag `seen` belum ada, buka Global Settings > General Settings
13. Saat Step 1 tampil, ubah ukuran viewport browser
14. Verifikasi walkthrough tertutup saat viewport di-resize tanpa menyimpan flag `seen`
15. Keluar lalu buka kembali Global Settings > General Settings
16. Verifikasi walkthrough muncul lagi otomatis dari Step 1

### Klik Overlay Gelap Setara Skip

17. Gunakan akun baru berflag `seen` belum ada, buka Global Settings > General Settings
18. Saat Step 1 tampil, klik area overlay gelap di luar tooltip
19. Verifikasi walkthrough tertutup dan flag `seen` tersimpan
20. Keluar lalu buka kembali Global Settings > General Settings
21. Verifikasi walkthrough tidak muncul otomatis

## Notes

- Menggabungkan TC-GS-GSET-14, TC-GS-GSET-17, TC-GS-GSET-146, dan TC-GS-GSET-147 (trigger dan persistensi flag Guided Tooltip). Tiap blok butuh akun baru agar flag `seen` benar-benar belum ada.
