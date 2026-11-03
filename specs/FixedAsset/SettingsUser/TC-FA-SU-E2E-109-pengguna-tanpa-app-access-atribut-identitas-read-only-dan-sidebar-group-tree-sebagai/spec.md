---
id: TC-FA-SU-E2E-109-pengguna-tanpa-app-access-atribut-identitas-read-only-dan-sidebar-group-tree-sebagai
title: "Pengguna Tanpa App Access dan Atribut Identitas Read-only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-373
  - TC-FA-SU-374
coverage:
  web: automated
---

# Pengguna Tanpa App Access dan Atribut Identitas Read-only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Data Pre-setup tambahan: pohon grup (#21) dan Global Settings (#38). Pengguna tanpa App Access FAMS (hanya punya akses Global Settings) dan pengguna tenant B (Data TC-FA-SU-373) dirujuk lewat `Fixture.fa-settings-user.penggunaTanpaAppAccess`, `penggunaTenantB`, dan `urlDetailTenantB`; keduanya disediakan tim FE (tidak diberi nama di TC).
- Pengguna milik spec untuk TC-FA-SU-374 (seed API di hook `before`, dihapus di hook `after`; S-06): `Budi Santoso {runId}-109`, email `budi.santoso+{runId}-109@qwertysystem.net`, Position awal `Fixture.fa-settings-user.positionAwal`. Perubahan Position di Global Settings memakai sesi API aktor (disediakan tim FE/BE, tanpa endpoint karangan) dan nilai kembali ke awal di hook `after`.
- Kemampuan menekan unduhan CSV dan membaca isi berkas (nama berkas dan baris) disediakan tim FE.

## Test Steps

### TC-FA-SU-373: Pengguna tanpa App Access FAMS dan isolasi tenant

1. Verifikasi tabel User List menampilkan sedikitnya satu baris
2. Ketik Search nama `Fixture.fa-settings-user.penggunaTanpaAppAccess`, tekan Enter
3. Verifikasi empty state `No results found` tampil (pengguna tanpa App Access FAMS tidak tampil di tabel dan hasil Search)
4. Klik `(←)` pada kotak Search
5. Klik ikon Filter, buka dropdown Status, centang `Active`, klik `[Apply]`
6. Verifikasi tabel menampilkan sedikitnya satu baris
7. Ketik Search nama `Fixture.fa-settings-user.penggunaTanpaAppAccess`, tekan Enter
8. Verifikasi empty state `No results found` tampil (pengguna tidak tampil pada hasil Filter)
9. Klik `(←)` pada kotak Search, klik `[Clear Field]` lalu `[Apply]` pada panel Filter
10. Klik ikon Download, pilih `Download as CSV`
11. Verifikasi berkas `User.csv` terunduh dan memuat sedikitnya satu baris pengguna
12. Verifikasi berkas `User.csv` tidak memuat pengguna tanpa App Access FAMS
13. Ketik Search nama `Fixture.fa-settings-user.penggunaTenantB`, tekan Enter
14. Verifikasi empty state `No results found` tampil (pengguna tenant B tidak tampil)
15. Klik `(←)` pada kotak Search
16. Buka URL Detail pengguna tenant B (`Fixture.fa-settings-user.urlDetailTenantB`)
17. Verifikasi sidebar menu Fixed Asset tampil
18. Verifikasi Detail pengguna tenant B tidak dapat dibuka

### TC-FA-SU-374: Atribut profil identitas read-only

19. Ketik Search `Budi Santoso {runId}-109`, tekan Enter
20. Klik ⋯ pada baris `Budi Santoso {runId}-109`, klik `Detail`
21. Verifikasi General Information menampilkan Nama, Email, Employee ID, Jabatan, Divisi, Foto Profil, TAG, dan Custom Field sebagai teks atau badge tanpa kontrol edit
22. Verifikasi tidak ada kontrol edit atau Save di Header dan General Information selain ikon edit Home Group
23. Ubah Position `Budi Santoso {runId}-109` di Global Settings menjadi `Fixture.fa-settings-user.positionBaru` lewat sesi API hingga tersimpan
24. Verifikasi Detail menampilkan Position baru tanpa muat ulang manual
25. Klik breadcrumb `User`
26. Verifikasi kolom Position baris `Budi Santoso {runId}-109` menampilkan Position baru tanpa muat ulang manual

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 4, 9, 15 (menutup Search dan membersihkan Filter, S-09), 5 (menerapkan Filter Status `Active` sebagai jalur Filter), 13 dan 19 (Search untuk menemukan baris, R-16).
- Expected a TC-FA-SU-373 menyebut empat permukaan (tabel, Search, Filter, Download); langkah Filter dan Download ditambahkan sebagai jalur asersi karena langkah TC hanya memuat Search, dan Search memakai empty state `No results found` sebagai anchor positif (8b butir 2).
- TC-FA-SU-375, ada di spec 130.
- Temuan untuk QA (S-15): (1) TC-FA-SU-373 tidak menyebut nama pengguna tanpa App Access dan pengguna tenant B, dan Expected b tidak menyebut hasil pembukaan URL tenant lain (halaman Not Found, 403, atau redirect); spec hanya mengasersi bahwa Detail tidak terbuka. (2) TC-FA-SU-374 langkah 2 mengubah Position, sedangkan Expected b menyebut "perubahan nama"; spec mengubah Position dan mengasersi Position di Detail dan User List. (3) Expected a TC-FA-SU-374 menyebut Temporary Until tampil sebagai teks tanpa kontrol edit, padahal field itu Hidden untuk pengguna non-temporary (TC-FA-SU-372); Temporary Until tidak diasersi pada pengguna non-temporary.
