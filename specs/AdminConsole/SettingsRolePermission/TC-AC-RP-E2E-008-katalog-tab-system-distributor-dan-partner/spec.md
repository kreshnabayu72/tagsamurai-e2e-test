---
id: TC-AC-RP-E2E-008-katalog-tab-system-distributor-dan-partner
title: "Katalog Tab System per Entitas: Role yang Berlaku untuk Distributor dan Partner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-31
  - TC-AC-RP-32
  - TC-AC-RP-33
coverage:
  web: automated
---

# Katalog Tab System per Entitas: Role yang Berlaku untuk Distributor dan Partner

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor `totalControlDistRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Gilang Ramadhan`, entitas `Distributor Nusantara`), password dari `Spectra.env.AC_RP_DIST_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit pada langkah 5): Default User Partner `defaultUserPartRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Wulan Sari`, entitas `Partner Mandiri`), password dari `Spectra.env.AC_RP_PART_DU_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, `AC_RP_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #19 (`Distributor Nusantara` dengan Total Control `Gilang Ramadhan`; `Partner Mandiri` dengan Default User `Wulan Sari` sebagai satu-satunya user, pohon group hanya `Default Group`, tanpa assignment individual). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_DIST_TC_PASSWORD` dan `AC_RP_PART_DU_PASSWORD` adalah nama baru, dan `AC_RP_TC_PASSWORD` dipakai hook `after`; ketiganya harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-31: Katalog Distributor hanya menampilkan role yang berlaku

1. Klik tab `System`
2. Verifikasi section Global Role menampilkan 6 baris berurutan A-Z: `Manage device master data`, `Manage group`, `Manage hardware stock`, `Manage plans & licensing`, `Manage TAG stock`, `Manage user and role`
3. Verifikasi section Group Role menampilkan 5 baris: `Manage active client`, `Manage allocation`, `Manage archived client`, `Manage partner`, `Manage wallet & pricing`
4. Verifikasi role `Manage language`, `Manage presetup`, `Manage preload`, `Manage privacy policy`, `Manage distributor` tidak tampil sama sekali

### TC-AC-RP-32: Katalog Partner hanya menampilkan role yang berlaku

5. Logout dari akun `Gilang Ramadhan`
6. Login sebagai `Wulan Sari` (Default User Partner) dengan password dari `Spectra.env.AC_RP_PART_DU_PASSWORD`
7. Buka halaman `Settings > Role & Permission` lewat menu Settings di sidebar
8. Klik tab `System`
9. Verifikasi section Global Role menampilkan 3 baris: `Manage group`, `Manage plans & licensing`, `Manage user and role`
10. Verifikasi section Group Role menampilkan 4 baris: `Manage active client`, `Manage allocation`, `Manage archived client`, `Manage wallet & pricing`
11. Verifikasi `Manage TAG stock`, `Manage hardware stock`, `Manage partner`, `Manage distributor` tidak tampil

### TC-AC-RP-33: Role yang hanya dipegang Default User tetap tampil di Tab System

12. Verifikasi seluruh 7 role Partner tetap tampil di kedua section
13. Verifikasi Users bernilai "1" pada setiap role
14. Verifikasi daftar role tidak menyusut mengikuti jumlah penugasan

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Ganti akun eksplisit pada langkah 5: TC-AC-RP-31 mensyaratkan aktor Total Control entitas Distributor, TC-AC-RP-32 dan TC-AC-RP-33 mensyaratkan Default User entitas Partner. Login dan pembukaan halaman sesudahnya adalah langkah penghubung ganti akun (S-07).
- Absence pada TC-AC-RP-31 dan TC-AC-RP-32 memakai baris role yang tampil di section yang sama pada langkah sebelumnya sebagai anchor positif (8b butir 2).
- TC-AC-RP-33 memakai sesi dan halaman TC-AC-RP-32 (aktor, entitas, dan Tab System yang sama) sehingga tidak ada langkah buka halaman ulang; Precondition TC-AC-RP-33 (Default User sebagai satu-satunya pemegang tingkat akses, tanpa assignment individual) sama dengan data Pre-setup #19 yang dipakai TC-AC-RP-32. Verifikasi "daftar role tidak menyusut mengikuti jumlah penugasan" ditulis sebagai klausa Expected tersendiri tanpa data tambahan.
- Temuan untuk QA:
  - TC-AC-RP-33 Expected menyebut "7 role Partner" tetapi tidak merinci dua section; spec memakai 3 Global Role dan 4 Group Role dari TC-AC-RP-32 (jumlah yang sama, 7).
  - TC-AC-RP-33 tidak menyatakan cara mengamati bahwa daftar "tidak menyusut mengikuti jumlah penugasan" selain pembandingan jumlah baris dengan katalog; kriteria pembanding tidak dinyatakan TC.
