---
id: TC-FA-TAG-E2E-276-pencatatan-activity-log-dan-system-log-replace-dan-pair
title: "Pencatatan Activity Log dan System Log untuk Replace dan Pair TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1091
  - TC-FA-TAG-1092
  - TC-FA-TAG-1093
coverage:
  web: automated
---

# Pencatatan Activity Log dan System Log untuk Replace dan Pair TAG

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Nama tampil akun aktor: 'Budi S.' (Detail User pada Global Settings > User).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00330` Paired; 'Excavator 20 Ton - 51' (AST-0051, Plant A, RFID saja) Not Paired Yet.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Activity Log dan System Log Detail User 'Budi S.' dibaca lewat kemampuan baca (disediakan tim FE/BE) pada langkah 1, 10, dan 20, masing-masing sebelum aksi pemicu TC-FA-TAG-1091, 1092, dan 1093 (dibaca ulang sesudah pemulihan fixture, butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 14); entri Changelog `Pair TAG` per Tag (langkah 25); entri TAG Log Global (langkah 5, 14, 25); entri Activity Log (Admin Console) (langkah 5, 25); entri System Log pelaku (langkah 14, 25).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1091: Activity Log mencatat Replace

1. Catat jumlah entri Activity Log (Admin Console) sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
3. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit]
6. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
7. Buka Admin Console > Activity Log
8. Verifikasi satu entri baru terbaru (selisih jumlah entri Activity Log terhadap baseline langkah 1): Action `Replace`, Object `Tag`, Name `Excavator 20 Ton - 220`, Field `TAG`, Old Value `[RFID] RF-00330`, New Value `[RFID] RF-00412`, Modified By `Budi S.`

### TC-FA-TAG-1092: System Log pelaku mencatat Replace tanpa kolom Modified By

9. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
10. Catat jumlah entri System Log Detail User 'Budi S.' sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
14. Klik [Submit]
15. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
16. Buka Global Settings > User > Detail user 'Budi S.' > tab System Log
17. Verifikasi satu entri baru terbaru (selisih jumlah entri System Log terhadap baseline langkah 10): Action `Replace`, Object `Tag`, Name `Excavator 20 Ton - 220`, Field `TAG`, Old Value `[RFID] RF-00330`, New Value `[RFID] RF-00412`
18. Verifikasi tabel System Log tidak memuat kolom Modified By

### TC-FA-TAG-1093: Activity Log dan System Log mencatat Pair TAG per Tag

19. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
20. Catat jumlah entri Activity Log dan System Log Detail User 'Budi S.' sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
21. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
22. Klik `Show` di samping `Not Paired Yet`
23. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
25. Klik [Submit]
26. Tunggu aksi selesai (dialog "Pair TAG" tertutup dan tombol aktif kembali)
27. Buka Admin Console > Activity Log
28. Verifikasi Activity Log memuat satu entri baru (selisih jumlah entri terhadap baseline langkah 20) dengan Action `Pair TAG`, Name `Excavator 20 Ton - 51`, Field `TAG`, Old Value `—`, New Value `[RFID] RF-00412`, Modified By `Budi S.`
29. Buka Global Settings > User > Detail user 'Budi S.' > tab System Log
30. Verifikasi System Log Detail User 'Budi S.' memuat satu entri baru yang sama (selisih jumlah entri terhadap baseline langkah 20) tanpa kolom Modified By

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1, 6, 9, 10, 15, 19, 20 dan 26 (mencatat baseline sebelum pemicu; memulihkan data lewat fixture dan kembali ke halaman TAG antar TC, S-09). Langkah 6, 15 dan 26 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 14); entri Changelog `Pair TAG` per Tag (langkah 25); entri TAG Log Global (langkah 5, 14, 25); entri Activity Log (Admin Console) (langkah 5, 25); entri System Log pelaku (langkah 14, 25).
- Temuan untuk QA:
  - TC-FA-TAG-1091 sampai 1093 menyebut 'Entri terbaru' tanpa menyebut Date; spec mengenali entri lewat selisih jumlah terhadap baseline per TC serta Name, Action, dan Field (S-12, S-14, butir A-18).
  - TC-FA-TAG-1091 sampai 1093 Post Condition ('Satu entri ... tersimpan') sama dengan Expected yang diasersi.
