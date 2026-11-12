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
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) pembacaan state data lewat fixture backend (status aset dan status Tag); (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Global. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired | `aset220` |
| Aset Plant B | 'Excavator 20 Ton - 11' (AST-0011, Group Plant B, TAG Type Asset Name RFID) dengan Tag RFID `RF-00101` Paired | `aset11` |
| Aset Pair | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset Pair Plant B | 'Excavator 20 Ton - 55' (AST-0055, Group Plant B, TAG Type RFID), Not Paired Yet | `aset55` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: tidak ada (semua request ditolak); hook `after` memastikan data di tabel di atas dalam keadaan awal dan sesi ke akun default suite.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 1, 5, 9, 14, 17, 22, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.

## Test Steps

### Blok 1: Read Only (TC-FA-TAG-1268, TC-FA-TAG-1271, TC-FA-TAG-1273)

1. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00330` dengan Tag baru `RF-00412` pada aset AST-0220
2. Verifikasi respons 403
3. Verifikasi (lewat fixture BE) penggantian tidak diproses: Tag `RF-00330` tetap Paired pada AST-0220
4. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available
5. Kirim request langsung ke server lewat klien HTTP: Submit Pair Tag `RF-00412` pada aset AST-0051
6. Verifikasi respons 403
7. Verifikasi (lewat fixture BE) pairing tidak diproses: AST-0051 tetap Not Paired Yet
8. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available
9. Kirim request langsung ke server lewat klien HTTP: Start Print dengan Quantity 2 dan Start position Left
10. Verifikasi respons 403
11. Verifikasi tidak ada pencetakan yang berjalan
12. Verifikasi (lewat fixture BE) tidak ada kode QR yang dibuat dan data cetak tidak tersimpan

### Blok 2: Manage asset & TAG (Read) (TC-FA-TAG-1269, TC-FA-TAG-1274)

13. Logout dari akun Read Only, lalu Login sebagai akun Manage asset & TAG (Read)
14. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00330` dengan Tag baru `RF-00412` pada aset AST-0220
15. Verifikasi respons 403
16. Verifikasi (lewat fixture BE) penggantian tidak diproses: Tag `RF-00330` tetap Paired pada AST-0220
17. Kirim request langsung ke server lewat klien HTTP: Start Print dengan Quantity 2 dan Start position Left
18. Verifikasi respons 403
19. Verifikasi tidak ada pencetakan yang berjalan
20. Verifikasi (lewat fixture BE) tidak ada kode QR yang dibuat

### Blok 3: Update Plant A dan hanya Read Plant B (TC-FA-TAG-1270, TC-FA-TAG-1272)

21. Logout dari akun Manage asset & TAG (Read), lalu Login sebagai akun Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B
22. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00101` dengan Tag baru `RF-00412` pada aset AST-0011 (Group Plant B)
23. Verifikasi respons 403
24. Verifikasi (lewat fixture BE) penggantian tidak diproses: Tag `RF-00101` tetap Paired pada AST-0011
25. Kirim request langsung ke server lewat klien HTTP: Submit Pair Tag `RF-00412` pada aset AST-0055 (Group Plant B)
26. Verifikasi respons 403
27. Verifikasi (lewat fixture BE) pairing tidak diproses: AST-0055 tetap Not Paired Yet
28. Verifikasi (lewat fixture BE) Tag `RF-00412` tetap Available

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1268 s.d. 1274). Tidak ada TC hanya-BE.
- K-1: TC defense-in-depth dengan Expected respons API tetap di spec FE+BE; semua langkah request langsung (1, 5, 9, 14, 17, 22, 25) hanya mengasersi respons server dan state data lewat fixture BE (bagian 8b butir 1). Halaman TAG tidak dibuka karena request tidak melewati browser.
- Pembagian TC lintas spec: TC-FA-TAG-1275 s.d. 1280 ada di spec 326 (submit langsung ditolak server untuk kondisi aset, stok, plan, dan Return Group).
- Urutan TC di dalam spec mengikuti akun aktor (satu ganti akun per blok), bukan urutan nomor TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 13 dan 21 (ganti akun).
- Pembagian TC lintas spec (S-05): klausa "tidak ada entri Changelog baru" TC-FA-TAG-1268, TC-FA-TAG-1269, dan TC-FA-TAG-1270 diasersi di spec 388 (absence kelas g) dengan request langsung sebagai pemicu dan baseline sendiri; spec ini mengasersi respons 403 dan state data lewat fixture BE. TC-FA-TAG-1268, TC-FA-TAG-1269, dan TC-FA-TAG-1270 tetap di `sourceTc` kedua spec.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 1, 5, 9, 14, 17, 22, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.
- Temuan untuk QA:
  - TC-FA-TAG-1273 dan TC-FA-TAG-1274 tidak menyebut cara membaca "tidak ada pencetakan" selain lewat fixture BE; spec mengasersi lewat fixture BE.
  - Post Condition "Tidak ada perubahan data bisnis" pada TC-FA-TAG-1268 s.d. 1274 mengikuti Expected yang sudah diasersi; tidak ada asersi tambahan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
