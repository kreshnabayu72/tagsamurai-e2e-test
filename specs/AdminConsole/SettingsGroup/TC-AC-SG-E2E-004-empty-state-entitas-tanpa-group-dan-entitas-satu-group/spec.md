---
id: TC-AC-SG-E2E-004-empty-state-entitas-tanpa-group-dan-entitas-satu-group
title: "Empty State Entitas Tanpa Group dan Entitas dengan Satu Group"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-12
  - TC-AC-SG-14
coverage:
  web: automated
---

# Empty State Entitas Tanpa Group dan Entitas dengan Satu Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (TC-AC-SG-12): Total Control `Distributor Tanpa Group` (Pre-setup #41) `totalControlTanpaGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_TANPAGROUP_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (TC-AC-SG-14): Total Control `Distributor Satu Group` (Pre-setup #22) `totalControlSatuGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_SATU_PASSWORD`; dipakai lewat langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env `AC_SG_TANPAGROUP_PASSWORD` dan `AC_SG_SATU_PASSWORD`: pendaftaran mengikuti `suite.md`.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite untuk kedua akun UI (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Distributor Tanpa Group` tanpa satu pun group selain root `All Groups` (#41; kondisi seed onboarding gagal, tidak normal) dan `Distributor Satu Group` yang hanya berisi `Default Group` (#22).
- Kemampuan teknis: keadaan entitas `Distributor Tanpa Group` (0 group) dijaga oleh Fixture BE, disediakan tim FE/BE (lihat `suite.md`); pembentukannya tidak dijelaskan TC (lihat Temuan untuk QA).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-004`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-12: Tabel utama genuinely empty sebagai pengaman bila seed onboarding gagal (0 group)

1. Perhatikan area tabel dan Sidebar Group Tree
2. Verifikasi tabel menampilkan empty state dengan Illustration, Title "No group yet", dan Description "Get started by creating your first group."
3. Verifikasi tidak ada baris tabel
4. Verifikasi sidebar menampilkan "All Groups (0)" (root "All Groups" tidak dihitung sebagai group)
5. Verifikasi tidak ada pemulihan otomatis: tidak ada group yang dibuat sendiri

### TC-AC-SG-14: Entitas dengan satu group menampilkan satu baris, bukan empty state

6. Ganti akun: logout, login sebagai Total Control `Distributor Satu Group` (`totalControlSatuGroup_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_SG_SATU_PASSWORD`)
7. Buka halaman `Settings > Group` lewat sidebar
8. Amati tabel dan sidebar
9. Verifikasi tabel menampilkan tepat 1 baris `Default Group`
10. Verifikasi tidak ada empty state pada tabel
11. Verifikasi sidebar menampilkan "All Groups (1)"
12. Verifikasi sidebar menampilkan satu node anak `Default Group`

## Notes

- Langkah penghubung (S-03, S-07): langkah 1 dan 8 mengamati tanpa asersi sendiri; langkah 6 dan 7 mengganti akun dan membuka halaman sebagai akun kedua. Hook `beforeEach` suite membuka halaman hanya untuk akun pertama.
- Dua blok memakai akun berbeda (entitas lain) sehingga dipisah sebagai dua blok dengan ganti akun eksplisit; keduanya baca-saja.
- Asersi absence langkah 3 dan 5 berjangkar pada empty state yang tampil (langkah 2) dan sidebar "All Groups (0)" (langkah 4); langkah 10 berjangkar pada baris `Default Group` (langkah 9) (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-SG-12 precondition d ("seed onboarding disimulasikan gagal") tidak menjelaskan cara membentuk keadaan itu, dan TC bertanda `Manual Only`; Pre-setup #41 menyebut entitas sudah tersedia. Spec memakainya sebagai keadaan entitas yang dijaga Fixture BE (disediakan tim FE/BE) tanpa endpoint karangan (S-13).
  - TC-AC-SG-12 Expected b "tidak ada pemulihan otomatis (group tidak dibuat sendiri)" tidak punya langkah observasi di TC (misalnya menunggu atau memuat ulang); spec mengasersinya pada halaman yang sama tanpa menambah langkah (langkah 5).
