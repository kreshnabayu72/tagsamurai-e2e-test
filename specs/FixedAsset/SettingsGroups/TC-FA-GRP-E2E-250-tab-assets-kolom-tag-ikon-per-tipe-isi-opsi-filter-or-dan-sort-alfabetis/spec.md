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
- Ikon uji hover (dipakai langkah 8 sampai 9):
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

1. Buka Detail Value Gate Node A (Tab Assets)
2. Amati kolom TAG pada G1 sampai G6
3. Verifikasi kolom TAG tampil default (Visible) antara Asset ID dan Brand
4. Verifikasi G1 menampilkan dua ikon (RFID dan QR) penuh, G3 satu ikon NFC, G4 satu ikon BARCODE, dan G6 satu ikon QR
5. Verifikasi G2 (tanpa tag) dan G5 (pairing BARCODE berstatus tidak aktif) menampilkan `—`
6. Verifikasi sel tidak menampilkan Tag Code apa pun
7. Untuk setiap baris tabel Ikon uji hover (langkah 8 sampai 9):
8. Hover ikon pada baris aset
9. Verifikasi hover ikon menampilkan label tipe pada kolom Label hover

### TC-FA-GRP-1192: Isi opsi dropdown Filter TAG (populate dari data tabel)

10. Klik icon Filter
11. Buka dropdown field TAG
12. Verifikasi field TAG berupa dropdown multi-select searchable dengan placeholder `All tags`
13. Verifikasi opsi dropdown = `BARCODE`, `NFC`, `QR`, `RFID` (tipe tag yang ada di baris tabel)
14. Verifikasi kotak search internal tampil
15. Centang opsi `NFC` dan `QR`
16. Verifikasi opsi `NFC` dan `QR` tercentang bersamaan (dapat dicentang lebih dari satu)
17. Uncheck opsi `NFC` dan `QR`
18. Ketik `QR` pada kotak search internal
19. Verifikasi opsi menyempit ke `QR` (case-insensitive)
20. Kosongkan kotak search internal, tutup dropdown, klik [Clear Field]

### TC-FA-GRP-1193: Filter by TAG, satu opsi dan dua opsi (OR); pairing tidak aktif tidak dihitung

21. Buka dropdown field TAG, centang opsi `QR`, tutup dropdown
22. Klik [Apply]
23. Verifikasi G1 dan G6 tampil (aset dengan tag QR aktif, termasuk G1 yang juga ber-RFID)
24. Verifikasi G2, G3, G4, dan G5 tidak tampil
25. Verifikasi indikator filter aktif tampil pada icon Filter
26. Klik icon Filter
27. Klik [Clear Field]
28. Buka dropdown field TAG, centang opsi `BARCODE`, tutup dropdown
29. Klik [Apply]
30. Verifikasi G4 tampil
31. Verifikasi G5 tidak tampil karena pairing BARCODE-nya berstatus tidak aktif
32. Verifikasi G1, G2, G3, dan G6 tidak tampil
33. Klik icon Filter
34. Klik [Clear Field]
35. Buka dropdown field TAG, centang opsi `NFC` dan `BARCODE`, tutup dropdown
36. Klik [Apply]
37. Verifikasi G3 dan G4 tampil (OR di dalam field)
38. Verifikasi baris lain (G1, G2, G5, G6) tidak tampil
39. Klik icon Filter
40. Klik [Clear Field]
41. Klik [Apply]

### TC-FA-GRP-1194: Sort by kolom TAG, alfabetis atas label ikon

42. Klik header TAG sekali (Asc)
43. Verifikasi urutan Ascending: G4 (`BARCODE`), G3 (`NFC`), G6 (`QR`), G1 (`QR, RFID`; `QR` adalah awalan `QR, RFID` sehingga sel berjumlah tag lebih sedikit lebih dulu), lalu baris `—` (G2, G5) di akhir
44. Klik header TAG lagi (Desc)
45. Verifikasi urutan Descending kebalikan penuh: baris `—` (G2, G5) di awal, lalu G1, G6, G3, G4
46. Klik header TAG sekali lagi
47. Verifikasi urutan kembali ke default tabel (Name A→Z)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): membuka ulang Filter Panel dengan klik icon Filter; [Clear Field] dan [Apply] untuk membersihkan filter sebelum blok berikutnya; mencentang lalu meng-uncheck dua opsi dropdown untuk kembali ke state kosong; mengosongkan kotak search internal dan menutup dropdown. Langkah 8 sampai 9 diulang per baris tabel Ikon uji hover (8b butir 7).
- Spec ini 47 langkah, di atas smell 35 langkah dengan ekspansi: satu kelas (fungsional kolom TAG), satu dataset (Value Gate Node A), tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; sebagian besar langkah adalah Verifikasi per klausa.
- NC-07 (ikon final tipe tag dan transaksi) belum final: spec tidak mengasersi bentuk visual (glyph) ikon, hanya keberadaan, urutan, dan label hover.
- Temuan untuk QA (S-15): (1) TC tidak menyatakan apakah Filter Panel tertutup sesudah [Apply]; spec membuka ulang dengan klik icon Filter sebelum tiap blok. (2) TC-1193 menulis "Clear Field, lalu Filter ..." tanpa menyebut apakah [Clear Field] sendiri menerapkan filter; spec memakai [Clear Field] lalu memilih opsi baru dan [Apply]. (3) Expected TC-1192 butir b "dapat dicentang lebih dari satu" tidak punya langkah di TC; spec menambah centang dua opsi lalu meng-uncheck.
