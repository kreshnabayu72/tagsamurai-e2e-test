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
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 51' (AST-0051, Plant A, RFID saja) Not Paired Yet; 'Excavator 20 Ton - 220' (AST-0220) dengan Tag RFID `RF-00330` Paired; 'Excavator 20 Ton - 60' (AST-0060, Plant A, RFID dan QR) dengan Tag combined Paired RFID `RF-00800` + QR `QR-00800`.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) pada langkah 1 sebelum aksi pemicu TC-FA-TAG-1085 (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 14, 24); entri Changelog `Pair TAG` per Tag (langkah 6); entri TAG Log Global (langkah 6, 14, 24).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1085: Pair TAG satu slot menulis satu baris

1. Catat jumlah entri Changelog Paired TAG untuk 'Excavator 20 Ton - 51' dengan Action `Pair TAG` sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
2. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
3. Klik `Show` di samping `Not Paired Yet`
4. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
5. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
6. Klik [Submit]
7. Tunggu aksi selesai (dialog "Pair TAG" tertutup dan tombol aktif kembali)
8. Klik tombol `Changelog` di toolbar tab Paired
9. Verifikasi satu baris baru (selisih jumlah entri Changelog Paired TAG terhadap baseline langkah 1): Action `Pair TAG`, Name `Excavator 20 Ton - 51`, Field `TAG`, Old Value `—`, New Value `[RFID] RF-00412`
10. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1086: Old Value dan New Value Changelog Replace berupa teks polos

11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
14. Klik [Submit]
15. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
16. Klik tombol `Changelog` di toolbar tab Paired
17. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
18. Verifikasi kolom Old Value, New Value, dan Action menampilkan teks polos tanpa badge berwarna
19. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1087: Changelog Replace tidak memuat nasib Tag lama maupun baris Separate

20. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
21. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 60'
22. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
23. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
24. Klik [Submit]
25. Tunggu aksi selesai (dialog "Replace TAG" tertutup dan tombol aktif kembali)
26. Klik tombol `Changelog` di toolbar tab Paired
27. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
28. Verifikasi baris hanya berisi pasangan Old Value ke New Value dengan Field `TAG`
29. Verifikasi tidak ada baris dengan status Tag lama (`Available` atau `Damaged/Missing`)
30. Verifikasi tidak ada baris Separate

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1, 7, 10, 15, 19 dan 25 (mencatat baseline sebelum pemicu; menutup modal dan memulihkan data antar TC, S-09). Langkah 7, 15 dan 25 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface.
- Absence TC-FA-TAG-1087 (baris status Tag lama dan baris Separate): didahului `Verifikasi` isi Modal Changelog dan baris pasangan Old ke New sebagai anchor positif (bagian 8b butir 2).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 14, 24); entri Changelog `Pair TAG` per Tag (langkah 6); entri TAG Log Global (langkah 6, 14, 24).
- Temuan untuk QA:
  - TC-FA-TAG-1085 Expected tidak menyebut judul Modal Changelog; spec tidak menambah asersi judul (S-02).
  - TC-FA-TAG-1085 Expected ('Satu baris') dan Post Condition ('Satu entri Pair TAG tersimpan') tidak menyebut baseline; Changelog adalah audit trail permanen sehingga spec mengasersi satu baris baru sebagai selisih terhadap baseline langkah 1 (S-12, butir A-18).
  - TC-FA-TAG-1085 sampai 1087 Post Condition ('Satu entri Pair TAG tersimpan', 'Entri Changelog tersimpan permanen') sama dengan Expected yang diasersi.
