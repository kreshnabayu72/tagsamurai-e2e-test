---
id: TC-AUTH-SES-E2E-003-screening-popup-concurrent-dan-subscription
title: "Screening Popup Concurrent Session Limit Reached dan Subscription Not Active"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-10
  - TC-AUTH-SES-11
coverage:
  web: automated
---

# Screening Popup Concurrent Session Limit Reached dan Subscription Not Active

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BASE (TC-AUTH-SES-10 milik Client Q2, Tabel Data Uji Pre-setup #12; TC-AUTH-SES-11 milik Client Expired, Tabel Data Uji Pre-setup #14) (Tabel Data Uji Pre-setup #5: user Activated, Active ON; MFA dan Agreement tidak terpicu), masing-masing memiliki App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-10: `Maya Puspita` (`mayapuspita+{runId}-003@qwertysystem.net`), sesi platform aktif di Browser A tanpa sesi-produk Fixed Asset
  - TC-AUTH-SES-11: `Fajar Saputra` (`fajarsaputra+{runId}-003@qwertysystem.net`), tanpa sesi-produk Active
- User TC-AUTH-SES-10 dan kedua user seed seat (di bawah) di-seed oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26). User TC-AUTH-SES-11 di-seed oleh akun aktor Total Control (Global Settings) dengan scope Client Expired/uji (Tabel Data Uji Pre-setup #31).
- Kondisi yang di-seed untuk TC-AUTH-SES-10: Client Q2 (Tabel Data Uji Pre-setup #12; kuota concurrent Fixed Asset = 2) memiliki 2 sesi-produk Fixed Asset Active milik user lain, sehingga seat terpakai = 2. Kedua user seat adalah user seed milik Client Q2 (Tabel Data Uji Pre-setup #7), profil BASE dengan App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, dibuat di hook `before` dan dihapus di hook `after`, email bersuffix per run:
  - `Gunawan Prakoso` (`gunawanprakoso+{runId}-003@qwertysystem.net`), sesi-produk Fixed Asset Active
  - `Melati Anggun` (`melatianggun+{runId}-003@qwertysystem.net`), sesi-produk Fixed Asset Active
- Kondisi yang di-seed untuk TC-AUTH-SES-11: Client Expired (Tabel Data Uji Pre-setup #14) dengan status subscription Fixed Asset Expired (seed disediakan tim BE).
- Hook `after`: akhiri kedua sesi-produk seed Client Q2 dan semua sesi uji, pulihkan status subscription Fixed Asset Client Expired ke kondisi awal (oleh akun aktor `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`), tutup Browser A, hapus keempat user (dua user uji dan dua user seat). Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: seat concurrent Fixed Asset Client Q2 (2 dari 2 terpakai) dan status subscription Fixed Asset Client Expired, dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: Browser A satu konteks; seeding sesi-produk Fixed Asset untuk user seed Client Q2 (login API per user lalu masuk Fixed Asset); pengaturan status subscription Client uji; reCAPTCHA mode uji di environment (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A.

## Test Steps

### TC-AUTH-SES-10: Screening Popup Concurrent session limit reached

1. Di Browser A buka Portal — Product Hub sebagai `mayapuspita+{runId}-003@qwertysystem.net` → halaman Portal — Product Hub tampil
2. Klik card Fixed Asset → Popup muncul
3. Susuri popup dari atas ke bawah
4. Verifikasi **Header**: Title "Concurrent session limit reached"
5. Verifikasi **Header**: Popup modal
6. Verifikasi **Header**: Severity warning
7. Verifikasi **Header**: Popup dapat ditutup
8. Verifikasi **Body**: Body "You've reached the concurrent session limit for this product. Try again later once a session becomes available."
9. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

### TC-AUTH-SES-11: Screening Popup Subscription Not Active

10. Klik [OK] pada Popup Concurrent session limit reached, lalu tutup konteks Browser A milik `mayapuspita+{runId}-003@qwertysystem.net` dan buka konteks Browser A baru yang belum login
11. Di Browser A buka halaman `Auth > Login with Password` → halaman Login with Password tampil
12. Ketik email `fajarsaputra+{runId}-003@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → halaman Portal — Product Hub tampil
13. Klik card Fixed Asset → Popup muncul
14. Susuri popup dari atas ke bawah
15. Verifikasi **Header**: Title "Subscription Not Active"
16. Verifikasi **Header**: Popup modal
17. Verifikasi **Header**: Severity warning
18. Verifikasi **Header**: Popup dapat ditutup
19. Verifikasi **Body**: Body "Your subscription is not active. Please contact your administrator."
20. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan mengikuti TC sumber: TC-AUTH-SES-10 lalu TC-AUTH-SES-11; tidak ada penyimpangan (S-05, S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup Popup, menutup konteks Browser A milik user TC-AUTH-SES-10, dan membuka konteks Browser A baru pada langkah 10 agar TC-AUTH-SES-11 mulai dari konteks bersih; penyusuran popup tanpa klik.
- Asersi pencatatan (bila ada) untuk kedua popup tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-10 tidak menyebut langkah login; sesi platform Maya di-seed di hook `before`. (2) TC-AUTH-SES-10 dan 11 tidak menyebut reCAPTCHA pada halaman Login with Password; spec mengikuti TC.
