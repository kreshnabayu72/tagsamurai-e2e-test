---
id: TC-AUTH-ACT-E2E-032-halaman-activation-success-dan-navigasi
title: "Halaman Activation Success dan Navigasi Sesudah Aktivasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-73
  - TC-AUTH-ACT-74
  - TC-AUTH-ACT-75
  - TC-AUTH-ACT-76
  - TC-AUTH-ACT-77
coverage:
  web: automated
---

# Halaman Activation Success dan Navigasi Sesudah Aktivasi

## Prerequisites

- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-009@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `ACT_PASSWORD`, `ACT_PASSWORD_72`, `ACT_PASSWORD_SPECIAL`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: pemantauan request jaringan; jendela privat untuk konteks akun aktor; reload halaman (F5); tombol Back browser; menyalin URL dari address bar dan membukanya di tab baru; reCAPTCHA mode uji di environment.
- TC-AUTH-ACT-73: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-73: User `Teguh Puspita` (`teguhpuspita+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-73 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-74: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-74: User `Laras Hidayat` (`larashidayat+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-74 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-75: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-75: User `Ilham Ramadhan` (`ilhamramadhan+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-75 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-76: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-76: User `Wulan Mulyadi` (`wulanmulyadi+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-76 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-77: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-77: User `Darma Wulandari` (`darmawulandari+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-77 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`

## Test Steps

### TC-AUTH-ACT-73: Screening halaman Activation Success

1. Buka jendela privat baru (tanpa sesi login)
2. Buka link aktivasi user `Teguh Puspita` di browser → halaman `Auth > Account Activation > Set Password` tampil
3. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
4. Klik button "Set Password"
5. Susuri halaman Activation Success dari atas ke bawah tanpa klik apa pun
6. Verifikasi **Header**: Card (Elevated) single-column di tengah layar; ilustrasi sukses (success illustration) di atas
7. Verifikasi **Body**: Title "Account Activated"; Body "Your account is now active. You can log in with your new password."
8. Verifikasi **Footer**: CTA "Go to Login" enabled di dalam EmptyState; tidak ada aksi lain di halaman
9. Verifikasi Status user `Teguh Puspita` Activated dan token Consumed

### TC-AUTH-ACT-74: Klik Go to Login pada halaman sukses menuju Login with Password

10. Buka jendela privat baru (tanpa sesi login)
11. Buka link aktivasi user `Laras Hidayat` di browser → halaman `Auth > Account Activation > Set Password` tampil
12. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
13. Klik button "Set Password"
14. Klik CTA "Go to Login"
15. Verifikasi halaman Login with Password tampil
16. Verifikasi Tidak ada pemeriksaan atau pesan terkait sesi lain pada transisi
17. Verifikasi Status user `Laras Hidayat` Activated dan token Consumed

### TC-AUTH-ACT-75: Reload halaman Activation Success mengarahkan ke halaman Login

18. Buka jendela privat baru (tanpa sesi login)
19. Buka link aktivasi user `Ilham Ramadhan` di browser → halaman `Auth > Account Activation > Set Password` tampil
20. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
21. Klik button "Set Password"
22. Reload halaman Activation Success (F5)
23. Verifikasi Halaman Login tampil; halaman Activation Success tidak tampil kembali
24. Verifikasi Status user `Ilham Ramadhan` Activated dan token Consumed

### TC-AUTH-ACT-76: Tombol Back browser tidak membuka kembali halaman Activation Success

25. Buka jendela privat baru (tanpa sesi login)
26. Buka link aktivasi user `Wulan Mulyadi` di browser → halaman `Auth > Account Activation > Set Password` tampil
27. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
28. Klik button "Set Password"
29. Klik CTA "Go to Login" → halaman Login with Password tampil
30. Tekan tombol Back browser
31. Verifikasi Halaman Login tampil; halaman Activation Success tidak tampil kembali
32. Verifikasi Status user `Wulan Mulyadi` Activated dan token Consumed

### TC-AUTH-ACT-77: Akses langsung ke URL halaman Activation Success mengarahkan ke halaman Login

33. Buka jendela privat baru (tanpa sesi login)
34. Buka link aktivasi user `Darma Wulandari` di browser → halaman `Auth > Account Activation > Set Password` tampil
35. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
36. Klik button "Set Password"
37. Salin URL halaman Activation Success dari address bar
38. Tempel URL tersebut di tab baru dan buka
39. Verifikasi Halaman Login tampil di tab baru; halaman Activation Success tidak tampil
40. Verifikasi Status user `Darma Wulandari` Activated dan token Consumed

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Dipisah dari E2E-009 (aktivasi dan nilai batas) supaya screening halaman sukses dan skenario navigasi (reload, Back, URL langsung) tidak bergantung pada proses aktivasi yang sama; setiap blok mengaktifkan user sendiri.
- Spec ini 40 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena kelima blok satu topik (halaman Activation Success dan navigasi sesudahnya), tiap blok mengaktifkan user sendiri di jendela privat baru, sehingga blok berikutnya tidak bergantung pada hasil blok sebelumnya.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-ACT-74 terbagi lintas spec: asersi "tidak ada pencatatan dari Auth" (Post Condition) diuji di spec `TC-AUTH-ACT-E2E-017-absence-pencatatan-halaman-publik` (kelas g, prinsip 10).
