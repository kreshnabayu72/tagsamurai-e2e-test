---
id: TC-AC-RP-E2E-002-screening-tab-total-control-row-action-disabled
title: "Screening Tab Total Control: Overlay Row Action dan Remove Disabled dengan Tooltip"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-7
  - TC-AC-RP-8
  - TC-AC-RP-9
  - TC-AC-RP-10
coverage:
  web: automated
---

# Screening Tab Total Control: Overlay Row Action dan Remove Disabled dengan Tooltip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal) dan #13 (pemegang tingkat akses: baris `John Doe`, `Bambang Hartono` sebagai Default User, dan `Siti Nurhaliza` sebagai diri sendiri). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: aksi `Remove` tidak pernah dijalankan (hanya overlay dibuka dan tooltip diamati); tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Kemampuan teknis: pengamatan fokus keyboard dan tooltip on-focus (TC-AC-RP-10) memakai tombol Tab pada browser.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-7: Overlay row action Tab Total Control hanya berisi Remove

1. Klik ikon `⋯` pada baris `John Doe`
2. Verifikasi overlay row action memuat tepat satu aksi `Remove` (ikon `DeleteBin6Line`, severity danger)
3. Verifikasi tidak ada aksi Detail pada overlay
4. Tutup overlay row action

### TC-AC-RP-8: Remove pada baris Default User tampil Disabled dengan tooltip

5. Klik ikon `⋯` pada baris `Bambang Hartono`
6. Hover aksi `Remove`
7. Verifikasi aksi `Remove` tampil di overlay dalam keadaan Disabled
8. Verifikasi tooltip "Default User cannot be modified." tampil
9. Klik aksi `Remove`
10. Verifikasi tidak ada dialog yang terbuka
11. Tutup overlay row action

### TC-AC-RP-9: Remove pada baris diri sendiri tampil Disabled dengan tooltip

12. Klik ikon `⋯` pada baris `Siti Nurhaliza`
13. Hover aksi `Remove`
14. Verifikasi aksi `Remove` tampil Disabled
15. Verifikasi tooltip "You can't manage your own account from here." tampil
16. Klik aksi `Remove`
17. Verifikasi tidak ada dialog yang terbuka
18. Tutup overlay row action

### TC-AC-RP-10: Disabled Remove dapat difokus keyboard dan tooltip muncul on-focus

19. Buka overlay `⋯` baris `Bambang Hartono`
20. Pindahkan fokus ke aksi `Remove` dengan tombol Tab, tanpa hover
21. Verifikasi aksi `Remove` Disabled menerima fokus keyboard
22. Verifikasi tooltip "Default User cannot be modified." muncul saat fokus
23. Tutup overlay row action

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): menutup overlay pada langkah 4, 11, 18, dan 23 agar tiap TC mulai dari tabel tanpa overlay terbuka (S-09).
- Pada TC-AC-RP-8 dan TC-AC-RP-9 tooltip diasersi sebelum klik aksi `Remove` Disabled (8b.5: state sementara tepat waktu); urutan Expected TC (Disabled, tooltip, klik tidak membuka dialog) tetap.
- Temuan untuk QA:
  - TC-AC-RP-10 tidak menyatakan cara mengosongkan hover mouse sebelum fokus keyboard; spec menulis "tanpa hover" pada langkah fokus dan memakai pointer yang tidak berada di atas aksi `Remove`.
  - TC-AC-RP-7 Expected tidak menyatakan apakah baris `Siti Nurhaliza` dan `Bambang Hartono` memuat aksi tambahan; hanya baris `John Doe` diasersi.
