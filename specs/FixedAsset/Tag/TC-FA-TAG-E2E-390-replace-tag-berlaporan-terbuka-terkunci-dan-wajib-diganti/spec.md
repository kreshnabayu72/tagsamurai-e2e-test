---
id: TC-FA-TAG-E2E-390-replace-tag-berlaporan-terbuka-terkunci-dan-wajib-diganti
title: "Replace: Tag Berlaporan Terbuka Tercentang dan Terkunci pada Row Action, Overlay Scan, dan Bulk Batch Replace"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1504
  - TC-FA-TAG-1505
  - TC-FA-TAG-1506
  - TC-FA-TAG-1507
coverage:
  web: automated
---

# Replace: Tag Berlaporan Terbuka Tercentang dan Terkunci pada Row Action, Overlay Scan, dan Bulk Batch Replace

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00292` (tanpa laporan) dan Tag QR `QR-00300` (laporan terbuka Missing) Paired; aset 'Laptop Pro 14 - 12' (AST-0112, Group Plant A, TAG Type NFC) dengan Tag NFC `NF-00097` Paired. Untuk TC-FA-TAG-1506 laporan dipindah: `NF-00292` punya laporan terbuka (Report Type Damaged) dan `QR-00300` tanpa laporan.
- Stok Global (precondition TC, tidak diasersi): Tag NFC `NF-00500` dan `NF-00501`, Tag QR `QR-00701` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: status Tag di registri Global dan laporan Tag diubah oleh Replace pada TC-FA-TAG-1505; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` aset AST-0108 (langkah 15); entri TAG Log Global (langkah 15).

## Test Steps

### TC-FA-TAG-1504: Tag berlaporan terbuka pada aset multi-Tag tercentang dan terkunci dengan tooltip S-56

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
3. Arahkan kursor ke checkbox baris `QR-00300`
4. Verifikasi baris `QR-00300` tercentang dan checkbox Disabled
5. Verifikasi tooltip "This TAG has an open report and must be replaced." tampil pada checkbox `QR-00300`
6. Verifikasi baris `NF-00292` tidak tercentang dan checkbox aktif
7. Verifikasi bagian `Replacement TAG` memuat satu slot `QR TAG`

### TC-FA-TAG-1505: Centang Tag berlaporan terbuka tidak dapat dibatalkan dan Submit hanya mengganti Tag itu

8. Klik [Cancel] pada dialog Replace TAG
9. Verifikasi dialog menutup
10. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
11. Klik checkbox baris `QR-00300`
12. Verifikasi baris `QR-00300` tetap tercentang
13. Klik ButtonScan `Scan QR` pada slot `QR TAG`
14. Pindai Tag `QR-00701` dengan reader
15. Klik [Submit]
16. Verifikasi toast "Success, TAG has been replaced."
17. Verifikasi baris 'Laptop Pro 14 - 8' tidak lagi berbadge `Tag Reported`

### TC-FA-TAG-1506: Overlay scan: Tag terpindai berlaporan terbuka tidak dapat dibatalkan centangnya

18. Pulihkan lewat fixture BE: AST-0108 dengan `NF-00292` Paired berlaporan terbuka (Report Type Damaged) dan `QR-00300` Paired tanpa laporan, `NF-00500` Available
19. Tutup Popup Detail Assets
20. Klik tombol scan `Replace TAG` di toolbar tab Paired
21. Pindai Tag `NF-00292` dengan reader
22. Verifikasi baris `NF-00292` tercentang, berbadge `Scanned`, dan checkbox Disabled
23. Klik checkbox baris `NF-00292`
24. Verifikasi baris `NF-00292` tetap tercentang
25. Verifikasi baris `QR-00300` tidak tercentang dan checkbox aktif

### TC-FA-TAG-1507: Bulk Batch Replace TAG: Tag berlaporan terbuka tercentang awal dan terkunci, Tag lain tidak tercentang

26. Buka Fixed Asset > TAG > Paired
27. Pulihkan lewat fixture BE: AST-0108 dengan `NF-00292` Paired tanpa laporan dan `QR-00300` Paired berlaporan terbuka (Report Type Missing), AST-0112 dengan `NF-00097` Paired, `NF-00500`, `NF-00501`, dan `QR-00701` Available
28. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
29. Centang baris 'Laptop Pro 14 - 8' dan 'Laptop Pro 14 - 12'
30. Klik Bulk `Batch Replace TAG`
31. Verifikasi header `Replace TAG · Asset 1 of 2`
32. Verifikasi baris `QR-00300` tercentang dan checkbox Disabled dengan tooltip "This TAG has an open report and must be replaced."
33. Verifikasi baris `NF-00292` tidak tercentang, checkbox aktif, dan tanpa badge `Scanned`

## Notes

- Langkah penghubung (S-03): Cancel pada langkah 8 menutup Dialog Replace TAG sebelum TC berikutnya membukanya lagi dari row action; Popup Detail Assets ditutup sebelum memakai overlay scan (langkah 19); halaman dibuka ulang pada langkah 26 untuk menutup dialog overlay scan; pemulihan data lewat fixture BE sebelum TC-FA-TAG-1506 dan 1507.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent, pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` aset AST-0108 (langkah 15); entri TAG Log Global (langkah 15).
- Pembagian TC lintas spec: TC-FA-TAG-1508 (Tag berlaporan bertipe terkunci plan) ada di spec 391 karena membutuhkan perubahan plan Client.
- Temuan untuk QA:
  - TC-FA-TAG-1505 (Post Condition: laporan `QR-00300` ditutup `Replaced`, `NF-00292` tetap Paired, `QR-00701` Paired) tidak punya langkah observasi di TC dan tidak diasersi.
  - `[Cancel]` pada langkah 8 dipakai karena dialog belum berisi isian pengguna (hanya centang otomatis dan observasi), sehingga konfirmasi `Discard Replacement` (`D-09`, "di tengah pengisian") tidak diharapkan. Dialog yang terbuka lewat overlay scan membawa Tag terverifikasi dan PRD tidak menyatakan apakah itu terhitung isian, sehingga langkah 26 menutupnya dengan membuka ulang halaman, bukan `[Cancel]`.
