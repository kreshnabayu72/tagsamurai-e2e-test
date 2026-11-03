---
id: TC-FA-TAG-E2E-073-replace-nasib-tag-lama-available-damaged-missing-dan-keluar-bagian-1
title: "Replace: Nasib Tag Lama Tidak Dipindai (Damaged/Missing), Tag NFC Not scanned, Non-standard QR Keluar, dan Non-standard RFID Available (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-332
  - TC-FA-TAG-333
  - TC-FA-TAG-334
  - TC-FA-TAG-335
coverage:
  web: automated
---

# Replace: Nasib Tag Lama Tidak Dipindai (Damaged/Missing), Tag NFC Not scanned, Non-standard QR Keluar, dan Non-standard RFID Available (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired; 'Laptop Pro 14 - 8' (AST-0108, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00092` dan Tag QR `QR-00300` Paired; 'Excavator 20 Ton - 42' (AST-0042, TAG Type Asset Name RFID) dengan Tag QR `QR-00230` Paired (Non-standard); 'Laptop Pro 14 - 11' (AST-0111, TAG Type Asset Name NFC) dengan Tag RFID `RF-00135` Paired (Non-standard).
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` dan `NF-00501`, Tag QR `QR-00701` dan `QR-00702` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-332: Tag normal tidak terbaca diganti tanpa dipindai: Tag lama menjadi Damaged/Missing

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00412` dengan reader
5. Klik [Submit]
6. Verifikasi toast "Success, TAG has been replaced."
7. Verifikasi dialog Replace TAG menutup

### TC-FA-TAG-333: Tag NFC di daftar lepas yang tidak dipindai tetap dapat di-Submit dengan badge Not scanned

8. Tutup Popup Detail Assets
9. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
10. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
11. Centang baris `NF-00092`
12. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
13. Pindai Tag `NF-00500` dengan reader
14. Verifikasi baris `NF-00092` berbadge `Not scanned` (peringatan)
15. Verifikasi tidak ada pesan error pemindaian wajib
16. Klik [Submit]
17. Verifikasi toast "Success, TAG has been replaced."

### TC-FA-TAG-334: Tag Non-standard QR diganti RFID: Tag QR keluar dari registri dan tidak masuk To Be Returned

18. Pulihkan stok lewat fixture BE: Tag `RF-00412` dan `NF-00500` Available
19. Tutup Popup Detail Assets
20. Klik tombol scan `Replace TAG` di toolbar tab Paired
21. Pindai Tag `QR-00230` dengan reader
22. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
23. Pindai Tag `RF-00412` dengan reader
24. Klik [Submit]
25. Verifikasi toast "Success, TAG has been replaced."
26. Verifikasi dialog menutup

### TC-FA-TAG-335: Tag Non-standard RFID yang dipindai diganti NFC: Tag lama menjadi Available

27. Klik tombol scan `Replace TAG` di toolbar tab Paired
28. Pindai Tag `RF-00135` dengan reader
29. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
30. Pindai Tag `NF-00500` dengan reader
31. Klik [Submit]
32. Verifikasi toast "Success, TAG has been replaced."

## Notes

- Langkah penghubung (S-03): Popup Detail Assets ditutup sebelum berganti Asset Name dan sebelum memakai overlay scan; pemulihan stok lewat fixture BE sebelum TC-FA-TAG-334 karena `RF-00412` dan `NF-00500` sudah terpakai TC sebelumnya; urutan TC-FA-TAG-334 dan 335 (overlay scan) berada di akhir karena TC-FA-TAG-332 dan 333 memakai Popup Detail.
- Pembagian TC lintas spec: TC-FA-TAG-336 sampai 339 ada di spec 074.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition (status Tag di registri Global, entri TAG Log, Changelog, dan modul terdampak) tidak punya langkah observasi di TC dan tidak diasersi: TC-FA-TAG-332 (Tag baru Paired, `RF-00130` Damaged/Missing, tidak masuk To Be Returned), TC-FA-TAG-333 (`NF-00500` Paired, `NF-00092` Damaged/Missing, `QR-00300` tetap Paired), TC-FA-TAG-334 (`RF-00412` Paired, `QR-00230` keluar dari registri tanpa TAG Log, tidak di To Be Returned), TC-FA-TAG-335 (`NF-00500` Paired, `RF-00135` Available, aset tidak Non-standard).
  - Judul TC-FA-TAG-332 dan 334 menyatakan status Tag lama dan 'tidak masuk To Be Returned' sebagai inti pengujian, tetapi TC hanya menaruhnya di Post Condition tanpa langkah observasi; QA perlu menambah Expected atau langkah observasinya.
