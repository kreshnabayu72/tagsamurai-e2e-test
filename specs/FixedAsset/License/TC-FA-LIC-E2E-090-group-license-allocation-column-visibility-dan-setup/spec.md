---
id: TC-FA-LIC-E2E-090-group-license-allocation-column-visibility-dan-setup
title: "Group License Allocation: Screening Column Visibility dan Setup Column, serta Ceklis dan Unceklis Kolom Hideable Visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-315
  - TC-FA-LIC-316
  - TC-FA-LIC-317
coverage:
  web: automated
---

# Group License Allocation: Screening Column Visibility dan Setup Column, serta Ceklis dan Unceklis Kolom Hideable Visible

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; hierarki Produksi, Kantor Pusat, Cabang Surabaya, Cabang Medan. Tabel Group License Allocation pada node All Groups menampilkan empat baris level 1. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.kuotaHierarki` (belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada.
- Tabel "Kolom Hideable Visible default (13 kolom data)" (parameter langkah 15 sampai 24): `Group Name`, `Group Code`, `Allocated Quota`, `Allocated to Subgroups`, `Used by This Group`, `Reserved by This Group`, `Remaining Quota`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`, `+ Maps`, `+ IT Inventory`.
- Konfigurasi kolom: spec ini menyimpan Setup Column di browser. Tiap iterasi memulihkan kolom ke tampil dan hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12; pemulihan konfigurasi kolom. Kemampuan teknis: membaca isi Live Preview Setup Column.

## Test Steps

### TC-FA-LIC-315: Screening Overlay Column Visibility

1. Klik tab Allocation Quota di node All Groups
2. Klik header kolom Actions `⋯`
3. Verifikasi overlay (Quick Panel) menampilkan daftar kolom berurutan dengan checkbox dan drag handle: `Group Name` (tercentang), `Group Code` (tercentang), `Allocated Quota` (tercentang), `Allocated to Subgroups` (tercentang), `Used by This Group` (tercentang), `Reserved by This Group` (tercentang), `Remaining Quota` (tercentang), `+ Audit` (tercentang), `+ Tracking` (tercentang), `+ Maintenance Routine` (tercentang), `+ Repair Ticketing` (tercentang), `+ Maps` (tercentang), `+ IT Inventory` (tercentang)
4. Verifikasi item `Setup Column...` di bagian bawah panel

### TC-FA-LIC-316: Screening Popup Setup Column tiga zona

5. Klik item `Setup Column...` pada overlay yang terbuka
6. Verifikasi Header: Title `Setup Column`
7. Verifikasi Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
8. Verifikasi Header: tombol `(×)`
9. Verifikasi Body: daftar kolom dengan checkbox, drag handle, dan ikon Pin
10. Verifikasi Body: Live Preview tabel
11. Verifikasi Footer: tombol `[Reset to Default]`
12. Verifikasi Footer: tombol `[Save]`
13. Verifikasi tidak ada tombol `[Cancel]`
14. Klik `(×)` untuk menutup popup tanpa perubahan

### TC-FA-LIC-317: Ceklis dan unceklis per kelas kolom Hideable Visible default

15. Untuk setiap kolom pada tabel "Kolom Hideable Visible default (13 kolom data)" (langkah 15 sampai 24): buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
16. Hilangkan centang kolom itu
17. Verifikasi kolom itu hilang dari Live Preview
18. Klik `[Save]`
19. Verifikasi kolom itu hilang dari tabel setelah Save
20. Muat ulang halaman (F5)
21. Verifikasi kolom itu tetap hilang setelah F5
22. Buka Popup Setup Column, lalu centang kembali kolom itu
23. Verifikasi kolom itu kembali tampil di Live Preview
24. Klik `[Save]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: menutup popup dengan `(×)` pada TC-FA-LIC-316 dan `[Save]` penutup iterasi (langkah 24) yang memulihkan konfigurasi kolom (S-09). Setup Column tidak memakai "Tunggu aksi selesai" karena aksi sisi klien (butir 8 bagian 8b).
- Blok ulang: langkah 15 sampai 24 dijalankan 13 kali. Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: seluruh blok adalah Setup Column satu tabel dengan satu dataset Pre-setup #12 dan satu kelas harness, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Temuan untuk QA: pada TC-FA-LIC-317 Expected "kembali tampil saat dicentang ulang" tidak menyebut apakah diasersi di Live Preview atau tabel; spec mengasersi di Live Preview lalu menyimpan untuk memulihkan konfigurasi.
