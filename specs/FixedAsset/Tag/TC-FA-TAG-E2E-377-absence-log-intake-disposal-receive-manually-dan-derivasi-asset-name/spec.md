---
id: TC-FA-TAG-E2E-377-absence-log-intake-disposal-receive-manually-dan-derivasi-asset-name
title: "Absence Log: Intake Disposal, Derivasi TAG Type, dan Receive Manually Tidak Menulis Entri yang Tidak Semestinya"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1240
  - TC-FA-TAG-1071
  - TC-FA-TAG-1110
coverage:
  web: automated
---

# Absence Log: Intake Disposal, Derivasi TAG Type, dan Receive Manually Tidak Menulis Entri yang Tidak Semestinya

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Asset Admin (pelaku disposal) `assetAdminPelakuDisposal_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC, kode AA_DSPO), password `Spectra.env.FA_TAG_AA_DSPO_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
  - Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD`. Dipakai pada langkah ganti akun (langkah 6).
  - Manage asset & TAG dengan Update di group Disposal Center `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC, kode UP_DC), password `Spectra.env.FA_TAG_UP_DC_PASSWORD`. Dipakai pada langkah ganti akun (langkah 22 dan 23).
  - Nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk ketiga akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Event Log untuk Tag tertentu dan Changelog Paired TAG sebelum aksi (baseline, S-12); seed idempotent aset, Tag To Be Returned, dan entri Event Log; perubahan dan pemulihan TAG Type Asset Name lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0900 'Excavator 20 Ton - 2' (Group Plant B) berstatus In Disposal Process dengan Disposal Request disetujui, Disposal Group transaksi Disposal Center, Tag RFID RF-00071 Paired pada AST-0900 sejak awal spec (keadaan untuk TC-FA-TAG-1240, sampai Execute disposal pada langkah 3). Sesudah langkah 3, RF-00071 berstatus To Be Returned dan tidak lagi Paired pada AST-0900. Tag To Be Returned (untuk TC-FA-TAG-1110, keadaan sesudah langkah 3 dan pemulihan langkah 21): [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.). Event Log berisi satu entri untuk Tag lain NF-00093 (HQ Warehouse), dipakai sebagai anchor positif. Pre-setup tab Paired: grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Parameter: Note Receive Manually "Tag rusak saat serah terima".
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name 'Excavator 20 Ton' ke RFID, status AST-0900 dan Tag RF-00071, serta Tag To Be Returned ke keadaan awal lewat fixture backend, lalu kembalikan sesi ke akun default suite. TAG Type Asset Name adalah state global yang diubah spec ini (langkah 15) dan dipulihkan pada langkah 21.
- Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri TAG Log Global dari penyelesaian disposal (Tag RF-00071 masuk To Be Returned) (langkah 3); entri Event Log To Be Returned (Method `Manual`) (langkah 29); entri TAG Log Global `Marked Damaged/Missing` (langkah 29). Penyelesaian Execute disposal AST-0900 (langkah 3) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain; jejak transaksi Disposal AST-0900 di modul Disposal tidak terpulihkan. Perubahan TAG Type Asset Name disimpan lewat `[Save]` di Settings > Asset Name (langkah 15) dan dipulihkan lewat fixture backend (langkah 21); penyimpanan itu mengirim notifikasi in-app `tag_replacement_needed` ke pemegang Update scope (efek yang tidak terpulihkan, langkah 15; PRD tag.md §9.7), dan PRD tag.md serta TC tidak menyatakan efek tak terpulihkan lain untuk penyimpanan atau pemulihan itu. Jumlah entri Changelog dan Event Log dibaca sebagai baseline pada langkah 1, 13, 24; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.

## Test Steps

### TC-FA-TAG-1240: Intake disposal tidak menulis Event Log

1. Catat baseline jumlah entri Event Log untuk RF-00071 lewat kemampuan baca (N1)
2. Buka layar Disposal Execute aset AST-0900
3. Selesaikan langkah Execute sampai disposal selesai
4. Tunggu aksi selesai (status disposal AST-0900 selesai)
5. Logout dari akun Asset Admin (pelaku disposal)
6. Login sebagai Total Control
7. Buka Fixed Asset > TAG > To Be Returned
8. Verifikasi baris RF-00071 tampil pada tab To Be Returned
9. Klik tombol "Event Log"
10. Verifikasi Event Log tampil dan memuat entri lain milik NF-00093
11. Verifikasi Event Log tidak memuat entri baru untuk RF-00071 (jumlah entri RF-00071 sama dengan N1)
12. Tutup Modal Event Log

### TC-FA-TAG-1071: Derivasi Non-standard dan Reported tidak menulis Changelog

13. Catat baseline jumlah entri Changelog Paired TAG (N2) dan nilai Non-standard pada baris grup Excavator 20 Ton lewat kemampuan baca
14. Buka Fixed Asset > Settings > Asset Name
15. Ubah TAG Type Excavator 20 Ton dari RFID menjadi NFC lalu klik [Save]
16. Buka Fixed Asset > TAG
17. Verifikasi Non-standard pada baris grup Excavator 20 Ton naik dibanding nilai yang dicatat pada langkah 13
18. Klik `Changelog`
19. Verifikasi jumlah entri Changelog tetap sama dengan N2
20. Tutup Modal Changelog
21. Pulihkan TAG Type Excavator 20 Ton ke RFID lewat fixture backend dan setel Tag To Be Returned ke keadaan seed TC-FA-TAG-1110 (RF-00071, RF-00088, dan NF-00092 berstatus To Be Returned seperti pada bagian Data)

### Ganti akun

22. Logout dari akun Total Control
23. Login sebagai Manage asset & TAG dengan Update di group Disposal Center (UP_DC)

### TC-FA-TAG-1110: Receive Manually tidak menulis Changelog

24. Catat baseline jumlah entri Changelog Paired TAG (N3) dan jumlah entri Event Log untuk RF-00071 (N4) lewat kemampuan baca
25. Buka Fixed Asset > TAG > To Be Returned
26. Buka menu aksi baris RF-00071
27. Klik "Receive Manually"
28. Isi Note dengan "Tag rusak saat serah terima"
29. Klik [Submit]
30. Klik "Event Log"
31. Verifikasi jumlah entri Event Log untuk RF-00071 bertambah satu dibanding baseline N4, dan entri barunya untuk RF-00071
32. Tutup Modal Event Log
33. Buka tab Paired
34. Klik "Changelog"
35. Verifikasi Modal "Changelog: Paired TAG" tetap memuat N3 entri tanpa entri baru

## Notes

- Spec absence (kelas g, S-05). Pemicu (Execute disposal, perubahan TAG Type, Receive Manually) bukan objek uji; `P-5` butir (a). Tiap TC punya baseline sendiri (langkah 1, 13, 24).
- Langkah penghubung (tanpa awalan `Verifikasi`): 2 sampai 7 (pemicu dan navigasi), 12, 20, 32 (menutup modal), 14 sampai 16 (pemicu dan navigasi), 21 (pemulihan state, S-09), 22 dan 23 (ganti akun), 25, 33 (navigasi). Langkah 4 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi ganti akun.
- Anchor positif absence (bagian 8b butir 2): langkah 8 dan 10 (TC-1240), langkah 17 (TC-1071), langkah 31 (TC-1110). Anchor pada langkah 10 (entri NF-00093) adalah tambahan di luar Expected TC (S-03); alasannya agar hasil kosong bukan karena Event Log belum dimuat.
- Asersi urutan: pada TC-FA-TAG-1071 Expected b (Non-standard naik) ditaruh sebelum Expected a (Changelog tetap) dan pada TC-FA-TAG-1110 Expected b (Event Log memuat entri baru) sebelum Expected a, supaya anchor positif mendahului absence.
- Spec ini berjalan setelah spec lain yang sudah menambah entri Event Log RF-00071 (audit trail permanen); karena itu asersi memakai selisih terhadap baseline N1, N2, N3, N4 (S-12).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri TAG Log Global dari penyelesaian disposal (Tag RF-00071 masuk To Be Returned) (langkah 3); entri Event Log To Be Returned (Method `Manual`) (langkah 29); entri TAG Log Global `Marked Damaged/Missing` (langkah 29). Penyelesaian Execute disposal AST-0900 (langkah 3) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain; jejak transaksi Disposal AST-0900 di modul Disposal tidak terpulihkan. Perubahan TAG Type Asset Name disimpan lewat `[Save]` di Settings > Asset Name (langkah 15) dan dipulihkan lewat fixture backend (langkah 21); penyimpanan itu mengirim notifikasi in-app `tag_replacement_needed` ke pemegang Update scope (efek yang tidak terpulihkan, langkah 15; PRD tag.md §9.7), dan PRD tag.md serta TC tidak menyatakan efek tak terpulihkan lain untuk penyimpanan atau pemulihan itu.
- Temuan untuk QA:
  - TC-FA-TAG-1240 menulis Expected absolut "Event Log tidak memuat entri untuk RF-00071"; Event Log adalah audit trail permanen yang dapat memuat entri RF-00071 dari TC lain, sehingga spec mengasersi tidak ada entri baru terhadap baseline.
  - TC-FA-TAG-1071 menyebut "6 entri sebelum perubahan" di data; spec tidak mengasersi angka absolut 6 (S-12).
  - TC-FA-TAG-1071 tidak menyebut cara memulihkan TAG Type sesudah uji; spec menambah langkah pemulihan 21. Langkah 21 juga menyetel Tag To Be Returned ke keadaan seed TC-FA-TAG-1110 (RF-00071, RF-00088, NF-00092 berstatus To Be Returned), bukan ke keadaan Paired pada AST-0900 di awal spec.
  - TC-FA-TAG-1240 tidak menyebut bahwa pelaku disposal Asset Admin (pelaku disposal) berbeda dengan pelaku TC-FA-TAG-1110 (UP_DC); spec memakai ganti akun eksplisit.
  - TC-FA-TAG-1110 Pre-setup "Modal Changelog berisi N entri" ditulis di precondition d; spec menaruh baseline di langkah 24.
