---
id: TC-FA-TAG-E2E-272-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-1
title: "Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1078
  - TC-FA-TAG-1079
  - TC-FA-TAG-1080
  - TC-FA-TAG-1081
coverage:
  web: automated
---

# Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 1

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku aksi pada TC adalah pengguna login dengan nama tampil 'Budi S.'; kolom Modified By diasersi berformat [First Name] [Last Initial].
- Data (Pre-setup TC, tanpa suffix): 'Excavator 20 Ton - 220' (AST-0220, Plant A, RFID) dengan Tag RFID `RF-00330` Paired; 'Excavator 20 Ton - 42' (AST-0042, Plant A, RFID) dengan Tag QR `QR-00230` Paired (Non-standard); 'Forklift Manual - 61' (AST-0161, Plant A, Non-TAG) dengan Tag QR `QR-00251` Paired; 'Laptop Pro 14 - 10' (AST-0110, Plant A, NFC dan RFID) dengan Tag NFC `NF-00094` dan RFID `RF-00136` Paired.
- Stok Global (precondition TC): Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Waktu aksi dicatat pada langkah 5 sesudah [Submit]; kolom Date dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 14, 21, 31); entri TAG Log Global (langkah 4, 14, 21, 31). Jumlah entri Changelog dibaca sebagai baseline lewat kemampuan baca; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset, Tag, laporan, stok Tag per tipe di registri Global, dan TAG Type Asset Name ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: stok Tag per tipe di registri Global, status Tag, dan data aset/laporan Pre-setup. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1078: Replace RFID ke RFID, satu baris pasangan Old ke New

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Klik [Submit]
5. Catat waktu saat ini (jam browser) sebagai waktu aksi penggantian
6. Klik tombol `Changelog` di toolbar tab Paired
7. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
8. Verifikasi satu baris baru: Action `Replace`, Name `Excavator 20 Ton - 220`, Field `TAG`, Old Value `[RFID] RF-00330`, New Value `[RFID] RF-00412`, Modified By `Budi S.`
9. Verifikasi kolom Date baris itu memuat tanggal dan waktu penggantian dalam format General Settings, sama dengan waktu yang dicatat pada langkah 5 (toleransi satu menit)
10. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1079: Replace Tag QR Non-standard diganti RFID

11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 42'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
14. Klik [Submit]
15. Klik tombol `Changelog` di toolbar tab Paired
16. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
17. Verifikasi satu baris baru: Action `Replace`, Name `Excavator 20 Ton - 42`, Field `TAG`, Old Value `[QR] QR-00230`, New Value `[RFID] RF-00412`
18. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1080: Tag dilepas tanpa pengganti, New Value strip

19. Klik Asset Name 'Forklift Manual' pada baris grup Plant A untuk membuka Popup Detail
20. Klik row action `Replace TAG` pada baris 'Forklift Manual - 61'
21. Klik [Submit]
22. Klik tombol `Changelog` di toolbar tab Paired
23. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
24. Verifikasi satu baris baru: Action `Replace`, Name `Forklift Manual - 61`, Field `TAG`, Old Value `[QR] QR-00251`, New Value `—`
25. Tutup Modal Changelog, lalu pulihkan aset, Tag, dan stok lewat fixture backend

### TC-FA-TAG-1081: Replace dua Tag bertipe sama, Old ke New bertipe sama

26. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
27. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 10'
28. Centang baris `NF-00094` dan baris `RF-00136`
29. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
30. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
31. Klik [Submit]
32. Klik tombol `Changelog` di toolbar tab Paired
33. Verifikasi Modal berjudul `Changelog: Paired TAG` memuat entri terbaru di atas dengan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
34. Verifikasi dua baris untuk aset 'Laptop Pro 14 - 10': Old Value `[NFC] NF-00094` ke New Value `[NFC] NF-00500`, dan Old Value `[RFID] RF-00136` ke New Value `[RFID] RF-00412`
35. Verifikasi Field kedua baris itu `TAG`

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 5, 10, 18 dan 25 (mencatat waktu aksi; menutup modal dan memulihkan data antar TC, S-09). Tiap TC memakai aset berbeda sehingga baris Changelog dicari lewat Name.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 4, 14, 21, 31); entri TAG Log Global (langkah 4, 14, 21, 31).
- Temuan untuk QA:
  - Keempat TC menulis stok Tag yang sama (RF-00412) sebagai Tag pengganti; stok dipulihkan antar TC lewat fixture backend agar tiap TC tidak menumpang hasil TC sebelumnya.
  - TC-FA-TAG-1078 sampai 1081 Post Condition ('Entri Changelog tersimpan permanen') sama dengan Expected yang diasersi; tidak ada langkah observasi tambahan.
