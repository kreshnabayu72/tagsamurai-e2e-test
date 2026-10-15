---
id: TC-AUTH-LP-E2E-026-agreement-policy-version-change
title: "Versi Privacy Policy Berubah Saat Layar Confirm to Continue Terbuka"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-87
coverage:
  web: automated
---

# Versi Privacy Policy Berubah Saat Layar Confirm to Continue Terbuka

## Prerequisites

- Seeding: user subjek Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`; autentikasi API, bukan sesi browser). User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-026` (contoh `ninamarlina+{runId}-026@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Akun aktor kedua: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`, berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sesi browser terpisah (jendela privat pertama untuk user subjek, jendela privat kedua untuk Principal); reCAPTCHA mode uji di environment; seeding user dengan versi Privacy Policy yang disetujui lebih lama dari versi aktif (versi A), device terpercaya, dan tidak memicu MFA; konten versi Privacy Policy baru (versi B) yang dipublikasikan pada tiap run.
- State global Privacy Policy: publish bersifat append-only dan immutable tanpa restore (`ACPP-LOGIC-01`), sehingga versi aktif tidak dipulihkan dan naik pada setiap run; suite berjalan serial. Seeding user Agreement selalu relatif terhadap versi aktif saat hook `before` (versi yang disetujui user = versi sebelum versi aktif), tanpa nomor versi absolut. Publikasi versi B menjadi versi aktif; user subjek dihapus di hook `after` (tetap jalan walau spec gagal) sehingga persetujuan versi B ikut hilang.
- Mode: FE+BE
- TC-AUTH-LP-87: Tanpa login pada jendela pertama (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-LP-87: User `Nina Marlina` (`ninamarlina+{runId}-026@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif (versi A) lebih baru dari versi terakhir yang disetujui; device terpercaya (di-seed lewat API di hook `before`)
- TC-AUTH-LP-87 data: Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-87: Versi Privacy Policy berubah saat layar terbuka memuat ulang layar Confirm to Continue

1. Buka jendela privat baru (jendela pertama, tanpa sesi login)
2. Buka halaman Login with Password
3. Isi Email `ninamarlina+{runId}-026@qwertysystem.net` dan Password nilai `Spectra.env.LP_PASSWORD`
4. Selesaikan reCAPTCHA
5. Klik [Log in] → layar Confirm to Continue (versi A) tampil
6. Centang checkbox persetujuan
7. Ganti akun: buka jendela privat kedua (sesi terpisah), buka halaman Login with Password, login sebagai Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.AC_PRINCIPAL_PP_PASSWORD` dan selesaikan reCAPTCHA, lalu buka `Admin Console > Settings > Privacy Policy`
8. Publikasikan versi Privacy Policy baru (versi B)
9. Kembali ke jendela pertama pada layar Confirm to Continue (versi A)
10. Klik [Continue ➔]
11. Verifikasi layar Confirm to Continue dimuat ulang dengan konten versi B
12. Verifikasi checkbox persetujuan kembali unchecked
13. Verifikasi browser tidak menuju Portal — Product Hub
14. Centang checkbox persetujuan
15. Klik [Continue ➔]
16. Verifikasi browser menuju Portal — Product Hub
17. Logout dari Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Kelas harness: multi-konteks (prinsip 13c), dua sesi dan dua aktor. Penolakan karena versi berubah tanpa pencatatan log (TC-AUTH-LP-122) diuji di spec `TC-AUTH-LP-E2E-044-absence-policy-version-change` (kelas g, prinsip 10); asersi absence tidak ditulis di spec ini (S-05).
- Langkah 17 (logout) adalah langkah penghubung tanpa awalan `Verifikasi` (S-03; S-09). Post Condition TC ("Persetujuan Privacy Policy … tersimpan untuk versi B") tidak diasersi karena TC tidak punya langkah observasinya (S-01).
- Langkah "Di sesi browser lain, login sebagai Principal dan publikasikan versi … baru" pada TC sumber diperinci menjadi langkah 7–8 dengan langkah ganti akun eksplisit (S-07).
- Temuan untuk QA:
  - TC-AUTH-LP-87 tidak menyebut cara menyiapkan konten versi B; spec menuliskannya sebagai kemampuan fixture BE di Prerequisites tanpa endpoint (S-13).
  - Post Condition TC-AUTH-LP-87 ("Persetujuan Privacy Policy … tersimpan untuk versi B") tidak punya langkah observasi atau Expected padanan di TC, jadi spec tidak mengasersinya; perlu Expected padanan atau langkah observasi dari tim QA.
