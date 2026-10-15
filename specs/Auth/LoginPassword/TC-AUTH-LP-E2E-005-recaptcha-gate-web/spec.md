---
id: TC-AUTH-LP-E2E-005-recaptcha-gate-web
title: "Gate Google reCAPTCHA v2 pada Login Web"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-24
  - TC-AUTH-LP-25
  - TC-AUTH-LP-26
coverage:
  web: automated
---

# Gate Google reCAPTCHA v2 pada Login Web

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dengan status Activated dan Active, hitungan gagal 0. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-005` (contoh `jokosusilo+{runId}-005@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: reCAPTCHA di environment yang dapat diselesaikan otomatis (mode uji) dan token yang dapat dibiarkan kedaluwarsa sehingga widget kembali Unsolved (TC-AUTH-LP-25); kedaluwarsa token dipenuhi dengan memajukan jam browser/klien melebihi durasi kedaluwarsa token reCAPTCHA environment; kemampuan memajukan jam browser disediakan tim FE (bukan menunggu nyata), dan durasi tepatnya disediakan tim FE/BE. Jam browser dipulihkan ke waktu nyata di hook `after`.
- TC-AUTH-LP-24: Tanpa login (guest); browser web
- TC-AUTH-LP-24: User `Joko Susilo` (`jokosusilo+{runId}-005@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 (di-seed lewat API di hook `before`)
- TC-AUTH-LP-24 data: Email: `jokosusilo+{runId}-005@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-26: Tanpa login (guest); browser web
- TC-AUTH-LP-26: User `Joko Susilo` (`jokosusilo+{runId}-005@qwertysystem.net`, sama seperti TC-AUTH-LP-24), hitungan gagal 0
- TC-AUTH-LP-26 data: Email: `jokosusilo+{runId}-005@qwertysystem.net`; Password: (kosong)
- TC-AUTH-LP-25: Tanpa login (guest); browser web
- TC-AUTH-LP-25: User `Joko Susilo` (`jokosusilo+{runId}-005@qwertysystem.net`, sama seperti TC-AUTH-LP-24), hitungan gagal 0
- TC-AUTH-LP-25 data: Email: `jokosusilo+{runId}-005@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-24: Submit tanpa menyelesaikan reCAPTCHA (web)

1. Buka halaman Login with Password
2. Isi field Email dengan "jokosusilo+{runId}-005@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
3. Tanpa menyelesaikan reCAPTCHA, klik [Log in]
4. Verifikasi caption "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
5. Verifikasi widget reCAPTCHA berstatus Unsolved
6. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-26: Submit dengan Password kosong dan reCAPTCHA belum diselesaikan

7. Muat ulang halaman Login with Password
8. Isi field Email dengan "jokosusilo+{runId}-005@qwertysystem.net", kosongkan field Password, dan jangan selesaikan reCAPTCHA
9. Klik [Log in]
10. Verifikasi caption "Password must not be empty" tampil di bawah field Password
11. Verifikasi caption "Please verify that you are not a robot" tidak tampil
12. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-25: Submit dengan token reCAPTCHA yang sudah kedaluwarsa (web)

13. Muat ulang halaman Login with Password
14. Isi field Email dengan "jokosusilo+{runId}-005@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
15. Selesaikan reCAPTCHA
16. Majukan jam browser melebihi durasi kedaluwarsa token reCAPTCHA sampai widget menandai tokennya kedaluwarsa
17. Klik [Log in]
18. Verifikasi caption "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
19. Verifikasi widget reCAPTCHA berstatus Unsolved
20. Verifikasi tidak ada sesi dibuat

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan dalam spec: TC-AUTH-LP-25 ditaruh paling akhir karena memerlukan pemajuan jam browser sampai token kedaluwarsa; urutan spec berbeda dari urutan TC sumber (24, 25, 26).
- Langkah penghubung (S-03): "Muat ulang halaman Login with Password" sebelum tiap TC setelah yang pertama (S-09); tanpa `Verifikasi`.
- TC-AUTH-LP-25 berstatus Manual Only di TC sumber. Sesuai bagian 2 konvensi tetap masuk spec; kebutuhan reCAPTCHA yang dapat kedaluwarsa tertulis di Prerequisites.
- Temuan untuk QA (TC-AUTH-LP-25, CAUSE2): TC tidak menyebut durasi kedaluwarsa token dan tidak menyebut cara mengondisikannya; spec memakai satu mekanisme tetap (jam browser dimajukan) dan durasi konfigurasi reCAPTCHA environment yang harus disediakan tim FE/BE. Rincian: TC-AUTH-LP-25 langkah 4 ("Tunggu sampai widget reCAPTCHA menandai tokennya kedaluwarsa") tidak menyebut lama tunggu atau cara mengondisikan kedaluwarsa pada reCAPTCHA mode uji; spec menulis kebutuhan ini sebagai kemampuan teknis tanpa mengarang mekanisme.
