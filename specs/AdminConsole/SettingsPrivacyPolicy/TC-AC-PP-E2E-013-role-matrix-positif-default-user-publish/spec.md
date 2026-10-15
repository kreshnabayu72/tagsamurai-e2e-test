---
id: TC-AC-PP-E2E-013-role-matrix-positif-default-user-publish
title: "Role Matrix Positif: Default User Mengeksekusi Publish New Version"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-25
coverage:
  web: automated
---

# Role Matrix Positif: Default User Mengeksekusi Publish New Version

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-AC-PP-25 | Default User (tanpa Global Role "Manage privacy policy") | `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DU_PASSWORD` |

- Login akun Default User dilakukan di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; nama env `AC_DU_PASSWORD` dan `AC_TC_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`; selain `AC_TC_PASSWORD`, nama itu belum terdaftar.
- Dataset Riwayat A (Version 3 Active, 3 baris) di-seed di hook `before` lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat versi append-only sehingga `Version 4` hasil Publish tidak bisa dihapus lewat UI) dan hook `after` mengembalikan dataset ke Riwayat A.
- Suite berjalan serial (`parallel: false`) karena Publish mengubah dokumen Privacy Policy yang bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).

## Test Steps

### TC-AC-PP-25: Default User mengeksekusi Publish New Version sampai versi baru menjadi Active

1. Buka Settings > Privacy Policy
2. Klik `[⋯]` pada baris `Version 3`
3. Pilih `Edit`
4. Tunggu konten termuat
5. Klik di akhir konten editor
6. Ketik " Updated by Default User."
7. Klik `[Publish New Version]`
8. Klik `[Publish]` pada Dialog Publish Confirm
9. Verifikasi muncul toast sukses: "Success, Privacy Policy has been published."
10. Verifikasi Dialog Publish Confirm tertutup
11. Verifikasi Modal tertutup
12. Verifikasi tabel menampilkan `Version 4` dengan badge `Active` di baris teratas
13. Verifikasi badge `Active` pada `Version 3` tidak ada lagi

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Spec Role Matrix positif (bagian 3a konvensi) untuk satu role, dipisah dari spec positif Read Only karena spec ini membuat data (Version 4) dan mengubah state global.
- Tidak ada langkah penghubung.
- Temuan untuk QA: Post Condition TC-AC-PP-25 (Version 4 tersimpan dengan Published By nama Default User; satu record audit Publish tercatat) tidak punya langkah observasi sehingga tidak diasersi. Pre-setup TC (baris 3) tidak memberi nama tampil untuk akun Default User sehingga nilai sel Published By pada `Version 4` tidak dapat dituliskan; Expected TC juga tidak mengasersinya.
