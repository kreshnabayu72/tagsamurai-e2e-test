---
id: TC-FA-TAG-E2E-292-sinkron-lintas-modul-registri-global-asset-detail-dan-stok-bagian-1
title: "Sinkron Lintas Modul: Registri Global dan Stok setelah Replace, Bagian 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1144
  - TC-FA-TAG-1145
  - TC-FA-TAG-1146
  - TC-FA-TAG-1147
coverage:
  web: automated
---

# Sinkron Lintas Modul: Registri Global dan Stok setelah Replace, Bagian 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00330` Paired; 'Excavator 20 Ton - 221' (AST-0221, Plant A, RFID) dengan Tag RFID `RF-00140` Paired.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available. Pada TC-FA-TAG-1146 dan 1147 `RF-00412` adalah satu-satunya Tag RFID Available di stok Global.
- Baseline jumlah Tag RFID Available di registri Global dibaca lewat kemampuan baca (disediakan tim FE/BE) pada langkah 20, sesudah fixture langkah 19 menyiapkan `RF-00412` sebagai satu-satunya Tag RFID Available dan sebelum aksi pemicu (S-12, butir A-18).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 15, 24, 33); entri TAG Log Global (langkah 5, 15, 24, 33).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1144: registri Global setelah Replace, Tag lama dipindai Available dan Tag baru Paired

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada baris `RF-00330` lalu pindai Tag `RF-00330`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik [Submit]
6. Buka Global Settings > TAG
7. Ketik Search `RF-00330`, tekan Enter
8. Verifikasi `RF-00330` berstatus Available
9. Ganti isi kotak search dengan `RF-00412`, tekan Enter
10. Verifikasi `RF-00412` berstatus Paired dan tertaut ke aset 'Excavator 20 Ton - 220'

### TC-FA-TAG-1145: Tag lama RFID tidak dipindai menjadi Damaged/Missing

11. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
12. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
13. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
15. Klik [Submit]
16. Buka Global Settings > TAG
17. Ketik Search `RF-00330`, tekan Enter
18. Verifikasi `RF-00330` berstatus Damaged/Missing

### TC-FA-TAG-1146: stok Global per tipe berkurang setelah Tag pengganti dipasang

19. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired dengan `RF-00412` sebagai satu-satunya Tag RFID Available di stok Global
20. Catat jumlah Tag RFID Available di registri Global sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
21. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
22. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
23. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
24. Klik [Submit]
25. Buka Global Settings > TAG
26. Filter Status Available tipe RFID
27. Verifikasi jumlah RFID Available berkurang 1 terhadap baseline yang dicatat pada langkah 20
28. Verifikasi `RF-00412` tidak lagi tampil sebagai Available

### TC-FA-TAG-1147: stok habis memperbarui tooltip Disabled Replace TAG

29. Pulihkan aset, Tag, dan stok lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired dengan `RF-00412` sebagai satu-satunya Tag RFID Available di stok Global
30. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
31. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
32. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
33. Klik [Submit]
34. Klik Asset Name 'Excavator 20 Ton' lalu arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 221'
35. Verifikasi row action `Replace TAG` pada 'Excavator 20 Ton - 221' tetap tampil namun Disabled
36. Verifikasi tooltip "No available RFID TAG in stock. Activate TAG in Global Settings > TAG."

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 11, 19, 20 dan 29 (memulihkan data dan stok lewat fixture, kembali ke halaman TAG antar TC, S-09).
- Absence TC-FA-TAG-1146 b (`RF-00412` tidak lagi tampil sebagai Available): didahului `Verifikasi` jumlah RFID Available berkurang 1 terhadap baseline pada daftar Global yang sama sebagai anchor positif (bagian 8b butir 2).
- TC-FA-TAG-1147 langkah TC ke-5 ('Klik Asset Name lalu arahkan kursor ke row action ...') ditulis satu langkah mengikuti TC.
- Alasan spec ini tetap di atas 35 langkah (36 langkah, satu di atas ambang): keempat blok memakai satu alur (Replace TAG pada 'Excavator 20 Ton - 220' lalu amatan lintas modul) di satu kelas harness (FE+BE dengan simulator reader sebagai langkah rutin) dan berdiri sendiri: tiap blok sesudah yang pertama dimulai dari pemulihan aset, Tag, dan stok lewat fixture (langkah 11, 19, 29), sehingga kegagalan satu blok (status Tag di registri Global, Tag lama Damaged/Missing, stok Global per tipe, tooltip Disabled) tidak membuat blok lain kehilangan makna; memecah hanya menggandakan Prerequisites dan hook seed serta pemulihan tanpa melepas kopling antar blok.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 5, 15, 24, 33); entri TAG Log Global (langkah 5, 15, 24, 33).
- Temuan untuk QA:
  - TC-FA-TAG-1144 langkah TC ke-6 ('cari RF-00330 dan RF-00412') menyebut dua kode dalam satu pencarian; spec mencari satu per satu.
  - TC-FA-TAG-1146 langkah TC ke-5 ('filter Status Available tipe RFID') tidak menyebut kontrol filter; spec mengikuti teks TC.
  - TC-FA-TAG-1144 sampai 1147 tidak punya Post Condition yang perlu diasersi di luar Expected.
