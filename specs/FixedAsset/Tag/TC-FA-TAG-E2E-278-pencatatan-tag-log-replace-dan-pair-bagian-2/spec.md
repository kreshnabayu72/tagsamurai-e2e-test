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
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00130` Paired; Tag RFID `RF-00071` berstatus To be Returned (Return Group 'Disposal Center'); 'Laptop Pro 14 - 9' (AST-0109, Plant A, NFC dan QR) Not Paired Yet.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri TAG Log tiap Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1099: TAG Log Tag baru, entri Paired pada aset

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Klik [Submit]
5. Buka Global Settings > TAG
6. Klik aksi `TAG Log` pada Tag `RF-00412`
7. Verifikasi satu entri `Paired` oleh `Budi S.` untuk aset 'Excavator 20 Ton - 220'

### TC-FA-TAG-1100: TAG Log Tag baru berstatus To be Returned

8. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
9. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
10. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
11. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00071`
12. Klik [Submit]
13. Buka Global Settings > TAG
14. Klik aksi `TAG Log` pada Tag `RF-00071`
15. Verifikasi entri `Paired` dengan Previous Status `To be Returned`

### TC-FA-TAG-1101: TAG Log Pair TAG, entri Paired per Tag

16. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
17. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A
18. Klik `Show` di samping `Not Paired Yet`
19. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
20. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
21. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
22. Klik [Submit]
23. Buka Global Settings > TAG
24. Klik aksi `TAG Log` pada Tag `NF-00500`
25. Verifikasi TAG Log `NF-00500` memuat satu entri `Paired` oleh `Budi S.`

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 8 dan 16 (memulihkan data lewat fixture dan kembali ke halaman TAG antar TC, S-09).
- Temuan untuk QA:
  - TC-FA-TAG-1100 precondition menyebut Return Group 'Disposal Center' yang 'dipegang Update oleh user'; akun aktor adalah Total Control, sehingga tidak ada syarat tambahan pada akun.
  - TC-FA-TAG-1099 sampai 1101 Post Condition ('Satu entri TAG Log Paired ...') sama dengan Expected yang diasersi.
  - TC-FA-TAG-1101 hanya memeriksa TAG Log `NF-00500`; TAG Log `QR-00701` tidak diamati dan Expected tidak memintanya.
