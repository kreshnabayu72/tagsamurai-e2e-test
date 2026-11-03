---
id: TC-FA-LBL-E2E-013-role-matrix-positif-aksi-baca-download-changelog-drawer-per-role
title: "Role Matrix Positif: Aksi Baca (Download, Changelog, Drawer) per Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-38
  - TC-FA-LBL-39
  - TC-FA-LBL-40
  - TC-FA-LBL-41
  - TC-FA-LBL-44
coverage:
  web: automated
---

# Role Matrix Positif: Aksi Baca (Download, Changelog, Drawer) per Role

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Read Only Company Alpha login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; role lain lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Read Only (Company Alpha) | #2 | `Fixture.assetLabeling.akun.readOnly` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-LBL-38, TC-FA-LBL-40 | 1 sampai 9 |
| Read Only (`Company Changelog`) | #17 | `Fixture.assetLabeling.akun.readOnlyChangelog` | `Spectra.env.FA_RO_CHANGELOG_PASSWORD` | TC-FA-LBL-39 | 10 sampai 14 |
| Read-Capability | #6 | `Fixture.assetLabeling.akun.readCapability` | `Spectra.env.FA_READCAP_PASSWORD` | TC-FA-LBL-41 | 15 sampai 23 |
| Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` | TC-FA-LBL-44 | 24 |
| Total Control | #1 | `Fixture.assetLabeling.akun.totalControl` | `Spectra.env.FA_LBL_TC_PASSWORD` | TC-FA-LBL-44 | 25 sampai 26 |

- Email akun Read Only `Company Changelog` tidak tertulis di Pre-setup TC (Pre-setup #17 hanya menyebut `Total Control` dan `Read Only`); disediakan tim FE (lihat Temuan untuk QA).
- Environment variable: `FA_RO_PASSWORD`, `FA_RO_CHANGELOG_PASSWORD`, `FA_READCAP_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; dipakai: `Finance Department` dengan Total Asset 5), #13 (aset berlabel `Finance Department` untuk isi Drawer), #17 (`Company Changelog` dengan log tujuh entri: Create `High Priority`, Edit `High Priority` Color, Create `Finance Department`, Edit `Finance Department` Label Name, Create `Audit Ready`, Create `Executive Asset`, Delete `Old Tag`; dibaca saja dan tidak ditulis spec).
- Kemampuan teknis: pembacaan berkas unduhan (nama berkas) pada langkah 4 dan 23 (disediakan tim FE).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Read Only (Company Alpha): TC-FA-LBL-38 dan TC-FA-LBL-40

1. Klik icon Download
2. Klik `Download as CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas `Labels.csv` terunduh
5. Klik `⋯` pada baris `Finance Department` lalu `Detail`
6. Verifikasi Drawer berjudul `Tagged Assets` terbuka
7. Verifikasi Drawer menampilkan 5 baris aset (Total Asset `5`)
8. Verifikasi tidak ada tombol aksi di Drawer
9. Tutup Drawer Tagged Asset

### Read Only (Company Changelog): TC-FA-LBL-39

10. Ganti akun: Logout, login sebagai Read Only `Company Changelog` `Fixture.assetLabeling.akun.readOnlyChangelog` (`Spectra.env.FA_RO_CHANGELOG_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
11. Klik icon Changelog
12. Verifikasi modal berjudul `Changelog: Labels` terbuka
13. Verifikasi tabel audit menampilkan baris Pre-setup #17 (Create `High Priority`, Edit `High Priority`, Create `Finance Department`, Edit `Finance Department`, Create `Audit Ready`, Create `Executive Asset`, Delete `Old Tag`)
14. Tutup modal Changelog

### Read-Capability: TC-FA-LBL-41

15. Ganti akun: Logout, login sebagai Read-Capability `Fixture.assetLabeling.akun.readCapability` (`Spectra.env.FA_READCAP_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
16. Klik chip `Finance Department`
17. Verifikasi Drawer `Tagged Assets` terbuka
18. Verifikasi Drawer menampilkan 5 baris
19. Tutup Drawer dengan `[✕]`
20. Klik icon Download
21. Klik `Download as XLSX`
22. Verifikasi tidak ada toast sukses
23. Verifikasi berkas `Labels.xlsx` terunduh

### Update-Only dan Total Control: TC-FA-LBL-44

24. Ganti akun: Logout, login sebagai Update-Only `Fixture.assetLabeling.akun.updateOnly` (`Spectra.env.FA_UPDATEONLY_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`, catat daftar label dan Total Asset tiap label
25. Ganti akun: Logout, login sebagai Total Control `Fixture.assetLabeling.akun.totalControl` (`Spectra.env.FA_LBL_TC_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`, catat daftar label dan Total Asset tiap label
26. Verifikasi kedua pengguna melihat 9 label yang sama dengan Total Asset yang sama

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 10, 15, 24, 25) karena akun pertama login di hook `before` dan langkah tiap role berbeda (bagian 3a, varian A).
- Langkah penghubung (S-03): langkah 9, 14, dan 19 (menutup Drawer dan modal).
- Urutan TC: TC-FA-LBL-38 dan TC-FA-LBL-40 (Read Only Company Alpha) lebih dulu, TC-FA-LBL-39 (Read Only `Company Changelog`) kemudian, TC-FA-LBL-41, dan TC-FA-LBL-44; urutan ini mengelompokkan akun supaya login sekali per akun (S-10).
- Absence toast sukses (langkah 3 dan 22): pemicu unduh (langkah 2 dan 21) menjadi anchor positif yang buktinya menyusul pada Verifikasi berkas (langkah 4 dan 23) (bagian 8b butir 11). Absence tombol aksi Drawer (langkah 8): baris aset Drawer yang tampil (langkah 7) menjadi anchor.
- Langkah 26 mencakup butir "tidak ada label yang disembunyikan berdasarkan grup aset atau divisi pengguna" (kesimpulan dari daftar yang sama, tidak teramati terpisah, S-03).
- Temuan untuk QA:
  - TC-FA-LBL-39 Precondition "Login sbg Role: Read Only" dengan Pre-setup #17; Read Only Pre-setup #2 ada di Company Alpha dan Pre-setup #17 (`Company Changelog`) memuat akun `Read Only` sendiri yang tidak tertulis di Tabel Pre-setup. Spec memakai akun Read Only `Company Changelog` (`FA_RO_CHANGELOG_PASSWORD`).
  - TC-FA-LBL-44 Expected "9 label yang sama" bergantung pada katalog Company Alpha tepat 9 label saat spec dijalankan; label milik spec lain harus sudah dibersihkan.
