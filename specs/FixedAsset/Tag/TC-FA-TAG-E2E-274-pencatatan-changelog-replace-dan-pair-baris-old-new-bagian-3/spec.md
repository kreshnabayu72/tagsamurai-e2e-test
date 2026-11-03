---
id: TC-FA-TAG-E2E-274-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-3
title: "Pencatatan Changelog Pair Satu Slot dan Format Teks Polos Old dan New Value"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1085
  - TC-FA-TAG-1086
  - TC-FA-TAG-1087
coverage:
  web: automated
---

# Pencatatan Changelog Pair Satu Slot dan Format Teks Polos Old dan New Value

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 51' (AST-0051, Plant A, RFID saja) Not Paired Yet; 'Excavator 20 Ton - 220' (AST-0220) dengan Tag RFID `RF-00130` Paired; 'Excavator 20 Ton - 60' (AST-0060, Plant A, RFID dan QR) dengan Tag combined Paired RFID `RF-00800` + QR `QR-00800`.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1085: Pair TAG satu slot menulis satu baris

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
2. Klik `Show` di samping `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit]
6. Klik tombol `Changelog` di toolbar tab Paired
7. Verifikasi satu baris: Action `Pair TAG`, Name `Excavator 20 Ton - 51`, Field `TAG`, Old Value `—`, New Value `[RFID] RF-00412`
8. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1086: Old Value dan New Value Changelog Replace berupa teks polos

9. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
10. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
11. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
12. Klik [Submit]
13. Klik tombol `Changelog` di toolbar tab Paired
14. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
15. Verifikasi kolom Old Value, New Value, dan Action menampilkan teks polos tanpa badge berwarna
16. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1087: Changelog Replace tidak memuat nasib Tag lama maupun baris Separate

17. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
18. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 60'
19. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
20. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
21. Klik [Submit]
22. Klik tombol `Changelog` di toolbar tab Paired
23. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
24. Verifikasi baris hanya berisi pasangan Old Value ke New Value dengan Field `TAG`
25. Verifikasi tidak ada baris dengan status Tag lama (`Available` atau `Damaged/Missing`)
26. Verifikasi tidak ada baris Separate

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 8 dan 16 (menutup modal dan memulihkan data antar TC, S-09).
- Absence TC-FA-TAG-1087 (baris status Tag lama dan baris Separate): didahului `Verifikasi` isi Modal Changelog dan baris pasangan Old ke New sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1085 Expected tidak menyebut judul Modal Changelog; spec tidak menambah asersi judul (S-02).
  - TC-FA-TAG-1085 sampai 1087 Post Condition ('Satu entri Pair TAG tersimpan', 'Entri Changelog tersimpan permanen') sama dengan Expected yang diasersi.
