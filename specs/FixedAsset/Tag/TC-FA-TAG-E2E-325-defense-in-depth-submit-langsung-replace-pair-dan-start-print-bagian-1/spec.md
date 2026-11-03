---
id: TC-FA-TAG-E2E-325-defense-in-depth-submit-langsung-replace-pair-dan-start-print-bagian-1
title: "Defense-in-Depth: Submit Langsung Replace, Pair, dan Start Print Ditolak 403 untuk Role Tanpa Hak (Bagian 1)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1268
  - TC-FA-TAG-1269
  - TC-FA-TAG-1270
  - TC-FA-TAG-1271
  - TC-FA-TAG-1272
  - TC-FA-TAG-1273
  - TC-FA-TAG-1274
coverage:
  web: automated
---

# Defense-in-Depth: Submit Langsung Replace, Pair, dan Start Print Ditolak 403 untuk Role Tanpa Hak (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 2 | Manage asset & TAG (Read) | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |
| 3 | Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B | `manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: Read Only (blok 1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 3; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) pembacaan state data lewat fixture backend (status aset, status Tag, jumlah entri Changelog; baseline Changelog dicatat di hook `before`); (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Global. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired | `aset220` |
| Aset Plant B | 'Excavator 20 Ton - 11' (AST-0011, Group Plant B, TAG Type Asset Name RFID) dengan Tag RFID `RF-00101` Paired | `aset11` |
| Aset Pair | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset Pair Plant B | 'Excavator 20 Ton - 55' (AST-0055, Group Plant B, TAG Type RFID), Not Paired Yet | `aset55` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: tidak ada (semua request ditolak); hook `after` memastikan data di tabel di atas dalam keadaan awal dan sesi ke akun default suite.

## Test Steps

### Blok 1: Read Only (TC-FA-TAG-1268, TC-FA-TAG-1271, TC-FA-TAG-1273)

1. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00130` dengan Tag baru `RF-00412` pada aset AST-0220
2. Verifikasi respons 403
3. Verifikasi (lewat fixture BE) penggantian tidak diproses: Tag `RF-00130` tetap Paired pada AST-0220
4. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available
5. Verifikasi (lewat fixture BE) jumlah entri Changelog tidak bertambah dibanding baseline
6. Kirim request langsung ke server lewat klien HTTP: Submit Pair Tag `RF-00412` pada aset AST-0051
7. Verifikasi respons 403
8. Verifikasi (lewat fixture BE) pairing tidak diproses: AST-0051 tetap Not Paired Yet
9. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available
10. Kirim request langsung ke server lewat klien HTTP: Start Print dengan Quantity 2 dan Start position Left
11. Verifikasi respons 403
12. Verifikasi tidak ada pencetakan yang berjalan
13. Verifikasi (lewat fixture BE) tidak ada kode QR yang dibuat dan data cetak tidak tersimpan

### Blok 2: Manage asset & TAG (Read) (TC-FA-TAG-1269, TC-FA-TAG-1274)

14. Logout dari akun Read Only, lalu Login sebagai akun Manage asset & TAG (Read)
15. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00130` dengan Tag baru `RF-00412` pada aset AST-0220
16. Verifikasi respons 403
17. Verifikasi (lewat fixture BE) penggantian tidak diproses: Tag `RF-00130` tetap Paired pada AST-0220
18. Verifikasi (lewat fixture BE) jumlah entri Changelog tidak bertambah dibanding baseline
19. Kirim request langsung ke server lewat klien HTTP: Start Print dengan Quantity 2 dan Start position Left
20. Verifikasi respons 403
21. Verifikasi tidak ada pencetakan yang berjalan
22. Verifikasi (lewat fixture BE) tidak ada kode QR yang dibuat

### Blok 3: Update Plant A dan hanya Read Plant B (TC-FA-TAG-1270, TC-FA-TAG-1272)

23. Logout dari akun Manage asset & TAG (Read), lalu Login sebagai akun Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B
24. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00101` dengan Tag baru `RF-00412` pada aset AST-0011 (Group Plant B)
25. Verifikasi respons 403
26. Verifikasi (lewat fixture BE) penggantian tidak diproses: Tag `RF-00101` tetap Paired pada AST-0011
27. Verifikasi (lewat fixture BE) jumlah entri Changelog tidak bertambah dibanding baseline
28. Kirim request langsung ke server lewat klien HTTP: Submit Pair Tag `RF-00412` pada aset AST-0055 (Group Plant B)
29. Verifikasi respons 403
30. Verifikasi (lewat fixture BE) pairing tidak diproses: AST-0055 tetap Not Paired Yet
31. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1268 s.d. 1274). Tidak ada TC hanya-BE.
- K-1: TC defense-in-depth dengan Expected respons API tetap di spec FE+BE; semua langkah request langsung (1, 6, 10, 15, 19, 24, 28) hanya mengasersi respons server dan state data lewat fixture BE (bagian 8b butir 1). Halaman TAG tidak dibuka karena request tidak melewati browser.
- Pembagian TC lintas spec: TC-FA-TAG-1275 s.d. 1280 ada di spec 326 (submit langsung ditolak server untuk kondisi aset, stok, plan, dan Return Group).
- Urutan TC di dalam spec mengikuti akun aktor (satu ganti akun per blok), bukan urutan nomor TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14 dan 23 (ganti akun).
- Asersi "jumlah entri Changelog tidak bertambah" (langkah 5, 18, 27) ditulis di spec ini dengan baseline (S-12) dan didahului `Verifikasi` respons 403 serta state data sebagai anchor; spec absence kelas g milik modul ini tidak memuat TC-FA-TAG-1268, 1269, dan 1270.
- Temuan untuk QA:
  - TC-FA-TAG-1273 dan TC-FA-TAG-1274 tidak menyebut cara membaca "tidak ada pencetakan" selain lewat fixture BE; spec mengasersi lewat fixture BE.
  - Post Condition "Tidak ada perubahan data bisnis" pada TC-FA-TAG-1268 s.d. 1274 mengikuti Expected yang sudah diasersi; tidak ada asersi tambahan.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
