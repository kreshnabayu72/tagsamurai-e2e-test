---
id: TC-AC-SU-E2E-017-entitas-distributor-isolasi-data-dan-baris-global-role
title: "Entitas Distributor: Isolasi Data User Antar Entitas dan Baris Global Role Manage TAG Stock serta Manage Hardware Stock"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-54
  - TC-AC-SU-192
coverage:
  web: automated
---

# Entitas Distributor: Isolasi Data User Antar Entitas dan Baris Global Role Manage TAG Stock serta Manage Hardware Stock

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Distributor Nusantara (tidak ada di Pre-setup, email disediakan tim FE), password `Spectra.env.AC_DIST_TC_PASSWORD`.
- Env var `AC_DIST_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Total Control Distributor Nusantara; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-54 | `Dewi Lestari` | `Dewi Lestari {runId}-017` | `dewilestari+{runId}-017@qwertysystem.net` | di entitas Distributor Nusantara |
| TC-AC-SU-54 | `Mike Tan` | `Mike Tan {runId}-017` | `miketan+{runId}-017@qwertysystem.net` | di entitas Distributor Nusantara |
| TC-AC-SU-54 | `Agus Salim` | `Agus Salim {runId}-017` | `agussalim+{runId}-017@qwertysystem.net` | di entitas Distributor Sentosa (entitas lain) |
| TC-AC-SU-54 | `Hendra Gunawan` | `Hendra Gunawan {runId}-017` | `hendragunawan+{runId}-017@qwertysystem.net` | di entitas Principal |
| TC-AC-SU-192 | `Budi Santoso` | `Budi Santoso {runId}-017` | `budisantoso+{runId}-017@qwertysystem.net` | di entitas Distributor Nusantara; tanpa tingkat akses, bukan Group Manager |

- Entitas Distributor Nusantara dan Sentosa serta akun Total Control Nusantara tidak ada di Tabel Pre-setup; disediakan tim FE (lihat Temuan untuk QA). Seeding user lintas entitas lewat Fixture BE; penghapusan di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-54: Isolasi entitas, Distributor hanya melihat user entitasnya

1. Ketik Search `{runId}-017`, tekan Enter
2. Verifikasi `Dewi Lestari {runId}-017` dan `Mike Tan {runId}-017` (Distributor Nusantara) tampil
3. Verifikasi `Agus Salim {runId}-017` (Distributor Sentosa) dan `Hendra Gunawan {runId}-017` (Principal) tidak tampil
4. Ganti isi kotak search dengan `Agus Salim {runId}-017`, tekan Enter
5. Verifikasi empty state `No results found`
6. Ganti isi kotak search dengan `Hendra Gunawan {runId}-017`, tekan Enter
7. Verifikasi empty state `No results found`

### TC-AC-SU-192: Entitas Distributor, baris Manage TAG stock dan Manage hardware stock hanya punya switch

8. Ganti isi kotak search dengan `Budi Santoso {runId}-017`, tekan Enter
9. Klik nama `Budi Santoso {runId}-017` di User List
10. Verifikasi Settings > User > Detail terbuka dengan Tab Role aktif
11. Amati baris `Manage TAG stock`
12. Verifikasi baris `Manage TAG stock` dan `Manage hardware stock` tampil dengan switch
13. Verifikasi sel C, R, U, D kedua baris itu tampil `—` (bukan checkbox)
14. Verifikasi daftar baris Global Role sesuai katalog Distributor: `Manage group`, `Manage hardware stock`, `Manage plans & licensing`, `Manage TAG stock`, `Manage user and role`
15. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16; berlaku juga untuk Search sesudahnya), langkah 15 (kembali ke daftar), langkah 16 (reset Search).
- Temuan untuk QA:
  - TC-AC-SU-54 butir a "hanya user Distributor Nusantara tampil" bersifat universal; spec mengasersi dua user seed Nusantara tampil dan dua user entitas lain tidak tampil (anchor positif di surface yang sama), bukan seluruh isi tabel.
  - Akun Total Control Distributor Nusantara (TC-AC-SU-54 dan TC-AC-SU-192) tidak ada di Pre-setup (hanya #7 Default User Distributor); email disediakan tim FE dan password `Spectra.env.AC_DIST_TC_PASSWORD` (nama ditetapkan penulis spec).
  - TC-AC-SU-192 langkah 1 menyatakan Tab Role aktif sebagai hasil klik nama; spec mengasersinya sebagai `Verifikasi`.
  - Nama user TC (`Dewi Lestari`, `Mike Tan`, `Agus Salim`, `Hendra Gunawan`, `Budi Santoso`) dipakai sebagai nama bersuffix `{runId}-017` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
