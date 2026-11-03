---
id: TC-GS-USER-E2E-175-multi-konteks-resend-ditolak-server-dan-record-berubah-atau-dihapus-sesi-lain
title: "Multi-Konteks: Resend Ditolak Server saat Cooldown atau Status Berubah, Switch Tab Role dan Auto-Revert saat Record Berubah, serta Deactivate saat User Dihapus Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-1115
  - TC-GS-USER-1116
  - TC-GS-USER-1103
  - TC-GS-USER-1133
  - TC-GS-USER-1119
coverage:
  web: automated
---

# Multi-Konteks: Resend Ditolak Server saat Cooldown atau Status Berubah, Switch Tab Role dan Auto-Revert saat Record Berubah, serta Deactivate saat User Dihapus Admin Lain

## Prerequisites

- Mode: FE+BE (backend nyata; kelas harness c: multi-konteks dua admin, bagian 3 prinsip 13). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun Sesi A (Admin A, sesi UI utama): Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun Admin B (Total Control kedua, sesi API `[API Admin B]`): disediakan tim FE (tidak ada di Tabel Pre-setup TC), kredensial `Spectra.env.GS_TC2_PASSWORD`. Admin B hanya memicu perubahan state lewat sesi API (bukan sesi UI kedua); hasilnya diasersi di Sesi A yang tidak memuat ulang halaman. Klien HTTP untuk sesi API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD.
- Env var: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tidak dipakai sebagai target aksi dan tidak diubah; nama di TC diganti user seed milik spec (S-06).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after`; semua Activated kecuali `Mike Tan`, Division `Finance`, Access `Fixed Asset`, nilai field wajib lain seragam (kemampuan seeding user, Pending Activation, email pending, penetapan Holder `Manage TAG`, dan tier Total Control disediakan tim FE/BE):
  - `Mike Tan {runId}-175`, email `miketan+{runId}-175@qwertysystem.net`, Pending Activation, Resend belum dalam cooldown (TC-GS-USER-1115).
  - `Rina Putri {runId}-175`, email `rinaputri+{runId}-175@qwertysystem.net`, email pending `rinaputri.new+{runId}-175@qwertysystem.net`, Pending Email Confirmation (TC-GS-USER-1116).
  - `Ahmad Fauzi {runId}-175`, email `ahmadfauzi+{runId}-175@qwertysystem.net`, Active, Holder `Manage TAG` dengan baris `Manage TAG` Active di Tab Role (TC-GS-USER-1103).
  - `Andi Wijaya {runId}-175`, email `andiwijaya+{runId}-175@qwertysystem.net`, Active, tier Total Control (TC-GS-USER-1133).
  - `Lilis Handayani {runId}-175`, email `lilishandayani+{runId}-175@qwertysystem.net`, Active (TC-GS-USER-1119).
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Sesi API Admin B yang melakukan: Resend Activation Email, Edit user dengan Cancel pending email change, Remove baris user dari Role & Permission > Detail `Manage TAG`, Remove tier Total Control dari user, dan Delete user.
  - Sesi A tidak menerima pembaruan otomatis User List dan Detail dari perubahan sesi lain selama langkah "tanpa memuat ulang halaman".
  - Mail-catcher: membaca jumlah email per alamat (R-11) untuk `miketan+{runId}-175@qwertysystem.net` dan `rinaputri.new+{runId}-175@qwertysystem.net`.
  - Membaca lewat BE jumlah entri log Resend untuk user target, jumlah entri log milik user target (Changelog User dan System Log aktor), dan jumlah entri `Auto-Revert` di Changelog user target, tepat sebelum aksi Sesi A (8b butir 10).
- State global yang diubah: tidak ada selain data user milik spec. Spec tidak mengubah jam, plan, atau konfigurasi.
- Cleanup di hook `after` (tidak mengandalkan seeding berhasil penuh): hapus lewat API semua user seed yang masih ada, lepas sesi API Admin B, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-USER-1115: Resend single ditolak server karena cooldown, tanpa toast error dan tombol di-refresh ke countdown

1. Klik icon Search, ketik `Mike Tan {runId}-175`, tekan Enter
2. Klik Name `Mike Tan {runId}-175`
3. Verifikasi tombol `Resend Activation Email` di header Detail Enabled
4. Catat jumlah email ke `miketan+{runId}-175@qwertysystem.net` di mail-catcher sebagai `{e1}`
5. Catat jumlah entri log Resend untuk `Mike Tan {runId}-175` (dibaca lewat BE) sebagai `{l1}`
6. [API Admin B] Kirim `Resend Activation Email` untuk `Mike Tan {runId}-175` hingga email terkirim dan entri log Resend tersimpan
7. Klik `Resend Activation Email` tanpa memuat ulang halaman
8. Verifikasi tidak ada toast error
9. Verifikasi tombol `Resend Activation Email` Disabled
10. Hover tombol `Resend Activation Email`
11. Verifikasi tooltip countdown `"Please wait {X} seconds before resending."` tampil dengan `{X}` bilangan bulat kurang dari 60
12. Verifikasi jumlah email ke `miketan+{runId}-175@qwertysystem.net` sama dengan `{e1}` + 1 (hanya satu email terkirim)
13. Verifikasi jumlah entri log Resend untuk `Mike Tan {runId}-175` sama dengan `{l1}` + 1 (hanya satu entri log Resend)
14. Klik menu User di sidebar Global Settings

### TC-GS-USER-1116: Resend pada status yang sudah bukan Pending ditolak server dan UI me-refresh status

15. Klik icon Search, ketik `Rina Putri {runId}-175`, tekan Enter
16. Klik Name `Rina Putri {runId}-175`
17. Verifikasi tombol `Resend Confirmation Email` tampil di header Detail
18. Catat jumlah email ke `rinaputri.new+{runId}-175@qwertysystem.net` di mail-catcher sebagai `{e2}`
19. [API Admin B] Edit `Rina Putri {runId}-175`, Cancel pending email change hingga perubahan tersimpan
20. Klik `Resend Confirmation Email` tanpa memuat ulang halaman
21. Verifikasi tidak ada toast error
22. Verifikasi nama `Rina Putri {runId}-175` tampil di header Detail
23. Verifikasi badge `Pending Email Confirmation` dan tombol `Resend Confirmation Email` tidak tampil di Detail
24. Verifikasi jumlah email ke `rinaputri.new+{runId}-175@qwertysystem.net` sama dengan `{e2}` (tidak ada email dikirim)
25. Klik menu User di sidebar Global Settings

### TC-GS-USER-1103: Switch Active OFF atas baris yang sudah dihapus admin lain, toast netral dan data di-refresh

26. Klik icon Search, ketik `Ahmad Fauzi {runId}-175`, tekan Enter
27. Klik Name `Ahmad Fauzi {runId}-175`
28. Klik Tab `Role`
29. Verifikasi switch Active baris `Manage TAG` ON
30. [API Admin B] Buka Role & Permission > Detail `Manage TAG`, Remove baris `Ahmad Fauzi {runId}-175` hingga penghapusan tersimpan
31. Catat jumlah entri log milik `Ahmad Fauzi {runId}-175` (Changelog User dan System Log aktor, dibaca lewat BE) sebagai `{l2}`
32. Matikan switch Active baris `Manage TAG` tanpa memuat ulang halaman
33. Verifikasi toast netral "This role is no longer available."
34. Verifikasi baris `Manage TAG` tampil switch OFF
35. Verifikasi seluruh checkbox baris `Manage TAG` Disabled
36. Verifikasi jumlah entri log milik `Ahmad Fauzi {runId}-175` sama dengan `{l2}` (tidak ada entri dari aksi Sesi A)
37. Klik menu User di sidebar Global Settings

### TC-GS-USER-1133: Edit Tab Role yang memicu Auto-Revert saat tier target sudah dilepas aktor lain

38. Klik icon Search, ketik `Andi Wijaya {runId}-175`, tekan Enter
39. Klik Name `Andi Wijaya {runId}-175`
40. Klik Tab `Role`
41. Uncheck Delete baris `Manage files`
42. Verifikasi dialog auto-revert tampil
43. [API Admin B] Remove tier Total Control `Andi Wijaya {runId}-175` di Role & Permission hingga perubahan tersimpan
44. Catat jumlah entri `Auto-Revert` di Changelog `Andi Wijaya {runId}-175` (dibaca lewat BE) sebagai `{a1}`
45. Klik `[Remove]` pada dialog auto-revert
46. Verifikasi Delete baris `Manage files` tidak tercentang
47. Verifikasi jumlah entri `Auto-Revert` di Changelog `Andi Wijaya {runId}-175` sama dengan `{a1}` (tidak ada entri `Auto-Revert` kedua)
48. Verifikasi banner tidak tampil di Tab Role
49. Klik menu User di sidebar Global Settings

### TC-GS-USER-1119: Aksi tulis dari Detail pada user yang sudah dihapus sesi lain, toast netral, dialog ditutup, kembali ke List

50. Klik icon Search, ketik `Lilis Handayani {runId}-175`, tekan Enter
51. Klik Name `Lilis Handayani {runId}-175`
52. Klik switch Active di header Detail
53. Verifikasi dialog Deactivate tampil
54. [API Admin B] Delete `Lilis Handayani {runId}-175` hingga penghapusan tersimpan
55. Klik `[Deactivate]`
56. Verifikasi toast netral "This user is no longer available."
57. Verifikasi dialog Deactivate tertutup
58. Verifikasi Detail `Lilis Handayani {runId}-175` tidak lagi dirender
59. Verifikasi halaman User List tampil dengan Table Tools
60. Klik icon Search, ketik `{runId}-175`, tekan Enter
61. Verifikasi baris `Ahmad Fauzi {runId}-175` tampil di tabel
62. Verifikasi baris `Lilis Handayani {runId}-175` tidak tampil di tabel

## Notes

- Mode: FE+BE (backend nyata, kelas harness c: multi-konteks dua admin). Sumber: `global-settings/user/TestCases/tc-user.md`. Suite serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Penanda `[API Admin B]` menunjuk sesi API Admin B; langkah tanpa penanda dijalankan di Sesi A (sesi UI).
- Kelas c: seluruh TC mengasersi tampilan Sesi A yang basi (stale, tanpa memuat ulang halaman) setelah Admin B bertindak; hasil diasersi di jendela Sesi A, bukan pemicu semata. Admin B memakai sesi API karena hanya memicu perubahan state (pelaku kedua lewat sesi API bukan konteks kedua).
- Spec melewati sekitar 35 langkah (62 langkah). Alasan: kelima TC berada di satu kelas harness (c, dua admin pada entitas yang sama) dan satu aktor UI; tiap blok memakai user seed bersuffix sendiri sehingga blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah banyak karena satu baris per aksi per sesi dan satu `Verifikasi` per klausa Expected (S-01), termasuk baseline dan anchor.
- Urutan TC sumber diubah: TC-GS-USER-1115 dan 1116 (Resend, tanpa data terhapus) lebih dulu, lalu TC-GS-USER-1103 dan 1133 (mengubah Tab Role), dan TC-GS-USER-1119 (menghapus user) paling akhir (bagian 3 prinsip 5; S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 2, 15 sampai 16, 26 sampai 28, 38 sampai 40, dan 50 sampai 51 (Search baris target dibuka lewat Search nama persis, klik Name, dan buka Tab `Role`; 8b butir 12, R-16, R-23), langkah 4, 5, 18, 31, dan 44 (mencatat baseline; S-12, R-11, 8b butir 10), langkah 14, 25, 37, dan 49 (kembali ke User List lewat sidebar sebelum blok berikutnya; S-14), langkah 60 (Search `{runId}-175` agar baris pembanding tampil).
- Pelaku kedua `[API Admin B]` ditulis "... hingga ... tersimpan" (R-20). Langkah 7, 20, 32, dan 55 menekan kontrol di Sesi A tanpa memuat ulang halaman sehingga tampilan Sesi A tetap basi.
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 3 dan 17 (tombol Resend tampil sebelum pemicu, agar "tombol berubah" bermakna); langkah 22 (nama user tampil di header Detail sebagai anchor positif untuk absence badge dan tombol pada langkah 23; 8b butir 2); langkah 29 (switch ON sebelum pemicu); langkah 42 (dialog auto-revert tampil, ditulis sebagai Verifikasi sendiri, bukan keterangan kurung pada langkah; R-02); langkah 53 (dialog Deactivate tampil, idem); langkah 59, 60, dan 61 (halaman List tampil dan baris pembanding tampil sebagai anchor positif untuk absence baris `Lilis Handayani {runId}-175`); langkah 48 (banner) mengasersi klausa c TC-GS-USER-1133.
- Urutan Verifikasi pada TC-GS-USER-1116 diubah dari Expected: `Verifikasi` jumlah email (Expected a) ditulis setelah `Verifikasi` badge dan tombol hilang (Expected b) sebagai anchor positif untuk asersi "tidak ada email dikirim" (8b butir 2, S-12). Pada TC-GS-USER-1115 asersi absence toast error (langkah 8) ditulis segera setelah pemicu (8b butir 11).
- Asersi "hanya satu email", "hanya satu entri log Resend", "tidak ada entri log", dan "tidak ada entri `Auto-Revert` kedua" (TC-GS-USER-1115 Expected c, TC-GS-USER-1103 Expected c, TC-GS-USER-1133 Expected b) ditulis sebagai asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g; spec absence `147` tidak memuat aksi nyata untuk TC ini.
- Pembagian TC lintas spec: Resend sukses dan cooldown Resend oleh satu admin berada di spec lain (mis. spec 070 untuk record dihapus sesi lain pada Edit, Toggle, dan Delete); TC-GS-USER-1115, 1116, 1103, 1133, dan 1119 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-1115, 1116, 1119, dan 1103 menulis aksi "Sesi B" lewat UI dan berstatus Manual Only (1115, 1116, 1119, 1103, 1133); spec memakai Admin B lewat sesi API dan mengasersi hanya hasil di Sesi A. Mail-catcher dan pembacaan BE disediakan tim FE/BE.
  - TC-GS-USER-1115 Expected c ("hanya satu email terkirim dan hanya satu entri log Resend") tidak menyebut surface log; spec membaca jumlah entri log Resend lewat BE untuk user target. TC-GS-USER-1103 Expected c ("tidak ada entri log dari aksi sesi A") tidak menyebut surface; spec memakai Changelog User dan System Log aktor lewat BE.
  - TC-GS-USER-1116 Expected a tidak menyebut alamat penerima email; spec memakai alamat email pending `rinaputri.new+{runId}-175@qwertysystem.net`. Bagaimana "status di-refresh" diamati tidak disebut TC; spec mengasersi badge dan tombol tidak tampil.
  - TC-GS-USER-1103 Expected a ("data di-refresh") dan TC-GS-USER-1133 Expected c ("Tab Role di-refresh ke state server") tidak punya observasi terpisah selain Expected b dan Expected a pada TC yang sama; spec mengasersi keadaan akhir baris (switch OFF, checkbox Disabled; checkbox Delete tidak tercentang). Banner pada TC-GS-USER-1133 Expected c tidak diidentifikasi (teks dan jenis banner tidak disebut); spec mengasersi banner tidak tampil.
  - TC-GS-USER-1133 langkah 1 menyebut "dialog auto-revert terbuka" tanpa teks dialog; spec mengasersi dialog tampil tanpa teks. Baseline entri `Auto-Revert` dicatat setelah Admin B melepas tier karena aksi itu sendiri dapat menambah entri.
  - TC-GS-USER-1119 tidak menyebut keadaan kotak Search setelah kembali ke List; spec mengetik Search `{runId}-175` agar baris pembanding tampil.
  - TC-GS-USER-1115, 1116, 1103, 1133, dan 1119 menyebut Mike Tan, Rina Putri, Ahmad Fauzi, Andi Wijaya, dan Lilis Handayani tanpa suffix; spec memakai user seed milik spec bersuffix `{runId}-175` (S-06). "Resend belum dalam cooldown" (TC-GS-USER-1115) tidak punya mekanisme seeding di TC, PRD, atau LLD dan disediakan tim FE/BE.
