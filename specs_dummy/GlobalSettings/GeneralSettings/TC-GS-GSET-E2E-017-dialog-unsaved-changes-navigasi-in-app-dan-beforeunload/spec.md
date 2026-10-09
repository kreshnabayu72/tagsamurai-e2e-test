---
id: TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload
title: "Dialog Unsaved Changes: navigasi in-app (Cancel/Leave/Esc), tanpa dialog saat bersih/revert, setelah Save sukses, dan konfirmasi beforeunload"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-49
  - TC-GS-GSET-50
  - TC-GS-GSET-51
  - TC-GS-GSET-52
  - TC-GS-GSET-53
  - TC-GS-GSET-114
  - TC-GS-GSET-116
coverage:
  web: automated
---

# Dialog Unsaved Changes: navigasi in-app (Cancel/Leave/Esc), tanpa dialog saat bersih/revert, setelah Save sukses, dan konfirmasi beforeunload

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Cancel dan Leave pada Navigasi In-App

1. Buka Global Settings > General Settings, pilih Session Idle Timeout `1 hour`, lalu klik menu Global Settings > Activity Log
2. Verifikasi dialog muncul: "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
3. Klik `[Cancel]`
4. Verifikasi dialog tertutup, tetap di General Settings, dan Session Idle Timeout tetap `1 hour`
5. Klik menu Global Settings > Activity Log lagi, lalu klik `[Leave]`
6. Verifikasi pindah ke Activity Log tanpa menyimpan
7. Kembali ke Global Settings > General Settings dan verifikasi Session Idle Timeout `30 minutes` (perubahan tidak tersimpan)

### Esc Setara Cancel

8. Pilih Session Idle Timeout `1 hour`, klik menu Global Settings > Activity Log, lalu tekan `Esc`
9. Verifikasi dialog tertutup, tetap di General Settings dengan Session Idle Timeout `1 hour`, dan fokus keyboard terjebak di dalam dialog selama terbuka

### Tanpa Dialog saat Bersih atau Setelah Revert

10. Dengan form bersih, klik menu Global Settings > Activity Log
11. Verifikasi berpindah langsung ke Activity Log tanpa dialog Unsaved Changes
12. Kembali ke General Settings, pilih Session Idle Timeout `1 hour`, lalu pilih kembali `30 minutes`
13. Klik menu Global Settings > Activity Log
14. Verifikasi berpindah langsung ke Activity Log tanpa dialog Unsaved Changes

### Tanpa Dialog Setelah Save Sukses

15. Kembali ke General Settings, pilih Session Idle Timeout `1 hour`, lalu klik `[Save]` hingga toast sukses
16. Klik menu Global Settings > Activity Log
17. Verifikasi berpindah langsung ke Activity Log tanpa dialog Unsaved Changes (form sudah di-rebase ke nilai tersimpan)

### Konfirmasi Bawaan Browser saat Reload

18. Kembali ke General Settings, pilih Session Idle Timeout `1 hour`, lalu muat ulang halaman (F5)
19. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
20. Batalkan reload dan verifikasi form tetap terbuka dengan Session Idle Timeout `1 hour`

### Backdrop Tidak Menutup Dialog

21. Klik menu Global Settings > Activity Log, lalu saat Dialog Unsaved Changes tampil klik area backdrop di luar dialog
22. Verifikasi dialog tetap terbuka dan masih berada di General Settings

## Notes

- Menggabungkan TC-GS-GSET-49, 50, 51, 53, 114, 116 (navigasi in-app dan kondisi tanpa dialog) serta TC-GS-GSET-52 (konfirmasi beforeunload, Manual Only).
