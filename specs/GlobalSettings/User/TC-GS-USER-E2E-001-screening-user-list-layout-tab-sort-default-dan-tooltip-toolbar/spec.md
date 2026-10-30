---
id: TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar
title: "Screening User List: Layout, Tab, Breadcrumb, Sort Default Name A-Z, Loading Skeleton, dan Tooltip Toolbar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1
  - TC-GS-USER-2
  - TC-GS-USER-3
  - TC-GS-USER-4
  - TC-GS-USER-5
  - TC-GS-USER-6
  - TC-GS-USER-7
  - TC-GS-USER-8
  - TC-GS-USER-25
  - TC-GS-USER-1043
coverage:
  web: automated
---

# Screening User List: Layout, Tab, Breadcrumb, Sort Default Name A-Z, Loading Skeleton, dan Tooltip Toolbar

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk TC-GS-USER-8).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Dewi Lestari (No. 12), Hendra Gunawan (Default User, No. 1), serta user Pre-setup lain di tabel Login User. Spec tidak mengubah atau menghapus data Pre-setup.
- Data Default User seed (TC-GS-USER-1043): Default User `Hendra Gunawan` hasil seed registrasi entitas belum pernah diedit sejak seed, sehingga Modified By-nya `System`. Kondisi ini disediakan tim FE pada entitas uji; spec ini tidak mengedit Default User.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Tiap user diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `andi kecil {runId}-001`, email `andikecil+{runId}-001@qwertysystem.net`. Awal Name huruf kecil dipakai untuk asersi urutan Name A-Z case-insensitive (TC-GS-USER-7): U-1 berada di antara `Ahmad Fauzi` dan `Andi Wijaya`.
  - U-2: Name `Dewi Anggraini {runId}-001`, email `dewianggraini+{runId}-001@qwertysystem.net`. Dipakai sebagai baris kedua hasil Search `Dewi` supaya asersi sort Email (TC-GS-USER-6) memuat dua nilai Email berbeda.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 dan U-2 lewat API.
- Kebutuhan intercept (`Spectra.intercept()`) untuk TC-GS-USER-8: respons daftar User ditahan (tidak dijawab) sampai dilepas lewat langkah eksplisit. Nama endpoint ditentukan tim FE di tahap script. Hook `after` melepas intercept walau spec gagal di tengah.
- Kemampuan teknis: hover elemen; membaca indikator sort pada header kolom.
- State global yang diubah: tidak ada. Suite berjalan serial; spec ini berjalan sebelum spec yang mengedit Default User (lihat Notes).

## Test Steps

### TC-GS-USER-1: Screening halaman User tab User List sub-tab Login User oleh Total Control

1. Klik menu User di sidebar Global Settings
2. Verifikasi Header: Breadcrumb `User > User List > Login User`
3. Verifikasi Header: tidak ada Page Title Header
4. Verifikasi Header: Tab `User List | Position | Division | Custom Field`
5. Verifikasi Header: Tab `User List` berstatus aktif
6. Verifikasi Header: Sub-tab `Login User | Non-Login User`
7. Verifikasi Header: Sub-tab `Login User` berstatus aktif
8. Verifikasi Header: Table Tools rata kanan `Search | Filter | Download | Changelog | [+ User]`
9. Verifikasi Body: kolom checkbox di paling kiri, diikuti kolom `Active (sortable) | Name (sortable) | Email (sortable) | Position (sortable) | Division (sortable) | Access (sortable) | Employee ID (sortable) | Modified By (sortable) | Last Update (sortable) | Column Visibility (⋯) (unsortable)`
10. Klik header kolom Column Visibility (⋯)
11. Verifikasi Overlay Column Visibility terbuka dengan CTA `[Setup Column]` di dalamnya
12. Tutup Overlay Column Visibility dengan menekan Esc
13. Verifikasi Body: setiap baris halaman 1 memiliki row action menu pada kolom Column Visibility (⋯)
14. Verifikasi Body: kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan Custom Field aktif tidak tampil
15. Verifikasi Body: baris halaman 1 terurut Name A-Z
16. Verifikasi Footer: Pagination default 10 baris per halaman
17. Klik pilihan jumlah baris per halaman pada Pagination
18. Verifikasi Footer: pilihan jumlah baris per halaman `10 | 25 | 50 | 100`
19. Tutup pilihan jumlah baris per halaman dengan menekan Esc
20. Verifikasi Footer: input nomor halaman tampil

### TC-GS-USER-2: Tab User List menampilkan sub-tab Login User aktif secara default (diamati pada pembukaan menu User di langkah 1)

21. Verifikasi Tab `User List` aktif
22. Verifikasi Sub-tab `Login User` aktif
23. Verifikasi tabel Login User tampil

### TC-GS-USER-7: Default sort User List Name A-Z saat pertama dibuka (diamati pada pembukaan menu User di langkah 1)

24. Verifikasi baris halaman 1 terurut Name A-Z case-insensitive: `Ahmad Fauzi`, `andi kecil {runId}-001`, `Andi Wijaya` berurutan
25. Verifikasi tidak ada indikator sort aktif di header kolom selain default Name

### TC-GS-USER-3: Breadcrumb berubah ke `User > Position` saat pindah ke tab Position

26. Klik Tab `Position`
27. Verifikasi Breadcrumb `User > Position`
28. Verifikasi Tab `Position` aktif
29. Klik Tab `User List`

### TC-GS-USER-4: Breadcrumb berubah ke `User > Division` saat pindah ke tab Division

30. Klik Tab `Division`
31. Verifikasi Breadcrumb `User > Division`
32. Verifikasi Tab `Division` aktif
33. Klik Tab `User List`

### TC-GS-USER-5: Breadcrumb berubah ke `User > Custom Field` saat pindah ke tab Custom Field

34. Klik Tab `Custom Field`
35. Verifikasi Breadcrumb `User > Custom Field`
36. Verifikasi Tab `Custom Field` aktif
37. Klik Tab `User List`

### TC-GS-USER-8: Loading state User List menampilkan skeleton

38. Pasang intercept pada respons daftar User: tahan respons sampai dilepas
39. Klik menu User di sidebar Global Settings
40. Verifikasi tabel menampilkan skeleton loading selama respons belum diterima
41. Lepas intercept respons daftar User sehingga respons diterima
42. Verifikasi skeleton diganti baris data

### TC-GS-USER-25: Hover icon toolbar menampilkan tooltip nama fungsi

43. Hover icon Search
44. Verifikasi tooltip `Search`
45. Hover icon Filter
46. Verifikasi tooltip `Filter`
47. Hover icon Download
48. Verifikasi tooltip `Download`
49. Hover icon Changelog
50. Verifikasi tooltip `Changelog`
51. Hover header kolom Column Visibility (⋯)
52. Verifikasi tooltip `Column Visibility`

### TC-GS-USER-1043: User List, Modified By Default User seed menampilkan System

53. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
54. Verifikasi sel Modified By baris Hendra Gunawan menampilkan `System`

### TC-GS-USER-6: Pindah tab lalu kembali tidak mereset state Search dan Sort di tab User List

55. Ganti isi kotak search dengan `Dewi`, tekan Enter
56. Klik header kolom Email (sort ascending)
57. Klik Tab `Position`
58. Klik Tab `User List`
59. Verifikasi kotak Search tetap terisi `Dewi`
60. Verifikasi tabel tetap tersaring hanya ke baris `Dewi Lestari` dan `Dewi Anggraini {runId}-001`
61. Verifikasi indikator sort Email ascending tetap aktif dan kedua baris terurut ascending menurut Email

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (61 langkah) karena sepuluh TC screening User List berada di satu kelas harness (fungsional, baca saja; intercept hanya menahan respons untuk mengamati skeleton sehingga bukan kelas b) dan satu layar. Tiap blok TC berdiri sendiri dan hanya membaca data, jadi kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan layar dipakai bersama (langkah 1) dan dibuka ulang hanya untuk TC-GS-USER-8.
- Urutan TC sumber diubah: TC-GS-USER-7 dan TC-GS-USER-2 diasersi tepat sesudah TC-GS-USER-1 karena mengamati pembukaan menu User yang sama (langkah 1) dan keadaan default (sort, tab aktif) harus diasersi sebelum state diubah (8b butir 5). TC-GS-USER-6 ditaruh terakhir karena mengubah Search dan Sort; urutan itu menghindari langkah pembersihan state untuk TC lain. TC-GS-USER-1043 mendahului TC-GS-USER-6 supaya kotak Search masih kosong saat dipakai.
- TC-GS-USER-1043 mensyaratkan Default User yang belum pernah diedit. Suite berjalan serial dan spec ini harus berjalan sebelum spec yang mengedit Default User (TC-GS-USER-82 dan TC lain yang mengedit Default User); spec ini sendiri tidak mengedit Default User. Asersi Default User seed di Tab Changelog (TC-GS-USER-1044) ada di spec lain.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 dan 12 (membuka dan menutup Overlay Column Visibility untuk mengamati CTA `[Setup Column]` dan row action menu, Expected TC-GS-USER-1 b.i), 17 dan 19 (membuka dan menutup pilihan jumlah baris per halaman, Expected TC-GS-USER-1 c), 29, 33, dan 37 (kembali ke Tab `User List` agar precondition TC berikutnya terpenuhi), 38 dan 41 (pasang dan lepas intercept), 39 (membuka layar ulang untuk TC-GS-USER-8).
- Langkah 21 sampai 25 dan langkah 40 tidak punya aksi sendiri: mengamati keadaan hasil pembukaan menu User (langkah 1) dan hasil langkah 39.
- Pembagian TC: halaman Tab Position, Division, dan Custom Field hanya diasersi breadcrumb dan status aktif tab; isi tab diuji di file TC modul masing-masing. Guided Tooltip diuji di spec TC-GS-USER-E2E-005 dan TC-GS-USER-E2E-006 (flag `gs-user` sudah `seen` oleh hook suite di spec ini).
- Data U-1 dan U-2 ditambahkan oleh spec karena asersi urutan case-insensitive (TC-GS-USER-7) dan sort Email (TC-GS-USER-6) butuh sedikitnya dua nilai berbeda pada kolom itu; nilai Pre-setup tidak memuat Name berawalan huruf kecil.
- Temuan untuk QA:
  - TC-GS-USER-7 Expected a memberi contoh `Agus`, `andi`, `Budi`; Tabel Pre-setup tidak memuat user Login berawalan huruf kecil dan `Agus Prasetyo` adalah Non-Login User. Spec memakai user seed U-1 (`andi kecil {runId}-001`).
  - TC-GS-USER-6 Expected a berbunyi tabel tersaring ke baris Dewi Lestari (satu baris), sehingga urutan sort Email tidak dapat diamati. Spec menambah user seed U-2 dan mengasersi dua baris; TC perlu menyebut data pembanding.
  - TC-GS-USER-25 menyebut header kolom `Actions (⋯)`, sedangkan TC-GS-USER-1 menyebutnya `Column Visibility (⋯)` dan tooltip-nya `Column Visibility`. Spec memakai `Column Visibility (⋯)`.
  - TC-GS-USER-1043 mensyaratkan entitas yang baru diregistrasi dengan Default User belum pernah diedit; TC tidak menyebut cara menjamin kondisi itu pada entitas Pre-setup bersama. Disediakan tim FE.
  - TC-GS-USER-8 menyebut "network throttle" tanpa durasi atau endpoint; spec menahan respons sampai dilepas lewat langkah 41.
  - TC-GS-USER-1 Expected b.i menyebut Overlay Column Visibility dengan CTA `[Setup Column]`; label item di Division adalah `Setup Column...`. Spec mengikuti TC-GS-USER-1 (`[Setup Column]`).
