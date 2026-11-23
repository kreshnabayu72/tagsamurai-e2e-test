---
id: TC-FA-SU-E2E-459-tab-transaction-admin-log-assignment-filter-date-kombinasi-search-filter-dan-pelepasan-kontrol
title: "Tab Transaction Admin Log Sub-tab Assignment: Filter Date, Kombinasi Search dan Filter, dan Pelepasan Kontrol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1155
  - TC-FA-SU-1156
  - TC-FA-SU-1157
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Filter Date, Kombinasi Search dan Filter, dan Pelepasan Kontrol

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

### TC-FA-SU-1155: Filter kelas date, kolom Date

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Klik icon Filter
3. Pilih rentang 15/07/26 sampai 17/07/26 pada field `Date`
4. Klik `[Apply]`
5. Verifikasi rentang inklusif 15/07/26 sampai 17/07/26 menyisakan `ASG-20260717-0069`, `ASG-20260715-0068` (2 baris)
6. Klik `[Clear Field]` pada field `Date`, lalu klik `[Apply]`
7. Klik icon Filter untuk menutup panel

### TC-FA-SU-1156: Kombinasi Search dan Filter dua arah

8. Verifikasi tabel menampilkan empat baris
9. Ketik Search `0068`, tekan Enter
10. Klik icon Filter, buka dropdown `Group`, lalu centang `Branch Surabaya`
11. Klik `[Apply]`
12. Verifikasi irisan Search `0068` dan Filter Group `Branch Surabaya` tidak menyisakan baris (0 baris)
13. Verifikasi kotak Search tetap berisi `0068` setelah Filter diterapkan
14. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
15. Kosongkan isi kotak search, tekan Enter
16. Buka dropdown `Group`, lalu centang `Branch Surabaya`
17. Klik `[Apply]`
18. Ketik Search `0068`, tekan Enter
19. Verifikasi irisan Filter Group `Branch Surabaya` dan Search `0068` tidak menyisakan baris (0 baris), identik dengan urutan sebelumnya
20. Verifikasi chip `Branch Surabaya` tetap tampil di field `Group` setelah Search dijalankan
21. Verifikasi tabel berada di halaman 1
22. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
23. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1157: Pelepasan kontrol (Clear Field, Clear Search, ganti kolom sort, dan recovery empty state)

24. Ketik Search `0068`, tekan Enter
25. Buka dropdown `Group`, lalu centang `Branch Surabaya`
26. Klik `[Apply]`
27. Klik header `Transaction ID` satu kali
28. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
29. Verifikasi Search `0068` tetap berlaku (tabel menyisakan `ASG-20260715-0068`)
30. Verifikasi Sort pada kolom `Transaction ID` tetap berlaku (icon sort ascending (↑) pada header)
31. Buka dropdown `Group`, lalu centang `Branch Surabaya`
32. Klik `[Apply]`
33. Kosongkan isi kotak search, tekan Enter
34. Verifikasi Filter Group `Branch Surabaya` tetap berlaku (tabel menyisakan `ASG-20260720-0071`)
35. Verifikasi Sort pada kolom `Transaction ID` tetap berlaku
36. Klik header `Date` satu kali
37. Verifikasi sort pindah ke kolom `Date` (icon sort ascending (↑) pada header `Date`)
38. Verifikasi Filter Group `Branch Surabaya` tetap berlaku (tabel menyisakan `ASG-20260720-0071`)
39. Ketik Search `zzzz`, tekan Enter
40. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
41. Kosongkan isi kotak search, tekan Enter
42. Verifikasi tabel kembali menyisakan `ASG-20260720-0071`
43. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
44. Klik header `Date` dua kali untuk mengembalikan sort ke default
45. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pengosongan Search, `[Clear Field]` pada Filter, pemulihan sort ke default, dan penutupan panel Filter; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pembagian TC lintas spec: perilaku Filter Panel dan chip dropdown ada di spec 460.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1156 dan 1157 tidak menyebut keyword dan filter yang dipakai; spec memakai Search `0068` dan Filter Group `Branch Surabaya` dari Data Uji TC. (2) TC-FA-SU-1157 Langkah Uji nomor 6 tidak menyebut keyword tanpa hasil; spec memakai `zzzz`. (3) Post Condition tidak ada.
- Spec ini berjumlah 45 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
