---
id: TC-GS-PROFILE-E2E-058-sinkron-custom-field-tipe-nama-dan-dropdown
title: "Sinkron Custom Field: Ganti Data Type, Rename Field, Rename dan Hapus Value Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-258
  - TC-GS-PROFILE-319
  - TC-GS-PROFILE-320
  - TC-GS-PROFILE-321
coverage:
  web: automated
---

# Sinkron Custom Field: Ganti Data Type, Rename Field, Rename dan Hapus Value Dropdown

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Akun aktor: Pre-setup #1 (Andi Pratama, Total Control) `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_TC_PASSWORD`. Pelaku kedua admin: Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, hanya lewat sesi API.
- Env var: `GS_PROFILE_TC_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- Data Dinamis milik spec (S-06; Custom Field User Pre-setup #16 termasuk varian `Shirt Size` hanya dibaca dan tidak diubah). Custom Field User di bawah di-seed lewat sesi API admin di hook `before` (kemampuan seeding disediakan tim BE/FE), nilai Andi Pratama diberikan lewat API, dan nama sengaja tidak memuat nama field atau nilai Pre-setup #16 (R-13):

  | Kode | Nama | Tipe | Nilai Andi Pratama | Perubahan oleh spec | Dipakai oleh |
  |---|---|---|---|---|---|
  | CF-1 | `Tipe Uji {runId}-058` | Text, aktif, tidak Required | `Reading` | Data Type diganti ke Numeric | TC-GS-PROFILE-258 |
  | CF-2 | `Nama Awal {runId}-058` | Text, aktif, tidak Required | `Reading` | Field Name diganti menjadi `Nama Baru {runId}-058` | TC-GS-PROFILE-319 |
  | CF-3 | `Ukuran A {runId}-058` | Dropdown aktif, opsi `Small`, `Medium`, `Large`, tidak Required | `Medium` | value `Medium` diubah menjadi `Regular` | TC-GS-PROFILE-320 |
  | CF-4 | `Ukuran B {runId}-058` | Dropdown aktif, opsi `Small`, `Medium`, `Large`, tidak Required | `Medium` | value `Medium` dihapus | TC-GS-PROFILE-321 |

- Cleanup (R-08): hook `after` menghapus CF-1 sampai CF-4 (CF-2 dengan nama `Nama Baru {runId}-058` bila sudah di-rename) lewat sesi API admin tanpa berasumsi seeding berhasil penuh.
- State global yang diubah: Custom Field User milik spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-258: Data Type Custom Field diganti

1. Pelaku kedua admin (Pre-setup #6) mengganti Data Type CF-1 `Tipe Uji {runId}-058` dari Text ke Numeric lewat sesi API hingga perubahan tersimpan
2. Tunggu aksi selesai
3. Muat ulang My Profile (F5)
4. Klik header Section Custom Field untuk membuka Section
5. Verifikasi field `Tipe Uji {runId}-058` tampil dengan nilai `—`

### TC-GS-PROFILE-319: Field Name Custom Field di-rename

6. Pelaku kedua admin mengubah Field Name CF-2 dari `Nama Awal {runId}-058` menjadi `Nama Baru {runId}-058` lewat sesi API hingga perubahan tersimpan
7. Tunggu aksi selesai
8. Muat ulang My Profile (F5)
9. Klik header Section Custom Field untuk membuka Section
10. Verifikasi Section Custom Field menampilkan label `Nama Baru {runId}-058` dengan nilai `Reading`
11. Verifikasi label `Nama Awal {runId}-058` tidak tampil

### TC-GS-PROFILE-320: Value Dropdown di-rename

12. Pelaku kedua admin mengubah value `Medium` pada CF-3 `Ukuran A {runId}-058` menjadi `Regular` lewat sesi API hingga perubahan tersimpan
13. Tunggu aksi selesai
14. Muat ulang My Profile (F5)
15. Klik header Section Custom Field untuk membuka Section
16. Verifikasi field `Ukuran A {runId}-058` menampilkan nilai `Regular`
17. Verifikasi nilai `Medium` tidak tampil pada field `Ukuran A {runId}-058`

### TC-GS-PROFILE-321: Value Dropdown dihapus

18. Pelaku kedua admin menghapus value `Medium` dari CF-4 `Ukuran B {runId}-058` (konfirmasi `[Remove]` dan `[Save]` setara) lewat sesi API hingga perubahan tersimpan
19. Tunggu aksi selesai
20. Muat ulang My Profile (F5)
21. Klik header Section Custom Field untuk membuka Section
22. Verifikasi field `Ukuran B {runId}-058` menampilkan nilai `—`

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: TC-GS-PROFILE-321 (menghapus value) paling akhir (bagian 3 butir 5); tiap TC memakai Custom Field sendiri sehingga tidak bergantung pada hasil TC lain.
- Pelaku kedua admin memakai sesi API (bukan konteks kedua), sehingga tidak memakai butir `P-2`. TC menulis "Buka My Profile" sedangkan My Profile sudah dibuka hook `beforeEach`; spec memuat ulang halaman supaya definisi Custom Field terbaru dibaca.
- Penggantian nama (S-06): TC memakai `Hobby` (TC-GS-PROFILE-258 dan 319), `Pastime` (319), dan `Shirt Size` dengan value `Medium` dan `Regular` (TC-GS-PROFILE-320 dan 321); spec memakai CF-1 sampai CF-4 milik spec. Nama value `Small`, `Medium`, `Large`, dan `Regular` mengikuti TC.
- Langkah 17 diasersi pada field `Ukuran A {runId}-058` saja karena field `Ukuran B {runId}-058` masih bernilai `Medium` pada saat itu.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2, 7, 13, dan 19 (tunggu aksi selesai sebelum membaca di sesi UI), 3, 8, 14, dan 20 (memuat ulang halaman, menggantikan "Buka My Profile").
- Asersi tambahan di luar Expected TC (S-03): langkah 10 menjadi pembanding (anchor) untuk absence label lama pada langkah 11, dan langkah 16 untuk absence nilai pada langkah 17 (8b butir 2).
- Temuan untuk QA:
  - TC-GS-PROFILE-258, 319, 320, dan 321 mengubah Custom Field Pre-setup #16 (`Hobby`, `Shirt Size`) yang juga dibaca TC lain di section yang sama; spec memakai field milik spec bersuffix (S-06) sehingga nama field pada Expected diganti nama field spec.
  - TC-GS-PROFILE-321 menyebut aksi lewat popup Edit Custom Field (klik `x`, `[Remove]`, `[Save]`) di UI admin sedangkan spec memakai sesi API admin sebagai pemicu perubahan state; mekanisme API ditentukan tim FE.
  - TC-GS-PROFILE-258 menyatakan nilai lama "direset" tanpa cara mengamati nilai lama; spec mengasersi nilai `—` pada field.
