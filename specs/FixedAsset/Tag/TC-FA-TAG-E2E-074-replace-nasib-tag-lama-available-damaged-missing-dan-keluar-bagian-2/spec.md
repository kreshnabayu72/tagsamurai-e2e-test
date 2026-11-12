---
id: TC-FA-TAG-E2E-074-replace-nasib-tag-lama-available-damaged-missing-dan-keluar-bagian-2
title: "Replace: Nasib Tag Lama pada Aset Non-TAG, Dua Tag Dilepas Sekaligus, dan Aset Multi-Tag (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-336
  - TC-FA-TAG-337
  - TC-FA-TAG-338
  - TC-FA-TAG-339
coverage:
  web: automated
---

# Replace: Nasib Tag Lama pada Aset Non-TAG, Dua Tag Dilepas Sekaligus, dan Aset Multi-Tag (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Forklift Manual - 62' (AST-0162, Group Plant A, Asset Name Non-TAG) dengan Tag RFID `RF-00150` Paired (fixture BE memasang ulang `RF-00150` sebelum TC-FA-TAG-337); 'Laptop Pro 14 - 10' (AST-0110, TAG Type Asset Name NFC dan RFID) dengan Tag NFC `NF-00094` dan Tag RFID `RF-00136` Paired, keduanya bertipe sesuai; 'Laptop Pro 14 - 8' (AST-0108, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00292` dan Tag QR `QR-00300` Paired.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` dan `NF-00501`, Tag QR `QR-00701` dan `QR-00702` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 9, 22, 31); entri TAG Log Global (langkah 4, 9, 22, 31).

## Test Steps

### TC-FA-TAG-336: Aset Non-TAG: Tag yang dipindai di overlay dilepas saja dan menjadi Available

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00150` dengan reader
3. Verifikasi bagian `Replacement TAG` menampilkan "No replacement needed."
4. Klik [Submit]
5. Verifikasi toast "Success, TAG has been replaced."

### TC-FA-TAG-337: Aset Non-TAG lewat row action tanpa pindai: Tag lama menjadi Damaged/Missing

6. Pulihkan lewat fixture BE: Tag `RF-00150` Paired pada AST-0162
7. Klik Asset Name 'Forklift Manual' pada baris grup Plant A untuk membuka Popup Detail
8. Klik row action `Replace TAG` pada baris 'Forklift Manual - 62'
9. Klik [Submit]
10. Verifikasi toast "Success, TAG has been replaced."

### TC-FA-TAG-338: Dua Tag dilepas dalam satu transaksi: yang dipindai Available, yang tidak dipindai Damaged/Missing

11. Tutup Popup Detail Assets
12. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
13. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 10'
14. Centang baris `NF-00094` dan baris `RF-00136`
15. Klik ButtonScan `Scan NFC` pada baris Tag `NF-00094` di `TAG to replace`
16. Pindai Tag `NF-00094` dengan reader
17. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
18. Pindai Tag `NF-00500` dengan reader
19. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
20. Pindai Tag `RF-00412` dengan reader
21. Tunggu toast lama hilang otomatis
22. Klik [Submit]
23. Verifikasi toast "Success, TAG has been replaced."
24. Verifikasi hanya satu Toast dan satu dialog yang menutup

### TC-FA-TAG-339: Aset multi-Tag: hanya Tag terpindai yang diganti dan Tag lain tidak tersentuh

25. Pulihkan stok lewat fixture BE: Tag `NF-00500` Available
26. Tutup Popup Detail Assets
27. Klik tombol scan `Replace TAG` di toolbar tab Paired
28. Pindai Tag `NF-00292` dengan reader
29. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
30. Pindai Tag `NF-00500` dengan reader
31. Klik [Submit]
32. Verifikasi toast "Success, TAG has been replaced."

## Notes

- Langkah penghubung (S-03): Popup Detail Assets ditutup sebelum berganti Asset Name dan sebelum memakai overlay scan; pemulihan data dan stok lewat fixture BE sebelum TC-FA-TAG-337 dan 339 karena `RF-00150` dan `NF-00500` sudah terpakai TC sebelumnya; urutan TC-FA-TAG-336 (overlay scan) berada di awal; langkah 21 menunggu toast lama TC-FA-TAG-337 (langkah 10) hilang otomatis sebelum [Submit] TC-FA-TAG-338, supaya hitungan toast pada langkah 24 hanya memuat toast baru (R-12).
- Pembagian TC lintas spec: TC-FA-TAG-332 sampai 335 ada di spec 073 dan TC-FA-TAG-1379 ada di spec 085.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 9, 22, 31); entri TAG Log Global (langkah 4, 9, 22, 31).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition (status Tag di registri Global, entri TAG Log, Changelog, dan modul terdampak) tidak punya langkah observasi di TC dan tidak diasersi: TC-FA-TAG-336 (`RF-00150` Available, aset tanpa Tag Paired), TC-FA-TAG-337 (`RF-00150` Damaged/Missing), TC-FA-TAG-338 (Tag baru Paired, `NF-00094` Available, `RF-00136` Damaged/Missing), TC-FA-TAG-339 (`NF-00500` Paired, `NF-00292` Available, `QR-00300` tetap Paired).
  - Judul TC-FA-TAG-336 sampai 339 menyatakan nasib Tag lama sebagai inti pengujian, tetapi TC hanya menaruhnya di Post Condition tanpa langkah observasi; QA perlu menambah Expected atau langkah observasinya.
