---
id: TC-FA-NOTIF-E2E-013-android-bell-dropdown-panel-dan-notification-center
title: "Android: Dot Bell Icon, Dropdown Panel Bottom Sheet, dan Tata Letak Notification Center"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-6
  - TC-FA-NOTIF-385
  - TC-FA-NOTIF-399
coverage:
  mobile: automated
---

# Android: Dot Bell Icon, Dropdown Panel Bottom Sheet, dan Tata Letak Notification Center

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android, Fixed Asset > Dashboard, Dropdown Panel, dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di aplikasi Android di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Kemampuan teknis: perangkat atau emulator Android dengan aplikasi native terpasang serta kemampuan mengetuk dan membuka bottom sheet; disediakan tim FE. Spec memakai perangkat bersama sehingga suite berjalan serial (`parallel: false`).
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) milik akun aktor: N-01 sampai N-05 Unread, N-06 dan N-07 Read. Spec hanya membaca data; fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-6: Badge Bell icon berbentuk dot severity danger, bukan angka

1. Verifikasi badge Bell icon berupa dot berseverity `danger`
2. Verifikasi badge tidak menampilkan angka

### TC-FA-NOTIF-385: Tap Bell icon membuka Dropdown Panel sebagai bottom sheet layar penuh

3. Ketuk Bell icon pada top bar
4. Verifikasi Dropdown Panel tampil sebagai bottom sheet layar penuh, bukan dropdown kecil di bawah Bell icon

### TC-FA-NOTIF-399: Notification Center menampilkan Tabs segmented control dan Filter lewat menu [⋯]

5. Ketuk `[Show All]` pada bottom sheet
6. Verifikasi Notification Center tampil sebagai list kartu (bukan tabel)
7. Verifikasi Tab All (aktif default) dan Tab Unread tampil sebagai segmented control di atas list
8. Ketuk `Unread` pada segmented control
9. Verifikasi list hanya memuat lima notifikasi Unread (N-01 sampai N-05)
10. Ketuk icon `[⋯]`
11. Verifikasi bottom sheet menu terbuka dan memuat pilihan `Filter`
12. Pilih `Filter` pada bottom sheet menu
13. Verifikasi Filter menampilkan field `Event Type` dan `Date`
14. Tutup Filter tanpa menerapkan perubahan
15. Ketuk icon search di app bar
16. Verifikasi ikon search di app bar membuka field pencarian lebar penuh di atas list
17. Ketuk icon `[⋯]`, lalu pilih `Sort` pada bottom sheet
18. Verifikasi bottom sheet memuat pilihan Sort `Newest` (aktif default) dan `Oldest`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5 (TC-399 Langkah 1 "Tap Bell icon lalu tap `[Show All]`": Bell icon sudah diketuk pada langkah 3 dan bottom sheet masih terbuka), langkah 14 (menutup Filter agar langkah 15 dapat mengetuk app bar; cara menutup tidak tertulis di TC).
- Spec berjalan di aplikasi mobile; `coverage.mobile: automated` tanpa `coverage.web` (bagian 8). Bila tim FE tidak dapat menyediakan perangkat Android, `coverage.mobile` diubah menjadi `unsupported`, bukan spec dihapus.
- Temuan untuk QA:
  - TC-399 Expected d menyebut bottom sheet menu "memuat pilihan `Filter`" sedangkan Langkah 7 memilih `Sort` dari menu yang sama; spec mengasumsikan menu `[⋯]` memuat `Filter` dan `Sort`.
  - TC-399 tidak menyebut cara menutup Filter sebelum langkah 6 (ikon search); spec menutup Filter tanpa menerapkan perubahan.
