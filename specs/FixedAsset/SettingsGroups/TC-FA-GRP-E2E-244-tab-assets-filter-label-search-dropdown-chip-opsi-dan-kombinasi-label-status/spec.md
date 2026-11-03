---
id: TC-FA-GRP-E2E-244-tab-assets-filter-label-search-dropdown-chip-opsi-dan-kombinasi-label-status
title: "Tab Assets Filter Label: Search Dropdown, Chip Opsi (X dan Uncheck), dan Kombinasi Label + Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1174
  - TC-FA-GRP-1175
  - TC-FA-GRP-1176
  - TC-FA-GRP-1177
coverage:
  web: automated
---

# Tab Assets Filter Label: Search Dropdown, Chip Opsi (X dan Uncheck), dan Kombinasi Label + Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Multi Label Node (Pre-setup tambahan, Tabel Dinamis No 9, level 1) berisi hanya aset L1 (Finance, Fragile, Priority), L2 (Fragile, Priority), L3 (Priority), L4 (tanpa label), L5 (Finance); status aset bervariasi (sedikitnya dua status berbeda, termasuk status L1 yang berbeda dari sedikitnya satu aset lain). Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE). Warna hex tiap label dari katalog Labels.
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan kolom Label (langkah penghubung)

1. Ketik Search `Multi Label Node`, tekan Enter
2. Buka Detail Multi Label Node (Tab Assets)
3. Buka Popup Setup Column
4. Centang Label
5. Klik [Save]

### TC-FA-GRP-1174: Search internal dropdown Filter Label Tab Assets

6. Klik icon Filter
7. Buka dropdown Label
8. Ketik `fra` di kotak search dropdown
9. Verifikasi daftar opsi menyempit ke `Fragile` (case-insensitive)
10. Ganti isi kotak search dropdown dengan `zzzz`
11. Verifikasi daftar opsi kosong dengan teks "No results found"
12. Verifikasi tidak ada ilustrasi pada daftar opsi kosong (teks saja)
13. Kosongkan kotak search dropdown, tutup dropdown Label, klik [Clear Field]

### TC-FA-GRP-1175: Chip opsi Filter Label dihapus via (X) pada chip

14. Buka dropdown Label
15. Centang opsi `Finance`, lalu centang opsi `Fragile`
16. Tutup dropdown
17. Verifikasi chip `Finance` dan chip `Fragile` tampil di dalam field (chip kedua tidak menggantikan chip pertama)
18. Klik (X) pada chip `Finance`
19. Verifikasi chip `Finance` hilang
20. Verifikasi chip `Fragile` tetap ada
21. Buka dropdown Label
22. Verifikasi checkbox `Finance` di dropdown ter-uncheck
23. Tutup dropdown
24. Klik [Apply]
25. Verifikasi baris L1 dan L2 tampil
26. Verifikasi baris L3, L4, dan L5 tidak tampil

### TC-FA-GRP-1176: Chip opsi Filter Label dihapus via uncheck di dalam dropdown

27. Klik icon Filter
28. Klik [Clear Field]
29. Buka dropdown Label
30. Centang opsi `Finance`, lalu centang opsi `Fragile`
31. Uncheck opsi `Finance` dari dalam dropdown
32. Tutup dropdown
33. Verifikasi chip `Finance` hilang dari field
34. Verifikasi chip `Fragile` tetap ada
35. Klik [Apply]
36. Verifikasi baris L1 dan L2 tampil
37. Verifikasi baris L3, L4, dan L5 tidak tampil

### TC-FA-GRP-1177: Filter Tab Assets kombinasi Label + Status (AND antar-field)

38. Klik icon Filter
39. Klik [Clear Field]
40. Buka dropdown Label, centang opsi `Priority`, tutup dropdown
41. Buka dropdown Status, centang salah satu status yang dimiliki aset L1 (status L1 dibaca dari data seed sebelum aksi), tutup dropdown
42. Klik [Apply]
43. Verifikasi baris L1 tampil
44. Verifikasi hanya baris yang memenuhi kedua kriteria (Label `Priority` dan status L1) yang tampil (AND antar-field)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): Setup Column centang Label di awal spec (precondition d TC-1175 sampai TC-1177 "kolom curated Label sudah ditampilkan"); mengosongkan kotak search dropdown, menutup dropdown, [Clear Field] sebelum TC berikutnya; membuka ulang Filter Panel dengan klik icon Filter.
- Spec ini 44 langkah, di atas smell 35 langkah: satu kelas (fungsional), satu dataset (Multi Label Node), tiap blok TC berdiri sendiri dan tidak bergantung pada hasil blok lain; langkah dominan berupa Verifikasi per klausa (S-01).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA (S-15): (1) TC-1174 langkah 6 "teks yang tidak ada di opsi mana pun" tidak menyebut nilai; spec memakai `zzzz`. (2) TC-1177 menulis Status "salah satu status yang dimiliki aset L1" tanpa menyebut status konkret dan tanpa menyatakan aset lain mana yang berstatus sama sehingga hasil AND tidak terbukti membuang baris selain L1; precondition perlu menetapkan status tiap aset. (3) TC tidak menyatakan apakah Filter Panel tertutup sesudah [Apply]; spec membuka ulang dengan klik icon Filter sebelum tiap blok. (4) TC-1174 tidak memuat precondition d (kolom Label ditampilkan) sedangkan TC-1175 sampai TC-1177 memuatnya.
