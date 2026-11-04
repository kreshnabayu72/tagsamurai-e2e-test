---
id: TC-FA-LIC-E2E-152-group-license-allocation-setup-column-pin-dan-unpin
title: "Group License Allocation: Setup Column Pin dan Unpin Kolom Hideable Visible Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-319
coverage:
  web: automated
---

# Group License Allocation: Setup Column Pin dan Unpin Kolom Hideable Visible Default

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; tabel Group License Allocation pada node All Groups menampilkan empat baris level 1 dengan 13 kolom data tampil. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki` (belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada.
- Tabel "Kolom Hideable Visible default (13 kolom data)" (parameter langkah 3 sampai 10): `Group Name`, `Group Code`, `Allocated Quota`, `Allocated to Subgroups`, `Used by This Group`, `Reserved by This Group`, `Remaining Quota`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`.
- Konfigurasi kolom: spec ini menyimpan Pin kolom di browser. Hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12; pemulihan konfigurasi kolom. Kemampuan teknis: membaca posisi kolom beku (sticky) pada tabel saat scroll horizontal dan mengatur lebar viewport agar tabel dapat digeser horizontal.
- Viewport browser disempitkan pada langkah 2 sehingga tabel Group License Allocation dapat digeser horizontal (pilihan spec; TC hanya menulis "geser tabel horizontal") dan dipulihkan pada langkah 11.

## Test Steps

### TC-FA-LIC-319: Pin dan Unpin per kelas kolom Hideable Visible default

1. Klik tab Allocation Quota di node All Groups
2. Sempitkan viewport browser sehingga tabel dapat digeser horizontal
3. Untuk setiap kolom pada tabel "Kolom Hideable Visible default (13 kolom data)" (langkah 3 sampai 10): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
4. Klik ikon Pin kolom itu, lalu klik `[Save]`
5. Geser tabel secara horizontal
6. Verifikasi kolom itu membeku (sticky) di kiri saat scroll horizontal
7. Muat ulang halaman (F5), lalu geser tabel secara horizontal
8. Verifikasi kolom itu tetap membeku (sticky) di kiri setelah F5
9. Buka Popup Setup Column, klik ikon Pin kolom itu untuk Unpin, lalu klik `[Save]`
10. Verifikasi kolom itu tidak lagi membeku (sticky) setelah Unpin
11. Pulihkan viewport browser ke ukuran semula

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (membuka tab), menyimpan tiap iterasi (`[Save]`), Unpin di akhir tiap iterasi TC-FA-LIC-319 (S-09), serta langkah 2 dan 11 yang menyempitkan dan memulihkan viewport. Setup Column tidak memakai "Tunggu aksi selesai" karena aksi sisi klien (butir 8 bagian 8b).
- Blok ulang: langkah 3 sampai 10 dijalankan 13 kali. Setelah ekspansi spec ini melewati sekitar 35 langkah (11 langkah nominal). Alasan: satu TC, Setup Column satu tabel dengan satu dataset Pre-setup #12 dan satu kelas harness, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna; satu TC tidak dapat dibagi ke spec lain. Geser per kolom (TC-FA-LIC-318) ada di spec `TC-FA-LIC-E2E-091`.
- Temuan untuk QA: TC-FA-LIC-319 mengandaikan tabel lebih lebar dari viewport tanpa menyebut lebar viewport; spec menyempitkan viewport (langkah 2) dan memulihkannya (langkah 11).
