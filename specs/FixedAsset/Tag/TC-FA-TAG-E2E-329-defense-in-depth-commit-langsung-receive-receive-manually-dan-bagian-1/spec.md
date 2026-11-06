---
id: TC-FA-TAG-E2E-329-defense-in-depth-commit-langsung-receive-receive-manually-dan-bagian-1
title: "Defense-in-Depth: Commit Langsung Receive TAG, Receive Manually, dan Decline Report Ditolak Server (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1290
  - TC-FA-TAG-1291
  - TC-FA-TAG-1292
  - TC-FA-TAG-1293
  - TC-FA-TAG-1294
  - TC-FA-TAG-1295
  - TC-FA-TAG-1306
coverage:
  web: automated
---

# Defense-in-Depth: Commit Langsung Receive TAG, Receive Manually, dan Decline Report Ditolak Server (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 2 | Manage asset & TAG dengan Update di group Disposal Center | `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_DC_PASSWORD` |
| 3 | Manage asset & TAG (Read) | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |
| 4 | Manage asset & TAG dengan Update di group Plant A dan Read di group Plant B | `manageAssetTagDenganUpdateDiGroupPlantADanReadDiGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_RPB_PASSWORD` |
| 5 | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: Read Only (blok 1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 5; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) pembacaan state data lewat fixture backend (status Tag, status laporan, serta jumlah entri Event Log dan TAG Log RF-00071; baseline dicatat di hook `before` dan dibaca ulang pada langkah 23 sebelum pemicu sukses; Event Log dan TAG Log permanen, dan asersi entri baru memakai selisih terhadap baseline: butir A-18); (3) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned dan laporan terbuka. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal RF-00130 dan laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Note | Tag rusak saat serah terima | `noteReceiveManually` |
| Reason | Tag masih terbaca | `reasonDecline` |

- State yang diubah dan pemulihannya: langkah 24 menerima Tag `RF-00071` (status berubah dari To Be Returned); hook `after` memulihkan `RF-00071` ke To Be Returned dan entri terkait lewat fixture backend, dan mengembalikan sesi ke akun default suite.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 24); entri TAG Log Global `Received` (langkah 24). Aksi tulis pada langkah 1, 4, 8, 11, 15, 19 ditolak dan tidak menambah entri.

## Test Steps

### Blok 1: Read Only (TC-FA-TAG-1290, TC-FA-TAG-1294)

1. Kirim request commit Receive TAG untuk RF-00071 langsung ke server lewat klien HTTP memakai token pengguna Read Only
2. Verifikasi server membalas 403
3. Verifikasi (lewat fixture BE) Tag RF-00071 tetap To Be Returned
4. Kirim request commit Decline Report untuk RF-00130 dengan Reason "Tag masih terbaca" langsung ke server lewat klien HTTP memakai token pengguna Read Only
5. Verifikasi server membalas 403
6. Verifikasi (lewat fixture BE) laporan RF-00130 tetap terbuka

### Blok 2: Update di group Disposal Center (TC-FA-TAG-1291, TC-FA-TAG-1293)

7. Logout dari akun Read Only, lalu Login sebagai akun Manage asset & TAG dengan Update di group Disposal Center
8. Kirim request commit Receive TAG untuk NF-00092 (Return Group HQ Warehouse) langsung ke server lewat klien HTTP memakai token pengguna
9. Verifikasi server membalas 403
10. Verifikasi (lewat fixture BE) Tag NF-00092 tetap To Be Returned
11. Kirim request commit Receive Manually untuk NF-00092 (HQ Warehouse) dengan Note "Tag rusak saat serah terima" langsung ke server lewat klien HTTP
12. Verifikasi server membalas 403
13. Verifikasi (lewat fixture BE) Tag NF-00092 tetap To Be Returned

### Blok 3: Manage asset & TAG (Read) (TC-FA-TAG-1292)

14. Logout dari akun blok 2, lalu Login sebagai akun Manage asset & TAG (Read)
15. Kirim request commit Receive Manually untuk RF-00071 dengan Note "Tag rusak saat serah terima" langsung ke server lewat klien HTTP memakai token pengguna
16. Verifikasi server membalas 403
17. Verifikasi (lewat fixture BE) Tag RF-00071 tetap To Be Returned

### Blok 4: Update Plant A dan Read Plant B (TC-FA-TAG-1295)

18. Logout dari akun Read, lalu Login sebagai akun Manage asset & TAG dengan Update di group Plant A dan Read di group Plant B
19. Kirim request commit Decline Report untuk RF-00130 (aset group Plant B) langsung ke server lewat klien HTTP memakai token pengguna
20. Verifikasi server membalas 403
21. Verifikasi (lewat fixture BE) laporan RF-00130 tetap terbuka

### Blok 5: Total Control (TC-FA-TAG-1306)

22. Logout dari akun blok 4, lalu Login sebagai akun Total Control
23. Catat jumlah entri Event Log To Be Returned dan jumlah entri TAG Log `Received` untuk RF-00071 sebagai baseline per surface (dibaca lewat fixture BE)
24. Kirim request commit Receive TAG untuk RF-00071 langsung ke server lewat klien HTTP sampai sukses
25. Verifikasi request pertama berhasil dan Tag RF-00071 tidak lagi To Be Returned
26. Kirim ulang request commit yang sama untuk RF-00071 lewat klien HTTP
27. Verifikasi request kedua ditolak karena Tag tidak lagi To Be Returned
28. Verifikasi (lewat fixture BE) entri Event Log dan entri TAG Log "Received" untuk RF-00071 masing-masing bertambah tepat satu (selisih +1 per surface terhadap baseline langkah 23)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1290 s.d. 1295, 1306). Tidak ada TC hanya-BE.
- K-1: TC defense-in-depth dengan Expected respons API tetap di spec FE+BE; semua langkah request langsung hanya mengasersi respons server dan state data lewat fixture BE (bagian 8b butir 1). Halaman TAG tidak dibuka karena request tidak melewati browser.
- Pembagian TC lintas spec: TC-FA-TAG-1309 dan TC-FA-TAG-1310 (Search dan Filter To Be Returned dengan scope group) ada di spec 330.
- Urutan TC di dalam spec mengikuti akun aktor (satu ganti akun per blok), dengan TC-FA-TAG-1306 di akhir karena request sukses mengubah status `RF-00071` menjadi tidak lagi To Be Returned.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7, 14, 18, 22 (ganti akun), dan 23 (Catat jumlah baseline, butir A-18).
- Langkah 25 menambah `Verifikasi` bahwa request pertama berhasil; TC hanya menulis "sampai sukses". Asersi ini menjadi anchor positif bagi asersi hitungan entri pada langkah 28 dan dicatat di sini (S-03).
- Pembagian TC lintas spec (S-05): klausa "tidak ada entri baru" TC-FA-TAG-1290, TC-FA-TAG-1291, TC-FA-TAG-1292, dan TC-FA-TAG-1293 (Event Log dan TAG Log) serta TC-FA-TAG-1294 (Changelog) diasersi di spec 389 (absence kelas g), dengan request langsung sebagai pemicu dan baseline sendiri; spec ini mengasersi respons 403 serta status Tag atau laporan lewat fixture BE. TC-FA-TAG-1290, TC-FA-TAG-1291, TC-FA-TAG-1292, TC-FA-TAG-1293, dan TC-FA-TAG-1294 tetap di `sourceTc` kedua spec.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Scan`) (langkah 24); entri TAG Log Global `Received` (langkah 24). Aksi tulis pada langkah 1, 4, 8, 11, 15, 19 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - TC-FA-TAG-1295 menulis Expected tanpa butir "tidak ada entri baru"; spec hanya mengasersi respons 403 dan laporan tetap terbuka.
  - TC-FA-TAG-1306 Expected butir b ("satu entri TAG Log Received") membutuhkan pembacaan TAG Log lewat fixture BE; mekanisme pembacaan disediakan tim FE/BE.
  - TC-FA-TAG-1306 Expected butir b menyebut "satu entri Event Log dan satu entri TAG Log Received" untuk RF-00071 secara absolut, sedangkan Event Log dan TAG Log permanen dan tidak dipulihkan fixture (butir A-18); spec mengasersi selisih tepat +1 per surface terhadap baseline langkah 23, bukan jumlah absolut.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
