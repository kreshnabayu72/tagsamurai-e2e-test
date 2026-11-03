---
id: TC-FA-CAID-E2E-056-code-list-setup-column-screening-hide-drag
title: "Modal View Code List: Setup Column Screening, Hide, dan Drag Reorder"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-132
  - TC-FA-CAID-133
  - TC-FA-CAID-134
  - TC-FA-CAID-135
coverage:
  web: automated
---

# Modal View Code List: Setup Column Screening, Hide, dan Drag Reorder

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: Preferensi kolom Setup Column Modal View Code List disimpan di browser; hook `after` spec ini menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE. Kolom `Code` dan urutan kolom tab `Group Codes` diubah pada TC-FA-CAID-134 dan 135.
- Kemampuan teknis: seret-dan-lepas (drag and drop) baris kolom pada Popup Setup Column dan muat ulang halaman.

## Test Steps

### TC-FA-CAID-132: Screening overlay Column Visibility

1. Klik tautan `[View Code List]`
2. Hover header kolom Actions (⋯)
3. Verifikasi tooltip header kolom Actions berbunyi `Column Visibility`
4. Klik header kolom Actions (⋯)
5. Verifikasi overlay memuat daftar kolom `Group Name` dan `Code` masing-masing dengan checkbox tercentang dan enabled
6. Verifikasi tiap kolom pada overlay memiliki drag handle
7. Verifikasi overlay memuat item `Setup Column...` di bagian bawah

### TC-FA-CAID-133: Screening Popup Setup Column

8. Klik `Setup Column...`
9. Verifikasi Zona Header: Title `Setup Column`
10. Verifikasi Zona Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi Zona Header: tombol close `[✕]`
12. Verifikasi Zona Body: daftar kolom `Group Name` dan `Code` tercentang dengan drag handle dan icon Pin
13. Verifikasi Zona Body: Live Preview tabel
14. Verifikasi Zona Footer: tombol `[Reset to Default]` dan `[Save]`
15. Verifikasi Zona Footer: tidak ada tombol `[Cancel]`

### TC-FA-CAID-134: Hide dan Unhide kolom tersimpan setelah refresh

16. Hilangkan centang `Code`
17. Klik `[Save]`
18. Verifikasi setelah Save tabel hanya menampilkan kolom `Group Name`
19. Muat ulang halaman
20. Klik tautan `[View Code List]` untuk membuka kembali modal
21. Verifikasi setelah refresh kolom `Code` tetap tersembunyi
22. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
23. Centang `Code`
24. Klik `[Save]`
25. Verifikasi setelah dicentang lagi dan Save kolom `Code` tampil kembali

### TC-FA-CAID-135: Drag reorder kolom

26. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
27. Seret `Code` ke atas `Group Name`
28. Klik `[Save]`
29. Verifikasi setelah Save urutan kolom menjadi `Code` lalu `Group Name`
30. Muat ulang halaman
31. Klik tautan `[View Code List]` untuk membuka kembali modal
32. Verifikasi setelah refresh urutan tetap `Code`, `Group Name`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 32 langkah.
- Subjudul `###` memetakan langkah ke id TC granular. Modal tetap terbuka dari TC-FA-CAID-132 ke TC-FA-CAID-133 dan seterusnya sampai muat ulang pada langkah 19; langkah buka modal tidak diulang di antara TC yang tidak menutupnya.
- Muat ulang halaman (langkah 19 dan 30) dilakukan pada form Custom Asset ID yang tidak diubah (bukan dirty), sehingga tidak ada dialog `beforeunload`.
- Langkah penghubung (tanpa `Verifikasi`): tidak ada selain pembukaan kembali modal sesudah muat ulang (langkah TC).
- Pemulihan konfigurasi kolom dilakukan hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`, TC-FA-CAID-137 ada di spec 057).
- Pembagian TC lintas spec: TC-FA-CAID-136 sampai 138 ada di spec 057; TC-FA-CAID-139 sampai 141 ada di spec 065.
- Temuan untuk QA:
  - TC-FA-CAID-132 menyebut item overlay berlabel `Setup Column...`, sedangkan TC-FA-CAID-116 menyebut CTA `[Setup Column]` pada kolom Column Visibility; label yang benar perlu dikonfirmasi.
  - TC-FA-CAID-135 menyebut "Seret `Code` ke atas `Group Name`" tanpa menyebut mekanisme seret (mouse atau keyboard); spec memakai seret-dan-lepas.
