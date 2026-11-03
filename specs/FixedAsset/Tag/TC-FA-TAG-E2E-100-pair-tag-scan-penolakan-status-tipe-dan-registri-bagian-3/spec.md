---
id: TC-FA-TAG-E2E-100-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-3
title: "Pair TAG: Tag Tidak Berlaku, Konflik D-03, dan Tag To be Returned menurut Return Group (Bagian 3)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-430
  - TC-FA-TAG-431
  - TC-FA-TAG-432
  - TC-FA-TAG-433
  - TC-FA-TAG-434
coverage:
  web: automated
---

# Pair TAG: Tag Tidak Berlaku, Konflik D-03, dan Tag To be Returned menurut Return Group (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B | `manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD` |
| 3 | Manage asset & TAG (Read + Update) dengan Update pada Group Plant A | `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_UPA_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: Total Control (blok 1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 3; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Sesi API aktor: pelaku kedua pada TC-FA-TAG-434 (pengguna lain yang memasangkan Tag `RF-00412` ke aset lain) memakai login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya; akun pelaku disediakan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet, Tag per status registri (Available, To be Returned dengan Return Group), Tag yang tidak berlaku di client, dan Event Log To Be Returned; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset target | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Tag tidak berlaku | Tag RFID `RF-00605` terdaftar tetapi tidak berlaku di client ini | `tagTidakBerlaku605` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |
| TBR Return Group berhak Update | Tag RFID `RF-00071` To be Returned, Return Group 'Disposal Center' yang dipegang Update oleh user | `tbr71` |
| TBR Return Group hanya Read | Tag RFID `RF-00072` To be Returned, Return Group 'Plant B' yang hanya dipegang Read oleh user blok 2 | `tbr72` |
| TBR Return Group di luar scope | Tag RFID `RF-00073` To be Returned, Return Group 'Plant C' di luar scope user blok 3 | `tbr73` |

- State yang diubah dan pemulihannya: aset 51 dipasangkan `RF-00071` (blok 1) dan dipulihkan lewat fixture sebelum blok 2; `RF-00412` dipasangkan ke aset lain oleh pelaku kedua; hook `after` memulihkan aset 51 ke Not Paired Yet, `RF-00071`, `RF-00072`, `RF-00073` ke To be Returned dengan Return Group semula, `RF-00412` ke Available, dan sesi ke akun default suite.

## Test Steps

### Blok 1: Total Control (TC-FA-TAG-430, TC-FA-TAG-434, TC-FA-TAG-431)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00605`
5. Verifikasi error inline "Error, TAG isn't authorized. Please contact Admin."
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
7. Pelaku kedua lewat sesi API memasangkan Tag `RF-00412` ke aset lain hingga tersimpan
8. Klik [Submit]
9. Verifikasi dialog judul "Cannot Pair TAG", body "RF-00412 is no longer available. Scan another TAG.", tombol [OK]
10. Klik [OK] pada dialog
11. Verifikasi dialog Pair TAG kembali ke slot `RFID TAG` dalam keadaan `Not scanned`
12. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00071`
13. Verifikasi slot `RFID TAG` menerima `RF-00071` dengan badge `Verified`
14. Klik [Submit]
15. Verifikasi toast "Success, TAG has been paired."

### Blok 2: Update Plant A dan hanya Read Plant B (TC-FA-TAG-432)

16. Pulihkan 'Excavator 20 Ton - 51' ke Not Paired Yet dan atur Tag `RF-00072` To be Returned dengan Return Group 'Plant B' lewat fixture backend hingga tersimpan, lalu Logout dari akun Total Control
17. Login sebagai akun Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B
18. Buka Fixed Asset > TAG > Paired
19. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
20. Klik tombol teks `Show` di samping field `Not Paired Yet`
21. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
22. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00072`
23. Verifikasi error inline "RF-00072 is not available (To be Returned)."
24. Klik [Cancel]
25. Tutup Popup Detail, lalu Logout dari akun blok 2

### Blok 3: Update Plant A (TC-FA-TAG-433)

26. Login sebagai akun Manage asset & TAG (Read + Update) dengan Update pada Group Plant A
27. Buka Fixed Asset > TAG > Paired
28. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
29. Klik tombol teks `Show` di samping field `Not Paired Yet`
30. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
31. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00073`
32. Verifikasi error inline "RF-00073 is not available (To be Returned)."
33. Klik [Cancel]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-430 s.d. 434). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik penolakan scan Pair TAG ada di spec 098 (TC-FA-TAG-419 s.d. 423), spec 099 (TC-FA-TAG-424, 426 s.d. 429), dan spec 101 (TC-FA-TAG-1453, 1454, 1462). TC-FA-TAG-425 ada di spec kelas defense-in-depth tersendiri.
- Urutan TC di dalam spec: TC-430, TC-434, TC-431, TC-432, TC-433, sehingga seluruh TC akun Total Control berurutan sebelum ganti akun (bagian 3 butir "Step ganti akun eksplisit") dan TC-431 yang menyimpan perubahan ada di akhir blok 1. Blok 1 satu dialog: TC-430 dan TC-434 ditolak tanpa menyimpan, slot kembali `Not scanned` sebelum TC-431. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (keputusan ganti akun eksplisit, 2026-10-21).
- Pelaku kedua memakai sesi API (keputusan 2026-10-21/30): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 7).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 16 (memulihkan data lewat fixture backend hingga tersimpan dan Logout), 18 dan 27 (membuka halaman sesudah login akun lain), 24 dan 33 (menutup dialog tanpa isian dengan [Cancel], tanpa konfirmasi D-11), serta 25 (menutup popup dan Logout).
- Temuan untuk QA:
  - TC-FA-TAG-434 menulis "dipasangkan ke aset lain oleh pengguna lain setelah dialog dibuka" tanpa urutan terhadap pindaian; spec memindai `RF-00412` dulu, lalu pelaku kedua memasangkannya, lalu [Submit] (konsisten dengan TC-FA-TAG-408). TC juga tidak menyebut aset tujuan dan akun pelaku.
  - Tabel Pre-setup TC memuat dua akun yang hampir kembar ("Update di group Plant A dan Read di group Plant B" dan "Update pada Group Plant A dan hanya Read pada Group Plant B"); TC-432 memakai nama kedua dan spec mengikutinya.
  - Post Condition TC-431 butir b dan c ("Tag `RF-00071` hilang dari tab To Be Returned", "Event Log To Be Returned memuat satu entri `RF-00071` Method `Assigned` Final Status `Paired`") dan Post Condition TC-432, TC-433, TC-434 tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
