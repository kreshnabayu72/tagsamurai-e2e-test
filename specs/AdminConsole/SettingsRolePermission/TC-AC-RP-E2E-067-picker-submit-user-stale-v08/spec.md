---
id: TC-AC-RP-E2E-067-picker-submit-user-stale-v08
title: "Picker Submit: User Dihapus Admin Lain (V-08), Alert Jamak, dan Campuran Tidak Eligible"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-223
  - TC-AC-RP-224
  - TC-AC-RP-227
coverage:
  web: automated
---

# Picker Submit: User Dihapus Admin Lain (V-08), Alert Jamak, dan Campuran Tidak Eligible

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Admin B: sesi API sesuai Hook suite "Sesi API aktor" untuk menghapus user dan menetapkan Total Control; akun Admin B disediakan tim FE. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Pelaku kedua lewat sesi API tidak membuka konteks UI kedua.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`Alex Tan`, `Sarah Kimura`, `Dewi Anggreni`, `John Dohan`), #13 (pemegang Read Only `Dewi Anggraini`, `Lisa Wong`), #24 (Admin B).
- Data Dinamis: spec ini tidak membuat Data Dinamis; user yang dihapus atau ditetapkan Admin B adalah user Pre-setup #12 (nama tampil dipakai asersi alert TC). Nilai bersuffix `+{runId}-067` tidak dipakai karena tidak ada data yang dibuat spec.
- Perubahan Pre-setup: user Pre-setup `Alex Tan`, `Sarah Kimura`, `Dewi Anggreni` dihapus dan `Sarah Kimura` ditetapkan Total Control oleh Admin B. Pemulihan (user kembali Standard dan ada) memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC dan langkah akhir (langkah 37). Efek: Changelog Settings > User dan Tab Total Control menerima entri; Last Updated berubah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-223: Submit picker dengan user yang dihapus admin lain

1. Klik "+ Assign"
2. Centang `Alex Tan` dan `Sarah Kimura`
3. Sesi B (sesi API Admin B): hapus user `Alex Tan` (Settings > User) hingga user terhapus
4. Sesi A: klik `[Assign]`
5. Verifikasi inline alert "Alex Tan no longer exists. Please select another."
6. Verifikasi centangan `Alex Tan` auto-clear
7. Verifikasi `Sarah Kimura` tetap tercentang
8. Telusuri seluruh halaman Pagination popup dan amati seluruh baris kandidat
9. Verifikasi daftar di-refetch (`Alex Tan` tidak lagi ada di daftar kandidat)
10. Klik `✕` pada popup
11. Verifikasi tabel Tab Total Control memuat baris `Siti Nurhaliza`
12. Verifikasi seluruh submit ditolak: tabel Tab Total Control tidak memuat `Sarah Kimura` (tidak ada assignment)

### TC-AC-RP-224: Alert V-08 menyebut dua dan tiga user

13. Pulihkan baseline automation: `Alex Tan` dan `Sarah Kimura` kembali ada, lalu muat ulang halaman
14. Klik "+ Assign"
15. Centang `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni`
16. Sesi B (sesi API Admin B): hapus `Alex Tan` dan `Sarah Kimura` hingga terhapus
17. Sesi A: klik `[Assign]`
18. Verifikasi alert "Alex Tan and Sarah Kimura no longer exist. Please select another."
19. Pulihkan baseline automation: `Alex Tan` dan `Sarah Kimura` kembali ada, lalu muat ulang halaman
20. Klik "+ Assign"
21. Centang `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni`
22. Sesi B (sesi API Admin B): hapus `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni` hingga terhapus
23. Sesi A: klik `[Assign]`
24. Verifikasi alert "Alex Tan, Sarah Kimura, and Dewi Anggreni no longer exist. Please select another."

### TC-AC-RP-227: Campuran user stale dan tidak eligible menampilkan V-08 lebih dulu

25. Pulihkan baseline automation: `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni` kembali ada, lalu muat ulang halaman
26. Klik tab `Read Only`
27. Klik "+ Assign"
28. Centang `Alex Tan`, `Sarah Kimura`, dan `John Dohan`
29. Sesi B (sesi API Admin B): hapus `Alex Tan` dan tetapkan `Sarah Kimura` sebagai Total Control hingga tersimpan
30. Sesi A: klik `[Assign]`
31. Verifikasi alert "Alex Tan no longer exists. Please select another." tampil lebih dulu
32. Verifikasi centangan `Alex Tan` dan `Sarah Kimura` auto-clear
33. Verifikasi `John Dohan` tetap tercentang
34. Klik `✕` pada popup
35. Verifikasi tabel Tab Read Only memuat baris `Dewi Anggraini`
36. Verifikasi tidak ada assignment dibuat: tabel Tab Read Only tidak memuat `John Dohan`
37. Pulihkan baseline: `Alex Tan` kembali ada dan `Sarah Kimura` kembali Standard lewat kemampuan reset FE/BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Pembagian TC lintas spec: TC-AC-RP-225, TC-AC-RP-226, dan TC-AC-RP-229 ada di spec 068; TC-AC-RP-228 ada di spec 129.
- Langkah penghubung (S-03, S-09): langkah 8 (telusuri seluruh halaman Pagination popup agar asersi `Alex Tan` tidak ada di daftar kandidat pada langkah 9 menjangkau seluruh halaman, R-22 dan S-14; langkah 7 mengasersi `Sarah Kimura` tetap tercentang sebelum penelusuran, selagi popup belum berpindah halaman; penelusuran tanpa Search karena yang diamati seluruh baris kandidat), 10, 34 (tutup popup tanpa dialog Unsaved Changes karena popup picker bukan form), 11 dan 35 (anchor positif untuk asersi absence, bagian 8b butir 2), 13, 19, 25 (pemulihan baseline dan muat ulang), 26 (pilih tab), 37 (pemulihan baseline akhir). Langkah 19 hingga 24 mengulang langkah 14 hingga 18 dengan tiga user dihapus sesuai Langkah Uji TC-AC-RP-224.
- Langkah 3, 16, 22, dan 29 memakai sesi API Admin B hanya sebagai pemicu perubahan state; tidak memakai `P-2`.
- Alasan sekitar 35 langkah (37 langkah): seluruh blok berkelas sama (V-08 pada submit picker) dan berdiri sendiri; tiap blok memuat seeding state, pemicu, dan asersi V-08 sendiri, dan satu langkah penelusuran halaman picker (langkah 8) dan satu langkah pemulihan akhir (langkah 37) menambah dua langkah di atas batas.
- Temuan untuk QA:
  - TC-AC-RP-223, 224, dan 227 menghapus user Pre-setup (`Alex Tan`, `Sarah Kimura`, `Dewi Anggreni`) lewat Admin B; mekanisme penghapusan lewat API dan pemulihan user (identitas, role, data) tidak didefinisikan di TC, PRD, atau LLD (S-13) dan ditulis sebagai kemampuan yang disediakan tim FE/BE.
  - TC-AC-RP-223 Expected "daftar di-refetch" tidak menyebut cara teramati; spec mengasersi `Alex Tan` tidak lagi ada di daftar kandidat (langkah 9) setelah menelusuri seluruh halaman (langkah 8).
  - TC-AC-RP-223 dan TC-AC-RP-227 Expected "tidak ada assignment" tidak punya langkah observasi di TC; spec mengamatinya dengan menutup popup dan membaca tabel tab (langkah 11 dan 12, 35 dan 36).
  - TC-AC-RP-227 Expected "tidak ada assignment dibuat" tidak menyebut `Sarah Kimura` yang sudah ditetapkan Total Control oleh Admin B; spec hanya mengasersi `John Dohan` tidak masuk Tab Read Only.
  - TC-AC-RP-223, 224, dan 227 menyebut "dua sesi paralel" (Manual Only kriteria d) dengan Sesi B hanya memicu perubahan state; spec memakai sesi API. Bila QA menghendaki sesi UI kedua, spec dipindah ke kelas c.
  - Email Admin B (Pre-setup #24) tidak tertulis; ditulis "disediakan tim FE".
