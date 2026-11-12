---
id: TC-FA-TAG-E2E-323-defense-in-depth-akses-data-tab-paired-dan-isolasi-client
title: "Defense-in-Depth: Akses Data Tab Paired Ditolak Server, Isolasi Client, dan Tombol Hidden Bukan Pengganti Pemeriksaan Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-142
  - TC-FA-TAG-1262
  - TC-FA-TAG-1263
  - TC-FA-TAG-1264
  - TC-FA-TAG-1265
  - TC-FA-TAG-1266
  - TC-FA-TAG-1267
coverage:
  web: automated
---

# Defense-in-Depth: Akses Data Tab Paired Ditolak Server, Isolasi Client, dan Tombol Hidden Bukan Pengganti Pemeriksaan Server

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) (Update: Plant A) | `manageAssetTagReadUpdateUpdatePlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PA_PASSWORD` |
| 2 | Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 3 | Manage asset & TAG (Read) | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |
| 4 | Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B | `manageAssetTagDenganUpdatePadaGroupPlantADanHanyaReadPadaGroupPlantB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_UP_PA_ROPB_PASSWORD` |
| 5 | Role lain (tanpa akses menu TAG) | `roleLainTanpaAksesMenuTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_NOMENU_PASSWORD` |
| 6 | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: blok 1. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 6; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) klien HTTP untuk request langsung ke server memakai sesi akun yang sedang login (tanpa lewat browser); (2) pembacaan state data lewat fixture backend (status aset dan Tag); (3) manipulasi DOM untuk mengaktifkan tombol yang Hidden; (4) seed dan pemulihan idempotent lewat fixture backend, termasuk satu client lain yang memiliki grup 'Excavator 20 Ton' dengan Tag `RF-09999`. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |
| Aset Plant B | 'Excavator 20 Ton - 11' (AST-0011, Group Plant B) | `aset11` |
| Aset Not Paired Yet | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja) | `aset51` |
| Tag milik client lain | Tag `RF-09999` pada grup 'Excavator 20 Ton' di client lain | `tagClientLain` |

- State yang diubah dan pemulihannya: spec tidak mengubah data (semua request ditolak); hook `after` memastikan AST-0011 dan AST-0051 dalam keadaan awal dan sesi ke akun default suite.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 10 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.

## Test Steps

### Blok 1: Update Plant A (TC-FA-TAG-142)

1. Kirim request pengambilan detail grup 'Excavator 20 Ton' / Plant B langsung ke server lewat klien HTTP (tanpa lewat UI)
2. Verifikasi server menolak permintaan dengan 403
3. Verifikasi tidak ada data aset Plant B dikembalikan pada respons

### Blok 2: Read Only (TC-FA-TAG-1262, TC-FA-TAG-1267)

4. Logout dari akun blok 1, lalu Login sebagai akun Read Only
5. Kirim permintaan Replace TAG untuk AST-0011 langsung ke server lewat klien HTTP (tanpa lewat UI)
6. Verifikasi server menolak dengan 403
7. Verifikasi (lewat fixture BE) data AST-0011 tidak berubah
8. Buka Fixed Asset > TAG > Paired
9. Aktifkan tombol `Print QR` yang Hidden lewat manipulasi DOM, lalu klik tombol itu
10. Isi `Quantity` dengan 1 pada Dialog Print QR lalu klik [Start Print]
11. Verifikasi server menolak request `Start Print` dengan status 403
12. Verifikasi (lewat fixture BE) tidak ada data cetak tersimpan

### Blok 3: Manage asset & TAG (Read) (TC-FA-TAG-1263)

13. Logout dari akun Read Only, lalu Login sebagai akun Manage asset & TAG (Read)
14. Kirim permintaan Pair TAG untuk AST-0051 langsung ke server lewat klien HTTP (tanpa lewat UI)
15. Verifikasi server menolak dengan 403
16. Verifikasi (lewat fixture BE) AST-0051 tetap Not Paired Yet dan tidak ada perubahan data

### Blok 4: Update Plant A, Read Plant B (TC-FA-TAG-1264)

17. Logout dari akun blok 3, lalu Login sebagai akun Manage asset & TAG dengan Update pada Group Plant A dan hanya Read pada Group Plant B
18. Kirim permintaan Replace TAG untuk AST-0011 (Plant B) langsung ke server lewat klien HTTP (tanpa lewat UI)
19. Verifikasi server menolak dengan 403 karena group tidak dipegang Update
20. Verifikasi (lewat fixture BE) data AST-0011 tidak berubah

### Blok 5: Role lain tanpa akses menu TAG (TC-FA-TAG-1265)

21. Logout dari akun blok 4, lalu Login sebagai akun Role lain (tanpa akses menu TAG)
22. Panggil pengambilan data tab Paired langsung ke server lewat klien HTTP
23. Panggil pengambilan data tab To Be Returned langsung ke server lewat klien HTTP
24. Verifikasi server menolak kedua permintaan
25. Verifikasi tidak ada data Tag dikembalikan pada kedua respons

### Blok 6: Total Control (TC-FA-TAG-1266)

26. Logout dari akun blok 5, lalu Login sebagai akun Total Control
27. Buka Fixed Asset > TAG > Paired
28. Klik ikon Search, ketik Search `RF-09999`, tekan Enter
29. Verifikasi `No results found` tampil
30. Verifikasi data grup dan Tag client lain tidak muncul
31. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-142, 1262 s.d. 1267). Tidak ada TC hanya-BE.
- K-1: TC defense-in-depth dengan Expected respons API tetap di spec FE+BE; blok request langsung (langkah 1 s.d. 3, 5 s.d. 7, 14 s.d. 16, 18 s.d. 20, 22 s.d. 25) hanya mengasersi respons server dan state data lewat fixture BE (bagian 8b butir 1). Perilaku FE atas penolakan yang sama diasersi di spec jalur UI.
- Pembagian TC lintas spec (S-05): klausa "tidak ada log" TC-FA-TAG-1262 (Expected b) diasersi di spec 388 (absence kelas g) dengan request langsung sebagai pemicu dan baseline sendiri; spec ini mengasersi respons 403 dan data AST-0011 yang tidak berubah (langkah 6 dan 7). TC-FA-TAG-1262 tetap di `sourceTc` kedua spec.
- Urutan blok mengikuti akun aktor (satu ganti akun per blok) dan bukan urutan TC; tiap blok berdiri sendiri karena semua aksi ditolak dan tidak mengubah data.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4, 13, 17, 21, 26 (ganti akun), 8 dan 27 (membuka halaman), 31 (menutup input Search lewat `(←)` agar tabel kembali ke keadaan awal).
- Pada TC-FA-TAG-1262, TC-FA-TAG-1263, TC-FA-TAG-1264, dan TC-FA-TAG-1265 request dikirim langsung tanpa lewat browser sehingga halaman TAG tidak dibuka di blok 3, 4, dan 5.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 10 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.
- Temuan untuk QA:
  - TC-FA-TAG-1263 menulis "satu aset Not Paired Yet" tanpa menyebut aset; spec memakai AST-0051. TC-FA-TAG-1262 tidak menyebut Tag lama dan baru untuk request Replace; asersi hanya pada status 403 dan data aset yang tidak berubah.
  - TC-FA-TAG-1267: cara mengaktifkan tombol lewat manipulasi DOM tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE.
  - TC-FA-TAG-1265 tidak menyebut kode status penolakan; spec mengasersi "menolak" tanpa kode.
  - Post Condition semua TC ("Tidak ada perubahan data bisnis") tanpa langkah observasi di TC tidak diasersi, selain yang sudah menjadi Expected.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
