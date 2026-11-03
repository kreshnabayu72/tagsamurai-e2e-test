---
id: TC-FA-LIC-E2E-091-group-license-allocation-setup-column-geser-pin-dan-unpin
title: "Group License Allocation: Setup Column Geser (Drag), Pin, dan Unpin Kolom Hideable Visible Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-318
  - TC-FA-LIC-319
coverage:
  web: automated
---

# Group License Allocation: Setup Column Geser (Drag), Pin, dan Unpin Kolom Hideable Visible Default

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; tabel Group License Allocation pada node All Groups menampilkan empat baris level 1 dengan 13 kolom data tampil. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki` (belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada.
- Tabel "Kolom Hideable Visible default (13 kolom data)" (parameter langkah 2 sampai 8 dan 11 sampai 18): `Group Name`, `Group Code`, `Allocated Quota`, `Allocated to Subgroups`, `Used by This Group`, `Reserved by This Group`, `Remaining Quota`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`.
- Konfigurasi kolom: spec ini menyimpan urutan dan Pin kolom di browser. Hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12; pemulihan konfigurasi kolom. Kemampuan teknis: seret-dan-lepas item daftar kolom pada Popup Setup Column, membaca urutan kolom di Live Preview dan tabel, mengatur lebar viewport agar tabel dapat digeser horizontal.
- Viewport browser disempitkan pada langkah 10 sehingga tabel Group License Allocation dapat digeser horizontal (pilihan spec; TC hanya menulis "geser tabel horizontal") dan dipulihkan pada langkah 19.

## Test Steps

### TC-FA-LIC-318: Geser (drag) per kelas kolom Hideable Visible default

1. Klik tab Allocation Quota di node All Groups
2. Untuk setiap kolom pada tabel "Kolom Hideable Visible default (13 kolom data)" (langkah 2 sampai 8): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
3. Seret kolom itu ke posisi pertama
4. Verifikasi urutan kolom di Live Preview berubah sesuai seretan: kolom itu di posisi pertama
5. Klik `[Save]`
6. Verifikasi urutan kolom di tabel berubah sesuai seretan: kolom itu di posisi pertama
7. Muat ulang halaman (F5)
8. Verifikasi urutan kolom di tabel bertahan setelah F5: kolom itu di posisi pertama
9. Buka Popup Setup Column, klik `[Reset to Default]`, lalu klik `[Save]`

### TC-FA-LIC-319: Pin dan Unpin per kelas kolom Hideable Visible default

10. Sempitkan viewport browser sehingga tabel dapat digeser horizontal
11. Untuk setiap kolom pada tabel "Kolom Hideable Visible default (13 kolom data)" (langkah 11 sampai 18): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
12. Klik ikon Pin kolom itu, lalu klik `[Save]`
13. Geser tabel secara horizontal
14. Verifikasi kolom itu membeku (sticky) di kiri saat scroll horizontal
15. Muat ulang halaman (F5), lalu geser tabel secara horizontal
16. Verifikasi kolom itu tetap membeku (sticky) di kiri setelah F5
17. Buka Popup Setup Column, klik ikon Pin kolom itu untuk Unpin, lalu klik `[Save]`
18. Verifikasi kolom itu tidak lagi membeku (sticky) setelah Unpin
19. Pulihkan viewport browser ke ukuran semula

## Notes

- Langkah penghubung tanpa `Verifikasi`: menyimpan tiap iterasi (`[Save]`), `[Reset to Default]` lalu `[Save]` di akhir TC-FA-LIC-318 yang mengembalikan urutan kolom, Unpin di akhir tiap iterasi TC-FA-LIC-319 (S-09), serta langkah 10 dan 19 yang menyempitkan dan memulihkan viewport. Setup Column tidak memakai "Tunggu aksi selesai" karena aksi sisi klien (butir 8 bagian 8b).
- Blok ulang: langkah 2 sampai 8 dan langkah 11 sampai 18 masing-masing dijalankan 13 kali; urutan hasil iterasi TC-FA-LIC-318 tidak dipulihkan antar iterasi karena asersi hanya memeriksa kolom yang baru diseret berada di posisi pertama. Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: seluruh blok adalah Setup Column satu tabel dengan satu dataset Pre-setup #12 dan satu kelas harness, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Temuan untuk QA: TC-FA-LIC-318 tidak menyebut urutan kolom lain selain posisi pertama; spec tidak mengasersi urutan kolom lainnya. TC-FA-LIC-319 mengandaikan tabel lebih lebar dari viewport tanpa menyebut lebar viewport; spec menyempitkan viewport (langkah 10) dan memulihkannya (langkah 19).
