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
- Lebar viewport diatur supaya tabel Tab Assets dapat di-scroll horizontal (dipakai asersi pin/scroll horizontal); hook `after` memulihkan viewport (S-03).

## Test Steps

### TC-FA-GRP-1196: Setup Column, kolom TAG (Hideable): uncheck, geser (drag), dan pin

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Buka Popup Setup Column
4. Uncheck TAG
5. Klik [Save]
6. Verifikasi kolom TAG hilang dari tabel
7. Refresh F5
8. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
9. Buka Detail Value Gate Node A (Tab Assets)
10. Verifikasi kolom `Name` tampil di tabel
11. Verifikasi kolom TAG tetap hilang setelah F5
12. Buka Popup Setup Column
13. Centang TAG
14. Drag TAG ke posisi setelah Brand
15. Verifikasi urutan Live Preview mengikuti posisi baru
16. Klik [Save]
17. Verifikasi urutan kolom tabel berubah mengikuti posisi baru
18. Refresh F5
19. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
20. Buka Detail Value Gate Node A (Tab Assets)
21. Verifikasi urutan kolom tabel bertahan setelah F5
22. Buka Popup Setup Column
23. Klik icon Pin TAG
24. Klik [Save]
25. Atur lebar viewport supaya tabel Tab Assets dapat di-scroll horizontal
26. Scroll tabel horizontal
27. Verifikasi kolom TAG membeku (sticky) saat scroll horizontal
28. Refresh F5
29. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
30. Buka Detail Value Gate Node A (Tab Assets)
31. Scroll tabel horizontal
32. Verifikasi pin kolom TAG bertahan setelah F5
33. Buka Popup Setup Column
34. Klik icon Pin TAG untuk unpin
35. Klik [Save]
36. Scroll tabel horizontal
37. Verifikasi kolom TAG kembali ikut scroll

### TC-FA-GRP-1254: Search by kolom TAG, label aksesibilitas ikon

38. Ketik Search `RFID`, tekan Enter
39. Verifikasi G1 tampil (ikon ber-label RFID)
40. Verifikasi baris lain (G2, G3, G4, G5, G6) tidak tampil
41. Ganti isi kotak search dengan `qr`, tekan Enter
42. Verifikasi G1 dan G6 tampil (case-insensitive)
43. Ganti isi kotak search dengan `Tag-001`, tekan Enter
44. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (Tag Code tidak dicari)
45. Ganti isi kotak search dengan `LoRa`, tekan Enter
46. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
47. Ganti isi kotak search dengan `BARCODE`, tekan Enter
48. Verifikasi G4 tampil
49. Verifikasi G5 tidak tampil (pairing tidak aktif tidak dicocokkan)
50. Verifikasi G1, G2, G3, dan G6 tidak tampil
51. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): membuka ulang Detail Value Gate Node A sesudah Refresh F5 dan scroll horizontal ulang; Setup Column kolom TAG dicentang ulang sebelum geser; unpin lewat Popup Setup Column; mengosongkan Search dengan `(←)` di akhir. Search yang menghasilkan beberapa hasil (RFID, qr, BARCODE) menjadi anchor positif bagi empty state `Tag-001` dan `LoRa` (8b butir 2).
- Spec ini 51 langkah, di atas smell 35 langkah: satu kelas (fungsional kolom TAG), satu dataset, dua blok TC yang berdiri sendiri (Setup Column lalu Search); langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh F5.
- NC-07 (ikon final tipe tag dan transaksi) belum final: spec tidak mengasersi bentuk visual (glyph) ikon, hanya keberadaan, urutan, dan label hover.
- Langkah penghubung (S-03): "Atur lebar viewport ..." sebelum scroll horizontal pertama supaya tabel dapat di-scroll horizontal (asersi pin sticky); hook `after` memulihkan viewport.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA (S-15): (1) TC-1254 langkah-langkah tidak memuat Search `BARCODE` padahal Expected butir e mengasersinya; spec menambahkan langkah itu. (2) TC-1254 menyebut `Tag-001` sebagai "Tag Code contoh" tanpa Tag Code di Tabel Dinamis No 15; spec memakai `Tag-001` apa adanya sebagai keyword yang tidak cocok. (3) TC-1196 tidak menyatakan apakah Popup Detail Group tetap terbuka sesudah F5; spec membuka ulang. (4) TC-1196 tidak menyebut langkah buka Popup Setup Column untuk unpin; ditambahkan. (5) TC-1196 langkah 4 "geser TAG ke posisi setelah Brand" dan langkah 3 uncheck: kolom dicentang kembali sebelum geser.
