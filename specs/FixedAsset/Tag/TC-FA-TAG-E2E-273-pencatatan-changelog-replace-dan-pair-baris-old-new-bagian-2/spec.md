---
id: TC-FA-TAG-E2E-273-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-2
title: "Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 2"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1082
  - TC-FA-TAG-1083
  - TC-FA-TAG-1084
coverage:
  web: automated
---

# Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 50' (AST-0050, Plant A, RFID) dengan Tag QR `QR-00240` dan NFC `NF-00090` Paired (keduanya Non-standard); 'Excavator 20 Ton - 220' (`RF-00130`) dan 'Excavator 20 Ton - 221' (`RF-00140`) di Plant A, masing-masing satu Tag RFID Paired; 'Server Rack 42U - 101' (AST-0101, Plant A, RFID, NFC, dan QR) Not Paired Yet.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1082: Replace dua Tag Non-standard, satu pasangan dan satu Tag lama tanpa pasangan

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 50'
3. Centang baris `QR-00240` dan baris `NF-00090`
4. Verifikasi bagian `Replacement TAG` hanya memuat satu slot `RFID TAG` untuk dua Tag lama yang dicentang (tipe wajib kosong setelah pelepasan hanya RFID)
5. Verifikasi tidak ada slot kedua untuk `QR-00240`
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00420`
7. Klik [Submit]
8. Klik tombol `Changelog` di toolbar tab Paired
9. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
10. Verifikasi dua baris: Old Value `[NFC] NF-00090` ke New Value `[RFID] RF-00420`, dan Old Value `[QR] QR-00240` ke New Value `—` (tanpa Tag pemicu, Tag lama berpasangan menurut TAG Code A–Z)
11. Verifikasi kedua baris tidak pernah memuat Old Value dan New Value sama-sama `—`
12. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1083: Batch Replace, satu entri per aset Done dan tanpa entri untuk aset Skipped

13. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
14. Centang aset 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
15. Klik Bulk `Batch Replace TAG`
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
17. Klik [Submit & next]
18. Klik [Skip]
19. Klik [Close]
20. Klik tombol `Changelog` di toolbar tab Paired
21. Verifikasi satu baris untuk 'Excavator 20 Ton - 220': Old Value `[RFID] RF-00130` ke New Value `[RFID] RF-00412`
22. Verifikasi tidak ada baris untuk 'Excavator 20 Ton - 221'
23. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1084: Pair TAG menulis satu entri per Tag dengan Old Value strip

24. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A
25. Klik `Show` di samping `Not Paired Yet`
26. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
27. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
28. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
29. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
30. Klik [Submit]
31. Klik tombol `Changelog` di toolbar tab Paired
32. Verifikasi tiga baris untuk Name `Server Rack 42U - 101` dengan Action `Pair TAG` dan Field `TAG`
33. Verifikasi Old Value `—` dan New Value `[RFID] RF-00412`, `[NFC] NF-00500`, `[QR] QR-00701` masing-masing satu baris
34. Verifikasi Modified By `Budi S.`

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 12 dan 23 (menutup modal dan memulihkan data antar TC, S-09).
- Temuan untuk QA:
  - TC-FA-TAG-1083 Expected tidak menyebut judul Modal Changelog; spec tidak menambah asersi judul (S-02).
  - TC-FA-TAG-1082 sampai 1084 Post Condition ('Entri Changelog tersimpan permanen', 'Satu entri Replace untuk aset yang Done', 'Tiga entri Pair TAG tersimpan') sama dengan Expected yang diasersi.
