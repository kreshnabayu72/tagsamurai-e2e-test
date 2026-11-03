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
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00130` Paired; 'Forklift Manual - 62' (AST-0162, Plant A, Asset Name Non-TAG) dengan Tag RFID `RF-00150` Paired.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri TAG Log tiap Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1095: Tag lama RFID dipindai, Unpaired dengan Reason Replaced by

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada baris `RF-00130` lalu pindai Tag `RF-00130`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit]
6. Buka Global Settings > TAG
7. Klik aksi `TAG Log` pada Tag `RF-00130`
8. Verifikasi satu entri `Unpaired` dengan judul `TAG Unpaired by Budi S.`
9. Verifikasi Reason `Replaced by RF-00412`
10. Verifikasi baris `Status` berubah dari `Paired` ke `Available`

### TC-FA-TAG-1096: Tag lama RFID tidak dipindai, Status Paired ke Damaged/Missing

11. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
12. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
15. Klik [Submit]
16. Buka Global Settings > TAG
17. Klik aksi `TAG Log` pada Tag `RF-00130`
18. Verifikasi satu entri `Unpaired` dengan Reason `Replaced by RF-00412`
19. Verifikasi baris `Status` berubah dari `Paired` ke `Damaged/Missing`
20. Verifikasi tidak ada entri `Marked Damaged/Missing` terpisah

### TC-FA-TAG-1097: Tag lama dilepas tanpa pengganti, Reason Removed (no replacement)

21. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
22. Klik Asset Name 'Forklift Manual' pada baris grup Plant A untuk membuka Popup Detail
23. Klik row action `Replace TAG` pada baris 'Forklift Manual - 62'
24. Klik ButtonScan `Scan RFID` pada baris `RF-00150` lalu pindai Tag `RF-00150`
25. Klik [Submit]
26. Buka Global Settings > TAG
27. Klik aksi `TAG Log` pada Tag `RF-00150`
28. Verifikasi satu entri `Unpaired` dengan Reason `Removed (no replacement)`
29. Verifikasi baris `Status` berubah dari `Paired` ke `Available`

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 11 dan 21 (memulihkan data lewat fixture dan kembali ke halaman TAG antar TC, S-09).
- TC-FA-TAG-1098 (Tag QR lama keluar dari registri) ada di spec 303.
- Absence TC-FA-TAG-1096 (tidak ada entri `Marked Damaged/Missing` terpisah): didahului `Verifikasi` entri `Unpaired` dan perubahan Status pada TAG Log yang sama sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1095 sampai 1097 Post Condition ('Satu entri TAG Log untuk Tag lama') sama dengan Expected yang diasersi.
  - Langkah TC-FA-TAG-1095 'Klik aksi TAG Log pada Tag RF-00130' tidak menyebut pencarian baris di registri; spec mengikuti TC dan tim FE menentukan cara menemukan baris saat script.
