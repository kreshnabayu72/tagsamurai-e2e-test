---
id: TC-FA-GRP-E2E-010-group-context-header-all-groups-agregat-distinct-union-scope-aktor-scoped-dan-angka-tidak-dapat-diklik
title: "Group Context Header All Groups: Agregat Client Distinct Dedup, Union Scope Aktor Scoped (User di Luar Scope Tidak Dihitung), dan Angka Tidak Dapat Diklik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-25
  - TC-FA-GRP-29
  - TC-FA-GRP-969
coverage:
  web: automated
---

# Group Context Header All Groups: Agregat Client Distinct Dedup, Union Scope Aktor Scoped (User di Luar Scope Tidak Dihitung), dan Angka Tidak Dapat Diklik

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Akun aktor kedua (langkah 9 dan 10): Group Manager dengan scope Head Office level 1 beserta descendant (Pre-setup No 22; email perlu data dari tim FE/QA, berbeda dari No 4 yang ber-scope Region West), password `Spectra.env.FA_GMSEED_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite untuk akun Total Control (lihat `suite.md`); untuk akun Group Manager Pre-setup No 22, flag disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after`.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9) termasuk Head Office > Floor 2 > IT Department dan Region East.
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-FA-GRP-25, 969 | User X | `userX+{runId}-010@qwertysystem.net` | Group Role di dua group berbeda: Floor 2 dan IT Department |
| TC-FA-GRP-969 | User Y | `userY+{runId}-010@qwertysystem.net` | Group Role hanya di Region East (di luar scope Group Manager Pre-setup No 22) |
| TC-FA-GRP-969 | User Z | `userZ+{runId}-010@qwertysystem.net` | Tanpa assignment, bukan Total Control, Default User, maupun Read Only |

- Kemampuan teknis: fixture BE (seeding akun dan assignment, pembacaan himpunan user distinct dan agregat aset per aktor) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-25: Header All Groups, agregat client distinct dedup

1. Verifikasi Group Context Header menampilkan judul `All Groups` dengan metrik berlabel `Total Asset: [N]` dan `Total User: [N]`
2. Verifikasi Total User header All Groups menghitung User X sekali (distinct), sesuai himpunan user client yang dibaca lewat fixture BE
3. Verifikasi Total Asset header sama dengan seluruh aset aktif client sesuai pembacaan fixture BE

### TC-FA-GRP-29: Angka header All Groups tidak dapat diklik

4. Klik node `All Groups` di sidebar
5. Klik angka Total Asset pada header
6. Klik angka Total User pada header
7. Verifikasi kedua angka tampil sebagai teks biasa (bukan elemen yang dapat diklik)
8. Verifikasi tidak ada popup yang terbuka

### TC-FA-GRP-969: Header All Groups aktor scoped

9. Logout dari akun Total Control
10. Login sebagai Group Manager scope Head Office (Pre-setup No 22) dengan `Spectra.env.FA_GMSEED_PASSWORD`
11. Buka Fixed Asset > Settings > Groups
12. Klik node `All Groups` di sidebar
13. Verifikasi judul `All Groups` dengan `Total Asset: [N]` dan `Total User: [N]` sama dengan union himpunan Total Asset dan Total User seluruh node dalam scope aktor, distinct dedup, sesuai pembacaan fixture BE
14. Verifikasi User X dihitung sekali walau ter-assign di dua node
15. Verifikasi User Y (di luar scope) tidak termasuk himpunan Total User header
16. Verifikasi User Z (tidak ter-assign dan bukan Total Control, Default User, atau Read Only) tidak termasuk himpunan Total User header
17. Klik angka Total Asset pada header
18. Klik angka Total User pada header
19. Verifikasi angka header All Groups tidak dapat diklik dan tidak ada popup yang terbuka

## Notes

- Spec 19 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 4 (memilih `All Groups` sebagai kondisi TC-FA-GRP-29), langkah 9 sampai 11 (ganti akun eksplisit ke Group Manager; layar Groups dibuka langsung karena hook `beforeEach` hanya berlaku untuk akun aktor pertama). Hook `after` memulihkan sesi ke akun default suite (S-07).
- Urutan TC dalam spec: 25, 29, 969 (TC-FA-GRP-969 terakhir karena ganti akun).
- Temuan untuk QA:
  - Password `Spectra.env.FA_GMSEED_PASSWORD` adalah nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik script.
  - TC-FA-GRP-25 dan 969 tidak menyebut cara membaca himpunan user distinct; spec memakai pembacaan fixture BE (disediakan tim FE/BE).
