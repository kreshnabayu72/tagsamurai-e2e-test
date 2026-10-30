---
id: TC-GS-IMPORT-E2E-115-ai-field-shortening-badge-saran-tampil-pada-sel-yang-melanggar-batas
title: "AI Field Shortening: badge saran tampil pada sel yang melanggar batas panjang di semua Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-286
  - TC-GS-IMPORT-287
  - TC-GS-IMPORT-288
  - TC-GS-IMPORT-289
  - TC-GS-IMPORT-290
  - TC-GS-IMPORT-291
  - TC-GS-IMPORT-292
  - TC-GS-IMPORT-697
coverage:
  web: automated
---

# AI Field Shortening: badge saran tampil pada sel yang melanggar batas panjang di semua Tab

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Tab Brand); perpindahan Tab berikutnya ditulis sebagai langkah penghubung.
- Kondisi awal tiap TC (Kontrak Fixture R1): Client C tanpa draft pada Sub-Tab yang diuji. Skrip reset draft Client C disediakan tim FE/BE dan dijalankan di hook `before` serta sebagai langkah penghubung pada baris tabel dengan kolom Reset draft sebelum unggah = ya; mekanismenya tidak ada di TC (lihat Temuan untuk QA).
- Layanan AI: mock deterministik mode normal (Data Dinamis D-40, tabel D-41 dan D-42) yang diatur tim QA/BE lewat hook uji di lingkungan non-produksi; hook `before` memastikan mode normal dan hook `after` mengembalikannya ke normal.
- Data Dinamis (berkas upload disediakan tim QA; fixture baru `Fixture.import.aiFieldShortening115`; nilai sel melanggar batas 120 karakter sesuai D-41, tanpa suffix per run karena berkas statis dan draft direset per Tab):

| TC | Tab | Berkas | Sel yang diuji | Isi baris data #1 | Saran AI | Pindah Tab | Reset draft sebelum unggah |
|---|---|---|---|---|---|---|---|
| 286 | Brand | `ai-brand-long.csv` (D-44) | Brand Name | Brand Name = nilai sumber Brand pada D-41 (121 karakter) | `Samsung Electronics Indonesia` | tidak | tidak |
| 287 | Measurement | `ai-measurement-long.csv` (D-44) | Unit Name | Unit Name = nilai sumber Unit Name pada D-41 (121 karakter), Symbol `kg/m2` | `Kilogram per Square Meter` | ya | tidak |
| 288 | Position | `ai-position-long.csv` (D-44) | Position Name | Position Name = nilai sumber Position pada D-41 (121 karakter) | `Senior Regional Operations Coordinator` | ya | tidak |
| 289 | Division | `ai-division-long.csv` (D-44) | Division Name | Division Name = nilai sumber Division pada D-41 (121 karakter) | `Corporate Strategy and Business Development` | ya | tidak |
| 290 | User Login | `ai-ul-first-long.csv` (berkas User Login standar D-45) | First Name | First Name = nilai sumber First Name pada D-41 (121 karakter), Last Name `Rahmawati`, Email `siti.rahmawati@example.com`, Division `Engineering`, Position kosong | `Muhammad Abdurrahman Nurrahman` | ya | tidak |
| 291 | User Login | `ai-ul-last-long.csv` (D-45) | Last Name | First Name `Siti`, Last Name = nilai sumber Last Name pada D-41 (121 karakter), Email `siti.rahmawati@example.com`, Division `Engineering`, Position kosong | `Hadiningrat Prawirodiningrat` | tidak | ya |
| 292 | User Non Login | `ai-unl-first-long.csv` (berkas User Non Login standar D-45) | First Name | First Name = nilai sumber First Name pada D-41 (121 karakter), Last Name `Lestari`, Email `ayu.lestari@example.com`, Division `Engineering`, Position kosong, Represented By `budi.manager.c@example.com` | `Muhammad Abdurrahman Nurrahman` | ya | tidak |
| 697 | User Non Login | `ai-unl-last-long.csv` (D-45) | Last Name | First Name `Ayu`, Last Name = nilai sumber Last Name pada D-41 (121 karakter), Email `ayu.lestari@example.com`, Division `Engineering`, Position kosong, Represented By `budi.manager.c@example.com` | `Hadiningrat Prawirodiningrat` | tidak | ya |

- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft Client C pada semua Sub-Tab yang disentuh spec ini dan kembalikan mock AI ke mode normal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: input upload berkas; mock layanan AI mode normal (D-40); skrip reset draft (Kontrak Fixture R1) disediakan tim FE/BE.
- State global: mock layanan AI (dikembalikan ke normal di hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-IMPORT-286 sampai 292 dan 697: badge AI Field Shortening per Tab dan field

Untuk setiap baris tabel Data Dinamis, urut 286, 287, 288, 289, 290, 291, 292, 697, lakukan langkah 1 sampai 13 (iterasi 286 mulai di Tab Brand yang dibuka hook `beforeEach` dengan kolom Pindah Tab = tidak dan kolom Reset draft sebelum unggah = tidak, karena draft Brand sudah kosong dan Tab sudah aktif).

1. Buka Import > Tab pada kolom Tab baris tabel (kolom Pindah Tab = ya)
2. Reset draft Client C pada Tab tersebut lewat skrip reset (kolom Reset draft sebelum unggah = ya)
3. Klik [Upload File] di toolbar dan pilih berkas pada kolom Berkas
4. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
5. Verifikasi modal Confirm Mapping tertutup
6. Verifikasi Staging Table menampilkan baris #1 berstatus `error`
7. Verifikasi Staging Metric Cards: Total Rows 1
8. Verifikasi Staging Metric Cards: Errors 1
9. Perhatikan sel pada kolom "Sel yang diuji" di baris #1
10. Verifikasi sel tersebut menampilkan badge inline "AI suggestion: '<Saran AI>'?" sesuai kolom Saran AI
11. Verifikasi badge disertai `[Accept]` dan `[Dismiss]`
12. Verifikasi baris #1 tetap berstatus `error`
13. Verifikasi nilai sel yang diuji tetap 121 karakter semula (tidak berubah sendiri)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`, TC-GS-IMPORT-286 sampai 292 dan 697.
- Satu blok langkah 1 sampai 13 diulang delapan kali dengan parameter dari tabel Data Dinamis (idiom 8b butir 7); `Verifikasi` tetap satu per klausa Expected (a: langkah 5-8, b: langkah 10-11, c: langkah 12-13). Ekspansi 13 x 8 = 104 langkah melewati sekitar 35; alasan: seluruh blok satu kelas (AI Field Shortening, mock normal), berdiri sendiri, dan kegagalan satu Tab tidak membuat Tab lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Tab; kolom Pindah Tab = ya pada 287, 288, 289, 290, 292), langkah 2 (reset draft; kolom Reset draft sebelum unggah = ya pada 291 dan 697, yang memakai Tab yang sama dengan iterasi sebelumnya).
- Pembagian TC lintas spec: TC-GS-IMPORT-299, 300, 698, 699, 703, 866 (tanpa badge dan batas waktu) ada di spec 116; Accept dan Dismiss ada di spec 117; Read Only di spec 131.
- Temuan untuk QA:
  - Skrip reset draft Client C (Kontrak Fixture R1) tidak didefinisikan mekanismenya di TC; disediakan tim FE/BE, endpoint tidak dikarang.
  - Berkas `ai-ul-first-long.csv`, `ai-ul-last-long.csv`, `ai-unl-first-long.csv`, `ai-unl-last-long.csv` didefinisikan hanya pada Data Uji TC pemakai (D-44 menyebut berkas AI ini "didefinisikan pada Data Uji TC pemakai"); header kolom tidak ditulis per TC, spec mengikuti header berkas standar D-45.
  - Kolom Staging Table untuk TC-GS-IMPORT-290 dan 291 memakai Position kosong sehingga baris `error` hanya karena panjang nama; TC tidak menyatakan hal itu secara eksplisit.
