---
id: TC-AC-RP-E2E-106-konsumen-grup-gm-dan-group-role-exact-match
title: "Modul Konsumen: Wewenang GM atas Descendant, Group Role Exact Match, dan Peran Tanpa Penugasan Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-354
  - TC-AC-RP-355
  - TC-AC-RP-356
coverage:
  web: automated
---

# Modul Konsumen: Wewenang GM atas Descendant, Group Role Exact Match, dan Peran Tanpa Penugasan Group

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor pertama: Group Manager Principal `groupManagerRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Fajar Nugroho`, Pre-setup #6), password dari `Spectra.env.AC_RP_GM_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor ganti akun eksplisit (S-07): Standard `Alex Tan` (Group Role `Manage distributor` di `Region A` saja, Read; Pre-setup #15) pada langkah 5 dan Standard `Sarah Kimura` (peran `Manage partner` aktif tanpa penugasan group; Pre-setup #15) pada langkah 9. Email dan password kedua akun tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (user Standard), #14 dan #15 (penugasan GM dan peran individual), #16 (`Distributor Jakarta` di group `Jakarta`, anak `Region Jawa`; Distributor di `Region A` dan `Branch 1`), dan #26 (menu Distributor dan Partner).
- Data Dinamis: spec ini tidak membuat entitas baru dan tidak mengubah data Pre-setup (hanya membaca), sehingga suffix `+{runId}-106` dan pemulihan baseline tidak dibutuhkan.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_GM_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`) karena suite memakai state Pre-setup bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-354: GM di ancestor mengelola data descendant dengan CRUD penuh

1. Buka menu Distributor
2. Buka baris `Distributor Jakarta`
3. Verifikasi `Distributor Jakarta` tampil
4. Verifikasi aksi Edit dan Suspend tersedia walau `Fajar Nugroho` tidak di-assign langsung di `Jakarta`

### TC-AC-RP-355: Group Role exact match tidak diwariskan ke sub-group

5. Ganti akun: logout, lalu login sebagai Group Role `Manage distributor` di `Region A` saja `Alex Tan`
6. Buka menu Distributor
7. Verifikasi Distributor di `Region A` tampil
8. Verifikasi Distributor di `Branch 1` tidak tampil

### TC-AC-RP-356: Peran aktif tanpa penugasan grup tidak memberi akses

9. Ganti akun: logout, lalu login sebagai Group Role `Manage partner` aktif tanpa penugasan group `Sarah Kimura`
10. Buka menu Partner
11. Verifikasi halaman menu Partner termuat (Breadcrumb tampil)
12. Verifikasi tidak ada data Partner tampil
13. Verifikasi aksi diblokir (zero assignment = zero access)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dipertahankan; ganti akun terjadi pada awal TC-AC-RP-355 dan TC-AC-RP-356 (S-07).
- Pembanding absence (bagian 8b butir 2): Distributor di `Region A` tampil sebelum asersi Distributor di `Branch 1` tidak tampil; Breadcrumb menu Partner tampil sebelum asersi tidak ada data Partner (`Verifikasi` Breadcrumb ditambahkan sebagai anchor; S-03).
- Temuan untuk QA:
  - Email dan password `Alex Tan` dan `Sarah Kimura` sebagai aktor login tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - TC-AC-RP-356 Expected "Tidak ada data Partner tampil dan aksi diblokir" tidak menyebut bentuk keadaan (empty state, halaman 403, atau menu tersembunyi) dan tidak menyebut aksi yang diblokir; spec mengasersi dua klausa itu apa adanya dan menambah `Verifikasi` Breadcrumb sebagai anchor.
  - TC-AC-RP-354 langkah "Buka baris `Distributor Jakarta`" tidak menyebut dialog atau halaman Detail; spec mengasersi aksi Edit dan Suspend sesuai Expected pada baris itu.
  - TC-AC-RP-355 langkah dan Expected tidak menyebut jumlah Distributor di `Region A`; spec hanya mengasersi tampil atau tidak tampil.
