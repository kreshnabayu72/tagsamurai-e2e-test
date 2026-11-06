---
id: TC-FA-TAG-E2E-293-sinkron-lintas-modul-registri-global-asset-detail-dan-stok-bagian-2
title: "Sinkron Lintas Modul: Registri Global dan Asset Detail setelah Pair TAG dan Replace, Bagian 2"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1148
  - TC-FA-TAG-1149
  - TC-FA-TAG-1150
  - TC-FA-TAG-1151
coverage:
  web: automated
---

# Sinkron Lintas Modul: Registri Global dan Asset Detail setelah Pair TAG dan Replace, Bagian 2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 51' (AST-0051, Plant A, RFID saja) Not Paired Yet; 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00330` Paired (pada TC-FA-TAG-1151 dengan laporan terbuka Damaged).
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Replace pada Changelog Asset Detail aset 'Excavator 20 Ton - 220' dibaca pada langkah 10 lewat kemampuan baca (disediakan tim FE/BE) sesudah pemulihan fixture dan sebelum pemicu langkah 14; Changelog bersifat permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18 (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 14, 32); entri Changelog `Pair TAG` per Tag (langkah 5, 24); entri TAG Log Global (langkah 5, 14, 24, 32).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1148: registri Global setelah Pair TAG

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
2. Klik `Show` di samping `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit]
6. Buka Global Settings > TAG
7. Ketik Search `RF-00412`, tekan Enter
8. Verifikasi `RF-00412` berstatus Paired dan tertaut ke aset 'Excavator 20 Ton - 51'

### TC-FA-TAG-1149: Asset Detail menampilkan Tag baru dan Changelog Replace

9. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
10. Catat jumlah entri Replace pada Changelog Asset Detail aset 'Excavator 20 Ton - 220' sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
14. Klik [Submit]
15. Buka Asset > Asset List > Detail aset 'Excavator 20 Ton - 220' > tab TAG
16. Verifikasi tab TAG memuat `RF-00412` dan tidak memuat `RF-00330`
17. Klik tombol `Changelog` di Asset Detail
18. Verifikasi Changelog Asset Detail memuat satu entri Replace baru (selisih jumlah entri Replace terhadap baseline langkah 10) dengan Old Value `[RFID] RF-00330` dan New Value `[RFID] RF-00412`

### TC-FA-TAG-1150: Tagging aset berubah dari Not Paired Yet menjadi Paired

19. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
20. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
21. Klik `Show` di samping `Not Paired Yet`
22. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
23. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
24. Klik [Submit]
25. Buka Asset > Asset List > Detail aset 'Excavator 20 Ton - 51'
26. Verifikasi status Tagging aset `Paired` dan tab TAG memuat `RF-00412`
27. Verifikasi badge `Not Paired Yet` tidak lagi tampil

### TC-FA-TAG-1151: status Tag Reported dicabut setelah Replace menutup laporan

28. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired dengan laporan terbuka (Report Type Damaged) pada Tag `RF-00330`
29. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
30. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
31. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
32. Klik [Submit]
33. Buka Asset > Asset List > Detail aset 'Excavator 20 Ton - 220'
34. Verifikasi status Tagging aset `Paired` tampil pada status aset
35. Verifikasi badge `Tag Reported` tidak tampil pada status aset

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 9, 10, 19 dan 28 (memulihkan data dan stok lewat fixture, kembali ke halaman TAG antar TC, S-09). Langkah 10 adalah Catat jumlah baseline (butir A-18).
- Absence TC-FA-TAG-1151 (badge `Tag Reported` tidak tampil) dan TC-FA-TAG-1150 (badge `Not Paired Yet` tidak tampil): didahului `Verifikasi` status Tagging `Paired` pada Asset Detail yang sama sebagai anchor positif. Pada TC-FA-TAG-1151 anchor positifnya adalah Expected butir a TC (status Tagging `Paired` tampil pada status aset; langkah 34, bagian 8b butir 2).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 14, 32); entri Changelog `Pair TAG` per Tag (langkah 5, 24); entri TAG Log Global (langkah 5, 14, 24, 32).
- Temuan untuk QA:
  - TC-FA-TAG-1148 sampai 1151 tidak punya Post Condition yang perlu diasersi di luar Expected.
