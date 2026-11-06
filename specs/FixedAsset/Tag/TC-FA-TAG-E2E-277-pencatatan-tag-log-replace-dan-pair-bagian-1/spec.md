---
id: TC-FA-TAG-E2E-277-pencatatan-tag-log-replace-dan-pair-bagian-1
title: "Pencatatan TAG Log Replace: Tag Lama Dipindai, Tidak Dipindai, dan Dilepas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1095
  - TC-FA-TAG-1096
  - TC-FA-TAG-1097
coverage:
  web: automated
---

# Pencatatan TAG Log Replace: Tag Lama Dipindai, Tidak Dipindai, dan Dilepas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00330` Paired; 'Forklift Manual - 62' (AST-0162, Plant A, Asset Name Non-TAG) dengan Tag RFID `RF-00150` Paired.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri TAG Log tiap Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama dan dibaca ulang pada langkah 13 dan 25 sesudah pemulihan fixture (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 17, 29); entri TAG Log Global (langkah 5, 17, 29).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1095: Tag lama RFID dipindai, Unpaired dengan Reason Replaced by

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada baris `RF-00330` lalu pindai Tag `RF-00330`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit]
6. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
7. Buka Global Settings > TAG
8. Klik aksi `TAG Log` pada Tag `RF-00330`
9. Verifikasi satu entri `Unpaired` dengan judul `TAG Unpaired by Budi S.`
10. Verifikasi Reason `Replaced by RF-00412`
11. Verifikasi baris `Status` berubah dari `Paired` ke `Available`

### TC-FA-TAG-1096: Tag lama RFID tidak dipindai, Status Paired ke Damaged/Missing

12. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
13. Catat jumlah entri TAG Log Tag lama aset 'Excavator 20 Ton - 220' (kode yang sama dengan langkah 3) sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
15. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
17. Klik [Submit]
18. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
19. Buka Global Settings > TAG
20. Klik aksi `TAG Log` pada Tag `RF-00330`
21. Verifikasi satu entri baru `Unpaired` (selisih jumlah entri terhadap baseline langkah 13) dengan Reason `Replaced by RF-00412`
22. Verifikasi baris `Status` berubah dari `Paired` ke `Damaged/Missing`
23. Verifikasi tidak ada entri `Marked Damaged/Missing` terpisah

### TC-FA-TAG-1097: Tag lama dilepas tanpa pengganti, Reason Removed (no replacement)

24. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
25. Catat jumlah entri TAG Log Tag `RF-00150` sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
26. Klik Asset Name 'Forklift Manual' pada baris grup Plant A untuk membuka Popup Detail
27. Klik row action `Replace TAG` pada baris 'Forklift Manual - 62'
28. Klik ButtonScan `Scan RFID` pada baris `RF-00150` lalu pindai Tag `RF-00150`
29. Klik [Submit]
30. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
31. Buka Global Settings > TAG
32. Klik aksi `TAG Log` pada Tag `RF-00150`
33. Verifikasi satu entri baru `Unpaired` (selisih jumlah entri terhadap baseline langkah 25) dengan Reason `Removed (no replacement)`
34. Verifikasi baris `Status` berubah dari `Paired` ke `Available`

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 6, 12, 13, 18, 24, 25 dan 30 (memulihkan data lewat fixture dan kembali ke halaman TAG antar TC, S-09). Langkah 6, 18 dan 30 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface.
- TC-FA-TAG-1098 (Tag QR lama keluar dari registri) ada di spec 303.
- Absence TC-FA-TAG-1096 (tidak ada entri `Marked Damaged/Missing` terpisah): didahului `Verifikasi` entri `Unpaired` dan perubahan Status pada TAG Log yang sama sebagai anchor positif (bagian 8b butir 2).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 17, 29); entri TAG Log Global (langkah 5, 17, 29).
- Temuan untuk QA:
  - TC-FA-TAG-1095 sampai 1097 Post Condition ('Satu entri TAG Log untuk Tag lama') sama dengan Expected yang diasersi.
  - TC-FA-TAG-1095 sampai 1097 mengharapkan "satu entri" pada TAG Log permanen; spec mengasersi entri baru terhadap baseline yang dicatat per TC (S-12, butir A-18).
  - Langkah TC-FA-TAG-1095 'Klik aksi TAG Log pada Tag RF-00330' tidak menyebut pencarian baris di registri; spec mengikuti TC dan tim FE menentukan cara menemukan baris saat script.
