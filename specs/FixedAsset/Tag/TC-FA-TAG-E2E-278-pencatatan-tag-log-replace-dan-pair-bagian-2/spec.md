---
id: TC-FA-TAG-E2E-278-pencatatan-tag-log-replace-dan-pair-bagian-2
title: "Pencatatan TAG Log Tag Baru: Paired dan Pair TAG per Tag"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1099
  - TC-FA-TAG-1100
  - TC-FA-TAG-1101
coverage:
  web: automated
---

# Pencatatan TAG Log Tag Baru: Paired dan Pair TAG per Tag

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00330` Paired; Tag RFID `RF-00071` berstatus To be Returned (Return Group 'Disposal Center'); 'Laptop Pro 14 - 9' (AST-0109, Plant A, NFC dan QR) Not Paired Yet.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri TAG Log tiap Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama dan dibaca ulang untuk Tag `NF-00500` pada langkah 19 sesudah pemulihan fixture (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 13); entri Changelog `Pair TAG` per Tag (langkah 25); entri TAG Log Global (langkah 4, 13, 25); entri Event Log To Be Returned (Method `Assigned`) (langkah 13). Jumlah entri TAG Log dibaca sebagai baseline lewat kemampuan baca; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1099: TAG Log Tag baru, entri Paired pada aset

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Klik [Submit]
5. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
6. Buka Global Settings > TAG
7. Klik aksi `TAG Log` pada Tag `RF-00412`
8. Verifikasi satu entri `Paired` oleh `Budi S.` untuk aset 'Excavator 20 Ton - 220'

### TC-FA-TAG-1100: TAG Log Tag baru berstatus To be Returned

9. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
10. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
11. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
12. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00071`
13. Klik [Submit]
14. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
15. Buka Global Settings > TAG
16. Klik aksi `TAG Log` pada Tag `RF-00071`
17. Verifikasi entri `Paired` dengan Previous Status `To be Returned`

### TC-FA-TAG-1101: TAG Log Pair TAG, entri Paired per Tag

18. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
19. Catat jumlah entri TAG Log Tag `NF-00500` sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
20. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A
21. Klik `Show` di samping `Not Paired Yet`
22. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
23. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
24. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
25. Klik [Submit]
26. Tunggu aksi selesai (dialog "Pair TAG" tertutup dan tombol aktif kembali)
27. Buka Global Settings > TAG
28. Klik aksi `TAG Log` pada Tag `NF-00500`
29. Verifikasi TAG Log `NF-00500` memuat satu entri baru `Paired` oleh `Budi S.` (selisih jumlah entri terhadap baseline langkah 19)

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 5, 9, 14, 18, 19 dan 26 (memulihkan data lewat fixture dan kembali ke halaman TAG antar TC, S-09). Langkah 5, 14 dan 26 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface. Langkah 19 adalah Catat jumlah baseline (butir A-18).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 13); entri Changelog `Pair TAG` per Tag (langkah 25); entri TAG Log Global (langkah 4, 13, 25); entri Event Log To Be Returned (Method `Assigned`) (langkah 13).
- Temuan untuk QA:
  - TC-FA-TAG-1100 precondition menyebut Return Group 'Disposal Center' yang 'dipegang Update oleh user'; akun aktor adalah Total Control, sehingga tidak ada syarat tambahan pada akun.
  - TC-FA-TAG-1099 sampai 1101 Post Condition ('Satu entri TAG Log Paired ...') sama dengan Expected yang diasersi.
  - TC-FA-TAG-1101 hanya memeriksa TAG Log `NF-00500`; TAG Log `QR-00701` tidak diamati dan Expected tidak memintanya.
