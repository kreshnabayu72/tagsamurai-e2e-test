---
id: TC-FA-GRP-E2E-251-tab-assets-kolom-tag-setup-column-dan-search-label-aksesibilitas-ikon
title: "Tab Assets Kolom TAG: Setup Column (Uncheck, Geser, Pin) dan Search Label Aksesibilitas Ikon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1196
  - TC-FA-GRP-1254
coverage:
  web: automated
---

# Tab Assets Kolom TAG: Setup Column (Uncheck, Geser, Pin) dan Search Label Aksesibilitas Ikon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Value Gate Node A (Tabel Dinamis No 10, Assignable, level 1) berisi hanya aset G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Pairing tag (Tabel Dinamis No 15): aktif G1 RFID dan QR, G3 NFC, G4 BARCODE, G6 QR; G5 punya pairing BARCODE berstatus tidak aktif; G2 tanpa pairing. Pairing di-seed tanpa hardware. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun lintas group (lihat Temuan untuk QA).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1196: Setup Column, kolom TAG (Hideable): uncheck, geser (drag), dan pin

1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column
3. Uncheck TAG
4. Klik [Save]
5. Verifikasi kolom TAG hilang dari tabel
6. Refresh F5
7. Buka Detail Value Gate Node A (Tab Assets)
8. Verifikasi kolom `Name` tampil di tabel
9. Verifikasi kolom TAG tetap hilang setelah F5
10. Buka Popup Setup Column
11. Centang TAG
12. Drag TAG ke posisi setelah Brand
13. Verifikasi urutan Live Preview mengikuti posisi baru
14. Klik [Save]
15. Verifikasi urutan kolom tabel berubah mengikuti posisi baru
16. Refresh F5
17. Buka Detail Value Gate Node A (Tab Assets)
18. Verifikasi urutan kolom tabel bertahan setelah F5
19. Buka Popup Setup Column
20. Klik icon Pin TAG
21. Klik [Save]
22. Scroll tabel horizontal
23. Verifikasi kolom TAG membeku (sticky) saat scroll horizontal
24. Refresh F5
25. Buka Detail Value Gate Node A (Tab Assets)
26. Scroll tabel horizontal
27. Verifikasi pin kolom TAG bertahan setelah F5
28. Buka Popup Setup Column
29. Klik icon Pin TAG untuk unpin
30. Klik [Save]
31. Scroll tabel horizontal
32. Verifikasi kolom TAG kembali ikut scroll

### TC-FA-GRP-1254: Search by kolom TAG, label aksesibilitas ikon

33. Ketik Search `RFID`, tekan Enter
34. Verifikasi G1 tampil (ikon ber-label RFID)
35. Verifikasi baris lain (G2, G3, G4, G5, G6) tidak tampil
36. Ganti isi kotak search dengan `qr`, tekan Enter
37. Verifikasi G1 dan G6 tampil (case-insensitive)
38. Ganti isi kotak search dengan `Tag-001`, tekan Enter
39. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (Tag Code tidak dicari)
40. Ganti isi kotak search dengan `LoRa`, tekan Enter
41. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
42. Ganti isi kotak search dengan `BARCODE`, tekan Enter
43. Verifikasi G4 tampil
44. Verifikasi G5 tidak tampil (pairing tidak aktif tidak dicocokkan)
45. Verifikasi G1, G2, G3, dan G6 tidak tampil
46. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): membuka ulang Detail Value Gate Node A sesudah Refresh F5 dan scroll horizontal ulang; Setup Column kolom TAG dicentang ulang sebelum geser; unpin lewat Popup Setup Column; mengosongkan Search dengan `(←)` di akhir. Search yang menghasilkan beberapa hasil (RFID, qr, BARCODE) menjadi anchor positif bagi empty state `Tag-001` dan `LoRa` (8b butir 2).
- Spec ini 46 langkah, di atas smell 35 langkah: satu kelas (fungsional kolom TAG), satu dataset, dua blok TC yang berdiri sendiri (Setup Column lalu Search); langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh F5.
- NC-07 (ikon final tipe tag dan transaksi) belum final: spec tidak mengasersi bentuk visual (glyph) ikon, hanya keberadaan, urutan, dan label hover.
- Temuan untuk QA (S-15): (1) TC-1254 langkah-langkah tidak memuat Search `BARCODE` padahal Expected butir e mengasersinya; spec menambahkan langkah itu. (2) TC-1254 menyebut `Tag-001` sebagai "Tag Code contoh" tanpa Tag Code di Tabel Dinamis No 15; spec memakai `Tag-001` apa adanya sebagai keyword yang tidak cocok. (3) TC-1196 tidak menyatakan apakah Popup Detail Group tetap terbuka sesudah F5; spec membuka ulang. (4) TC-1196 tidak menyebut langkah buka Popup Setup Column untuk unpin; ditambahkan. (5) TC-1196 langkah 4 "geser TAG ke posisi setelah Brand" dan langkah 3 uncheck: kolom dicentang kembali sebelum geser.
