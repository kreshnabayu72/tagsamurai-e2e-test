---
id: TC-AC-RP-E2E-016-guided-tooltip-replay-guide
title: "Guided Tooltip: Tombol Replay Guide dan Tour per Tab Aktif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-65
  - TC-AC-RP-66
  - TC-AC-RP-67
coverage:
  web: automated
---

# Guided Tooltip: Tombol Replay Guide dan Tour per Tab Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit pada langkah 12): Read Only Principal `readOnlyRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Anggraini`), password dari `Spectra.env.AC_RP_RO_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission` mengikuti hook suite (disetel `seen` untuk akun aktor dan dipulihkan di `after`, lihat `suite.md`). TC tidak menyatakan keadaan flag; tombol `[?]` memutar ulang guide pada flag `seen`, dan spec tidak mengubah flag. Kemampuan membaca dan menyetel flag disediakan tim FE/BE.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` dan `AC_RP_RO_PASSWORD` adalah nama baru; keduanya harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-65: Tombol replay guide di kanan Breadcrumb

1. Hover tombol `[?]` di kanan Breadcrumb
2. Verifikasi tooltip hover "Show guide" tampil

### TC-AC-RP-66: Replay guide menampilkan Step 1 dan Step 2

3. Klik tombol `[?]`
4. Verifikasi Step 1 menyorot tab switcher
5. Verifikasi Step 1 menampilkan Title "How access works"
6. Verifikasi Step 1 menampilkan Description "Each tab shows a different way users get access. Switch tabs to see who has it."
7. Klik tombol lanjut pada tooltip
8. Verifikasi Step 2 menyorot header kolom Actions `[⋯]`
9. Verifikasi Step 2 menampilkan Title "Manage access"
10. Verifikasi Step 2 menampilkan Description "Use the actions on each row to change or review access."
11. Tutup tour guide

### TC-AC-RP-67: Tour dimulai di tab yang sedang aktif bagi aktor Read Only

12. Logout dari akun `Siti Nurhaliza`
13. Login sebagai `Dewi Anggraini` (Read Only) dengan password dari `Spectra.env.AC_RP_RO_PASSWORD`
14. Buka halaman `Settings > Role & Permission` lewat menu Settings di sidebar
15. Klik tab `System`
16. Klik tombol `[?]`
17. Verifikasi tour berjalan pada Tab System yang sedang aktif
18. Verifikasi Step 1 menyorot tab switcher dan target tampil bagi aktor Read Only
19. Klik tombol lanjut pada tooltip
20. Verifikasi Step 2 menyorot header kolom Actions dan target tampil bagi aktor Read Only
21. Tutup tour guide

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus. Hook `beforeEach` suite membuka halaman; spec ini menguji tombol `[?]` sehingga tidak ada tour otomatis yang diasersi.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Ganti akun eksplisit pada langkah 12: TC-AC-RP-67 mensyaratkan aktor Read Only sedangkan TC-AC-RP-65 dan TC-AC-RP-66 mensyaratkan Total Control. Login, pembukaan halaman, dan klik tab sesudahnya adalah langkah penghubung ganti akun (S-07).
- Langkah penghubung tanpa awalan Verifikasi (S-03): menutup tour guide pada langkah 11 dan 21 agar tidak ada overlay tour yang menutupi aksi berikutnya; kontrol penutup tour tidak didefinisikan TC (lihat Temuan untuk QA).
- Temuan untuk QA:
  - TC-AC-RP-65 sampai TC-AC-RP-67 tidak menyatakan keadaan flag Guided Tooltip akun aktor maupun cara menutup tour; spec memakai flag `seen` dari hook suite dan langkah "Tutup tour guide" tanpa menyebut kontrol.
  - TC-AC-RP-66 menyebut "tombol lanjut pada tooltip" tanpa label; spec memakai istilah itu persis.
  - TC-AC-RP-67 Expected menggabungkan tiga klausa ("tour berjalan pada Tab System", "Step 1 menyorot tab switcher dan Step 2 header Actions", "kedua target tampil bagi aktor Read Only"); spec memecahnya per langkah tour (S-01) dan menyatakan target tampil pada tiap langkah.
  - TC-AC-RP-67 tidak menyatakan Title dan Description Step 1 dan Step 2 untuk aktor Read Only; hanya target sorotan yang diasersi.
