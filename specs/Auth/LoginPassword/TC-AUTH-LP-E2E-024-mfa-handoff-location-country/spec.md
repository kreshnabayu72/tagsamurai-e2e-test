---
id: TC-AUTH-LP-E2E-024-mfa-handoff-location-country
title: "Handoff ke MFA karena Lokasi Berjarak Lebih dari 100 km atau Negara Berbeda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-73
  - TC-AUTH-LP-74
  - TC-AUTH-LP-158
coverage:
  web: automated
---

# Handoff ke MFA karena Lokasi Berjarak Lebih dari 100 km atau Negara Berbeda

## Prerequisites

- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: koneksi jaringan penguji yang dapat disimulasikan berasal dari lokasi atau negara tertentu (proxy atau VPN dengan geo-IP yang dikenali server) sehingga lokasi B dapat berjarak lebih dari 100 km di negara yang sama (TC-AUTH-LP-73), serta negara B berjarak kurang dari 100 km dari lokasi login terakhir (TC-AUTH-LP-74 dan TC-AUTH-LP-158); fixture BE untuk lokasi login terakhir user, device terpercaya, tidak ada gate Agreement, bukan login pertama dan tidak idle; fixture modul MFA untuk pasangan negara A–B yang sudah trusted (TC-AUTH-LP-158); akses ke kotak masuk email user subjek (TC-AUTH-LP-158); jendela privat baru; reCAPTCHA mode uji di environment.
- Mode: FE+BE.
- State global: lokasi koneksi penguji (proxy atau VPN dengan geo-IP) diubah oleh spec ini dan dipakai bersama seluruh suite, sehingga suite berjalan serial (`parallel: false`). Hook `after` memulihkan koneksi penguji ke jaringan semula walau spec gagal di tengah; langkah 31 tetap ditulis sebagai aksi eksplisit pemulihan pada alur normal.
- TC-AUTH-LP-73: User `Bayu Nugroho` (`bayunugroho+{runId}-024@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; login terakhir dari lokasi A; tidak ada gate Agreement; koneksi penguji dari lokasi B yang berjarak lebih dari 100 km di negara yang sama
- TC-AUTH-LP-73: User belum login (guest); browser web
- TC-AUTH-LP-73 data: Email `bayunugroho+{runId}-024@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-74: User `Citra Dewi` (`citradewi+{runId}-024@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; login terakhir dari negara A; tidak ada gate Agreement; koneksi penguji dari negara B yang berjarak kurang dari 100 km dari lokasi login terakhir
- TC-AUTH-LP-74: User belum login (guest); browser web
- TC-AUTH-LP-74 data: Email `citradewi+{runId}-024@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-158: User `Bagas Permana` (`bagaspermana+{runId}-024@qwertysystem.net`) berstatus Activated dan Active; device terpercaya; bukan login pertama dan tidak idle; tidak ada gate Agreement; login terakhir dari negara A; pasangan negara A–B sudah trusted untuk user ini (fixture modul MFA); koneksi penguji dari negara B yang berjarak kurang dari 100 km dari lokasi login terakhir; kotak masuk email akun dapat dibuka penguji
- TC-AUTH-LP-158: User belum login (guest); browser web
- TC-AUTH-LP-158 data: Email `bagaspermana+{runId}-024@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-73: Login dari lokasi lebih dari 100 km dari login sebelumnya mengalihkan ke halaman MFA

1. Hubungkan koneksi penguji dari lokasi B (lebih dari 100 km dari lokasi login terakhir, negara yang sama)
2. Buka halaman Login with Password
3. Ketik email `bayunugroho+{runId}-024@qwertysystem.net` di field Email
4. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
5. Selesaikan reCAPTCHA
6. Klik [Log in]
7. Verifikasi browser menuju halaman MFA
8. Verifikasi browser tidak menuju Portal — Product Hub

### TC-AUTH-LP-74: Login dari negara berbeda walau jarak kurang dari 100 km mengalihkan ke halaman MFA

9. Hubungkan koneksi penguji dari negara B (kurang dari 100 km dari lokasi login terakhir)
10. Buka jendela privat baru (tanpa sesi login)
11. Buka halaman Login with Password
12. Ketik email `citradewi+{runId}-024@qwertysystem.net` di field Email
13. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
14. Selesaikan reCAPTCHA
15. Klik [Log in]
16. Verifikasi browser menuju halaman MFA
17. Verifikasi browser tidak menuju Portal — Product Hub
18. Tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-LP-158: Pasangan negara yang sudah trusted tidak memicu MFA karena negara

19. Catat jumlah email alert login tak biasa di kotak masuk `bagaspermana+{runId}-024@qwertysystem.net` sebagai pembanding
20. Buka jendela privat baru (tanpa sesi login)
21. Buka halaman Login with Password
22. Ketik email `bagaspermana+{runId}-024@qwertysystem.net` di field Email
23. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
24. Selesaikan reCAPTCHA
25. Klik [Log in]
26. Verifikasi browser menuju Portal — Product Hub
27. Verifikasi halaman MFA tidak tampil
28. Buka kotak masuk email `bagaspermana+{runId}-024@qwertysystem.net`
29. Verifikasi tidak ada email alert login tak biasa baru dibanding langkah 19
30. Logout dari Portal — Product Hub
31. Pulihkan koneksi penguji ke jaringan semula

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Urutan: dua kasus yang memicu MFA (TC-AUTH-LP-73, TC-AUTH-LP-74) lebih dulu, kasus yang tidak memicu MFA (TC-AUTH-LP-158) terakhir karena menghasilkan sesi penuh. TC-AUTH-LP-74 dan TC-AUTH-LP-158 berbagi konfigurasi koneksi negara B.
- Langkah 1, 9, 19, 20, 30, dan 31 serta langkah buka jendela privat baru adalah langkah penghubung tanpa awalan `Verifikasi` (S-03); langkah 19 dibutuhkan agar asersi "tidak ada email baru" dapat dibuktikan.
- TC-AUTH-LP-155 (geo-IP service tidak tersedia, trigger lokasi dilewati) diuji di spec `TC-AUTH-LP-E2E-028-resilience-provider-failure-injection`.
- Langkah 18 (menutup semua jendela privat dan menghapus sesi browser terkait) adalah langkah penghubung tanpa awalan `Verifikasi` supaya TC berikutnya mulai dari konteks browser bersih (S-03; S-09).
- Temuan untuk QA: lokasi A, lokasi B, negara A, dan negara B pada TC-AUTH-LP-73, TC-AUTH-LP-74, dan TC-AUTH-LP-158 tidak diberi nilai konkret (kota atau negara), jadi pemilihan lokasi uji diserahkan ke tim FE (Prerequisites). TC-AUTH-LP-73 dan TC-AUTH-LP-74 bertanda Manual Only karena membutuhkan koneksi dari lokasi lain; spec tetap dirancang untuk otomasi sesuai konvensi.
