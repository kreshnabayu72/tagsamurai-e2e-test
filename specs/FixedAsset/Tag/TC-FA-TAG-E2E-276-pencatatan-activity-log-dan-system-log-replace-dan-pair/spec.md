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
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00130` Paired; 'Excavator 20 Ton - 51' (AST-0051, Plant A, RFID saja) Not Paired Yet.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Activity Log dan System Log Detail User 'Budi S.' dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1091: Activity Log mencatat Replace

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Klik [Submit]
5. Buka Admin Console > Activity Log
6. Verifikasi entri baru terbaru: Action `Replace`, Object `Tag`, Name `Excavator 20 Ton - 220`, Field `TAG`, Old Value `[RFID] RF-00130`, New Value `[RFID] RF-00412`, Modified By `Budi S.`

### TC-FA-TAG-1092: System Log pelaku mencatat Replace tanpa kolom Modified By

7. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
8. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
9. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
10. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
11. Klik [Submit]
12. Buka Global Settings > User > Detail user 'Budi S.' > tab System Log
13. Verifikasi entri baru terbaru: Action `Replace`, Object `Tag`, Name `Excavator 20 Ton - 220`, Field `TAG`, Old Value `[RFID] RF-00130`, New Value `[RFID] RF-00412`
14. Verifikasi tabel System Log tidak memuat kolom Modified By

### TC-FA-TAG-1093: Activity Log dan System Log mencatat Pair TAG per Tag

15. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
16. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
17. Klik `Show` di samping `Not Paired Yet`
18. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
19. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
20. Klik [Submit]
21. Buka Admin Console > Activity Log
22. Verifikasi Activity Log memuat entri Action `Pair TAG`, Name `Excavator 20 Ton - 51`, Field `TAG`, Old Value `—`, New Value `[RFID] RF-00412`, Modified By `Budi S.`
23. Buka Global Settings > User > Detail user 'Budi S.' > tab System Log
24. Verifikasi System Log Detail User 'Budi S.' memuat entri yang sama tanpa kolom Modified By

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 7 dan 15 (memulihkan data lewat fixture dan kembali ke halaman TAG antar TC, S-09).
- Temuan untuk QA:
  - TC-FA-TAG-1091 sampai 1093 menyebut 'Entri terbaru' tanpa menyebut Date; spec mengenali entri lewat selisih jumlah terhadap baseline serta Name, Action, dan Field (S-12, S-14).
  - TC-FA-TAG-1091 sampai 1093 Post Condition ('Satu entri ... tersimpan') sama dengan Expected yang diasersi.
