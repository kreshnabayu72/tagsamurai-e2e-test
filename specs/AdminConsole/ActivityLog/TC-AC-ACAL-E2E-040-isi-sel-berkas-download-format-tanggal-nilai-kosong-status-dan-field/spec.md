---
id: TC-AC-ACAL-E2E-040-isi-sel-berkas-download-format-tanggal-nilai-kosong-status-dan-field
title: "Isi Sel Berkas Download: Format Tanggal, Nilai Kosong, Status, dan Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-127
  - TC-AC-ACAL-134
  - TC-AC-ACAL-179
coverage:
  web: automated
---

# Isi Sel Berkas Download: Format Tanggal, Nilai Kosong, Status, dan Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global yang diubah (General Settings entitas Principal), disetel hook `before` setelah mencatat nilai awal dan dipulihkan hook `after`: Date Format `dd/MM/yy`, Time Format 24-hour (Precondition TC-AC-ACAL-127), dan Time Zone `Asia/Jakarta` (TC tidak menyebut Time Zone; dipilih spec agar jam terbaca deterministik). Kemampuan menyetel General Settings disediakan tim FE/BE tanpa endpoint yang dikarang di spec ini; pemulihan menambah entri Edit General Settings pada audit trail dan mengubah Last Updated General Settings.
- Data Pre-setup (nama literal dan seed BE, Pre-setup No 15; nama literal menurut Lampiran A butir A-3: data Pre-setup No 13 sampai 15 hanya dibaca, seeding idempotent): entri User Action `Duplicate Approved` Object `Hardware` Name `SN-ZEBRA-FX9600-000108`, Modified By `Rina Wijaya` (tampil `Rina W`).
- Data Dinamis (bersuffix `{runId}-040`), disediakan lewat seed BE di hook `before` (mekanisme seeding log tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE):
  - Tab Session: user `John Doe {runId}-040` (Position `Staff`) dengan satu baris Session bercap `18 Jun 2026 09:00 UTC` (tampil tanggal `18/06/26` pukul `16:00` pada zona Jakarta) dan user `Jane Smith {runId}-040` tanpa Position dengan satu baris Session.
  - Tab User Action: entri `Create` Object `Distributor` Name `Distributor Format {runId}-040`, Field `Company Name`, Old Value kosong; entri Name `Entri Tanpa Field {runId}-040` dengan Field kosong (tidak diisi modul pengirim; TC-AC-ACAL-179).
  - Baris log tidak dapat dihapus (append-only).
- Kemampuan teknis (disediakan tim FE/BE): menangkap berkas unduhan browser ke direktori bersih per unduhan; membaca isi CSV (baris header, sel per kolom, pencarian baris berdasarkan teks sel) sebagai kelas binary buffer (bagian 3 prinsip 13f); mengamati ada atau tidaknya toast dan peringatan. Berkas unduhan dihapus di hook `after`.
- State yang diubah dan dipulihkan: Search tab User Action (dibersihkan di langkah 18). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-127 (tab Session) dan TC-AC-ACAL-134: Isi sel berkas Download tab Session

1. Pada tab Session klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
2. Verifikasi sel Date baris `John Doe {runId}-040` di berkas memuat tanggal `18/06/26` dan jam 24-hour `16:00` (format `dd/MM/yy` zona tampilan)
3. Verifikasi sel User baris tersebut berisi `John Doe {runId}-040` (nama lengkap)
4. Verifikasi sel Position baris `Jane Smith {runId}-040` berisi `-`
5. Verifikasi sel Status di semua baris berkas berisi `-` (hyphen)
6. Verifikasi tidak ada sel Status berkas yang berisi `—`, `Success`, atau `Failed`

### TC-AC-ACAL-127 (tab User Action): Isi sel berkas Download tab User Action

7. Klik tab "User Action", klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
8. Verifikasi sel Modified By baris `Duplicate Approved` Name `SN-ZEBRA-FX9600-000108` berisi `Rina Wijaya` (nama lengkap)
9. Verifikasi sel Old Value baris `Create` Name `Distributor Format {runId}-040` berisi `-`

### TC-AC-ACAL-179: Field kosong tampil `—` di tabel dan `-` di berkas

10. Ketik Search `Entri Tanpa Field {runId}-040`, tekan Enter
11. Verifikasi sel Field baris `Entri Tanpa Field {runId}-040` tampil `—`
12. Klik icon Filter, buka dropdown Field
13. Verifikasi sedikitnya satu opsi Field tampil di dropdown Field
14. Verifikasi dropdown Field tidak menampilkan opsi kosong, `—`, atau "None"
15. Tutup dropdown dengan Esc, lalu tutup Filter Panel tanpa [Apply] dengan klik icon Filter
16. Klik icon Download, klik `Download as CSV`, lalu buka isi berkas yang terunduh
17. Verifikasi sel Field baris `Entri Tanpa Field {runId}-040` di berkas berisi `-`
18. Klik `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 127 (tab Session) dan 134 pada satu unduhan CSV tab Session, 127 (tab User Action), lalu 179. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Kelas binary buffer (prinsip 13f): spec ini memuat isi sel berkas. TC-AC-ACAL-179 mencampur klausa UI (a dan b) dengan klausa isi berkas (c) dalam satu TC sehingga tidak dapat dipecah (satu TC satu spec); klausa UI ditempatkan di spec ini bersama klausa berkas (langkah 11 sampai 14).
- TC-AC-ACAL-134 dan butir tab Session TC-AC-ACAL-127 berbagi satu unduhan CSV tab Session tanpa Search (langkah 1) karena Langkah Uji identik ("Download > CSV, buka berkas"); asersi Status di semua baris memakai seluruh baris berkas.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 7, 16 (membuka isi berkas), langkah 15 (menutup dropdown dan Filter Panel tanpa [Apply]), langkah 18 (pemulihan Search, S-09), serta langkah 10 (Search `Entri Tanpa Field {runId}-040` menemukan baris seed; Search ikut menyempitkan berkas Download pada langkah 16).
- Asersi absence (langkah 14) didahului `Verifikasi` yang membuktikan sesuatu pada surface yang sama sudah tampil (langkah 13: opsi Field lain tampil).
- Langkah 6 (tidak ada `—`, `Success`, `Failed`) memakai langkah 5 sebagai anchor positif sel Status berkas.
- Temuan untuk QA:
  - TC-AC-ACAL-127 menyebut entri `John Doe` dan `Jane Smith` (Position kosong); spec memakai nama bersuffix (`John Doe {runId}-040`) karena asersi nama lengkap tidak bergantung pada singkatan nama di tabel.
  - TC-AC-ACAL-127 tidak menyebut Time Zone dan cap waktu entri; spec menyetel Time Zone `Asia/Jakarta` dan seed `18 Jun 2026 09:00 UTC`. TC juga tidak menulis string persis sel Date (pemisah tanggal dan jam); spec mengasersi tanggal `18/06/26` dan jam `16:00` sebagai bagian sel.
  - TC-AC-ACAL-127 tidak menyebut baris User Action untuk Modified By dan Old Value; spec memakai entri Pre-setup No 15 (`Rina Wijaya`) dan entri `Create` seed.
  - TC-AC-ACAL-179 Precondition c tidak menyebut data Pre-setup untuk entri dengan Field kosong; spec meminta seed BE `Entri Tanpa Field {runId}-040`.
  - Post Condition TC-AC-ACAL-127, 134, dan 179 bernilai `-` atau tidak diasersi.
