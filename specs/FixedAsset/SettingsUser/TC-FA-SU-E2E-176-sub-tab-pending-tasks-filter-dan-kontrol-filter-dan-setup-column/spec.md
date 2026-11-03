---
id: TC-FA-SU-E2E-176-sub-tab-pending-tasks-filter-dan-kontrol-filter-dan-setup-column
title: "Sub-tab Pending Tasks: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-523
  - TC-FA-SU-524
  - TC-FA-SU-525
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.

## Test Steps

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-523: Chip dan checkbox dropdown Filter sinkron dua arah, logika OR dalam field

2. Klik icon Filter
3. Buka dropdown Transaction
4. Centang `Assignment` dan `Borrowing`
5. Klik `[Apply]`
6. Verifikasi dua chip `Assignment` dan `Borrowing` tampil di dalam field Transaction
7. Verifikasi hasil adalah gabungan (OR) kedua opsi: `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`
8. Klik ✕ pada chip `Assignment` tanpa membuka dropdown
9. Verifikasi chip `Assignment` hilang
10. Buka dropdown Transaction
11. Verifikasi checkbox opsi `Assignment` ter-uncheck
12. Verifikasi chip `Borrowing` tetap tampil
13. Hilangkan centang opsi `Borrowing`
14. Verifikasi chip `Borrowing` hilang
15. Ketik `assign` di kotak cari dropdown Transaction
16. Verifikasi opsi dropdown menyempit menjadi `Assignment` (substring, tidak case-sensitive)
17. Ganti isi kotak cari dropdown dengan `zzz`
18. Verifikasi `No results found` tampil di dalam dropdown
19. Klik icon Filter

### TC-FA-SU-524: Screening Overlay Column Visibility

20. Hover header kolom Actions (⋯)
21. Verifikasi tooltip `Column Visibility`
22. Klik header kolom Actions (⋯)
23. Verifikasi overlay Column Visibility tampil
24. Verifikasi daftar kolom berurutan `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`
25. Verifikasi checkbox ☑ Hideable terpilih dan enabled pada tiap kolom
26. Verifikasi drag handle tampil pada tiap kolom
27. Verifikasi item `Setup Column...` di bagian bawah overlay
28. Tekan Esc

### TC-FA-SU-525: Screening Popup Setup Column dan Preview Table

29. Klik `Setup Column...`
30. Verifikasi header popup: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, icon close ✕
31. Verifikasi daftar kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`
32. Verifikasi checkbox tampil pada tiap kolom
33. Verifikasi drag handle tampil pada tiap kolom
34. Verifikasi icon Pin tampil pada tiap kolom
35. Verifikasi Live Preview tabel tampil
36. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan
37. Verifikasi tanpa `[Cancel]` di footer
38. Klik ✕ pada popup Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; `Klik icon Filter` menutup panel sebelum TC-FA-SU-524; `Tekan Esc` menutup overlay Column Visibility; `✕` menutup popup Setup Column (S-09).
- Langkah `Ketik assign` dan `Verifikasi opsi dropdown menyempit` pada TC-FA-SU-523 ditambahkan karena Expected d menyebut penyempitan opsi (substring, tidak case-sensitive) sementara langkah TC hanya mengetik keyword tanpa hasil (S-03).
- Jumlah langkah: 38 tertulis, 38 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (38 langkah). Seluruh blok berada pada satu surface (satu sub-tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-SU-523 langkah 3 mencentang dua opsi lalu langkah 5 meng-uncheck "opsi yang tersisa" sehingga Expected c ("chip lain tetap") tidak punya chip pembanding; spec mengasersi chip `Borrowing` hilang setelah di-uncheck dan chip lain tidak ada.
  - TC-FA-SU-523 tidak menyebut opsi yang dicentang; spec memilih `Assignment` dan `Borrowing` (seluruh opsi DISTINCT dari TC-FA-SU-516).
