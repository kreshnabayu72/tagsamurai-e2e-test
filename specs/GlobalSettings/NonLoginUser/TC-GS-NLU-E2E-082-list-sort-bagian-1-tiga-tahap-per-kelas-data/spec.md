---
id: TC-GS-NLU-E2E-082-list-sort-bagian-1-tiga-tahap-per-kelas-data
title: "List Sort bagian 1: sort tiga tahap per kelas data (teks, tanggal, boolean, curated), nilai kosong, dan ikon sort"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-280
  - TC-GS-NLU-281
  - TC-GS-NLU-282
  - TC-GS-NLU-283
  - TC-GS-NLU-284
  - TC-GS-NLU-285
coverage:
  web: automated
---

# List Sort bagian 1: sort tiga tahap per kelas data (teks, tanggal, boolean, curated), nilai kosong, dan ikon sort

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): seluruh Non-Login User Pre-setup; `Siti Rahayu` (tanpa Position dan Employee ID, Position tampil `—`), `Rina Marlina` (Temporary User), baris Active dan Inactive, serta nilai Name, Position, Division, Employee ID, Represented By, dan Last Update yang berbeda (sedikitnya dua nilai berbeda per kolom pada halaman termuat). Jumlah baris lebih dari 10 (ukuran halaman default 10), sehingga halaman terakhir berbeda dari halaman 1 dan baris tanpa nilai kolom uji ada di halaman terakhir (Pre-setup No. 9 sampai 12). Fixture baru `Fixture.nonLoginUser.preSetup` di `fixtures/non-login-user.json` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Tabel "Kolom uji TC-GS-NLU-280" (langkah 1 sampai 6 diulang untuk setiap baris tabel):

| Kolom uji |
|---|
| `Name` |
| `Position` |
| `Division` |
| `Employee ID` |
| `Represented By` |

- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan urutan baris dan label sort (`Oldest First`, `Newest First`, `Active First`, `Inactive First`, `Yes First`, `No First`) pada header kolom; penghapusan preferensi kolom di browser di hook `after` (disediakan tim FE; spec ini menyimpan konfigurasi kolom untuk TC-GS-NLU-283).
- State global: konfigurasi kolom (Temporary User dan Temporary Until diaktifkan pada TC-GS-NLU-283, dipulihkan langkah 33 dan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-280: Sort 3 tahap kelas teks alfabetis

Untuk setiap baris tabel "Kolom uji TC-GS-NLU-280" (langkah 1 sampai 6):

1. Klik header kolom uji
2. Verifikasi klik #1: kolom uji terurut ascending A-Z
3. Klik header kolom uji
4. Verifikasi klik #2: kolom uji terurut descending Z-A
5. Klik header kolom uji
6. Verifikasi klik #3: tabel kembali ke default sort tabel

### TC-GS-NLU-281: Sort 3 tahap kelas tanggal

7. Klik header kolom `Last Update`
8. Verifikasi klik #1: `Oldest First`
9. Klik header kolom `Last Update`
10. Verifikasi klik #2: `Newest First`
11. Klik header kolom `Last Update`
12. Verifikasi klik #3: tabel kembali ke default sort tabel

### TC-GS-NLU-282: Sort 3 tahap kelas boolean toggle

13. Klik header kolom `Active`
14. Verifikasi klik #1: `Active First`
15. Klik header kolom `Active`
16. Verifikasi klik #2: `Inactive First`
17. Klik header kolom `Active`
18. Verifikasi klik #3: tabel kembali ke default sort tabel

### TC-GS-NLU-283: Sort kolom curated Temporary User dan Temporary Until

19. Klik `⋯` header Actions > `Setup Column...`, centang kolom Temporary User dan Temporary Until, klik `[Save]`
20. Klik header kolom `Temporary User`
21. Verifikasi klik #1: `Yes First`
22. Klik header kolom `Temporary User`
23. Verifikasi klik #2: `No First`
24. Klik header kolom `Temporary User`
25. Verifikasi klik #3: tabel kembali ke default sort tabel
26. Klik header kolom `Temporary Until`
27. Pindah ke halaman terakhir tabel
28. Verifikasi klik #1: `Oldest First` dan baris yang bukan Temporary User selalu di akhir saat ascending
29. Klik header kolom `Temporary Until`
30. Verifikasi klik #2: `Newest First`
31. Klik header kolom `Temporary Until` sekali lagi hingga kembali ke default sort
32. Pindah ke halaman 1 tabel
33. Klik `⋯` header Actions > `Setup Column...`, hapus centang kolom Temporary User dan Temporary Until, klik `[Save]`

### TC-GS-NLU-284: Nilai kosong Position dan Employee ID diurutkan di akhir saat ascending dan di awal saat descending

34. Klik header kolom `Position` (ascending)
35. Pindah ke halaman terakhir tabel
36. Verifikasi ascending: baris `Siti Rahayu` (Position `—`) berada di akhir
37. Klik header kolom `Position` (descending)
38. Pindah ke halaman 1 tabel
39. Verifikasi descending: baris Position kosong berada di awal
40. Klik header kolom `Position` sekali lagi hingga kembali ke default sort

### TC-GS-NLU-285: Kolom checkbox dan Column Visibility tidak memiliki ikon sort

41. Verifikasi tidak ada ikon sort pada header kolom checkbox dan kolom Actions `⋯`

## Notes

- Langkah penghubung (S-03): klik ketiga pada tiap kolom TC-GS-NLU-283 dan TC-GS-NLU-284 yang mengembalikan default sort (S-09), langkah 33 yang memulihkan kolom, dan langkah 27, 32, 35, 38 (pindah ke halaman terakhir atau halaman 1; S-14, S-03). Klik header tidak mengubah nomor halaman (TC-GS-NLU-306), sehingga langkah 27 dan 35 menempatkan tabel di halaman terakhir sebelum asersi "di akhir" (nilai kosong ascending berada di halaman terakhir karena populasi Pre-setup lebih dari 10 baris), dan langkah 32 serta 38 mengembalikan halaman 1 sebelum asersi "di awal" dan langkah berikutnya.
- Langkah yang diulang: langkah 1 sampai 6 diulang lima kali (satu per baris tabel "Kolom uji TC-GS-NLU-280"); `Verifikasi` tetap satu per klausa.
- Di atas 35 langkah, alasan: Spec ini sekitar 65 langkah setelah ekspansi (41 langkah nominal) dan dipertahankan utuh karena seluruh blok satu kelas harness (fungsional, tabel List yang sama, data Pre-setup yang sama, tanpa data milik spec) dan berdiri sendiri: kegagalan sort satu kolom tidak membuat kolom lain kehilangan makna.
- Asersi tambahan (S-03): baris `Siti Rahayu` dan sedikitnya dua nilai berbeda per kolom dipakai sebagai pembanding urutan (S-11).
- Temuan untuk QA:
  - TC-GS-NLU-280 sampai TC-GS-NLU-283 menyebut `Oldest First`, `Newest First`, `Active First`, `Inactive First`, `Yes First`, `No First` tanpa menyebut elemen UI tempat label itu tampil (tooltip atau label header); spec mengasersinya apa adanya.
  - TC-GS-NLU-284 judul menyebut Employee ID, tetapi langkah dan Expected hanya mengasersi kolom Position.
  - TC-GS-NLU-281: sort Oldest First dan Newest First pada Last Update berketelitian menit hanya diasersi pada pasangan entri dengan menit berbeda; urutan entri bermenit sama tidak diasersi.
  - TC-GS-NLU-281: kolom Last Update berketelitian menit; asersi urutan memerlukan sedikitnya dua nilai Last Update berbeda pada halaman termuat.
