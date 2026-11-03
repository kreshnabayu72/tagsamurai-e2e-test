---
id: TC-AC-SU-E2E-014-entitas-baru-tanpa-user-lain-dan-tanpa-custom-field
title: "Entitas Baru: Hanya Default User di User List dan Detail User tanpa Section Custom Field"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-18
  - TC-AC-SU-47
coverage:
  web: automated
---

# Entitas Baru: Hanya Default User di User List dan Detail User tanpa Section Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User entitas baru E1 (email disediakan tim FE, password `Spectra.env.AC_E1_DU_PASSWORD`) dan Total Control E1 (email disediakan tim FE, password `Spectra.env.AC_E1_TC_PASSWORD`). Kedua email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Env var `AC_E1_DU_PASSWORD` dan `AC_E1_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec).
- Login di hook `before` spec ini sebagai Default User entitas baru (E1); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Entitas baru E1 (bukan entitas Principal Pre-setup), disediakan tim FE/BE lewat Fixture BE: tanpa user lain selain Default User dan tanpa Custom Field aktif. Hook `before` membuat E1 dan hook `after` menghapusnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-47 | `John Doe` | `John Doe {runId}-014` | `johndoe+{runId}-014@qwertysystem.net` | Activated, Active, di E1; ditambahkan lewat Fixture BE sesudah blok TC-AC-SU-18 |

- Total Control E1 untuk blok TC-AC-SU-47 disediakan tim FE/BE di E1 pada saat yang sama dengan John Doe; blok TC-AC-SU-18 dijalankan sebelum John Doe ditambahkan.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-18: Entitas hanya punya Default User

1. Amati tabel User List E1
2. Verifikasi satu baris Default User tampil
3. Verifikasi tidak ada empty illustration

### TC-AC-SU-47: Section Custom Field hidden bila tidak ada field aktif

4. Tambahkan `John Doe {runId}-014` dan akun Total Control ke E1 lewat Fixture BE
5. Logout dari akun Default User E1
6. Login sebagai Total Control E1 (email disediakan tim FE, password dari `Spectra.env.AC_E1_TC_PASSWORD`)
7. Buka Settings > User lewat sidebar
8. Ketik Search `John Doe {runId}-014`, tekan Enter
9. Klik Name `John Doe {runId}-014`
10. Verifikasi General Information tampil
11. Verifikasi section `Custom Field` tidak dirender
12. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
13. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 4 (seeding sebagai precondition TC-AC-SU-47, tidak diasersi), langkah 5 dan dua langkah sesudahnya (ganti akun eksplisit, S-07), langkah 8 (Search untuk menemukan baris target, R-16), langkah 12 dan 13 (kembali ke daftar dan reset Search); langkah-langkah ini juga anchor tambahan bagi Verifikasi sesudahnya (S-03, dasar 8b.2). Hook `after` memulihkan sesi ke Default User Pre-setup #1.
- Perbedaan aktor: TC-AC-SU-18 berjalan sebagai Default User dan TC-AC-SU-47 sebagai Total Control; keduanya digabung karena entitas E1 yang sama (tanpa Custom Field) dan ganti akun ditulis eksplisit; blok sesudah ganti akun tetap bermakna.
- Temuan untuk QA:
  - TC-AC-SU-18 dan TC-AC-SU-47 mensyaratkan entitas khusus (hanya Default User; tanpa Custom Field aktif) yang tidak ada di Tabel Pre-setup; akun dan data E1 disediakan tim FE/BE.
  - TC-AC-SU-47 memakai `John Doe` yang tidak mungkin ada di entitas "tanpa user lain" milik TC-AC-SU-18; spec menambahkannya sesudah blok TC-AC-SU-18.
  - Nama user TC (`John Doe`) dipakai sebagai nama bersuffix `{runId}-014` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
