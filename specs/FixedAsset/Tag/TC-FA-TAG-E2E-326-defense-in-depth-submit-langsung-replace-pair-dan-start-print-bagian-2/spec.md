---
id: TC-FA-TAG-E2E-326-defense-in-depth-submit-langsung-replace-pair-dan-start-print-bagian-2
title: "Defense-in-Depth: Submit Langsung Replace dan Pair Ditolak Server karena Kondisi Aset, Stok, Status Tag, Plan, dan Return Group (Bagian 2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1275
  - TC-FA-TAG-1276
  - TC-FA-TAG-1277
  - TC-FA-TAG-1278
  - TC-FA-TAG-1279
  - TC-FA-TAG-1280
coverage:
  web: automated
---

# Defense-in-Depth: Submit Langsung Replace dan Pair Ditolak Server karena Kondisi Aset, Stok, Status Tag, Plan, dan Return Group (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B | `manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: Total Control (blok 1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 2; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) pembacaan state data lewat fixture backend (status aset dan status Tag); (3) seed dan pemulihan idempotent lewat fixture backend untuk aset (termasuk Asset Status In Disposal Process dan Disposed), Tag per status registri (Available, Reserved, Paired, To be Returned dengan Return Group), dan stok per tipe di registri Global; (4) perubahan plan Client lewat fixture backend (kemampuan ganti plan Client disediakan tim FE/BE; akun pelaku disediakan tim FE). Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset In Disposal Process | 'Excavator 20 Ton - 22' (AST-0022, Group Plant A, Asset Status In Disposal Process) dengan Tag RFID `RF-00142` Paired | `aset22` |
| Aset Disposed | 'Excavator 20 Ton - 56' (AST-0056, Group Plant A, TAG Type RFID, Asset Status Disposed), Not Paired Yet | `aset56` |
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired | `aset220` |
| Aset NFC | 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type NFC dan QR) dengan Tag NFC `NF-00092` Paired | `aset108` |
| Aset Pair | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Stok Available | Tag RFID `RF-00412`, Tag NFC `NF-00500` | `stokAvailable` |
| Tag Reserved | Tag RFID `RF-00601` berstatus Reserved | `tagReserved601` |
| Tag To be Returned Plant B | Tag RFID `RF-00072` To be Returned, Return Group 'Plant B' yang hanya dipegang Read oleh user blok 2 | `tbr72` |

- State yang diubah dan pemulihannya: stok Global (tidak ada Tag RFID Available) diatur di langkah 9 dan dipulihkan di langkah 18; plan Client yang mengunci Tag NFC diatur di langkah 18 dan dipulihkan di langkah 23. Hook `after` memulihkan stok per tipe, plan Client, dan status Tag ke keadaan awal walau spec gagal di tengah, serta mengembalikan sesi ke akun default suite.

## Test Steps

### Blok 1: Total Control (TC-FA-TAG-1275, TC-FA-TAG-1276, TC-FA-TAG-1277, TC-FA-TAG-1278, TC-FA-TAG-1279)

1. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00142` dengan Tag baru `RF-00412` pada aset AST-0022 (Asset Status In Disposal Process)
2. Verifikasi server menolak penggantian
3. Verifikasi (lewat fixture BE) Tag `RF-00142` tetap Paired pada AST-0022
4. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available
5. Kirim request langsung ke server lewat klien HTTP: Submit Pair Tag `RF-00412` pada aset AST-0056 (Asset Status Disposed)
6. Verifikasi server menolak pairing
7. Verifikasi (lewat fixture BE) AST-0056 tetap Not Paired Yet
8. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available
9. Atur stok Global lewat fixture BE hingga tidak ada Tag RFID berstatus Available dan `RF-00601` berstatus Reserved
10. Kirim request langsung ke server lewat klien HTTP: Submit Pair Tag `RF-00601` pada aset AST-0051
11. Verifikasi server menolak pairing
12. Verifikasi (lewat fixture BE) AST-0051 tetap Not Paired Yet
13. Verifikasi (lewat fixture BE) `RF-00601` tetap Reserved
14. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00130` dengan Tag baru `RF-00601` pada aset AST-0220
15. Verifikasi server menolak penggantian
16. Verifikasi (lewat fixture BE) Tag `RF-00130` tetap Paired pada AST-0220
17. Verifikasi (lewat fixture BE) `RF-00601` tetap Reserved
18. Atur plan Client lewat fixture BE ke plan yang mengunci Tag NFC, dan pulihkan stok Global (Tag RFID `RF-00412` Available)
19. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `NF-00092` dengan Tag baru NFC `NF-00500` pada aset AST-0108
20. Verifikasi server menolak penggantian
21. Verifikasi (lewat fixture BE) Tag `NF-00092` tetap Paired
22. Verifikasi (lewat fixture BE) `NF-00500` tetap Available
23. Pulihkan plan Client ke plan awal lewat fixture BE

### Blok 2: Update Plant A dan hanya Read Plant B (TC-FA-TAG-1280)

24. Logout dari akun Total Control, lalu Login sebagai akun Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B
25. Kirim request langsung ke server lewat klien HTTP: Submit Pair Tag `RF-00072` pada aset AST-0051
26. Verifikasi server menolak pairing
27. Verifikasi (lewat fixture BE) `RF-00072` tetap To be Returned
28. Verifikasi (lewat fixture BE) AST-0051 tetap Not Paired Yet

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1275 s.d. 1280). Tidak ada TC hanya-BE.
- K-1: TC defense-in-depth dengan Expected respons API tetap di spec FE+BE; semua langkah request langsung hanya mengasersi respons server dan state data lewat fixture BE (bagian 8b butir 1). Halaman TAG tidak dibuka karena request tidak melewati browser.
- Pembagian TC lintas spec: TC-FA-TAG-1268 s.d. 1274 ada di spec 325 (request langsung ditolak 403 untuk role tanpa hak).
- Urutan TC di dalam spec: TC-1275, TC-1276, TC-1277, TC-1278, TC-1279 (akun Total Control), lalu TC-1280 di akun lain. TC-1277 sesudah TC-1275 dan TC-1276 karena TC-1275 dan TC-1276 memakai Tag `RF-00412` Available sedangkan TC-1277 mensyaratkan tidak ada Tag RFID Available di stok Global.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 dan 18 (mengatur stok dan plan lewat fixture BE sebagai precondition TC-1277 dan TC-1279), 23 (memulihkan plan), 24 (ganti akun).
- Temuan untuk QA:
  - TC-FA-TAG-1277 menyebut `RF-00601` Reserved dan tidak ada Tag RFID Available; spec mengatur stok lewat fixture BE (kemampuan ganti stok Global disediakan tim FE/BE).
  - TC-FA-TAG-1279 mensyaratkan "plan yang mengunci Tag NFC" tanpa menyebut nama plan; spec memakai fixture ganti plan Client yang disediakan tim FE/BE.
  - Post Condition "Tidak ada perubahan data bisnis" mengikuti Expected yang sudah diasersi; tidak ada asersi tambahan.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
