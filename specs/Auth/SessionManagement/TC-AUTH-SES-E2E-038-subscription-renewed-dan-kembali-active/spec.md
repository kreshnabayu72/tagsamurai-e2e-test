---
id: TC-AUTH-SES-E2E-038-subscription-renewed-dan-kembali-active
title: "Subscription Kembali Active dan Renewed Mengizinkan Pembukaan Produk Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-279
  - TC-AUTH-SES-281
coverage:
  web: automated
---

# Subscription Kembali Active dan Renewed Mengizinkan Pembukaan Produk Baru

## Prerequisites

- Mode: FE+BE.
- Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota concurrent masing-masing 2, 0 seat Fixed Asset terpakai di awal spec. Status subscription Fixed Asset Client Q2 dikondisikan per TC lewat langkah eksplisit oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD` (aksi Admin Console atau lifecycle subscription di-seed BE; jam server uji tidak digeser karena menggeser jam membuat sesi platform kedua user uji melewati batas idle).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q2 (Tabel Data Uji Pre-setup #26), kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) milik Client Q2 dengan App Access Fixed Asset dan Supply Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-281: `Putri Saputra` (`putrisaputra+{runId}-038@qwertysystem.net`)
  - TC-AUTH-SES-279: `Lestari Utami` (`lestariutami+{runId}-038@qwertysystem.net`)
- Sesi platform web aktif per user, di Portal — Product Hub, dibuat di hook `before` lewat login API; tidak ada sesi-produk Active milik kedua user. Browser A pada tiap TC = konteks browser yang memuat sesi platform user TC bersangkutan (satu konteks per user, dibuat di `before`).
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): pulihkan status subscription Fixed Asset Client Q2 ke Active, akhiri semua sesi seed termasuk sesi-produk Fixed Asset yang dibuat TC, tutup semua konteks browser, hapus kedua user.
- Suite berjalan serial (`parallel: false`); state global yang diubah: status subscription Fixed Asset Client Q2 (Expired, Active, Renewed), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness h: state tenant): pengaturan status subscription per langkah oleh akun principal Admin Console, termasuk term baru berstatus Active dan status Renewed dengan term aktif Active (di-seed BE); satu konteks browser per user uji; pembacaan hitungan seat aktif Fixed Asset Client Q2 dan sesi-produk milik user uji dari sisi backend.
- Akun yang dipakai: user uji masing-masing TC pada Browser A; akun aktor principal Admin Console (langkah pengondisian status subscription dan hook `after`); akun aktor Total Control (Global Settings) dengan scope Client Q2 (#26, seeding di hook `before`).

## Test Steps

### TC-AUTH-SES-281: Subscription kembali Active mengizinkan pembukaan produk baru lagi

1. Akhiri semua sesi-produk aktif Client Q2 lewat API, lalu atur status subscription Fixed Asset Client Q2 menjadi Expired (kuota 2, 0 seat terpakai)
2. Di Browser A (sesi `Putri Saputra`) klik card Fixed Asset → Popup muncul
3. Verifikasi Popup "Subscription Not Active" tampil
4. Ubah subscription Fixed Asset Client Q2 menjadi term baru berstatus Active
5. Klik [OK]
6. Catat hitungan seat aktif Fixed Asset Client Q2 dari BE sebelum klik card
7. Klik card Fixed Asset lagi
8. Verifikasi Browser A masuk Fixed Asset
9. Verifikasi Seat Fixed Asset terpakai bertambah 1 dari hitungan yang dicatat pada langkah 6

### TC-AUTH-SES-279: Subscription Renewed mengikuti status term aktifnya untuk pembukaan produk baru

10. Akhiri semua sesi-produk aktif Client Q2 lewat API, lalu atur status subscription Fixed Asset Client Q2 menjadi Renewed dengan term aktif Active
11. Catat hitungan seat aktif Fixed Asset Client Q2 dari BE sebelum klik card
12. Di Browser A (sesi `Lestari Utami`) klik card Fixed Asset
13. Verifikasi Browser A masuk Fixed Asset tanpa popup karena term aktif berstatus Active
14. Verifikasi Sesi-produk Fixed Asset dibuat untuk `Lestari Utami`
15. Verifikasi Seat Fixed Asset terpakai bertambah 1 dari hitungan yang dicatat pada langkah 11

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness h (state tenant).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-281 lalu 279 (urutan TC sumber 279, 281). TC-AUTH-SES-281 mensyaratkan 0 seat Fixed Asset terpakai dan kuota 2; bila TC-AUTH-SES-279 dijalankan lebih dulu, sesi-produk `Lestari Utami` memakai satu seat sehingga precondition TC-AUTH-SES-281 tidak terpenuhi.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah 1 dan 10 mengondisikan state tenant per TC dan mengakhiri sesi-produk aktif Client Q2; langkah 6 dan 11 mencatat hitungan seat aktif dari BE sebelum klik card (S-14); langkah 4 adalah langkah TC-AUTH-SES-281 sendiri (aksi di luar Browser A).
- Pada TC-AUTH-SES-281 langkah 3 memverifikasi butir Expected a ("Pertama kali Popup tampil"); isi Body popup tidak diasersikan karena TC tidak menyebutnya pada butir itu (diasersikan di spec `TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk`).
- Temuan untuk QA: (1) TC-AUTH-SES-279 dan 281 menyebut subscription "Renewed" dan "term baru berstatus Active" tanpa menyebut cara memicunya; spec mengondisikannya lewat akun principal Admin Console (Prerequisites). (2) TC-AUTH-SES-279 menyebut "Client dengan subscription ..." (Tabel Data Uji Pre-setup #14) sedangkan TC-AUTH-SES-281 menyebut Client Q2 (#12); spec memakai Client Q2 untuk keduanya. (3) TC-AUTH-SES-279 tidak menyebut nilai seat awal; "seat terpakai bertambah 1" diasersikan relatif terhadap hitungan sebelum klik card, sehingga spec membaca hitungan itu dari sisi backend (Prerequisites).
