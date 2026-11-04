---
id: TC-FA-NOTIF-E2E-053-infinite-scroll-retensi-state-dan-kombinasi-kontrol
title: "Infinite Scroll dan Retensi State Notification Center setelah Back dan Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-220
  - TC-FA-NOTIF-221
  - TC-FA-NOTIF-224
  - TC-FA-NOTIF-225
coverage:
  web: automated
---

# Infinite Scroll dan Retensi State Notification Center setelah Back dan Refresh

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi) milik akun aktor, dipulihkan fixture BE pemulih di hook `before` dan `after`. Spec hanya membaca data. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-220: Infinite scroll memuat 10 item pertama lalu 10 berikutnya otomatis

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Verifikasi list memuat 10 item awal
3. Scroll mendekati akhir list
4. Verifikasi skeleton row tampil
5. Verifikasi list memuat 20 item
6. Verifikasi tidak ada tombol `[Load More]`
7. Verifikasi tidak ada pagination bernomor

### TC-FA-NOTIF-221: Infinite scroll sampai akhir data tidak memuat lagi

8. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
9. Scroll sampai akhir list berulang kali hingga tidak ada item baru yang termuat
10. Verifikasi seluruh 37 item termuat
11. Scroll sekali lagi sampai akhir list
12. Verifikasi tidak ada muat tambahan setelahnya (jumlah item tetap 37)

### TC-FA-NOTIF-224: Back dari halaman tujuan mempertahankan Search, Sort, Filter, dan Tab

13. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
14. Klik Tab `Unread`, ketik Search `access`, tekan Enter
15. Klik toggle Sort hingga Sort `Oldest`
16. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
17. Klik item hasil untuk menavigasi ke halaman tujuan
18. Klik Back browser untuk kembali ke Notification Center
19. Verifikasi Tab `Unread` aktif
20. Verifikasi kotak Search berisi `access`
21. Verifikasi Sort `Oldest` aktif
22. Verifikasi indikator titik pada icon Filter tampil (Filter tetap ter-Apply)

### TC-FA-NOTIF-225: Refresh F5 mempertahankan Search, Sort, Filter, dan Tab

23. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
24. Klik Tab `Unread`, ketik Search `access`, tekan Enter
25. Klik toggle Sort hingga Sort `Oldest`
26. Klik icon Filter, pilih Event Type `Access Total Control Removed`, lalu klik `[Apply]`
27. Tekan F5
28. Verifikasi Tab `Unread` aktif
29. Verifikasi kotak Search berisi `access`
30. Verifikasi Sort `Oldest` aktif
31. Verifikasi indikator titik pada icon Filter tampil (Filter tetap ter-Apply)
32. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-226 dan TC-228 ada di spec 114.
- Topik infinite scroll dan retensi state dipisah dari spec 114 (perilaku reset) dan 052 (independensi kontrol) meski memakai seed N-01 sampai N-37 yang sama: objek ujinya berbeda (pemuatan bertahap dan retensi navigasi) dan seed hanya dibaca, sehingga tidak ada keadaan yang dibawa antar spec.
- Langkah penghubung (S-03): langkah 1, 8, 13, 23, 32 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 9 dan 11 (scroll sampai akhir), 3 (scroll untuk memicu muat berikutnya).
- Asersi tambahan di luar Expected TC (S-03): tidak ada. Langkah 6 dan 7 (absence tombol dan pagination) didahului langkah 5 yang membuktikan list sudah memuat halaman kedua.
- Langkah 17 memilih item hasil Search dan Filter dan menavigasi ke halaman tujuan lewat klik item; Back dilakukan lewat tombol Back browser.
- Temuan untuk QA:
  - TC-220 butir b ("skeleton row tampil lalu 20 item") menyebut state sementara tanpa cara menahannya; spec mengasersi skeleton segera setelah scroll dan 20 item sesudahnya (8b butir 5), sehingga asersi skeleton dapat tidak stabil pada respons cepat.
  - TC-224 langkah 4 menulis "Back/breadcrumb" tanpa memilih; spec memakai Back browser, dan langkah 3 menulis "item hasil" tanpa menyebut item tujuan.
