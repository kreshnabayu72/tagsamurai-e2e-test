---
id: TC-FA-GRP-E2E-019-aktor-scoped-variasi-scope-guided-tooltip-all-groups-level-1-empty-dan-union-scope
title: "Aktor Scoped Variasi Scope: Guided Tooltip Tanpa [+] Group, All Groups Level 1 Ter-assign, Empty State Tanpa Node, Dan Node Terpilih Keluar Scope"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-40
  - TC-FA-GRP-58
  - TC-FA-GRP-59
  - TC-FA-GRP-1062
coverage:
  web: automated
---

# Aktor Scoped Variasi Scope: Guided Tooltip Tanpa [+] Group, All Groups Level 1 Ter-assign, Empty State Tanpa Node, Dan Node Terpilih Keluar Scope

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (langkah 1 sampai 11): Group Manager scope Region West (Pre-setup No 4) `groupManagerGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor lain (email perlu data dari tim FE/QA; assignment `Revoke Own` di-seed di hook `before` lewat API dan dihapus di hook `after`). Password keduanya `Spectra.env.FA_GMSEED_PASSWORD`:

| TC | Akun | Scope Group Manager |
|---|---|---|
| TC-FA-GRP-58 | Pre-setup No 22 | `Head Office` (node level 1 beserta descendant) |
| TC-FA-GRP-1062 | Pre-setup No 23 | dua node level 1: `Head Office` dan `Revoke Own {runId}-019` |

- Data Dinamis (di-seed di hook `before`, dihapus di hook `after`): `Revoke Own {runId}-019` (level 1, kosong, milik spec ini, di-assign ke aktor TC-FA-GRP-1062 sebagai node scope kedua selain `Head Office`) dan `Level1 Other {runId}-019` (level 1, di luar scope aktor TC-FA-GRP-58, berisi satu aset dan satu user ber-Group Role yang tidak dihitung pada header aktor itu).
- Flag Guided Tooltip `fa-settings-groups`: untuk akun No 4 flag disetel belum diset oleh langkah 2 dan dipulihkan di hook `after`; untuk kedua akun Pre-setup (No 22 dan No 23) flag disetel `seen` di hook `before` (kemampuan menyetel flag disediakan tim FE/BE).
- Data Pre-setup (hanya dibaca, kecuali assignment akun seed yang milik spec): pohon group baku Tabel A (Pre-setup No 9): Global HQ > Region West > Branch West 1 > Room 301; Region East; Region North.
- Kemampuan teknis: fixture BE (seeding akun dan assignment, pembacaan agregat union scope) dan sesi API aktor (admin lain Total Control mencabut assignment pada langkah 21), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-GRP-59: Empty state All Groups untuk aktor scoped tanpa node level 1

1. Verifikasi tabel menampilkan Illustration dengan title `No groups at this level` dan body `Select a group from the sidebar to see its subgroups.`

### TC-FA-GRP-40: Guided Tooltip tetap 3 step untuk aktor tanpa tombol [+] Group

2. Setel flag `fa-settings-groups` akun Group Manager menjadi belum diset
3. Muat ulang halaman dengan F5
4. Verifikasi walkthrough muncul otomatis pada Step 1 yang menyorot Sidebar Group Tree dengan penomor `Step 1 of 3`
5. Klik [Next]
6. Verifikasi Step 2 menyorot kolom Function dengan penomor `Step 2 of 3`
7. Klik [Next]
8. Verifikasi Step 3 menyorot kolom Total Asset dengan penomor `Step 3 of 3`
9. Verifikasi tombol [+] Group bukan target dari ketiga step
10. Klik [Done]
11. Muat ulang halaman dengan F5

### TC-FA-GRP-58: All Groups hanya menampilkan node level 1 yang ter-assign

12. Logout dari akun Group Manager scope Region West
13. Login sebagai Group Manager scope Head Office level 1 (Pre-setup No 22) dengan `Spectra.env.FA_GMSEED_PASSWORD`
14. Buka Fixed Asset > Settings > Groups
15. Verifikasi tabel All Groups hanya berisi node level 1 yang ter-assign (`Head Office`) dan tidak memuat `Level1 Other {runId}-019`
16. Verifikasi header All Groups sama dengan agregat union scope aktor (distinct) sesuai pembacaan fixture BE sehingga angka di luar scope tidak dihitung

### TC-FA-GRP-1062: Refresh F5 saat node terpilih sudah di luar scope aktor

17. Logout dari akun Group Manager scope level 1
18. Login sebagai Group Manager dengan dua node scope level 1 `Head Office` dan `Revoke Own {runId}-019` (Pre-setup No 23) dengan `Spectra.env.FA_GMSEED_PASSWORD`
19. Buka Fixed Asset > Settings > Groups
20. Klik `Revoke Own {runId}-019` di sidebar
21. Cabut assignment Group Manager aktor pada `Revoke Own {runId}-019` lewat sesi API admin lain hingga pencabutan tersimpan
22. Muat ulang halaman dengan F5
23. Verifikasi tampilan kembali ke `All Groups`
24. Verifikasi `Head Office` tampil di sidebar
25. Verifikasi `Revoke Own {runId}-019` tidak tampil di sidebar
26. Verifikasi tabel tidak memuat `Revoke Own {runId}-019` dan hanya memuat node level 1 yang masih ter-assign ke aktor

## Notes

- Langkah penghubung (S-03): langkah 2 dan 3 (menyetel flag dan muat ulang agar flag dievaluasi), langkah 11 (muat ulang untuk membersihkan state setelah [Done]), langkah 12 sampai 14 dan 17 sampai 19 (ganti akun eksplisit), langkah 24 (`Verifikasi` anchor positif untuk absence `Revoke Own`, 8b butir 2; tidak ada di Expected TC).
- Urutan TC dalam spec: 59, 40, 58, 1062 (TC-FA-GRP-59 pertama karena memakai akun hook `before`; TC-FA-GRP-1062 terakhir karena mencabut assignment).
- Pelaku kedua (admin lain Total Control) hanya memicu perubahan state lewat sesi API, bukan konteks kedua (P-2 `[KEPUTUSAN 2026-10-30]`).
- Temuan untuk QA:
  - Password `Spectra.env.FA_GMSEED_PASSWORD` adalah nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik script.
  - TC-FA-GRP-40 tidak menyebut keadaan tabel (kosong untuk akun No 4) saat walkthrough menyorot kolom Function dan Total Asset; spec mengikuti TC dan mengasersi penomor serta target step.
