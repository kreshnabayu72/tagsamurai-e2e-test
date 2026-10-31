---
id: TC-GS-PROFILE-E2E-057-sinkron-custom-field-siklus-hidup
title: "Sinkron Custom Field: Buat, Nonaktifkan, Aktifkan, Wajib, dan Hapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-254
  - TC-GS-PROFILE-255
  - TC-GS-PROFILE-256
  - TC-GS-PROFILE-257
  - TC-GS-PROFILE-259
coverage:
  web: automated
---

# Sinkron Custom Field: Buat, Nonaktifkan, Aktifkan, Wajib, dan Hapus

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Akun aktor: Pre-setup #1 (Andi Pratama, Total Control) `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_TC_PASSWORD`. Pelaku kedua admin: Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, hanya lewat sesi API.
- Env var: `GS_PROFILE_TC_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- Data Dinamis milik spec (S-06; Custom Field User Pre-setup #16 hanya dibaca dan tidak diubah). Custom Field User di bawah di-seed lewat sesi API admin di hook `before` (kemampuan seeding disediakan tim BE/FE), Andi Pratama diberi nilai lewat API, dan nama sengaja tidak memuat nama field Pre-setup #16 (R-13):

  | Kode | Nama | Tipe | Status awal | Nilai Andi Pratama | Dipakai oleh |
  |---|---|---|---|---|---|
  | CF-1 | `Blood Type {runId}-057` | Text, tidak Required | dibuat oleh langkah 1 (TC-GS-PROFILE-254) | belum ada | TC-GS-PROFILE-254 |
  | CF-2 | `Kebiasaan {runId}-057` | Text, tidak Required | aktif | `Reading` | TC-GS-PROFILE-255, 256, 257 |
  | CF-3 | `Catatan Kosong {runId}-057` | Text, tidak Required | aktif | kosong | TC-GS-PROFILE-259 |

- Cleanup (R-08): hook `after` menghapus CF-1, CF-2 (bila belum terhapus oleh langkah 24), dan CF-3 lewat sesi API admin tanpa berasumsi seeding berhasil penuh.
- State global yang diubah: Custom Field User milik spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-254: Custom Field baru dibuat dan aktif

1. Pelaku kedua admin (Pre-setup #6) membuat Custom Field CF-1 `Blood Type {runId}-057` (Text, aktif, tidak Required) lewat sesi API hingga perubahan tersimpan
2. Tunggu aksi selesai
3. Muat ulang My Profile (F5)
4. Klik header Section Custom Field untuk membuka Section
5. Verifikasi field `Blood Type {runId}-057` tampil di Section Custom Field pada urutan definisi
6. Verifikasi nilai field `Blood Type {runId}-057` adalah `—`

### TC-GS-PROFILE-255: Custom Field dinonaktifkan

7. Pelaku kedua admin menonaktifkan CF-2 `Kebiasaan {runId}-057` lewat sesi API hingga perubahan tersimpan
8. Tunggu aksi selesai
9. Muat ulang My Profile (F5)
10. Klik header Section Custom Field untuk membuka Section
11. Verifikasi field `Blood Type {runId}-057` tampil di Section Custom Field
12. Verifikasi field `Kebiasaan {runId}-057` tidak tampil di Section Custom Field

### TC-GS-PROFILE-256: Custom Field diaktifkan kembali

13. Pelaku kedua admin mengaktifkan CF-2 `Kebiasaan {runId}-057` lewat sesi API hingga perubahan tersimpan
14. Tunggu aksi selesai
15. Muat ulang My Profile (F5)
16. Klik header Section Custom Field untuk membuka Section
17. Verifikasi field `Kebiasaan {runId}-057` tampil dengan nilai `Reading`

### TC-GS-PROFILE-259: Custom Field diubah menjadi Required

18. Pelaku kedua admin mengubah CF-3 `Catatan Kosong {runId}-057` menjadi Required lewat sesi API hingga perubahan tersimpan
19. Tunggu aksi selesai
20. Muat ulang My Profile (F5)
21. Klik header Section Custom Field untuk membuka Section
22. Verifikasi field `Catatan Kosong {runId}-057` menampilkan alert `⚠ "Catatan Kosong {runId}-057 is required."`
23. Verifikasi nilai `—` tidak tampil pada field `Catatan Kosong {runId}-057`

### TC-GS-PROFILE-257: Custom Field dihapus

24. Pelaku kedua admin menghapus CF-2 `Kebiasaan {runId}-057` lewat sesi API hingga perubahan tersimpan
25. Tunggu aksi selesai
26. Muat ulang My Profile (F5)
27. Klik header Section Custom Field untuk membuka Section
28. Verifikasi field `Catatan Kosong {runId}-057` tampil di Section Custom Field
29. Verifikasi field `Kebiasaan {runId}-057` tidak tampil di Section Custom Field

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: TC-GS-PROFILE-257 (hapus) paling akhir (bagian 3 butir 5); TC-GS-PROFILE-255 mendahului 256 karena 256 memerlukan field yang baru dinonaktifkan; TC-GS-PROFILE-259 memakai CF-3 yang kosong sehingga tidak bergantung pada CF-2.
- Pelaku kedua admin memakai sesi API (bukan konteks kedua), sehingga tidak memakai butir `P-2`. TC menulis "Buka My Profile" sedangkan My Profile sudah dibuka hook `beforeEach`; spec memuat ulang halaman supaya definisi Custom Field terbaru dibaca.
- Penggantian nama (S-06): TC memakai nama field `Hobby` pada TC-GS-PROFILE-255, 256, 257, dan 259; spec memakai CF-2 `Kebiasaan {runId}-057` (TC-GS-PROFILE-255, 256, dan 257) dan CF-3 `Catatan Kosong {runId}-057` (TC-GS-PROFILE-259) milik spec.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2, 8, 14, 19, dan 25 (tunggu aksi selesai sebelum membaca di sesi UI), 3, 9, 15, 20, dan 26 (memuat ulang halaman, menggantikan "Buka My Profile").
- Asersi tambahan di luar Expected TC (S-03): langkah 11, 28 adalah pembanding (anchor) untuk absence field (8b butir 2).
- Temuan untuk QA:
  - TC-GS-PROFILE-255, 256, 257, dan 259 menonaktifkan, mengaktifkan, menghapus, dan mengubah menjadi Required Custom Field `Hobby` Pre-setup #16 yang juga dibaca TC-GS-PROFILE-17 sampai 20; spec memakai field milik spec bersuffix (S-06) sehingga nama dan teks alert pada Expected diganti nama field spec.
  - TC-GS-PROFILE-254 Expected "pada urutan definisi" tidak menyebut posisi; spec mengasersi field tampil di Section pada urutan definisi tanpa menetapkan nomor posisi.
  - TC-GS-PROFILE-256 mensyaratkan Custom Field nonaktif dengan nilai tersimpan `Reading`; spec memperolehnya dari urutan langkah 7 sampai 13 (nonaktif lalu aktif) pada CF-2 yang di-seed dengan nilai `Reading`.
