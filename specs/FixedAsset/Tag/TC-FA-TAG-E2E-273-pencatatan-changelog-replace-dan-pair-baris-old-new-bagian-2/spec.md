---
id: TC-FA-TAG-E2E-273-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-2
title: "Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 2"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1082
  - TC-FA-TAG-1083
  - TC-FA-TAG-1084
coverage:
  web: automated
---

# Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 50' (AST-0050, Plant A, RFID) dengan Tag QR `QR-00240` dan NFC `NF-00090` Paired (keduanya Non-standard); 'Excavator 20 Ton - 220' (`RF-00330`) dan 'Excavator 20 Ton - 221' (`RF-00140`) di Plant A, masing-masing satu Tag RFID Paired; 'Server Rack 42U - 101' (AST-0101, Plant A, RFID, NFC, dan QR) Not Paired Yet.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Jumlah baris Changelog dengan Name 'Excavator 20 Ton - 221' dibaca lewat kemampuan baca (disediakan tim FE/BE) pada langkah 13, sesudah pemulihan langkah 12; nama aset itu dipakai spec lain dan Changelog bersifat permanen (butir A-18).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 7, 18); entri Changelog `Pair TAG` per Tag (langkah 31); entri TAG Log Global (langkah 7, 18, 31).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1082: Replace dua Tag Non-standard, satu pasangan dan satu Tag lama tanpa pasangan

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 50'
3. Centang baris `QR-00240` dan baris `NF-00090`
4. Verifikasi bagian `Replacement TAG` hanya memuat satu slot `RFID TAG` untuk dua Tag lama yang dicentang (tipe wajib kosong setelah pelepasan hanya RFID)
5. Verifikasi tidak ada slot kedua untuk `QR-00240`
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00420`
7. Klik [Submit]
8. Klik tombol `Changelog` di toolbar tab Paired
9. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
10. Verifikasi dua baris: Old Value `[NFC] NF-00090` ke New Value `[RFID] RF-00420`, dan Old Value `[QR] QR-00240` ke New Value `—` (tanpa Tag pemicu, Tag lama berpasangan menurut TAG Code A–Z)
11. Verifikasi kedua baris tidak pernah memuat Old Value dan New Value sama-sama `—`
12. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend
13. Catat jumlah baris Changelog Paired TAG dengan Name 'Excavator 20 Ton - 221' sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)

### TC-FA-TAG-1083: Batch Replace, satu entri per aset Done dan tanpa entri untuk aset Skipped

14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
15. Centang aset 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
16. Klik Bulk `Batch Replace TAG`
17. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
18. Klik [Submit & next]
19. Klik [Skip]
20. Klik [Close]
21. Klik tombol `Changelog` di toolbar tab Paired
22. Verifikasi satu baris untuk 'Excavator 20 Ton - 220': Old Value `[RFID] RF-00330` ke New Value `[RFID] RF-00412`
23. Verifikasi jumlah baris Changelog dengan Name 'Excavator 20 Ton - 221' sama dengan baseline langkah 13 (tidak ada baris baru untuk 'Excavator 20 Ton - 221')
24. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1084: Pair TAG menulis satu entri per Tag dengan Old Value strip

25. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A
26. Klik `Show` di samping `Not Paired Yet`
27. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
28. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
29. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
30. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
31. Klik [Submit]
32. Klik tombol `Changelog` di toolbar tab Paired
33. Verifikasi tiga baris untuk Name `Server Rack 42U - 101` dengan Action `Pair TAG` dan Field `TAG`
34. Verifikasi Old Value `—` dan New Value `[RFID] RF-00412`, `[NFC] NF-00500`, `[QR] QR-00701` masing-masing satu baris
35. Verifikasi Modified By `Budi S.`

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 12, 13 dan 24 (menutup modal dan memulihkan data antar TC, S-09).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 7, 18); entri Changelog `Pair TAG` per Tag (langkah 31); entri TAG Log Global (langkah 7, 18, 31).
- Temuan untuk QA:
  - TC-FA-TAG-1083 Expected tidak menyebut judul Modal Changelog; spec tidak menambah asersi judul (S-02).
  - TC-FA-TAG-1082 sampai 1084 Post Condition ('Entri Changelog tersimpan permanen', 'Satu entri Replace untuk aset yang Done', 'Tiga entri Pair TAG tersimpan') sama dengan Expected yang diasersi.
  - TC-FA-TAG-1083 Expected b ("Tidak ada baris untuk 'Excavator 20 Ton - 221'") ditulis absolut padahal Changelog bersifat permanen dan nama aset dipakai spec lain; spec mengasersi selisih nol terhadap baseline (S-12, butir A-18).
