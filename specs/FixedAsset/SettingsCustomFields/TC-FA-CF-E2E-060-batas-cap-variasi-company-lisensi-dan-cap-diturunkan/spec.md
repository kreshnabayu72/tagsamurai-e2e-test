---
id: TC-FA-CF-E2E-060-batas-cap-variasi-company-lisensi-dan-cap-diturunkan
title: "Batas Cap: Variasi Company, Lisensi FA-7 Tidak Aktif, dan Cap Diturunkan Saat Modal Create Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-194
  - TC-FA-CF-195
  - TC-FA-CF-196
  - TC-FA-CF-605
coverage:
  web: automated
---

# Batas Cap: Variasi Company, Lisensi FA-7 Tidak Aktif, dan Cap Diturunkan Saat Modal Create Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`): spec menurunkan lalu memulihkan Max custom fields per asset name Company Cap.
- Akun aktor utama (login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada Fixed Asset > Settings > Custom Fields, tab General): Total Control Company Cap `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Cap (Pre-setup #16). Password lewat `Spectra.env.FA_TC_CAP_PASSWORD`.
- Akun tambahan (ganti akun eksplisit di langkah 12, 22, dan 31): Total Control Company Cap NoAN dengan `Spectra.env.FA_TC_CAPNOAN_PASSWORD`, Total Control Company Cap Many dengan `Spectra.env.FA_TC_CAPMANY_PASSWORD`, dan Total Control Company Cap FA7 dengan `Spectra.env.FA_TC_CAPFA7_PASSWORD`. Keempat akun Total Control dan nama env password tidak tertulis sebagai baris sendiri di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE dan keempat nama env adalah nama baru yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor utama dan tambahan, dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (Pre-setup #16; hanya dibaca, dipulihkan hook `before` lewat seed reset Company yang disediakan tim FE/BE):
  - Company Cap: Max custom fields per asset name 2; Asset Name `Compressor`, `Generator`, `Pump`, `Turbine`; field Active `Cap General` (General), `Cap Pump` (`Pump`), `Cap Compressor` (`Compressor`); field Inactive `Cap Pump Inactive`, `Cap Gen Inactive`, `Cap Both Inactive`, `Cap Orphan`.
  - Company Cap NoAN: cap 2, dua field General Active, tanpa Asset Name.
  - Company Cap Many: cap 1, lima Asset Name `Boiler`, `Compressor`, `Generator`, `Pump`, `Turbine` masing-masing penuh.
  - Company Cap FA7: cap 2, lisensi FA-7 tidak aktif, `Pump` memiliki satu field General Active dan satu field Accounting Active.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-060`; tidak ada yang tersimpan): `Cap Down {runId}-060` (Company Cap), `Gen Self {runId}-060` (Company Cap NoAN), `Cap Many {runId}-060` (Company Cap Many), dan `Cap Acc {runId}-060` (Company Cap FA7).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field keempat Company yang namanya memuat `{runId}-060`; kembalikan Max custom fields per asset name Company Cap ke 2.
- Kemampuan teknis: sesi API aktor (login API dengan akun yang sama; tidak dihitung sebagai sesi web) yang mengubah Max custom fields per asset name Company Cap lewat Plans and Features (disediakan tim FE/BE; TC tidak mendefinisikan mekanismenya); ganti akun dan Company di tengah spec.
- State global yang diubah: Max custom fields per asset name Company Cap (diturunkan ke 1 pada langkah 3, dipulihkan ke 2 pada langkah 11 dan hook `after`).

## Test Steps

### TC-FA-CF-605: Cap diturunkan saat modal Create terbuka: Submit berikutnya mengikuti cap baru

1. Klik [+ Custom Field]
2. Isi Field Name `Cap Down {runId}-060` dan Data Type `Text`, pilih Scope `Specific Asset Name` dengan `Generator`
3. Turunkan Max custom fields per asset name Company Cap menjadi 1 lewat sesi API aktor hingga cap baru tersimpan
4. Klik [Submit]
5. Verifikasi dialog `Limit Reached` dengan `[Limit]` 1 tampil di atas modal Create
6. Klik `[OK]`
7. Klik `[✕]`
8. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
9. Klik `[Leave]`
10. Verifikasi field existing tidak dihapus: baris `Cap General`, `Cap Pump`, `Cap Compressor`, `Cap Pump Inactive`, `Cap Gen Inactive`, `Cap Both Inactive`, dan `Cap Orphan` tampil pada tabel
11. Kembalikan Max custom fields per asset name Company Cap menjadi 2 lewat sesi API aktor hingga cap tersimpan

### TC-FA-CF-194: Submit Scope General ditolak bila jumlah field Active ber-Scope General sudah mencapai cap saat belum ada Asset Name

12. Ganti akun: logout, lalu login sebagai Total Control Company Cap NoAN dengan `Spectra.env.FA_TC_CAPNOAN_PASSWORD` dan buka Fixed Asset > Settings > Custom Fields (tab General)
13. Klik [+ Custom Field]
14. Isi Field Name `Gen Self {runId}-060` dan Data Type `Text`, Scope `General`
15. Klik [Submit]
16. Verifikasi dialog `Limit Reached` dengan teks "You've reached the limit of 2 custom fields for General scope. Remove an existing field or narrow the scope, or contact support if you need a higher limit."
17. Verifikasi field tidak tersimpan: modal tetap terbuka
18. Klik `[OK]`
19. Klik `[✕]`
20. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
21. Klik `[Leave]`

### TC-FA-CF-195: Dialog batas menyebut maksimal tiga nama Asset Name lalu sisanya dengan and n more

22. Ganti akun: logout, lalu login sebagai Total Control Company Cap Many dengan `Spectra.env.FA_TC_CAPMANY_PASSWORD` dan buka Fixed Asset > Settings > Custom Fields (tab General)
23. Klik [+ Custom Field]
24. Isi Field Name `Cap Many {runId}-060` dan Data Type `Text`, Scope `General`
25. Klik [Submit]
26. Verifikasi dialog `Limit Reached` dengan teks "You've reached the limit of 1 custom fields for Boiler, Compressor, Generator, and 2 more. Remove an existing field or narrow the scope, or contact support if you need a higher limit."
27. Klik `[OK]`
28. Klik `[✕]`
29. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
30. Klik `[Leave]`

### TC-FA-CF-196: Field Accounting Active tetap dihitung ke cap per Asset Name saat lisensi FA-7 tidak aktif

31. Ganti akun: logout, lalu login sebagai Total Control Company Cap FA7 dengan `Spectra.env.FA_TC_CAPFA7_PASSWORD` dan buka Fixed Asset > Settings > Custom Fields (tab General)
32. Klik [+ Custom Field]
33. Isi Field Name `Cap Acc {runId}-060` dan Data Type `Text` pada tab General, pilih Scope `Specific Asset Name` dengan `Pump`
34. Klik [Submit]
35. Verifikasi dialog `Limit Reached` tampil karena field Accounting Active tetap dihitung
36. Verifikasi field tidak tersimpan: modal tetap terbuka
37. Klik `[OK]`
38. Klik `[✕]`
39. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
40. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 605, 194, 195, 196 (urutan sumber 194, 195, 196, 605). TC-FA-CF-605 memakai Company Cap, akun yang login di hook `before`, sehingga lebih dulu; tiga TC berikutnya masing-masing memakai Company varian dan akun sendiri sehingga ganti akun eksplisit (langkah 12, 22, 31; S-07). Pelaku kedua pada TC-FA-CF-605 hanya memicu perubahan state sehingga memakai sesi API dan langkah pemicunya ditulis "... hingga ... tersimpan" (R-20); itu bukan konteks kedua kelas c.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 6, 7, 9, 11, 12, 13, 18, 19, 21, 22, 23, 27, 28, 30, 31, 32, 37, 38, 40, serta pengisian form dan klik tombol sebagai bagian langkah TC. Klik `[OK]` dan penutupan form lewat `[✕]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08) menutup form dirty sebelum ganti akun atau akhir spec. Langkah 11 memulihkan cap sebelum ganti akun (R-08).
- Spec melewati sekitar 35 langkah (40 langkah): empat TC satu topik (batas cap per Asset Name) dengan empat Company varian yang berdiri sendiri; tiap blok memakai Company dan akunnya sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Pemecahan hanya menambah login, hook, dan seed reset Company.
- Asersi "field tidak tersimpan" (langkah 17 dan 36) diamati lewat modal yang tetap terbuka; tabel Company varian tidak dibaca ulang.
- Teks dialog TC-FA-CF-605 diasersi hanya `[Limit]` bernilai 1 karena TC tidak menyebut teks lengkap dialog.
- Temuan untuk QA:
  - Akun Total Control untuk Company Cap, Cap NoAN, Cap Many, dan Cap FA7 tidak tertulis sebagai baris sendiri di Pre-setup TC; ditulis "disediakan tim FE" (S-11).
  - TC-FA-CF-605: Langkah 2 TC ("Sesi 2 menurunkan cap menjadi 1 di Plans and Features") tidak menyebut akun maupun mekanismenya; spec memakai sesi API aktor yang disediakan tim FE/BE dan tidak mengarang endpoint (S-13). Teks lengkap dialog `Limit Reached` tidak ditulis di Expected.
  - TC-FA-CF-605: Expected "field existing tidak dihapus" tidak menyebut field yang dimaksud; spec memakai tujuh field Company Cap pada Pre-setup #16.
  - Nama field memakai suffix `{runId}-060` (S-12) sehingga tidak sama dengan `Gen Self`, `Cap Many`, dan `Cap Acc` pada Data Uji TC.
