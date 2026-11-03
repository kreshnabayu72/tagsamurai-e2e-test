---
id: TC-FA-TAG-E2E-075-replace-efek-pada-perhitungan-non-standard-discard-dan-stok-bagian-1
title: "Replace: Efek pada Hitungan Non-standard, Aksi Grup Replace non-standard TAGs, dan Jumlah Slot per Tag Dicentang (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-327
  - TC-FA-TAG-328
  - TC-FA-TAG-329
  - TC-FA-TAG-341
coverage:
  web: automated
---

# Replace: Efek pada Hitungan Non-standard, Aksi Grup Replace non-standard TAGs, dan Jumlah Slot per Tag Dicentang (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 42' (AST-0042, Group Plant A, TAG Type Asset Name RFID) dengan Tag QR `QR-00230` Paired (Non-standard); 'Excavator 20 Ton - 243' (AST-0243, TAG Type RFID) dengan Tag QR `QR-00231` Paired (Non-standard); 'Server Rack 42U - 102' (AST-0102, TAG Type Asset Name RFID, NFC, dan QR) dengan Tag RFID `RF-00137`, Tag NFC `NF-00095`, dan Tag QR `QR-00302` Paired; 'Excavator 20 Ton - 220' (AST-0220) dengan Tag RFID `RF-00130` Paired. Fixture BE memulihkan AST-0042 dan stok sebelum TC-FA-TAG-341.
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` dan `NF-00501`, Tag QR `QR-00701` dan `QR-00702` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-327: Aksi grup Replace non-standard TAGs menyelesaikan Non-standard setelah sesi ditutup

1. Klik kebab di ujung baris grup Excavator 20 Ton Plant A
2. Klik aksi `Replace non-standard TAGs`
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
4. Pindai Tag `RF-00412` dengan reader
5. Klik [Submit & next]
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
7. Pindai Tag `RF-00415` dengan reader
8. Klik [Submit & next]
9. Verifikasi toast "Success, asset has been replaced."
10. Klik [Close]
11. Verifikasi angka `Non-standard` grup Excavator 20 Ton Plant A menjadi 0

### TC-FA-TAG-341: Replace Tag Non-standard mengeluarkan aset dari hitungan Non-standard

12. Pulihkan lewat fixture BE: aset AST-0042 dengan Tag QR `QR-00230` Paired (Non-standard) dan Tag `RF-00412` Available
13. Catat angka `Non-standard` grup Excavator 20 Ton Plant A sebelum aksi
14. Klik tombol scan `Replace TAG` di toolbar tab Paired
15. Pindai Tag `QR-00230` dengan reader
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
17. Pindai Tag `RF-00412` dengan reader
18. Klik [Submit]
19. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
20. Verifikasi baris 'Excavator 20 Ton - 42' tidak lagi menampilkan ikon peringatan Non-standard pada TAG Code
21. Tutup Popup Detail Assets
22. Verifikasi angka `Non-standard` grup berkurang 1 dari angka yang dicatat

### TC-FA-TAG-328: Dialog Replace aset tiga Tag: centang ketiganya menghasilkan tiga slot

23. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
24. Klik row action `Replace TAG` pada baris 'Server Rack 42U - 102'
25. Centang baris `RF-00137`, `NF-00095`, dan `QR-00302`
26. Verifikasi bagian `Replacement TAG` menampilkan tiga slot: `RFID TAG`, `NFC TAG`, `QR TAG`
27. Klik [Cancel] pada dialog Replace TAG

### TC-FA-TAG-329: Tombol ButtonScan berpindah ke state Scanning saat menunggu pindaian

28. Tutup Popup Detail Assets
29. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
30. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
31. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
32. Verifikasi ButtonScan `Scan RFID` berada dalam state Scanning
33. Pindai Tag `RF-00412` dengan reader
34. Verifikasi slot `RFID TAG` menampilkan `RF-00412`
35. Verifikasi slot `RFID TAG` menampilkan badge `Verified`
36. Klik [Cancel] pada dialog Replace TAG
37. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
38. Klik [Discard]
39. Tutup Popup Detail Assets

## Notes

- Langkah penghubung (S-03): Pencatatan angka `Non-standard` adalah baseline tanpa asersi; pemulihan data lewat fixture BE sebelum TC-FA-TAG-341 karena TC-FA-TAG-327 sudah menyelesaikan Non-standard AST-0042; Popup Detail Assets ditutup sebelum berganti Asset Name dan sebelum membaca angka grup; dialog TC-FA-TAG-329 yang terisi ditutup lewat [Cancel], verifikasi dialog `Discard Replacement`, dan [Discard]; urutan TC-FA-TAG-327 dan 341 (tanpa Popup atau overlay scan) berada di awal.
- Pembagian TC lintas spec: TC-FA-TAG-342 sampai 344 ada di spec 076.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Alasan di atas sekitar 35 langkah: semua blok satu kelas (fungsional) pada topik efek Replace; empat TC berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; tambahan langkah berasal dari penutupan Popup, pemulihan data, dan penutupan dialog dirty.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition (status Tag di registri Global, entri TAG Log, Changelog, dan modul terdampak) tidak punya langkah observasi di TC dan tidak diasersi: TC-FA-TAG-327 (kedua aset ber-Tag RFID, Tag QR lama keluar dari registri), TC-FA-TAG-341 (aset 'Excavator 20 Ton - 42' tidak Non-standard).
  - TC-FA-TAG-327 menulis Expected toast sesudah langkah [Close] tanpa menyatakan kapan toast tampil; spec mengasersi toast segera sesudah [Submit & next] terakhir sebelum [Close] (asersi state sementara tepat waktu).
  - TC-FA-TAG-327 menyebut Tag lama 'keluar dari registri' sebagai Post Condition tanpa langkah observasi.
