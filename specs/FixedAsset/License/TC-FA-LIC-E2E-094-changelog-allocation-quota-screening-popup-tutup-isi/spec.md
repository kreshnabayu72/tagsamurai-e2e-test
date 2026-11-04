---
id: TC-FA-LIC-E2E-094-changelog-allocation-quota-screening-popup-tutup-isi
title: "Modal Changelog Allocation Quota: Screening Popup, Penutupan, Isi Entri, Opsi Filter, dan Format Tanggal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-328
  - TC-FA-LIC-329
  - TC-FA-LIC-330
  - TC-FA-LIC-348
  - TC-FA-LIC-362
coverage:
  web: automated
---

# Modal Changelog Allocation Quota: Screening Popup, Penutupan, Isi Entri, Opsi Filter, dan Format Tanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, Setup Column, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup: riwayat Changelog Allocation Quota #27 (6 entri) dirujuk lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` (fixture belum ada, disediakan tim FE). Hook `before` dan `after` memulihkannya lewat fixture BE pemulih riwayat. Spec ini hanya membaca data.

  | Date | Action | Group Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Edit | — | Quota Alert Level | Normal | Low | System |
  | 29/09/26 10:05 | Edit | Divisi Logistik | Allocated Quota | 500 | 600 | Rudi H |
  | 28/09/26 15:30 | Edit | Divisi IT | Allocated Quota | — | 100 | Dewi L |
  | 27/09/26 09:00 | Remove Allocation | Gudang A | Allocated Quota | 100 | — | Rudi H |
  | 26/09/26 11:20 | Edit | Divisi Keuangan | Allocated Quota | — | 50 | Dewi L |
  | 25/09/26 08:45 | Remove Allocation | Divisi IT | Allocated Quota | 100 | — | Rudi H |

- State global yang diubah: General Settings Date Format `dd MMM yy` dan Time Format 12 jam dipasang lewat fixture BE penyetel state pada blok TC-FA-LIC-362 (langkah 31). Jam fixture 29/09/26 dan format awal `dd/MM/yy`, `HH:mm` dipulihkan di langkah 37 dan di hook `after`. Suite berjalan serial (`parallel: false`).
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: Urutan dan jumlah entri Changelog (langkah 5 dan 29) diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #27 dan #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.
- Kemampuan teknis: mengubah General Settings lewat fixture BE (disediakan tim FE/BE); mengirim tombol `Esc` ke browser (langkah 14); tidak ada endpoint yang dikarang.

## Test Steps

### TC-FA-LIC-328: Screening popup Changelog Allocation Quota tiga zona

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
2. Verifikasi header modal berisi Title `Changelog: Allocation Quota` dan icon close `[×]`
3. Verifikasi toolbar memuat `Search | Filter | Download`
4. Verifikasi kolom body: `Date (sortable) | Action (sortable) | Group Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
5. Verifikasi urutan default Date terbaru: 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45
6. Verifikasi Action ditulis plain text (bukan badge)
7. Verifikasi Modified By berformat `[First Name] [Last Initial]`
8. Verifikasi footer memuat paginasi default 10 per halaman

### TC-FA-LIC-329: Popup ditutup lewat X dan Esc, klik backdrop tidak menutup

9. Klik area di luar modal
10. Verifikasi klik backdrop diabaikan (modal Changelog tetap terbuka)
11. Klik `[×]`
12. Verifikasi `[×]` menutup modal
13. Klik ikon Changelog pada toolbar Level 1 Groups Quota
14. Tekan Esc
15. Verifikasi Esc menutup modal

### TC-FA-LIC-330: Isi entri alokasi pertama, Edit, Remove Allocation, dan penanda tingkat

16. Klik ikon Changelog pada toolbar Level 1 Groups Quota
17. Verifikasi entri seed Pre-setup #27 (bukan entri baru) Divisi Logistik (29/09/26 10:05) tampil di modal `Changelog: Allocation Quota`: Action `Edit`, Group Name `Divisi Logistik`, Field `Allocated Quota`, Old Value `500`, New Value `600`, Modified By `Rudi H`
18. Verifikasi entri Divisi IT (alokasi pertama, 28/09/26 15:30): Action `Edit`, Field `Allocated Quota`, Old Value `—`, New Value `100`, Modified By `Dewi L`
19. Verifikasi entri Gudang A (27/09/26 09:00): Action `Remove Allocation`, Field `Allocated Quota`, Old Value `100`, New Value `—`, Modified By `Rudi H`
20. Verifikasi entri penanda tingkat peringatan kuota: Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
21. Verifikasi tidak ada entri dengan Action `Force Logout` atau Field `Session Status`

### TC-FA-LIC-348: Filter Panel memuat Field dan Action dengan lebih dari satu nilai

22. Klik ikon Filter pada toolbar modal
23. Verifikasi field filter berurutan: Date, Action, Group Name, Field, Modified By
24. Buka dropdown `Field`
25. Verifikasi dropdown Field memuat dua opsi: Allocated Quota, Quota Alert Level
26. Tutup dropdown `Field`, lalu buka dropdown `Action`
27. Verifikasi dropdown Action memuat dua opsi: Edit, Remove Allocation
28. Tutup dropdown `Action`, klik ikon Filter untuk menutup Filter Panel, ketik Search `Allocated`, tekan Enter
29. Verifikasi kolom Field tetap Searchable: tabel menampilkan 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45
30. Klik `(←)` pada kotak Search, lalu tutup modal dengan `[×]`

### TC-FA-LIC-362: Format tanggal mengikuti General Settings dan Modified By format singkat dengan tooltip

31. Atur lewat fixture BE General Settings Date Format `dd MMM yy` dan Time Format 12 jam
32. Muat ulang halaman License, buka tab Allocation Quota, klik ikon Changelog pada toolbar Level 1 Groups Quota
33. Verifikasi kolom Date pada entri 29/09/26 10:05 memakai format General Settings `29 Sep 26, 10:05 AM`
34. Arahkan kursor ke `Rudi H` pada kolom Modified By entri tersebut
35. Verifikasi tooltip menampilkan nama lengkap `Rudi Hartono`
36. Tutup modal dengan `[×]`
37. Pulihkan lewat fixture BE General Settings Date Format `dd/MM/yy` dan Time Format `HH:mm`
38. Muat ulang halaman License

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 13 dan 16 membuka kembali modal; langkah 26 dan 28 menutup dropdown dan Filter Panel; langkah 28 (Search `Allocated`) mengambil data dari TC-FA-LIC-332 karena TC-FA-LIC-348 tidak memberi cara mengamati kolom Field Searchable; langkah 30 mengosongkan Search dan menutup modal; langkah 31, 32, 37, dan 38 menyetel dan memulihkan format tanggal. Muat ulang pada langkah 32 diperlukan supaya format baru terbaca (S-03).
- Absence di langkah 21 didahului `Verifikasi` entri Edit dan Remove Allocation tampil pada modal yang sama (langkah 17 sampai 20) sebagai anchor positif (bagian 8b butir 2).
- Baris Modified By di Changelog diasersi berformat `[First Name] [Last Initial]` (R-14).
- Spec di atas 35 langkah (38 langkah): alasan dipertahankan, seluruh blok membaca modal Changelog Allocation Quota yang sama dengan dataset Pre-setup #27 dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok format tanggal (TC-FA-LIC-362) berada di akhir karena mengubah state global dan dipulihkan sebelum spec selesai (P-5 butir b: satu objek uji ringan kelas h).
- P-5: TC-FA-LIC-362 (format tanggal General Settings) adalah satu objek uji ringan kelas h yang berpermukaan sama (modal Changelog) dengan blok lain.
- Temuan untuk QA:
  - TC-FA-LIC-348 butir d ("kolom Field tetap Searchable") tidak punya langkah pengamatan di TC; spec memakai data Search dari TC-FA-LIC-332 (langkah 28 dan 29).
  - TC-FA-LIC-362 butir a menyebut format `29 Sep 26, 10:05 AM` tanpa menyebut baris yang diamati; spec memakai entri 29/09/26 10:05 dari Pre-setup #27.
