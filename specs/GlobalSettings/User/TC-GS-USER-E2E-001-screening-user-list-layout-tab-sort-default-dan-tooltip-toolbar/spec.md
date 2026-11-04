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
  - TC-GS-USER-1044
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
- Data Default User seed (TC-GS-USER-1043 dan TC-GS-USER-1044): Default User `Hendra Gunawan` hasil seed registrasi entitas belum pernah diedit sejak seed, sehingga Modified By-nya `System` dan baris Changelog paling awalnya `Create` oleh `System`. Kondisi ini disediakan tim FE pada entitas uji; spec ini tidak mengedit Default User. Spec ini berjalan pada client bersama (bukan client khusus; hanya spec 004 memakai client khusus) dan harus berjalan sebelum spec yang mengedit Default User (012, 015, 017, 032) menurut urutan eksekusi serial suite (`suite.md`).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Tiap user diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `andi kecil {runId}-001`, email `andikecil+{runId}-001@qwertysystem.net`. Awal Name huruf kecil dipakai untuk asersi urutan Name A-Z case-insensitive (TC-GS-USER-7): Urutan diasersi lewat Search `{runId}-001` (langkah 24 dan 25) sehingga hanya memuat baris seed, tidak bergantung pada baris Pre-setup.
  - U-2: Name `Dewi Anggraini {runId}-001`, email `dewianggraini+{runId}-001@qwertysystem.net`. Dipakai bersama U-1 sebagai pasangan baris seed hasil Search `{runId}-001` supaya asersi sort Email (TC-GS-USER-6, langkah 69 dan 70) memuat dua nilai Email berbeda tanpa baris Pre-setup, dan sebagai baris kedua hasil Search `Dewi`.
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
15. Verifikasi Body: header kolom Name menampilkan indikator sort aktif default (urutan baris diasersi pada langkah 25 setelah Search `{runId}-001`)
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

24. Ketik Search `{runId}-001`, tekan Enter
25. Verifikasi baris halaman 1 terurut Name A-Z case-insensitive: `andi kecil {runId}-001` sebelum `Dewi Anggraini {runId}-001`
26. Verifikasi tidak ada indikator sort aktif di header kolom selain default Name
27. Klik `(←)` pada kotak Search

### TC-GS-USER-3: Breadcrumb berubah ke `User > Position` saat pindah ke tab Position

28. Klik Tab `Position`
29. Verifikasi Breadcrumb `User > Position`
30. Verifikasi Tab `Position` aktif
31. Klik Tab `User List`

### TC-GS-USER-4: Breadcrumb berubah ke `User > Division` saat pindah ke tab Division

32. Klik Tab `Division`
33. Verifikasi Breadcrumb `User > Division`
34. Verifikasi Tab `Division` aktif
35. Klik Tab `User List`

### TC-GS-USER-5: Breadcrumb berubah ke `User > Custom Field` saat pindah ke tab Custom Field

36. Klik Tab `Custom Field`
37. Verifikasi Breadcrumb `User > Custom Field`
38. Verifikasi Tab `Custom Field` aktif
39. Klik Tab `User List`

### TC-GS-USER-8: Loading state User List menampilkan skeleton

40. Pasang intercept pada respons daftar User: tahan respons sampai dilepas
41. Klik menu User di sidebar Global Settings
42. Verifikasi tabel menampilkan skeleton loading selama respons belum diterima
43. Lepas intercept respons daftar User sehingga respons diterima
44. Verifikasi skeleton diganti baris data

### TC-GS-USER-25: Hover icon toolbar menampilkan tooltip nama fungsi

45. Hover icon Search
46. Verifikasi tooltip `Search`
47. Hover icon Filter
48. Verifikasi tooltip `Filter`
49. Hover icon Download
50. Verifikasi tooltip `Download`
51. Hover icon Changelog
52. Verifikasi tooltip `Changelog`
53. Hover header kolom Column Visibility (⋯)
54. Verifikasi tooltip `Column Visibility`

### TC-GS-USER-1043: User List, Modified By Default User seed menampilkan System

55. Ketik Search `Hendra Gunawan`, tekan Enter
56. Verifikasi sel Modified By baris Hendra Gunawan menampilkan `System`

### TC-GS-USER-1044: Tab Changelog Default User seed, baris paling awal Create oleh System

57. Klik Name `Hendra Gunawan` di User List
58. Klik Tab `Changelog`
59. Urutkan Oldest First
60. Verifikasi baris paling awal (Oldest First): Action `Create`, Name `Hendra Gunawan`, Field `Name`, Old Value `—`, New Value `Hendra Gunawan`, Modified By `System`

### TC-GS-USER-6: Pindah tab lalu kembali tidak mereset state Search dan Sort di tab User List

61. Kembali ke User List dengan klik Back
62. Ganti isi kotak search dengan `Dewi`, tekan Enter
63. Klik header kolom Email (sort ascending)
64. Klik Tab `Position`
65. Klik Tab `User List`
66. Verifikasi kotak Search tetap terisi `Dewi`
67. Verifikasi tabel tetap tersaring hanya ke baris `Dewi Lestari` dan `Dewi Anggraini {runId}-001`
68. Verifikasi indikator sort Email ascending tetap aktif
69. Ganti isi kotak search dengan `{runId}-001`, tekan Enter
70. Verifikasi baris `andi kecil {runId}-001` dan `Dewi Anggraini {runId}-001` terurut ascending menurut Email: `andikecil+{runId}-001@qwertysystem.net` sebelum `dewianggraini+{runId}-001@qwertysystem.net`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (70 langkah) karena sebelas TC screening User List berada di satu kelas harness (fungsional, baca saja; intercept hanya menahan respons untuk mengamati skeleton sehingga bukan kelas b) dan satu layar. Tiap blok TC berdiri sendiri dan hanya membaca data, jadi kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan layar dipakai bersama (langkah 1) dan dibuka ulang hanya untuk TC-GS-USER-8.
- Urutan TC sumber diubah: TC-GS-USER-7 dan TC-GS-USER-2 diasersi tepat sesudah TC-GS-USER-1 karena mengamati pembukaan menu User yang sama (langkah 1) dan keadaan default (sort, tab aktif) harus diasersi sebelum state diubah (8b butir 5). TC-GS-USER-6 ditaruh terakhir karena mengubah Search dan Sort; urutan itu menghindari langkah pembersihan state untuk TC lain. TC-GS-USER-1043 dan TC-GS-USER-1044 (berada di spec ini supaya berjalan sebelum spec yang mengedit Default User, suite serial) mendahului TC-GS-USER-6 supaya kotak Search masih kosong saat dipakai; TC-GS-USER-1044 melanjutkan Detail Default User dari Search TC-GS-USER-1043.
- TC-GS-USER-1043 mensyaratkan Default User yang belum pernah diedit. Suite berjalan serial dan spec ini harus berjalan sebelum spec yang mengedit Default User (TC-GS-USER-82 dan TC lain yang mengedit Default User); spec ini sendiri tidak mengedit Default User. Asersi Default User seed di Tab Changelog (TC-GS-USER-1044) ada di spec ini (langkah 57 sampai 60).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 dan 12 (membuka dan menutup Overlay Column Visibility untuk mengamati CTA `[Setup Column]` dan row action menu, Expected TC-GS-USER-1 b.i), 17 dan 19 (membuka dan menutup pilihan jumlah baris per halaman, Expected TC-GS-USER-1 c), 31, 35, dan 39 (kembali ke Tab `User List` agar precondition TC berikutnya terpenuhi), 40 dan 43 (pasang dan lepas intercept), 41 (membuka layar ulang untuk TC-GS-USER-8), 57 sampai 59 (membuka Tab Changelog Default User dan mengurutkan Oldest First), 61 (kembali ke User List dari Detail Default User), 24 dan 27 (Search `{runId}-001` agar asersi urutan Name hanya memuat baris seed, lalu mengosongkan Search lewat `(←)` supaya langkah berikutnya mulai dari kotak kosong), 69 (mengganti Search ke `{runId}-001` agar asersi sort Email hanya memuat baris seed).
- Langkah 21 sampai 23 tidak punya aksi sendiri: mengamati keadaan hasil pembukaan menu User (langkah 1); langkah 25 dan 26 mengamati hasil Search langkah 24; langkah 42 mengamati hasil langkah 41. Asersi urutan baris halaman 1 TC-GS-USER-1 (Expected b.iii) dan TC-GS-USER-7 dijadikan satu pada langkah 25 (observasi yang sama, hanya pada baris seed); langkah 15 hanya memeriksa indikator sort default Name.
- Pembagian TC: halaman Tab Position, Division, dan Custom Field hanya diasersi breadcrumb dan status aktif tab; isi tab diuji di file TC modul masing-masing. Guided Tooltip diuji di spec TC-GS-USER-E2E-005 dan TC-GS-USER-E2E-006 (flag `gs-user` sudah `seen` oleh hook suite di spec ini).
- Data U-1 dan U-2 ditambahkan oleh spec karena asersi urutan case-insensitive (TC-GS-USER-7) dan sort Email (TC-GS-USER-6) butuh sedikitnya dua nilai berbeda pada kolom itu; nilai Pre-setup tidak memuat Name berawalan huruf kecil.
- Temuan untuk QA:
  - TC-GS-USER-7 Expected a memberi contoh `Agus`, `andi`, `Budi`; Tabel Pre-setup tidak memuat user Login berawalan huruf kecil dan `Agus Prasetyo` adalah Non-Login User. Spec memakai user seed U-1 (`andi kecil {runId}-001`).
  - TC-GS-USER-6 Expected a berbunyi tabel tersaring ke baris Dewi Lestari (satu baris), sehingga urutan sort Email tidak dapat diamati. Spec menambah user seed U-2 dan mengasersi dua baris; TC perlu menyebut data pembanding.
  - TC-GS-USER-25 menyebut header kolom `Actions (⋯)`, sedangkan TC-GS-USER-1 menyebutnya `Column Visibility (⋯)` dan tooltip-nya `Column Visibility`. Spec memakai `Column Visibility (⋯)`.
  - TC-GS-USER-1044: Expected menyebut kolom Name pada Tab Changelog Detail, sedangkan Expected TC-GS-USER-873 butir b tidak menyebut kolom Name pada Tab Changelog Detail; spec mengikuti Expected tiap TC. Precondition "Entitas baru diregistrasi" tidak bisa dibuktikan oleh spec; spec mengandalkan urutan eksekusi dan keadaan seed, dan Dependensi TC menyebut `TC-GS-USER-82`.
  - TC-GS-USER-1043 mensyaratkan entitas yang baru diregistrasi dengan Default User belum pernah diedit; TC tidak menyebut cara menjamin kondisi itu pada entitas Pre-setup bersama. Disediakan tim FE.
  - TC-GS-USER-8 menyebut "network throttle" tanpa durasi atau endpoint; spec menahan respons sampai dilepas lewat langkah 43.
  - TC-GS-USER-1 Expected b.i menyebut Overlay Column Visibility dengan CTA `[Setup Column]`; label item di Division adalah `Setup Column...`. Spec mengikuti TC-GS-USER-1 (`[Setup Column]`).
