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
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) pembacaan state data lewat fixture backend (status Tag, status laporan, jumlah entri Event Log, TAG Log, dan Changelog; baseline dicatat di hook `before`); (3) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned dan laporan terbuka. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Aset berlaporan | AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal RF-00130 dan laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Note | Tag rusak saat serah terima | `noteReceiveManually` |
| Reason | Tag masih terbaca | `reasonDecline` |

- State yang diubah dan pemulihannya: langkah 28 menerima Tag `RF-00071` (status berubah dari To Be Returned); hook `after` memulihkan `RF-00071` ke To Be Returned dan entri terkait lewat fixture backend, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Blok 1: Read Only (TC-FA-TAG-1290, TC-FA-TAG-1294)

1. Kirim request commit Receive TAG untuk RF-00071 langsung ke server lewat klien HTTP memakai token pengguna Read Only
2. Verifikasi server membalas 403
3. Verifikasi (lewat fixture BE) Tag RF-00071 tetap To Be Returned
4. Verifikasi (lewat fixture BE) jumlah entri Event Log dan TAG Log RF-00071 tidak bertambah dibanding baseline
5. Kirim request commit Decline Report untuk RF-00130 dengan Reason "Tag masih terbaca" langsung ke server lewat klien HTTP memakai token pengguna Read Only
6. Verifikasi server membalas 403
7. Verifikasi (lewat fixture BE) laporan RF-00130 tetap terbuka
8. Verifikasi (lewat fixture BE) jumlah entri Changelog tidak bertambah dibanding baseline

### Blok 2: Update di group Disposal Center (TC-FA-TAG-1291, TC-FA-TAG-1293)

9. Logout dari akun Read Only, lalu Login sebagai akun Manage asset & TAG dengan Update di group Disposal Center
10. Kirim request commit Receive TAG untuk NF-00092 (Return Group HQ Warehouse) langsung ke server lewat klien HTTP memakai token pengguna
11. Verifikasi server membalas 403
12. Verifikasi (lewat fixture BE) Tag NF-00092 tetap To Be Returned
13. Verifikasi (lewat fixture BE) jumlah entri Event Log dan TAG Log NF-00092 tidak bertambah dibanding baseline
14. Kirim request commit Receive Manually untuk NF-00092 (HQ Warehouse) dengan Note "Tag rusak saat serah terima" langsung ke server lewat klien HTTP
15. Verifikasi server membalas 403
16. Verifikasi (lewat fixture BE) Tag NF-00092 tetap To Be Returned
17. Verifikasi (lewat fixture BE) jumlah entri Event Log dan TAG Log NF-00092 tidak bertambah dibanding baseline

### Blok 3: Manage asset & TAG (Read) (TC-FA-TAG-1292)

18. Logout dari akun blok 2, lalu Login sebagai akun Manage asset & TAG (Read)
19. Kirim request commit Receive Manually untuk RF-00071 dengan Note "Tag rusak saat serah terima" langsung ke server lewat klien HTTP memakai token pengguna
20. Verifikasi server membalas 403
21. Verifikasi (lewat fixture BE) Tag RF-00071 tetap To Be Returned
22. Verifikasi (lewat fixture BE) jumlah entri Event Log dan TAG Log RF-00071 tidak bertambah dibanding baseline

### Blok 4: Update Plant A dan Read Plant B (TC-FA-TAG-1295)

23. Logout dari akun Read, lalu Login sebagai akun Manage asset & TAG dengan Update di group Plant A dan Read di group Plant B
24. Kirim request commit Decline Report untuk RF-00130 (aset group Plant B) langsung ke server lewat klien HTTP memakai token pengguna
25. Verifikasi server membalas 403
26. Verifikasi (lewat fixture BE) laporan RF-00130 tetap terbuka

### Blok 5: Total Control (TC-FA-TAG-1306)

27. Logout dari akun blok 4, lalu Login sebagai akun Total Control
28. Kirim request commit Receive TAG untuk RF-00071 langsung ke server lewat klien HTTP sampai sukses
29. Verifikasi request pertama berhasil dan Tag RF-00071 tidak lagi To Be Returned
30. Kirim ulang request commit yang sama untuk RF-00071 lewat klien HTTP
31. Verifikasi request kedua ditolak karena Tag tidak lagi To Be Returned
32. Verifikasi (lewat fixture BE) hanya satu entri Event Log dan satu entri TAG Log "Received" untuk RF-00071

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1290 s.d. 1295, 1306). Tidak ada TC hanya-BE.
- K-1: TC defense-in-depth dengan Expected respons API tetap di spec FE+BE; semua langkah request langsung hanya mengasersi respons server dan state data lewat fixture BE (bagian 8b butir 1). Halaman TAG tidak dibuka karena request tidak melewati browser.
- Pembagian TC lintas spec: TC-FA-TAG-1309 dan TC-FA-TAG-1310 (Search dan Filter To Be Returned dengan scope group) ada di spec 330.
- Urutan TC di dalam spec mengikuti akun aktor (satu ganti akun per blok), dengan TC-FA-TAG-1306 di akhir karena request sukses mengubah status `RF-00071` menjadi tidak lagi To Be Returned.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9, 18, 23, dan 27 (ganti akun).
- Langkah 29 menambah `Verifikasi` bahwa request pertama berhasil; TC hanya menulis "sampai sukses". Asersi ini menjadi anchor positif bagi asersi hitungan entri pada langkah 32 dan dicatat di sini (S-03).
- Asersi "jumlah entri tidak bertambah" (langkah 4, 8, 13, 17, 22) ditulis di spec ini dengan baseline (S-12) dan didahului `Verifikasi` respons 403 serta status Tag atau laporan sebagai anchor; spec absence kelas g milik modul ini tidak memuat TC-FA-TAG-1290 s.d. 1295.
- Temuan untuk QA:
  - TC-FA-TAG-1293 Expected butir b ("tidak ada entri baru") tidak menyebut surface; spec memakai Event Log dan TAG Log seperti TC-FA-TAG-1291.
  - TC-FA-TAG-1295 menulis Expected tanpa butir "tidak ada entri baru"; spec hanya mengasersi respons 403 dan laporan tetap terbuka.
  - TC-FA-TAG-1306 Expected butir b ("satu entri TAG Log Received") membutuhkan pembacaan TAG Log lewat fixture BE; mekanisme pembacaan disediakan tim FE/BE.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
