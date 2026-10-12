---
id: TC-GS-BRAND-E2E-061-log-bulk-delete-dan-aktor-non-total-control
title: "Pencatatan Log Bulk Delete Homogen dan Log Aktor Non-Total Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-209
  - TC-GS-BRAND-215
coverage:
  web: automated
---

# Pencatatan Log Bulk Delete Homogen dan Log Aktor Non-Total Control

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (spec memakai dua akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | System Role: Create dan Read (Rina Marlina) | `createOnly_automated_qaTeam1@qwertysystem.net` | `GS_CREATE_PASSWORD` |
  | 2 | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |

  Login akun 1 di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun 2).
- Environment variable: `GS_CREATE_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi):
  - `Mosaic Brands {runId}-061` (D-04): dibuat spec lewat UI oleh Rina Marlina pada TC-GS-BRAND-215 (setara dependensi TC-GS-BRAND-36).
  - `Iris Optics {runId}-061`, `Juniper Labs {runId}-061`, `Keystone Mfg {runId}-061`: tiga brand bebas relasi, di-seed lewat API di hook `before` oleh akun Total Control (brand milik spec sendiri, bukan Population D-01, karena spec ini menghapusnya). Dihapus lewat UI (Bulk Delete) pada TC-GS-BRAND-209 (setara dependensi TC-GS-BRAND-116).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Mosaic Brands {runId}-061` serta ketiga brand bersuffix `{runId}-061` bila masih ada, dan pulihkan page size tabel Brand ke 10 serta seleksi tabel ke default.
- Tabel Brand berurut A-Z dengan page size 10 dan Client A punya lebih dari satu halaman brand, sehingga ketiga brand pada TC-GS-BRAND-209 tidak dijamin tampil bersamaan di halaman 1; opsi page size 50 tersedia pada paginasi tabel dan menampilkan seluruh brand (paling banyak 12 Pre-setup, 12 Population, dan brand milik spec ini).
- Kemampuan teknis: logout dan login ulang dalam satu spec (ganti akun).
- Tidak ada state global yang diubah.
- TC-GS-BRAND-209: login sebagai Total Control. TC-GS-BRAND-215: login sebagai System Role: Create dan Read.

## Test Steps

### TC-GS-BRAND-215: Log aktor non-Total Control masuk ke System Log aktor itu

1. Buka Global Settings > Master Reference > Brand
2. Klik [+ Brand], isi Brand Name `Mosaic Brands {runId}-061`, klik [Submit]
3. Verifikasi toast sukses: "Success, brand has been created."
4. Buka Global Settings > User > Detail Rina Marlina > Tab System Log
5. Verifikasi entri Create `Mosaic Brands {runId}-061` dengan Object `Brand` ada di System Log Rina Marlina
6. Logout, lalu login sebagai Total Control Client A (`totalControl_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`
7. Buka Global Settings > User > Detail Sari Dewi > Tab System Log
8. Verifikasi entri Create `Mosaic Brands {runId}-061` tidak muncul di System Log Sari Dewi

### TC-GS-BRAND-209: Bulk Delete homogen mencatat satu entri Delete per brand

9. Buka Global Settings > Master Reference > Brand
10. Ubah page size tabel menjadi 50, lalu centang baris `Iris Optics {runId}-061`, `Juniper Labs {runId}-061`, dan `Keystone Mfg {runId}-061`
11. Klik `Bulk Action` > `Delete`
12. Klik [Delete] pada dialog konfirmasi
13. Buka Changelog, filter Action `Delete`
14. Verifikasi Changelog memuat tiga entri Delete: `Iris Optics {runId}-061`, `Juniper Labs {runId}-061`, `Keystone Mfg {runId}-061`
15. Buka Global Settings > User > Detail Sari Dewi > Tab System Log
16. Verifikasi System Log memuat tiga entri Delete yang sama
17. Buka Global Settings > Activity Log
18. Verifikasi Activity Log memuat tiga entri Delete yang sama

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec: 215 lebih dulu karena memakai akun Create dan Read (satu kali ganti akun, langkah 6), lalu 209 yang menghapus data paling akhir (prinsip 5).
- Langkah penghubung: langkah 1, 9, dan 17 (membuka halaman Brand atau Activity Log sebelum aksi berikutnya) tidak tertulis di Langkah Uji TC sumber. Pada langkah 10, mengubah page size tabel menjadi 50 (agar ketiga brand tampil sekaligus untuk dicentang) juga tidak tertulis di Langkah Uji TC sumber; page size dipulihkan ke 10 di hook `after`.
- TC-GS-BRAND-215 Expected Result b ("Entri tidak muncul di System Log Sari Dewi", langkah 8) adalah asersi kepemilikan log per aktor, bukan asersi absence kelas g (konvensi bagian 3 prinsip 13g), sehingga berada di spec pencatatan ini.
- Nama brand pada TC sumber (`Iris Optics`, `Juniper Labs`, `Keystone Mfg`) adalah bagian Population D-01; spec memakai brand sendiri bersuffix agar tidak menghapus Population yang dibutuhkan spec lain.
- "Bulk Delete homogen" berarti ketiganya bebas relasi; kasus campuran (sebagian in-use) ada di spec `TC-GS-BRAND-E2E-062-log-absence-no-op-skip-cancel-dan-import`.
