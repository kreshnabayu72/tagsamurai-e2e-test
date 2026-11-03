---
id: TC-FA-CAID-E2E-057-code-list-setup-column-pin-reset-to-default-dan-penutupan-popup
title: "Modal View Code List: Setup Column Pin, Reset to Default, dan Penutupan Popup"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-136
  - TC-FA-CAID-137
  - TC-FA-CAID-138
coverage:
  web: automated
---

# Modal View Code List: Setup Column Pin, Reset to Default, dan Penutupan Popup

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: Preferensi kolom Setup Column Modal View Code List disimpan di browser; hook `after` spec ini menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE. Pin kolom dan urutan kolom tab `Group Codes` diubah pada TC-FA-CAID-136 dan 137.
- Kemampuan teknis: seret-dan-lepas baris kolom pada Popup Setup Column dan scroll horizontal tabel.

## Test Steps

### TC-FA-CAID-136: Pin kolom Group Name dan Code

1. Klik tautan `[View Code List]`
2. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
3. Klik icon Pin pada `Group Name`
4. Klik `[Save]`
5. Verifikasi `Group Name` ter-pin ke kiri
6. Scroll tabel secara horizontal
7. Verifikasi `Group Name` tetap di posisinya saat tabel di-scroll horizontal
8. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
9. Klik Unpin pada `Group Name`
10. Klik icon Pin pada `Code`
11. Klik `[Save]`
12. Verifikasi setelah Unpin `Group Name` dan Pin `Code` hanya `Code` yang ter-pin

### TC-FA-CAID-137: Reset to Default

13. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
14. Hilangkan centang `Code`
15. Seret `Code` ke atas `Group Name`
16. Klik `[Reset to Default]`
17. Klik `[Save]`
18. Verifikasi setelah Reset dan Save kolom `Group Name` lalu `Code` tampil keduanya dengan urutan default
19. Verifikasi tidak ada kolom yang di-pin

### TC-FA-CAID-138: Menutup Popup Setup Column membuang perubahan

20. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
21. Hilangkan centang `Code`
22. Klik `[✕]`
23. Verifikasi setelah `[✕]` Popup Setup Column tertutup
24. Verifikasi setelah `[✕]` tabel Code List tetap menampilkan kolom `Group Name` dan `Code` (perubahan tidak tersimpan)
25. Buka Popup Setup Column (klik header kolom Actions (⋯), lalu klik `Setup Column...`)
26. Hilangkan centang `Code`
27. Tekan `Esc`
28. Verifikasi setelah `Esc` Popup Setup Column tertutup
29. Verifikasi setelah `Esc` tabel Code List tetap menampilkan kolom `Group Name` dan `Code` (perubahan tidak tersimpan)

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 29 langkah.
- Subjudul `###` memetakan langkah ke id TC granular. Modal View Code List dibuka sekali pada langkah 1 dan tetap terbuka; TC-FA-CAID-137 dan 138 tidak mengulang pembukaan modal.
- Pembukaan Popup Setup Column ditulis sebagai satu langkah (klik header kolom Actions (⋯), lalu `Setup Column...`) mengikuti "Buka Popup Setup Column" pada TC.
- TC-FA-CAID-137 menyimpan `[Reset to Default]` lalu `[Save]` sehingga konfigurasi kolom tersimpan kembali ke default; pin yang diatur TC-FA-CAID-136 dihapus oleh langkah itu. Hook `after` tetap menghapus preferensi kolom di browser sebagai cadangan.
- Pembagian TC lintas spec: TC-FA-CAID-132 sampai 135 ada di spec 056; TC-FA-CAID-139 sampai 141 ada di spec 065.
- Temuan untuk QA:
  - TC-FA-CAID-138 Expected menulis "modal tertutup"; spec menafsirkannya sebagai Popup Setup Column tertutup dan tabel Code List tetap terlihat (Modal View Code List tetap terbuka), karena Expected menyebut tabel Code List tetap menampilkan kolom. Perlu konfirmasi.
  - TC-FA-CAID-136 menyebut "tetap di posisinya saat tabel di-scroll horizontal" tanpa menyebut lebar viewport yang membuat tabel dapat di-scroll; kemampuan scroll horizontal dicatat di Prerequisites.
