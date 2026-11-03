---
id: TC-FA-TAG-E2E-071-replace-penutupan-laporan-terbuka-dan-alur-ujung-ke-ujung-bagian-1
title: "Replace: Laporan Terbuka pada Tag Lain Tetap Terbuka, Penutupan Laporan Tag QR, dan Alur Ujung ke Ujung Admin Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-324
  - TC-FA-TAG-325
  - TC-FA-TAG-326
coverage:
  web: automated
---

# Replace: Laporan Terbuka pada Tag Lain Tetap Terbuka, Penutupan Laporan Tag QR, dan Alur Ujung ke Ujung Admin Aset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun aktor tambahan (ganti akun lewat langkah eksplisit): Manage asset & TAG (Read + Update) dengan Update pada Group Plant A `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_MU_UPA_PASSWORD`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00092` dan Tag QR `QR-00300` Paired, `QR-00300` punya laporan terbuka (Report Type Missing); 'Excavator 20 Ton - 42' (AST-0042, TAG Type Asset Name RFID) dengan Tag QR `QR-00230` Paired (Non-standard) dan laporan terbuka (Report Type Unreadable); 'Excavator 20 Ton - 220' (AST-0220) dengan Tag RFID `RF-00130` Paired dan laporan terbuka (Report Type Damaged) sehingga grup Excavator 20 Ton Plant A bernilai Reported 1 (diatur fixture BE sebelum TC-FA-TAG-326).
- Stok Global (dipakai sebagai precondition TC, tidak diasersi): Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-324: Replace Tag tanpa laporan membiarkan laporan terbuka pada Tag lain tetap terbuka

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
3. Centang baris `NF-00092`
4. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
5. Pindai Tag `NF-00500` dengan reader
6. Klik [Submit]
7. Verifikasi toast "Success, TAG has been replaced."
8. Verifikasi baris 'Laptop Pro 14 - 8' tetap berbadge `Tag Reported`
9. Verifikasi row action `Decline Report` tetap tersedia untuk aset itu

### TC-FA-TAG-325: Replace Tag QR yang punya laporan terbuka menutup laporan dan mencabut status Tag Reported

10. Tutup Popup Detail Assets
11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 42'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
14. Pindai Tag `RF-00412` dengan reader
15. Klik [Submit]
16. Verifikasi toast "Success, TAG has been replaced."
17. Verifikasi baris 'Excavator 20 Ton - 42' tidak lagi berbadge `Tag Reported`

### TC-FA-TAG-326: Alur ujung ke ujung Admin aset: dari kartu Reported ke Replace hingga aset keluar dari Reported

18. Pulihkan lewat fixture BE: Tag `RF-00130` Paired pada AST-0220 dengan laporan terbuka (Report Type Damaged), grup Excavator 20 Ton Plant A bernilai Reported 1, dan Tag `RF-00412` Available
19. Tutup Popup Detail Assets
20. Ganti akun: klik Logout
21. Login sebagai Manage asset & TAG (Read + Update) dengan Update pada Group Plant A (`manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_MU_UPA_PASSWORD`)
22. Buka Fixed Asset > TAG > Paired
23. Klik kartu `Reported`
24. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
25. Klik tombol `Show` di samping field `Reported`
26. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
27. Klik ButtonScan `Scan RFID` pada baris `RF-00130`
28. Pindai Tag `RF-00130` dengan reader
29. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
30. Pindai Tag `RF-00412` dengan reader
31. Klik [Submit]
32. Verifikasi toast "Success, TAG has been replaced."
33. Verifikasi baris 'Excavator 20 Ton - 220' tidak lagi berbadge `Tag Reported`
34. Tutup Popup Detail Assets
35. Verifikasi angka `Reported` grup Excavator 20 Ton Plant A menjadi 0

## Notes

- Langkah penghubung (S-03): Popup Detail Assets ditutup sebelum berganti Asset Name dan sebelum ganti akun; TC-FA-TAG-326 memakai akun Manage asset & TAG (Read + Update) dengan Update pada Group Plant A lewat ganti akun eksplisit (hook `after` mengembalikan sesi ke akun default suite); pemulihan data lewat fixture BE sebelum TC-FA-TAG-326; Popup ditutup sebelum membaca angka kartu grup.
- Pembagian TC lintas spec: TC-FA-TAG-340 dan 1378 ada di spec 072.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Post Condition TC-FA-TAG-324 (laporan terbuka pada `QR-00300` tetap terbuka, aset tetap dihitung Reported), TC-FA-TAG-325 (laporan `QR-00230` ditutup `Replaced`, aset keluar dari Reported dan Non-standard), dan TC-FA-TAG-326 (laporan ditutup `Replaced`, `RF-00130` Available, `RF-00412` Paired) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-FA-TAG-326 tidak menyebut pilihan Total Control sebagai akun alternatif; spec memakai akun Pre-setup `MU_UPA` yang sesuai Role pada Precondition TC.
