---
id: TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired
title: "Edit User: Temporary User (Set, Uncheck, Batas Tanggal Hari Ini dan Kemarin, Tanggal Kosong, dan Temporary-Expired)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-198
  - TC-GS-USER-199
  - TC-GS-USER-200
  - TC-GS-USER-201
  - TC-GS-USER-202
  - TC-GS-USER-203
  - TC-GS-USER-204
coverage:
  web: automated
---

# Edit User: Temporary User (Set, Uncheck, Batas Tanggal Hari Ini dan Kemarin, Tanggal Kosong, dan Temporary-Expired)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup yang dipakai: Position `Staff` (No. 22), Division `Finance` (No. 23), dan produk `Fixed Asset` (No. 26); hanya dibaca. Spec tidak mengubah atau menghapus data Pre-setup (Ahmad Fauzi No. 13, Dewi Lestari No. 12, dan Budi Hartono No. 16 diganti user seed milik spec, S-06).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user: Position `Staff`, Division `Finance`, Access `Fixed Asset` dan `Global Settings`:
  - U-P (permanen, TC-GS-USER-202 dan 198): Name `Ahmad Fauzi {runId}-037`, Email `ahmadfauzi+{runId}-037@qwertysystem.net`, Temporary User tidak dicentang, Active ON.
  - U-T (Temporary aktif, TC-GS-USER-201, 200, dan 199): Name `Dewi Lestari {runId}-037`, Email `dewilestari+{runId}-037@qwertysystem.net`, Temporary User aktif dengan Temporary Until +30 hari, Active ON.
  - U-E1 (Temporary-expired, TC-GS-USER-203): Name `Budi Hartono {runId}-037`, Email `budihartono+{runId}-037@qwertysystem.net`, Temporary Until sudah lewat, Inactive.
  - U-E2 (Temporary-expired, TC-GS-USER-204): Name `Bambang Hartono {runId}-037`, Email `bambanghartono+{runId}-037@qwertysystem.net`, Temporary Until sudah lewat, Inactive.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-P, U-T, U-E1, dan U-E2 lewat API.
- Kemampuan teknis, disediakan tim FE/BE (TC tidak memberi cara): membuat user Temporary-expired yang Inactive (U-E1 dan U-E2). Bila hanya bisa dicapai lewat jam, jam server dan jam browser dimajukan melewati Temporary Until di hook `before`, job auto-deactivate dipicu, lalu kedua jam dipulihkan sebelum langkah 1 (tanggal "hari ini", "kemarin", "+14 hari", dan "+10 hari" di langkah dihitung dari tanggal nyata menurut zona waktu client General Settings, NC-06; jam harus sudah pulih sebelum langkah pertama).
- Kemampuan teknis lain: memilih dan mengetik tanggal pada field Temporary Until, termasuk tanggal hari ini dan kemarin; membaca teks `Temporary until [tanggal]` di Detail; mengatur kolom lewat Setup Column.
- State global yang diubah: konfigurasi kolom tabel User List akun Total Control (kolom `Temporary User` dan `Temporary Until` ditampilkan di langkah 1 sampai 4) dan dipulihkan lewat `[Reset to Default]` di langkah 46 sampai 49; hook `after` memulihkan konfigurasi kolom tabel User List ke default sebagai cadangan.

## Test Steps

### Persiapan kolom tabel

1. Klik header kolom Column Visibility (⋯)
2. Klik `[Setup Column]`
3. Centang kolom `Temporary User` dan `Temporary Until`
4. Klik `[Save]`

### TC-GS-USER-202 lalu TC-GS-USER-198: Set Temporary User pada user permanen

5. Klik icon Search, ketik `Ahmad Fauzi {runId}-037`, tekan Enter
6. Buka row action baris `Ahmad Fauzi {runId}-037` lalu klik `Edit`
7. Centang `Set as Temporary User`
8. Klik `[Save]`
9. Verifikasi inline error `Temporary until must not be empty`
10. Pilih tanggal Temporary Until +14 hari
11. Klik `[Save]`
12. Verifikasi toast sukses: `Success, user has been updated.`
13. Klik Name `Ahmad Fauzi {runId}-037` untuk membuka Detail
14. Verifikasi Detail menampilkan `Temporary until` dengan tanggal +14 hari yang dipilih
15. Verifikasi switch Active tetap ON
16. Kembali ke User List

### TC-GS-USER-201, TC-GS-USER-200, lalu TC-GS-USER-199: Batas tanggal dan uncheck Temporary pada user Temporary aktif

17. Klik icon Search, ketik `Dewi Lestari {runId}-037`, tekan Enter
18. Buka row action baris `Dewi Lestari {runId}-037` lalu klik `Edit`
19. Ubah Temporary Until ke kemarin
20. Klik `[Save]`
21. Verifikasi inline error `Please select a future date.`
22. Ubah Temporary Until ke hari ini
23. Klik `[Save]`
24. Verifikasi inline error `Please select a future date.`
25. Uncheck `Set as Temporary User`
26. Klik `[Save]`
27. Verifikasi toast sukses: `Success, user has been updated.`
28. Verifikasi kolom Temporary User baris `Dewi Lestari {runId}-037` `No`
29. Klik Name `Dewi Lestari {runId}-037` untuk membuka Detail
30. Verifikasi info Temporary hilang di Detail
31. Kembali ke User List

### TC-GS-USER-203: Uncheck Temporary pada user Temporary-expired

32. Klik icon Search, ketik `Budi Hartono {runId}-037`, tekan Enter
33. Buka row action baris `Budi Hartono {runId}-037` lalu klik `Edit`
34. Uncheck `Set as Temporary User`
35. Klik `[Save]`
36. Verifikasi toast sukses: `Success, user has been updated.`
37. Verifikasi switch Active baris `Budi Hartono {runId}-037` tetap OFF
38. Verifikasi kolom Temporary User baris `Budi Hartono {runId}-037` `No`
39. Verifikasi kolom Temporary Until baris `Budi Hartono {runId}-037` `—`

### TC-GS-USER-204: Ubah Temporary Until user Temporary-expired ke tanggal depan

40. Ganti isi kotak search dengan `Bambang Hartono {runId}-037`, tekan Enter
41. Buka row action baris `Bambang Hartono {runId}-037` lalu klik `Edit`
42. Ubah Temporary Until ke +10 hari
43. Klik `[Save]`
44. Verifikasi toast sukses: `Success, user has been updated.`
45. Verifikasi switch Active baris `Bambang Hartono {runId}-037` tetap OFF

### Pemulihan kolom tabel

46. Klik header kolom Column Visibility (⋯)
47. Klik `[Setup Column]`
48. Klik `[Reset to Default]`
49. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-198 sampai 204). Mode FE+BE; kelas harness: Edit Temporary User pada layar yang sama (satu kelas). Pengaturan jam (HK5) hanya dipakai bila perlu menyiapkan user Temporary-expired di hook `before`, tidak di Test Steps.
- Urutan TC di spec: 202, 198, 201, 200, 199, 203, 204. Urutan sumber (198, 199, 200, 201, 202, 203, 204) diubah karena validasi yang diblokir dijalankan sebelum aksi sukses pada user yang sama (bagian 3 butir 3 dan 7): TC-GS-USER-202 sebelum 198 pada U-P, dan TC-GS-USER-201 dan 200 sebelum 199 pada U-T; setiap pasangan memakai satu pembukaan Edit sampai `[Save]` sukses menutup form, sehingga tidak ada penutupan form dirty.
- Empat user seed (U-P, U-T, U-E1, U-E2) dipakai karena TC-GS-USER-203 dan 204 sama-sama menuntut user Temporary-expired yang belum diubah (203 menjadikannya permanen), dan TC-GS-USER-198 dan 199 membutuhkan status Temporary yang berlawanan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 dan 46 sampai 49 (menampilkan dan memulihkan kolom `Temporary User` dan `Temporary Until` agar Expected kolom TC-GS-USER-199 dan 203 bisa diamati), 5 sampai 7, 16 sampai 18, 31 sampai 33, 40 sampai 41 (membuka form dan kembali ke daftar).
- Pembagian TC lintas spec: TC-GS-USER-198 sampai 204 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-203 dan 204 menyebut "Temporary-expired" dan Inactive tanpa cara menyiapkannya; kemampuan disediakan tim FE/BE.
  - TC-GS-USER-204 butir b ("tetap OFF sampai di-toggle ON manual") memuat klausa toggle manual yang tidak punya langkah di TC; spec hanya mengasersi switch Active tetap OFF.
  - TC-GS-USER-200 dan 201 tidak menyebut cara memasukkan tanggal hari ini atau kemarin (date picker bisa menolak tanggal lampau); spec menulis "Ubah Temporary Until ke hari ini/kemarin".
  - TC-GS-USER-198 butir b (`Temporary until [tanggal]`) tidak menyebut format tanggal; spec mengasersi tanggal yang dipilih dalam format yang tampil menurut General Settings.
- Spec melewati sekitar 35 langkah (49 langkah) karena memuat satu kelas (Edit Temporary User) pada satu layar Edit, tiap user seed berdiri sendiri, dan tiap blok TC tidak membuat blok lain kehilangan makna bila gagal; sebagian langkah adalah persiapan dan pemulihan kolom tabel.
