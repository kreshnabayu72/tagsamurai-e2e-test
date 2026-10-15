---
id: TC-AUTH-SES-E2E-004-screening-session-expired-dan-idle-warning-web
title: "Screening Dialog Session Expired dan Toast Idle Warning di Web"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-3
  - TC-AUTH-SES-12
coverage:
  web: automated
---

# Screening Dialog Session Expired dan Toast Idle Warning di Web

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-3: `Andi Permata` (`andipermata+{runId}-004@qwertysystem.net`)
  - TC-AUTH-SES-12: `Lestari Firmansyah` (`lestarifirmansyah+{runId}-004@qwertysystem.net`)
- Sesi web Browser A (Chrome on Windows) untuk kedua user dibuat oleh langkah login di `## Test Steps` (bukan di hook `before`), karena jam server yang sudah dimajukan TC sebelumnya akan ikut menuakan sesi yang di-seed lebih awal.
- Hook `after`: kembalikan jam server uji dan jam browser ke waktu nyata, akhiri semua sesi uji, tutup Browser A, hapus kedua user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser (diatur bersama) serta sesi aktif kedua user, dipulihkan di hook `after`. Batas idle Client `Alpha Logistik` (15 menit) dibaca, tidak diubah.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel): jam server dan jam browser/perangkat diatur bersama dan dapat dimajukan dengan presisi menit (Tabel Data Uji Pre-setup #18), sehingga perubahan itu diteruskan ke penilaian idle di server maupun timer idle/heartbeat web; Browser A satu konteks dengan user agent Chrome on Windows; reCAPTCHA mode uji di environment (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A.

## Test Steps

### TC-AUTH-SES-3: Screening Dialog Session Expired di web

1. Di Browser A buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Ketik email `andipermata+{runId}-004@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → halaman Portal — Product Hub tampil
3. Biarkan Browser A tanpa aktivitas
4. Majukan jam server uji dan jam browser bersama 16 menit tanpa aktivitas di Browser A → Dialog muncul
5. Susuri dialog dan halaman di belakangnya dari atas ke bawah
6. Verifikasi **Header**: Title "Session Expired"
7. Verifikasi **Header**: Dialog modal
8. Verifikasi **Header**: Severity warning
9. Verifikasi **Body**: Body "Your session has expired due to inactivity."
10. Verifikasi Halaman di belakang dialog tertutup overlay dan tidak dapat diinteraksi (frozen)
11. Verifikasi **Footer**: [Refresh] (variant text, severity contrast) sebagai satu-satunya tombol
12. Verifikasi Tidak ada tombol [Login] dan tidak ada tombol [OK]

### TC-AUTH-SES-12: Screening Toast Idle Warning di web

13. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), buka konteks Browser A baru yang belum login, lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
14. Ketik email `lestarifirmansyah+{runId}-004@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → halaman Portal — Product Hub tampil
15. Biarkan Browser A tanpa aktivitas
16. Majukan jam server uji dan jam browser bersama sampai sisa waktu kedaluwarsa 5 menit (idle 10 menit) → Toast muncul
17. Susuri toast dari atas ke bawah
18. Verifikasi **Header**: Ikon TimeLine dengan severity warning
19. Verifikasi **Body**: Title "Session Expiring Soon"
20. Verifikasi **Body**: Body "Your session will expire in 5 minutes due to inactivity. Move your mouse or press any key to stay logged in."
21. Verifikasi **Footer**: Toast non-blocking, halaman di belakang tetap dapat diinteraksi
22. Verifikasi Toast tanpa tombol aksi
23. Verifikasi Hanya satu toast tampil (tanpa stacking)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (jam server).
- Urutan mengikuti TC sumber: TC-AUTH-SES-3 lalu TC-AUTH-SES-12; tidak ada penyimpangan (S-05, S-10). Jam server uji dan jam browser dimajukan bersama dan tidak dipulihkan antar-TC (spec ini tidak membuka Activity Log atau User Log); tiap TC memakai user dan sesi yang dibuat pada langkahnya sendiri, sehingga pergeseran kumulatif tidak mengubah hasil. Pemulihan jam di hook `after`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah 13 menutup konteks Browser A TC-AUTH-SES-3 beserta sesi login browsernya dan membuka konteks Browser A bersih agar sesi TC-AUTH-SES-3 yang sudah expired tidak terpakai ulang; menyusuri dialog dan toast tanpa klik.
- Langkah 1-2 dan 13-14 (login user uji di Browser A) adalah langkah TC sumber ("Login web sebagai ..." dan "buka Portal — Product Hub sebagai ..."); sesi tidak di-seed karena alasan jam server di Prerequisites.
- Asersi pencatatan (Session Expired di Activity Log > Session dan User Log) tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-3 dan 12 mencantumkan "sesi web aktif di Browser A" sebagai precondition sementara Langkah Uji 1 juga login; spec membuat sesi lewat langkah login. (2) TC-AUTH-SES-3 dan 12 tidak menyebut reCAPTCHA pada halaman Login with Password; spec mengikuti TC dan mengandalkan reCAPTCHA mode uji. (3) TC-AUTH-SES-12 langkah 2 menyebut "sisa waktu kedaluwarsa 5 menit (idle 10 menit)"; spec memajukan jam server uji sampai idle 10 menit. Karena penilaian idle toast bisa memakai timer di klien, spec memajukan jam server dan jam browser bersama (Prerequisites).
