---
id: TC-FA-TAG-E2E-388-absence-log-request-langsung-replace-ditolak-tidak-menulis-changelog
title: "Absence Log: Request Langsung Replace yang Ditolak 403 Tidak Menulis Changelog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1262
  - TC-FA-TAG-1268
  - TC-FA-TAG-1269
  - TC-FA-TAG-1270
coverage:
  web: automated
---

# Absence Log: Request Langsung Replace yang Ditolak 403 Tidak Menulis Changelog

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
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) kemampuan baca jumlah entri Changelog Paired TAG sebelum dan sesudah request (baseline per TC, S-12, butir A-18); (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Global. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (pengecualian S-06/S-12 butir A-15; kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE; tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00330` Paired | `aset220` |
| Aset Plant B | 'Excavator 20 Ton - 11' (AST-0011, Group Plant B, TAG Type Asset Name RFID) dengan Tag RFID `RF-00101` Paired | `aset11` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available (dipakai sebagai precondition TC, tidak diasersi) | `stokAvailable` |

- State yang diubah dan pemulihannya: tidak ada (semua request ditolak); hook `after` memastikan data di tabel di atas dalam keadaan awal dan sesi ke akun default suite. Efek yang tidak terpulihkan: tidak ada entri baru yang dibuat spec ini; Changelog adalah audit trail permanen dan tidak dipulihkan fixture (butir A-18).

## Test Steps

### TC-FA-TAG-1262: Read Only, Replace TAG langsung untuk AST-0011

1. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N1)
2. Kirim permintaan Replace TAG untuk AST-0011 langsung ke server lewat klien HTTP (tanpa lewat UI)
3. Verifikasi server menolak dengan 403
4. Verifikasi jumlah entri Changelog Paired TAG tidak bertambah dibanding N1

### TC-FA-TAG-1268: Read Only, Submit Replace langsung pada AST-0220

5. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N2)
6. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00330` dengan Tag baru `RF-00412` pada aset AST-0220
7. Verifikasi respons 403
8. Verifikasi jumlah entri Changelog Paired TAG tidak bertambah dibanding N2

### Ganti akun

9. Logout dari akun Read Only, lalu Login sebagai akun Manage asset & TAG (Read)

### TC-FA-TAG-1269: Manage asset & TAG (Read), Submit Replace langsung pada AST-0220

10. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N3)
11. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00330` dengan Tag baru `RF-00412` pada aset AST-0220
12. Verifikasi respons 403
13. Verifikasi jumlah entri Changelog Paired TAG tidak bertambah dibanding N3

### Ganti akun

14. Logout dari akun Manage asset & TAG (Read), lalu Login sebagai akun Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B

### TC-FA-TAG-1270: Update Plant A dan hanya Read Plant B, Submit Replace langsung pada AST-0011

15. Catat baseline jumlah entri Changelog Paired TAG lewat kemampuan baca (N4)
16. Kirim request langsung ke server lewat klien HTTP: Submit penggantian Tag `RF-00101` dengan Tag baru `RF-00412` pada aset AST-0011 (Group Plant B)
17. Verifikasi respons 403
18. Verifikasi jumlah entri Changelog Paired TAG tidak bertambah dibanding N4

## Notes

- Spec absence (kelas g, S-05). Pemicu (request langsung ke server yang ditolak 403, kelas a) bukan objek uji; `P-5` butir (a). Tiap TC punya user dan baseline sendiri (langkah 1, 5, 10, 15); baseline dibaca ulang sebelum tiap pemicu karena aset yang sama dipakai TC lain di spec ini (AST-0220 pada TC-FA-TAG-1268 dan TC-FA-TAG-1269, AST-0011 pada TC-FA-TAG-1262 dan TC-FA-TAG-1270; butir A-18).
- Pembagian TC lintas spec (S-05): TC-FA-TAG-1262 ada juga di spec 323 dan TC-FA-TAG-1268, TC-FA-TAG-1269, dan TC-FA-TAG-1270 ada juga di spec 325, tempat respons 403 dan state data diasersi. Spec ini hanya memuat klausa "tidak ada entri Changelog baru" dengan request langsung sebagai pemicu.
- Urutan blok mengikuti akun aktor (satu ganti akun per blok), bukan urutan nomor TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 dan 14 (ganti akun). Langkah Catat baseline (1, 5, 10, 15) adalah aksi baca (S-12).
- Anchor positif absence (bagian 8b butir 2): langkah 3, 7, 12, dan 17 (`Verifikasi` respons 403 atas pemicu yang sama, butir Expected TC) mendahului tiap asersi jumlah entri pada langkah 4, 8, 13, dan 18; jumlah awal yang dicatat (N1 sampai N4) adalah pembanding pada surface Changelog yang sama.
- Total entri Changelog tidak diasersi sebagai angka absolut (S-12); semua asersi jumlah memakai selisih terhadap baseline N1 sampai N4.
- Butir A-15: nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; seeding idempotent dan pemulihan lewat fixture backend (suite serial).
- Temuan untuk QA:
  - TC-FA-TAG-1262 Expected b ("tidak ada perubahan data dan tidak ada log") tidak menyebut surface log; spec memakai Changelog Paired TAG seperti TC-FA-TAG-1268. TC-FA-TAG-1262 juga tidak menyebut Tag lama dan baru untuk request Replace; asersi hanya pada status 403 dan jumlah entri Changelog.
  - TC-FA-TAG-1268 sampai TC-FA-TAG-1270 menulis klausa "Tidak ada entri Changelog baru" sebagai Post Condition; langkah observasinya adalah "Periksa state data lewat fixture BE", sehingga spec membacanya lewat kemampuan baca jumlah entri Changelog.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
