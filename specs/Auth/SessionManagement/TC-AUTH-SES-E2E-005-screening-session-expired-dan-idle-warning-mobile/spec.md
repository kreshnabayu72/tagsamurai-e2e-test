---
id: TC-AUTH-SES-E2E-005-screening-session-expired-dan-idle-warning-mobile
title: "Screening Dialog Session Expired dan Toast Idle Warning di Aplikasi Mobile"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-4
  - TC-AUTH-SES-13
coverage:
  mobile: automated
---

# Screening Dialog Session Expired dan Toast Idle Warning di Aplikasi Mobile

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) pada perangkat Android uji A (Tabel Data Uji Pre-setup #10), terpasang di perangkat atau emulator uji.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-4: `Dewi Lestari` (`dewilestari+{runId}-005@qwertysystem.net`), sesi mobile aktif di perangkat Android uji A (status Active) dibuat di hook `before` lewat login nyata di aplikasi dengan email dan password user, lalu mengetuk [Not now] pada Prompt Enable Biometric (Tabel Data Uji Pre-setup #28)
  - TC-AUTH-SES-13: `Dimas Damayanti` (`dimasdamayanti+{runId}-005@qwertysystem.net`), sesi mobile dibuat oleh langkah login di `## Test Steps` (alasan di Notes)
- Hook `after`: kembalikan jam server uji dan jam perangkat ke waktu nyata, akhiri semua sesi uji, pastikan aplikasi mobile tidak menyimpan sesi, hapus kedua user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam perangkat (diatur bersama) serta sesi mobile kedua user, dipulihkan di hook `after`. Batas idle Client `Alpha Logistik` (15 menit) dibaca, tidak diubah.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel): jam server dan jam browser/perangkat diatur bersama dan dapat dimajukan dengan presisi menit (Tabel Data Uji Pre-setup #18), sehingga perubahan itu diteruskan ke penilaian idle di server maupun timer idle aplikasi mobile; driver otomasi Android (aplikasi native) untuk membuka aplikasi di foreground, mengetuk layar, dan membaca dialog serta toast; pengukuran ukuran dialog terhadap lebar layar ponsel.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada aplikasi mobile di perangkat Android uji A.

## Test Steps

### TC-AUTH-SES-4: Screening Dialog Session Expired di aplikasi mobile

1. Buka aplikasi mobile yang sedang login sebagai `dewilestari+{runId}-005@qwertysystem.net` di perangkat Android uji A, pada Portal — Product Hub → halaman Portal — Product Hub tampil
2. Biarkan aplikasi tanpa sentuhan
3. Majukan jam server uji dan jam perangkat bersama 16 menit, lalu ketuk layar → Dialog muncul
4. Susuri dialog dari atas ke bawah
5. Verifikasi **Header**: Title "Session Expired"
6. Verifikasi **Header**: Dialog modal
7. Verifikasi **Header**: Severity warning
8. Verifikasi Dialog berukuran proporsional terhadap lebar layar ponsel
9. Verifikasi **Body**: Body "Your session has expired due to inactivity."
10. Verifikasi **Footer**: [OK] sebagai satu-satunya tombol
11. Verifikasi Tidak ada tombol [Refresh]

### TC-AUTH-SES-13: Screening Toast Idle Warning di aplikasi mobile memakai copy mobile

12. Tutup paksa aplikasi mobile di perangkat Android uji A, lalu hapus sesi lokal aplikasi agar sesi TC sebelumnya tidak dipakai ulang
13. Buka aplikasi mobile di perangkat Android uji A → halaman Login tampil
14. Login dengan `dimasdamayanti+{runId}-005@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD` → halaman Portal — Product Hub tampil (aplikasi di foreground)
15. Biarkan aplikasi tanpa sentuhan
16. Majukan jam server uji dan jam perangkat bersama sampai sisa waktu kedaluwarsa 5 menit (idle 10 menit) → Toast muncul
17. Susuri toast dari atas ke bawah
18. Verifikasi **Header**: Ikon TimeLine dengan severity warning
19. Verifikasi **Body**: Title "Session Expiring Soon"
20. Verifikasi **Body**: Body "Your session will expire in 5 minutes due to inactivity. Tap the screen to stay logged in."
21. Verifikasi Frasa "Move your mouse or press any key" tidak ada
22. Verifikasi **Footer**: Toast non-blocking
23. Verifikasi **Footer**: Toast tanpa tombol aksi

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (jam server) dan mobile.
- Urutan mengikuti TC sumber: TC-AUTH-SES-4 lalu TC-AUTH-SES-13; tidak ada penyimpangan (S-05, S-10). Jam server uji dan jam perangkat dimajukan bersama dan tidak dipulihkan antar-TC (spec ini tidak membuka Activity Log atau User Log). Sesi Dimas dibuat pada langkah 14 (bukan di-seed) karena pergeseran jam 16 menit di TC-AUTH-SES-4 akan menuakan sesi yang di-seed lebih awal; langkah 12-14 menyalin alur login yang TC sumber andaikan sudah terjadi (precondition b TC-AUTH-SES-13).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): tutup paksa aplikasi dan hapus sesi lokal aplikasi (langkah 12); menyusuri dialog dan toast tanpa sentuhan.
- Asersi pencatatan (Session Expired di Activity Log > Session dan User Log) tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-4 dan 13 menyebut "sedang login" / "foreground" pada Langkah Uji tanpa menyebut login ulang; langkah 12-14 ditambahkan sebagai langkah penghubung (S-15). (2) TC-AUTH-SES-13 langkah 2 menyebut "sisa waktu kedaluwarsa 5 menit" tanpa angka menit server yang dimajukan; spec memakai idle 10 menit dari kolom Data Uji. (3) Mekanisme timer idle mobile (jam server vs timer lokal aplikasi) tidak disebut TC; kebutuhan pergeseran jam server dan jam perangkat bersama dicatat di Prerequisites.
