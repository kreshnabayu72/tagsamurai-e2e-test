---
id: TC-AUTH-ACT-E2E-031-pemicu-email-distributor-partner
title: "Activation Email dari Pembuatan Distributor dan Partner di Admin Console"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-138
  - TC-AUTH-ACT-139
coverage:
  web: automated
---

# Activation Email dari Pembuatan Distributor dan Partner di Admin Console

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: mail-catcher uji yang dapat dibaca spec (API inbox per alamat); jendela privat browser terpisah dari sesi Admin Console.
- Akun aktor: login sbg Role: Total Control (Admin Console), pre-setup `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (baris 2 Tabel Data Uji Pre-setup); kredensial dari environment variable `AC_TC_PASSWORD` (`Spectra.env.AC_TC_PASSWORD`). Login dilakukan di hook `before`.
- Data yang dibuat lewat UI di spec, semuanya bersuffix per run `{runId}-031`:
  - TC-AUTH-ACT-138: Distributor `PT Mitra Distribusi Baru {runId}-031` dengan Default User `Galang Prakasa` (`galangprakasa+{runId}-031@qwertysystem.net`).
  - TC-AUTH-ACT-139: Partner `PT Rekan Solusi Baru {runId}-031` dengan Default User `Hana Wijayanti` (`hanawijayanti+{runId}-031@qwertysystem.net`).
- Hook `after`: hapus Distributor dan Partner di atas beserta Default User masing-masing (lewat API Admin Console). Hook ini tetap jalan walau pembuatan gagal sebagian dan tidak berasumsi pembuatan berhasil penuh.
- Tanpa login pada jendela privat untuk membuka link aktivasi (halaman publik).

## Test Steps

### TC-AUTH-ACT-138: Membuat Distributor di Admin Console memicu Activation Email ke Default User

1. Di Admin Console, jalankan alur pembuatan Distributor baru `PT Mitra Distribusi Baru {runId}-031` dengan Default User Name `Galang Prakasa`, Email `galangprakasa+{runId}-031@qwertysystem.net`, isi field wajib lainnya sesuai form Create Distributor, lalu klik [Submit]
2. Verifikasi Distributor `PT Mitra Distribusi Baru {runId}-031` dan Default User `Galang Prakasa` terbentuk
3. Buka inbox `galangprakasa+{runId}-031@qwertysystem.net` di mail-catcher dan baca email aktivasi yang diterima
4. Verifikasi Email dengan Subject "Activate your TAG Samurai account" diterima di inbox `galangprakasa+{runId}-031@qwertysystem.net`
5. Buka jendela privat baru (tanpa sesi Admin Console), lalu buka link [Activate Account] dari email tersebut di jendela itu
6. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for galangprakasa+{runId}-031@qwertysystem.net." (alur aktivasi identik dengan user buatan Global Settings > User)
7. Verifikasi Token aktivasi Default User `Galang Prakasa` Active dan status user Pending Activation

### TC-AUTH-ACT-139: Membuat Partner di Admin Console memicu Activation Email ke Default User

8. Di Admin Console, jalankan alur pembuatan Partner baru `PT Rekan Solusi Baru {runId}-031` dengan Default User Name `Hana Wijayanti`, Email `hanawijayanti+{runId}-031@qwertysystem.net`, isi field wajib lainnya sesuai form Create Partner, lalu klik [Submit]
9. Verifikasi Partner `PT Rekan Solusi Baru {runId}-031` dan Default User `Hana Wijayanti` terbentuk
10. Buka inbox `hanawijayanti+{runId}-031@qwertysystem.net` di mail-catcher dan baca email aktivasi yang diterima
11. Verifikasi Email dengan Subject "Activate your TAG Samurai account" diterima di inbox `hanawijayanti+{runId}-031@qwertysystem.net`
12. Buka jendela privat baru (tanpa sesi Admin Console), lalu buka link [Activate Account] dari email tersebut di jendela itu
13. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for hanawijayanti+{runId}-031@qwertysystem.net." (alur aktivasi identik dengan user buatan Global Settings > User)
14. Verifikasi Token aktivasi Default User `Hana Wijayanti` Active dan status user Pending Activation

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness d (mail-catcher). Dipisah dari E2E-025 (Client + Resend) supaya E2E-025 tidak melewati sekitar 35 langkah dan cleanup Distributor/Partner tidak bercampur dengan cleanup Client (Cancel Subscription, Auto-Archive).
- Kolom Automation kedua TC sumber bernilai Manual Only; sesuai bagian 2 konvensi itu bukan alasan mengeluarkan TC, jadi kebutuhan mail-catcher dan pembuatan entitas ditulis di Prerequisites.
- Untuk QA: TC sumber tidak merinci field wajib form Create Distributor/Partner dan menyatakan email terkirim setelah entitas dibuat, sedangkan TC-AUTH-ACT-12 (Client) mengikuti `ACC-LOGIC-05.2` yaitu email terkirim saat subscription pertama Active. Perlu dipastikan pemicu Distributor/Partner memang berbeda dari Client; langkah 1 dan 8 memakai teks "isi field wajib lainnya" sampai field-nya dirinci.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
