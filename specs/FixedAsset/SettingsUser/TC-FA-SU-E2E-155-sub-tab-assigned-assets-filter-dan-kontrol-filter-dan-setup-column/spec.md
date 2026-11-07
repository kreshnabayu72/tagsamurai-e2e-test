---
id: TC-FA-SU-E2E-155-sub-tab-assigned-assets-filter-dan-kontrol-filter-dan-setup-column
title: "Sub-tab Assigned Assets: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-456
  - TC-FA-SU-457
  - TC-FA-SU-458
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-456: Chip dan checkbox dropdown Filter Sub-tab Assigned Assets sinkron dua arah, logika OR dalam field

1. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Klik icon Filter
4. Buka dropdown Name
5. Centang `AC Split Ruang Kerja`
6. Centang `Lemari Arsip`
7. Klik `[Apply]`
8. Verifikasi dua chip `AC Split Ruang Kerja` dan `Lemari Arsip` tampil di dalam field Name
9. Verifikasi hasil tabel adalah gabungan (OR) kedua opsi
10. Klik ✕ pada chip `Lemari Arsip` tanpa membuka dropdown
11. Verifikasi chip `Lemari Arsip` hilang
12. Verifikasi chip `AC Split Ruang Kerja` tetap tampil
13. Buka dropdown Name
14. Verifikasi checkbox opsi `Lemari Arsip` ter-uncheck
15. Centang kembali `Lemari Arsip`
16. Uncheck `AC Split Ruang Kerja`
17. Verifikasi chip `AC Split Ruang Kerja` hilang
18. Verifikasi chip `Lemari Arsip` tetap tampil
19. Ketik `ARSIP` di kotak cari dropdown
20. Verifikasi opsi dropdown dipersempit menjadi `Lemari Arsip` (substring, tidak case-sensitive)
21. Ganti isi kotak cari dropdown dengan `zzz-tidak-ada`
22. Verifikasi dropdown menampilkan `No results found`
23. Tekan Esc untuk menutup dropdown
24. Klik `[Clear Field]`
25. Klik `[Apply]`
26. Klik icon Filter untuk menutup panel

### TC-FA-SU-457: Screening Overlay Column Visibility Sub-tab Assigned Assets

27. Hover header kolom Actions (⋯)
28. Verifikasi tooltip `Column Visibility` tampil pada header
29. Klik header kolom Actions (⋯)
30. Verifikasi overlay Column Visibility tampil
31. Verifikasi daftar kolom berurutan `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `PIC`
32. Verifikasi tiap kolom memiliki checkbox ☑ Hideable terpilih dan enabled
33. Verifikasi tiap kolom memiliki drag handle
34. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
35. Tekan Esc untuk menutup overlay

### TC-FA-SU-458: Screening Popup Setup Column dan Preview Table Sub-tab Assigned Assets

36. Klik header kolom Actions (⋯)
37. Klik `Setup Column...`
38. Verifikasi Title popup `Setup Column`
39. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
40. Verifikasi icon close ✕ tampil di header popup
41. Verifikasi body memuat daftar kolom `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `PIC`
42. Verifikasi tiap kolom memiliki checkbox
43. Verifikasi tiap kolom memiliki drag handle
44. Verifikasi tiap kolom memiliki icon Pin
45. Verifikasi Live Preview tabel tampil
46. Verifikasi footer menampilkan `[Reset to Default]` dan `[Save]` rata kanan
47. Verifikasi footer tanpa `[Cancel]`
48. Klik ✕ pada popup Setup Column

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): Search nama `Budi Santoso` serta pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Opsi `AC Split Ruang Kerja` dan `Lemari Arsip` (field Name) serta kata kunci cari dropdown `ARSIP` dan `zzz-tidak-ada` dipilih spec karena TC-FA-SU-456 tidak menyebut nilainya; `ARSIP` berhuruf besar untuk membuktikan pencarian tidak case-sensitive.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (48 langkah, 48 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: Setup Column yang menyimpan konfigurasi (TC-FA-SU-459 sampai 462) ada di spec 156 dan 157; TC-FA-SU-457 dan 458 hanya screening dan tidak menyimpan apa pun.
- Temuan untuk QA (S-15):
  - TC-FA-SU-456 Langkah 5 ("uncheck opsi yang tersisa") meninggalkan nol chip sehingga Expected c ("chip lain tetap") tidak teramati; spec mencentang kembali satu opsi lalu meng-uncheck opsi lain sebelum mengasersi Expected c.
  - TC-FA-SU-456 Expected d tidak menyebut kata kunci pencarian yang mempersempit opsi; spec memakai `ARSIP`.
