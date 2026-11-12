---
id: TC-FA-TAG-E2E-354-absence-log-replace-pair-start-print-receive-dan-intake-bagian-2
title: "Absence Log: Pair TAG Gagal 5xx dan Receive TAG Tidak Menulis Changelog atau TAG Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1102
  - TC-FA-TAG-1106
coverage:
  web: automated
---

# Absence Log: Pair TAG Gagal 5xx dan Receive TAG Tidak Menulis Changelog atau TAG Log

## Prerequisites

- Mode: FE+BE (backend nyata; kegagalan 5xx dipaksa lewat `Spectra.intercept` parsial di atas backend nyata).
- Akun aktor:
  - Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
  - Manage asset & TAG dengan Update di group Disposal Center `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC, kode UP_DC), password `Spectra.env.FA_TAG_UP_DC_PASSWORD`. Dipakai pada langkah ganti akun (langkah 22 dan 23).
  - Nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); intercept jaringan (5xx pada Submit Pair); kemampuan baca jumlah entri Changelog Paired TAG, TAG Log Tag, dan Event Log tab To Be Returned sebelum aksi (baseline per TC, S-12, butir A-18); seed idempotent aset dan Tag lewat fixture backend.
- Data aset dan Tag (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0051 'Excavator 20 Ton - 51' (Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet); Tag RFID `RF-00412` berstatus Available. Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): lepas intercept, kembalikan aset AST-0051, stok Tag, dan Tag To Be Returned ke keadaan awal lewat fixture backend, lalu kembalikan sesi ke akun default suite.
- State global: tidak ada yang diubah selain data di atas dan efek yang tidak terpulihkan yang tercatat di bawah. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 29); entri TAG Log Global `Received` (langkah 29). Aksi tulis pada langkah 8 ditolak dan tidak menambah entri.

## Test Steps

### TC-FA-TAG-1102: Pair TAG gagal 5xx

1. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N1)
2. Catat baseline jumlah entri TAG Log Tag `RF-00412` lewat kemampuan baca (N2)
3. Tahan Submit Pair dengan respons 5xx lewat intercept
4. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
5. Klik `Show` di samping `Not Paired Yet`
6. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
8. Klik [Submit]
9. Verifikasi Toast "Error, failed to pair TAG."
10. Lepas intercept
11. Klik `✕` pada Dialog Pair TAG
12. Verifikasi dialog `Discard Pairing` dengan body "Discard this pairing? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
13. Klik [Discard]
14. Tutup Popup Detail
15. Klik tombol `Changelog` di toolbar tab Paired
16. Verifikasi Modal Changelog tampil dan memuat sedikitnya satu entri lain
17. Verifikasi Changelog tidak memuat entri `Pair TAG` untuk 'Excavator 20 Ton - 51' (jumlah entri sama dengan N1)
18. Tutup Modal Changelog
19. Buka Global Settings > TAG, klik aksi `TAG Log` pada Tag `RF-00412`
20. Verifikasi popup TAG Log `RF-00412` tampil
21. Verifikasi TAG Log `RF-00412` tidak memuat entri `Paired` (jumlah entri sama dengan N2)

### Ganti akun

22. Logout dari akun Total Control
23. Login sebagai Manage asset & TAG dengan Update di group Disposal Center (UP_DC)

### TC-FA-TAG-1106: Receive TAG tidak menulis Changelog

24. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N3)
25. Catat baseline jumlah entri Event Log tab To Be Returned untuk RF-00071 lewat kemampuan baca (N4)
26. Buka Fixed Asset > TAG > To Be Returned
27. Klik tombol "Receive TAG"
28. Pindai Tag RF-00071
29. Klik [Receive] sampai penerimaan RF-00071 selesai
30. Klik "Event Log"
31. Verifikasi Event Log tab To Be Returned memuat entri baru RF-00071 (jumlah entri Event Log untuk RF-00071 bertambah satu terhadap baseline N4)
32. Tutup Modal Event Log
33. Buka tab Paired
34. Klik "Changelog"
35. Verifikasi Modal "Changelog: Paired TAG" tetap memuat N3 entri tanpa entri baru untuk RF-00071

## Notes

- Spec absence (kelas g, S-05). Pemicu (kegagalan 5xx yang dipaksa, Receive TAG) bukan objek uji; `P-5` butir (a). Tiap TC punya baseline sendiri (langkah 1 dan 2, 24 dan 25).
- Langkah penghubung (tanpa awalan `Verifikasi`): 3 dan 10 (memasang dan melepas intercept, S-09), 11 sampai 14 (menutup form dirty secara deterministik, S-08), 18 (menutup modal), 19 (navigasi ke TAG Log), 22 dan 23 (ganti akun), 26, 32, 33 (navigasi).
- Anchor positif absence (bagian 8b butir 2): langkah 9 dan 16 (TC-1102 untuk Changelog), langkah 20 (TC-1102 untuk TAG Log), langkah 31 (TC-1106). Anchor "entri lain pada Changelog" dan "popup TAG Log tampil" adalah tambahan di luar Expected TC (S-03) supaya hasil kosong bukan karena surface belum dimuat.
- Asersi urutan: pada TC-FA-TAG-1106, Expected a (Event Log memuat entri baru) ditaruh sebelum Expected b (Changelog tanpa entri baru) agar menjadi anchor positif absence; urutan di TC terbalik.
- Total entri Changelog dan TAG Log tidak diasersi sebagai angka absolut (S-12); asersi memakai selisih terhadap N1, N2, N3, N4.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 29); entri TAG Log Global `Received` (langkah 29). Aksi tulis pada langkah 8 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - TC-FA-TAG-1102 menyebut Role Total Control sekaligus "Pelaku adalah pengguna login 'Budi S.'"; pengguna Budi S. tidak ada di Pre-setup. Spec memakai akun Total Control dan tidak membuat akun lain.
  - TC-FA-TAG-1102 tidak menyebut cara menutup Dialog Pair TAG setelah toast error; spec menutup lewat langkah 11 sampai 13.
  - TC-FA-TAG-1106 tidak menyebut Tag yang dipindai dan langkah penyelesaian Receive selain "sampai selesai"; spec memakai RF-00071 dan langkah 27 sampai 29.
  - TC-FA-TAG-1102 dan TC-FA-TAG-1106 menyebut "Tidak ada entri log baru" atau "N entri" sebagai Post Condition atau Pre-setup; hanya Expected yang diasersi.
