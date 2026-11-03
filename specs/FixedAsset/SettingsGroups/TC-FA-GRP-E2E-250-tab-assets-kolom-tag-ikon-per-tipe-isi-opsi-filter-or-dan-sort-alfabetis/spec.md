---
id: TC-FA-GRP-E2E-250-tab-assets-kolom-tag-ikon-per-tipe-isi-opsi-filter-or-dan-sort-alfabetis
title: "Tab Assets Kolom TAG: Satu Ikon per Tipe Tag Aktif, Isi Opsi Filter, Filter OR (Pairing Tidak Aktif Tidak Dihitung), dan Sort Alfabetis Label Ikon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1191
  - TC-FA-GRP-1192
  - TC-FA-GRP-1193
  - TC-FA-GRP-1194
coverage:
  web: automated
---

# Tab Assets Kolom TAG: Satu Ikon per Tipe Tag Aktif, Isi Opsi Filter, Filter OR (Pairing Tidak Aktif Tidak Dihitung), dan Sort Alfabetis Label Ikon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Value Gate Node A (Tabel Dinamis No 10, Assignable, level 1) berisi hanya aset G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Pairing tag (Tabel Dinamis No 15): aktif G1 RFID dan QR, G3 NFC, G4 BARCODE, G6 QR; G5 punya pairing BARCODE berstatus tidak aktif; G2 tanpa pairing. Pairing di-seed tanpa hardware. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Ikon uji hover (dipakai langkah 9 sampai 10):
  | Baris aset | Ikon | Label hover |
  |---|---|---|
  | G1 | ikon RFID | `RFID` |
  | G1 | ikon QR | `QR` |
  | G3 | ikon NFC | `NFC` |
  | G4 | ikon BARCODE | `BARCODE` |
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1191: Kolom TAG, satu ikon per tipe tag aktif, tanpa Tag Code

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Amati kolom TAG pada G1 sampai G6
4. Verifikasi kolom TAG tampil default (Visible) antara Asset ID dan Brand
5. Verifikasi G1 menampilkan dua ikon (RFID dan QR) penuh, G3 satu ikon NFC, G4 satu ikon BARCODE, dan G6 satu ikon QR
6. Verifikasi G2 (tanpa tag) dan G5 (pairing BARCODE berstatus tidak aktif) menampilkan `—`
7. Verifikasi sel tidak menampilkan Tag Code apa pun
8. Untuk setiap baris tabel Ikon uji hover (langkah 9 sampai 10):
9. Hover ikon pada baris aset
10. Verifikasi hover ikon menampilkan label tipe pada kolom Label hover

### TC-FA-GRP-1192: Isi opsi dropdown Filter TAG (populate dari data tabel)

11. Klik icon Filter
12. Buka dropdown field TAG
13. Verifikasi field TAG berupa dropdown multi-select searchable dengan placeholder `All tags`
14. Verifikasi opsi dropdown = `BARCODE`, `NFC`, `QR`, `RFID` (tipe tag yang ada di baris tabel)
15. Verifikasi kotak search internal tampil
16. Centang opsi `NFC` dan `QR`
17. Verifikasi opsi `NFC` dan `QR` tercentang bersamaan (dapat dicentang lebih dari satu)
18. Uncheck opsi `NFC` dan `QR`
19. Ketik `QR` pada kotak search internal
20. Verifikasi opsi menyempit ke `QR` (case-insensitive)
21. Kosongkan kotak search internal, tutup dropdown, klik [Clear Field]

### TC-FA-GRP-1193: Filter by TAG, satu opsi dan dua opsi (OR); pairing tidak aktif tidak dihitung

22. Buka dropdown field TAG, centang opsi `QR`, tutup dropdown
23. Klik [Apply]
24. Verifikasi G1 dan G6 tampil (aset dengan tag QR aktif, termasuk G1 yang juga ber-RFID)
25. Verifikasi G2, G3, G4, dan G5 tidak tampil
26. Verifikasi indikator filter aktif tampil pada icon Filter
27. Klik icon Filter
28. Klik [Clear Field]
29. Buka dropdown field TAG, centang opsi `BARCODE`, tutup dropdown
30. Klik [Apply]
31. Verifikasi G4 tampil
32. Verifikasi G5 tidak tampil karena pairing BARCODE-nya berstatus tidak aktif
33. Verifikasi G1, G2, G3, dan G6 tidak tampil
34. Klik icon Filter
35. Klik [Clear Field]
36. Buka dropdown field TAG, centang opsi `NFC` dan `BARCODE`, tutup dropdown
37. Klik [Apply]
38. Verifikasi G3 dan G4 tampil (OR di dalam field)
39. Verifikasi baris lain (G1, G2, G5, G6) tidak tampil
40. Klik icon Filter
41. Klik [Clear Field]
42. Klik [Apply]

### TC-FA-GRP-1194: Sort by kolom TAG, alfabetis atas label ikon

43. Klik header TAG sekali (Asc)
44. Verifikasi urutan Ascending: G4 (`BARCODE`), G3 (`NFC`), G6 (`QR`), G1 (`QR, RFID`; `QR` adalah awalan `QR, RFID` sehingga sel berjumlah tag lebih sedikit lebih dulu), lalu baris `—` (G2, G5) di akhir
45. Klik header TAG lagi (Desc)
46. Verifikasi urutan Descending kebalikan penuh: baris `—` (G2, G5) di awal, lalu G1, G6, G3, G4
47. Klik header TAG sekali lagi
48. Verifikasi urutan kembali ke default tabel (Name A→Z)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): membuka ulang Filter Panel dengan klik icon Filter; [Clear Field] dan [Apply] untuk membersihkan filter sebelum blok berikutnya; mencentang lalu meng-uncheck dua opsi dropdown untuk kembali ke state kosong; mengosongkan kotak search internal dan menutup dropdown. Langkah 9 sampai 10 diulang per baris tabel Ikon uji hover (8b butir 7).
- Spec ini 48 langkah, di atas smell 35 langkah dengan ekspansi: satu kelas (fungsional kolom TAG), satu dataset (Value Gate Node A), tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; sebagian besar langkah adalah Verifikasi per klausa.
- NC-07 (ikon final tipe tag dan transaksi) belum final: spec tidak mengasersi bentuk visual (glyph) ikon, hanya keberadaan, urutan, dan label hover.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA (S-15): (1) TC tidak menyatakan apakah Filter Panel tertutup sesudah [Apply]; spec membuka ulang dengan klik icon Filter sebelum tiap blok. (2) TC-1193 menulis "Clear Field, lalu Filter ..." tanpa menyebut apakah [Clear Field] sendiri menerapkan filter; spec memakai [Clear Field] lalu memilih opsi baru dan [Apply]. (3) Expected TC-1192 butir b "dapat dicentang lebih dari satu" tidak punya langkah di TC; spec menambah centang dua opsi lalu meng-uncheck.
