---
id: TC-FA-LIC-E2E-102-changelog-concurrent-user-screening-popup-tutup-isi-entri
title: "Modal Changelog Concurrent User: Screening Popup, Penutupan, Isi Entri Force Logout, Sort Kolom Bernilai Tunggal, dan Format Tanggal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-564
  - TC-FA-LIC-565
  - TC-FA-LIC-566
  - TC-FA-LIC-571
  - TC-FA-LIC-585
coverage:
  web: automated
---

# Modal Changelog Concurrent User: Screening Popup, Penutupan, Isi Entri Force Logout, Sort Kolom Bernilai Tunggal, dan Format Tanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Concurrent User #31 (4 entri) dan riwayat Changelog Allocation Quota #27 pada client yang sama, lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE).

  | Date | Action | User Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Force Logout | Budi Santoso | Session Status | Active | Force Logged Out | Rudi H |
  | 29/09/26 14:20 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |
  | 28/09/26 09:40 | Force Logout | Andi Pratama | Session Status | Active | Force Logged Out | Rudi H |
  | 27/09/26 16:05 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |

- Data Uji Sort kolom bernilai tunggal (TC-FA-LIC-571), dipakai langkah 22 sampai 27: Action, Field, Old Value, New Value. Untuk keempat kolom, klik 1 `↑` dan klik 2 `↓` menghasilkan urutan 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05 (nilai sama, tie-breaker default sort Date terbaru).
- State global yang diubah: General Settings Date Format `dd MMM yy` dan Time Format 12 jam dipasang lewat fixture BE penyetel state pada blok TC-FA-LIC-585 (langkah 28) dan dipulihkan ke `dd/MM/yy`, `HH:mm` pada langkah 34 serta di hook `after`. Suite berjalan serial (`parallel: false`).
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: Urutan dan jumlah entri Changelog (langkah 5, 20, 23, 25) diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #27 dan #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.

## Test Steps

### TC-FA-LIC-564: Screening popup Changelog Concurrent User tiga zona

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar
2. Verifikasi header modal berisi Title `Changelog: Concurrent User` dan icon close `[×]`
3. Verifikasi toolbar modal memuat `Search | Filter | Download`
4. Verifikasi kolom body: `Date (sortable) | Action (sortable) | User Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
5. Verifikasi urutan default Date terbaru: 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05
6. Verifikasi Action ditulis plain text (bukan badge)
7. Verifikasi Modified By berformat `[First Name] [Last Initial]`
8. Verifikasi footer memuat paginasi default 10 per halaman

### TC-FA-LIC-565: Popup ditutup lewat X dan Esc, klik backdrop tidak menutup

9. Klik area di luar modal
10. Verifikasi klik backdrop diabaikan (modal tetap terbuka)
11. Klik `[×]`
12. Verifikasi `[×]` menutup modal
13. Klik ikon Changelog pada toolbar
14. Tekan Esc
15. Verifikasi Esc menutup modal

### TC-FA-LIC-566: Isi hanya entri Force Logout dengan nama user target dan nilai Old/New

16. Klik ikon Changelog pada toolbar
17. Verifikasi entri Budi Santoso tampil di modal `Changelog: Concurrent User`: Action `Force Logout`, User Name `Budi Santoso`, Field `Session Status`, Old Value `Active`, New Value `Force Logged Out`, Modified By `Rudi H`
18. Verifikasi entri Siti Rahma ada dua (29/09/26 14:20 dan 27/09/26 16:05) dengan Modified By `Dewi L`
19. Verifikasi entri Andi Pratama dengan Modified By `Rudi H`
20. Verifikasi tabel memuat tepat 4 entri
21. Verifikasi tidak ada entri dengan Action `Edit` atau `Remove Allocation` dan tidak ada Field `Allocated Quota` atau `Quota Alert Level`

### TC-FA-LIC-571: Sort kolom bernilai tunggal tidak mengubah urutan

Untuk setiap kolom Action, Field, Old Value, New Value pada Data Uji Sort (langkah 22 sampai 27):

22. Klik header kolom sekali
23. Verifikasi indikator `↑` dan urutan: 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05
24. Klik header kolom kedua kali
25. Verifikasi indikator `↓` dan urutan: 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05
26. Klik header kolom ketiga kali
27. Verifikasi kolom kembali ke urutan default

### TC-FA-LIC-585: Format tanggal mengikuti General Settings dan Modified By format singkat dengan tooltip

28. Atur lewat fixture BE General Settings Date Format `dd MMM yy` dan Time Format 12 jam
29. Muat ulang halaman License, buka tab Concurrent User, klik ikon Changelog pada toolbar
30. Verifikasi kolom Date pada entri 30/09/26 11:15 memakai format General Settings `30 Sep 26, 11:15 AM`
31. Arahkan kursor ke `Rudi H` pada kolom Modified By entri tersebut
32. Verifikasi tooltip menampilkan nama lengkap `Rudi Hartono`
33. Tutup modal dengan `[×]`
34. Pulihkan lewat fixture BE General Settings Date Format `dd/MM/yy` dan Time Format `HH:mm`
35. Muat ulang halaman License

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 13 dan 16 membuka kembali modal; langkah 28, 29, 33, 34, dan 35 menyetel dan memulihkan format tanggal; muat ulang pada langkah 29 diperlukan supaya format baru terbaca (S-03).
- Langkah yang diulang per kolom: langkah 22 sampai 27 (4 iterasi) (bagian 8b butir 7).
- Spec ini memuat 35 langkah nominal dan sekitar 53 langkah dengan ekspansi. Alasan: seluruh blok membaca modal Changelog Concurrent User yang sama dengan dataset Pre-setup #31 dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok format tanggal berada di akhir karena mengubah state global dan dipulihkan sebelum spec selesai.
- P-5: TC-FA-LIC-585 (format tanggal General Settings) adalah satu objek uji ringan kelas h berpermukaan sama dengan blok lain.
- Temuan untuk QA:
  - TC-FA-LIC-566 butir d ("tepat 4 entri") adalah jumlah absolut pada audit trail permanen (S-12); asersi ini bergantung pada fixture pemulih riwayat Pre-setup #31.
  - TC-FA-LIC-566 butir b menyebut dua entri Siti Rahma tanpa nilai Action, Field, Old, dan New; spec tidak mengasersi bagian yang tidak tertulis.
  - TC-FA-LIC-571 tidak menyebut hasil indikator sort pada kolom bernilai tunggal selain urutan; spec mengasersi indikator `↑` dan `↓` karena Expected TC menyebut klik 1 `↑` dan klik 2 `↓`.
