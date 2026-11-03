---
id: TC-AC-ACC-E2E-140-bulk-selection-limit-dan-select-all-lintas-halaman
title: "Bulk Selection: Select All Lintas Halaman Menjadi Unselect All dan Selection Limit 100 (Live-block dan Cap Select All)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-205
  - TC-AC-ACC-206
  - TC-AC-ACC-207
coverage:
  web: automated
---

# Bulk Selection: Select All Lintas Halaman Menjadi Unselect All dan Selection Limit 100 (Live-block dan Cap Select All)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data (kelas e, volume data): Selection Limit awal bernilai default 1000 (System Limits); fixture Tabel A3 C-SEL-1 sampai C-SEL-130 `PT Seleksi Uji 001` sampai `PT Seleksi Uji 130` (Residen) tersedia; node Group `Regional Timur` memuat `PT Uji Halaman 01` sampai `PT Uji Halaman 30` (C-14), `PT Seleksi Uji 001` sampai `130`, dan Client Regional Timur lain (lebih dari 100 baris); sub-tab Active memuat minimal 101 Client (fixture seed massal di luar C-01 sampai C-14). Spec ini tidak mengonfirmasi aksi Bulk (tidak ada [Suspend] yang diklik), sehingga tidak ada perubahan status Client.
- State global yang diubah: Selection Limit diubah ke 100 di Admin Console > Plans & Licensing > Lifecycle Settings > tab System Limits lalu dipulihkan ke default 1000 oleh langkah penghubung dan hook `after`.
- Suite berjalan serial (`parallel: false`) karena Selection Limit adalah state global; flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-205: Select All ({N} records) lintas halaman lalu berubah menjadi Unselect All

1. Klik node "Regional Timur" pada Sidebar Group Tree, lalu buka sub-tab Active
2. Centang satu baris
3. Catat angka {N} pada tombol "Select All ({N} records)"
4. Klik tombol "Select All ({N} records)"
5. Verifikasi tombol berubah menjadi "Unselect All"
6. Verifikasi Bulk Action Bar menampilkan counter "{N} clients selected"
7. Pindah ke halaman 2
8. Verifikasi seluruh baris halaman 2 tercentang
9. Verifikasi counter tetap "{N} clients selected"
10. Klik "Unselect All"
11. Verifikasi seluruh seleksi lintas halaman dibatalkan
12. Verifikasi Bulk Action Bar tertutup
13. Ubah jumlah baris per halaman menjadi 100
14. Centang checkbox header di halaman pertama, lalu halaman berikutnya, dan seterusnya sampai tombol berubah menjadi "Unselect All"
15. Uncheck satu baris
16. Verifikasi tombol kembali "Select All ({N} records)" dengan {N} sama dengan angka yang dicatat pada langkah 3 (tidak berkurang)
17. Verifikasi counter menjadi satu kurang dari {N}
18. Klik ikon (X) pada Bulk Action Bar

### TC-AC-ACC-206: Selection Limit live-block pada checkbox ke-(limit+1) dengan limit minimum 100

19. Buka Admin Console > Plans & Licensing > Lifecycle Settings > tab System Limits
20. Ubah Selection Limit menjadi 100 lalu simpan
21. Buka Admin Console > Client, klik sub-tab Active
22. Ubah jumlah baris per halaman menjadi 100
23. Centang 100 baris pertama satu per satu
24. Verifikasi baris 1 sampai 100 tercentang
25. Verifikasi counter "100 clients selected"
26. Verifikasi Bulk Action Bar aktif
27. Pindah ke halaman 2
28. Arahkan kursor ke checkbox baris pertama halaman 2 (baris ke-101) dan coba centang
29. Verifikasi checkbox baris ke-101 disabled dengan tooltip "You've reached the maximum selection of 100 rows."
30. Verifikasi seratus baris yang sudah dicentang tetap tercentang
31. Verifikasi counter tetap "100 clients selected"

### TC-AC-ACC-207: Select All melebihi Selection Limit: seleksi di-cap ke limit dengan toast error

32. Klik ikon (X) pada Bulk Action Bar
33. Pindah ke halaman 1
34. Centang satu baris dan catat angka {N} pada tombol "Select All ({N} records)"
35. Klik tombol "Select All ({N} records)"
36. Verifikasi seratus baris pertama tercentang
37. Verifikasi counter "100 clients selected"
38. Verifikasi Bulk Action Bar tetap tampil
39. Klik `Bulk Action`
40. Verifikasi menu memuat `Suspend` yang dapat dipakai
41. Verifikasi toast error persist (tetap tampil sampai di-dismiss): "Error, only the first 100 of {N} rows were selected. Narrow your filter to include the rest." dengan {N} sama dengan angka yang dicatat pada langkah 34
42. Tutup menu Bulk Action dan klik ikon (X) pada Bulk Action Bar
43. Kembalikan Selection Limit ke nilai awal (default 1000) di Admin Console > Plans & Licensing > Lifecycle Settings > tab System Limits

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan langkah berulang pemilihan baris atas tiga TC satu topik dan satu kelas harness (kelas e, volume data dan Selection Limit), satu akun; TC-AC-ACC-206 dan 207 berbagi satu perubahan Selection Limit (langkah 19 dan 20) karena nilainya sama, dan pemulihan limit ada di akhir spec (langkah 43) dan di hook `after`.
- Langkah penghubung (tanpa awalan Verifikasi): menutup Bulk Action Bar lewat (X) (langkah 18, 32, 42), langkah 2 dan 34 (centang satu baris agar tombol Select All tampil, TC menyebut Select All tanpa menyebut baris yang dicentang), kembali ke halaman 1 (langkah 33), dan pemulihan Selection Limit (langkah 43).
- Langkah 14 mengulang centang header di halaman pertama sampai tombol berubah; jumlah iterasi bergantung pada {N} yang diturunkan dari populasi (kemampuan baca jumlah baris `Regional Timur` disediakan tim FE/BE).
- Post Condition TC-AC-ACC-205: `-`; TC-AC-ACC-206 dan 207 ("Kembalikan Selection Limit ke nilai awal (default 1000)") menjadi langkah 43.
- Temuan untuk QA:
  - TC-AC-ACC-205 langkah 2 menyebut mencatat {N} pada tombol "Select All" tanpa menyebut baris yang dicentang agar tombol tampil; spec mencentang satu baris lebih dulu.
  - TC-AC-ACC-206 Expected a menyebut Bulk Action Bar "aktif" tanpa definisi; spec mengasersi bar tampil dengan counter "100 clients selected".
