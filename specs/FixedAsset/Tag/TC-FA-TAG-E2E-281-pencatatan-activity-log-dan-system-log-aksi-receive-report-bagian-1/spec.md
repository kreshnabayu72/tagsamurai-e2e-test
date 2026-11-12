---
id: TC-FA-TAG-E2E-281-pencatatan-activity-log-dan-system-log-aksi-receive-report-bagian-1
title: "Pencatatan Activity Log dan System Log Aksi Receive TAG dan Receive Manually"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1113
  - TC-FA-TAG-1114
  - TC-FA-TAG-1115
  - TC-FA-TAG-1116
coverage:
  web: automated
---

# Pencatatan Activity Log dan System Log Aksi Receive TAG dan Receive Manually

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Manage asset & TAG dengan Update di group Disposal Center [UP_DC] `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_UP_DC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix) Tag To Be Returned: [RFID] `RF-00071` (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group 'Disposal Center', Current Holder Dedi K.); [RFID] `RF-00088` ('Excavator 20 Ton - 5', 'Disposal Center', Dedi K.); [NFC] `NF-00092` ('Laptop Pro 14 - 8', 'HQ Warehouse', Rina T.).
- Akses Admin Console > Activity Log dan Global Settings > User (Detail User, tab System Log) oleh akun aktor tidak disebut TC; kemampuan membuka halaman itu dinyatakan sebagai kebutuhan akun (disediakan tim FE).
- Baseline jumlah entri Activity Log dan System Log Detail User pelaku dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama dan dibaca ulang pada langkah 10, 18, dan 28 sesudah pemulihan fixture (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 4, 13); entri TAG Log Global `Received` (langkah 4, 13); entri Event Log To Be Returned (Method `Manual`) (langkah 22, 32); entri TAG Log Global `Marked Damaged/Missing` (langkah 22, 32); entri Activity Log (Admin Console) (langkah 4, 22); entri System Log pelaku (langkah 13, 32).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned `RF-00071`, `RF-00088`, `NF-00092`, status Tag di registri Global, aset, dan laporan ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: status Tag di registri Global dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1113: Receive TAG menulis satu entri Activity Log

1. Buka tab To Be Returned
2. Klik tombol "Receive TAG"
3. Pindai Tag RF-00071
4. Klik tombol [Receive]
5. Buka Admin Console > Activity Log
6. Filter entri terbaru
7. Verifikasi Activity Log memuat satu entri baru untuk aksi ini (selisih jumlah entri terhadap baseline hook `before`) dengan kolom Date terisi dan Modified By berisi nama pelaku aksi
8. Verifikasi tidak ada entri ganda untuk aksi yang sama

### TC-FA-TAG-1114: Receive TAG menulis satu entri System Log pelaku

9. Pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
10. Catat jumlah entri System Log Detail User pelaku sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
11. Klik tombol "Receive TAG"
12. Pindai Tag RF-00071
13. Klik tombol [Receive]
14. Buka Detail User pelaku aksi, tab System Log
15. Verifikasi System Log pelaku memuat satu entri baru untuk aksi ini (selisih jumlah entri terhadap baseline langkah 10) dengan kolom Date, Action, Object, Name, Field, Old Value, New Value terisi
16. Verifikasi tidak ada entri ganda untuk aksi yang sama

### TC-FA-TAG-1115: Receive Manually menulis satu entri Activity Log

17. Pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
18. Catat jumlah entri Activity Log (Admin Console) sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
19. Buka menu aksi baris RF-00071
20. Klik "Receive Manually"
21. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
22. Klik tombol [Submit]
23. Buka Admin Console > Activity Log
24. Filter entri terbaru
25. Verifikasi Activity Log memuat satu entri baru untuk aksi ini (selisih jumlah entri terhadap baseline langkah 18) dengan kolom Date terisi dan Modified By berisi nama pelaku aksi
26. Verifikasi tidak ada entri ganda untuk aksi yang sama

### TC-FA-TAG-1116: Receive Manually menulis satu entri System Log pelaku

27. Pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
28. Catat jumlah entri System Log Detail User pelaku sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
29. Buka menu aksi baris RF-00071
30. Klik "Receive Manually"
31. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
32. Klik tombol [Submit]
33. Buka Detail User pelaku aksi, tab System Log
34. Verifikasi System Log pelaku memuat satu entri baru untuk aksi ini (selisih jumlah entri terhadap baseline langkah 28) dengan kolom Date, Action, Object, Name, Field, Old Value, New Value terisi
35. Verifikasi tidak ada entri ganda untuk aksi yang sama

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 9, 10, 17, 18, 27 dan 28 (memulihkan Tag To Be Returned lewat fixture dan kembali ke tab To Be Returned antar TC, S-09). Langkah 10, 18, dan 28 adalah Catat jumlah baseline (butir A-18).
- Asersi "tidak ada entri ganda" bukan kelas g: asersi jumlah entri terhadap baseline, didahului `Verifikasi` entri aksi yang tercatat (bagian 3 prinsip 13g).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 4, 13); entri TAG Log Global `Received` (langkah 4, 13); entri Event Log To Be Returned (Method `Manual`) (langkah 22, 32); entri TAG Log Global `Marked Damaged/Missing` (langkah 22, 32); entri Activity Log (Admin Console) (langkah 4, 22); entri System Log pelaku (langkah 13, 32).
- Temuan untuk QA:
  - TC-FA-TAG-1113 sampai 1116 menulis "Buka Detail User pelaku aksi" tanpa menyebut nama pelaku; spec memakai Detail User akun aktor [UP_DC].
  - TC-FA-TAG-1113 sampai 1116 Expected menyebut "kolom Date terisi" tanpa nilai; spec mengasersi terisi.
