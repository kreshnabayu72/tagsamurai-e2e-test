---
id: TC-AC-LA-E2E-139-preservasi-state-list-tab-browser-baru-dan-sesi-baru
title: "Preservasi State List Multi-Konteks: Tab Browser Baru dan Sesi Login Baru Memulai dari Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-352
coverage:
  web: automated
---

# Preservasi State List Multi-Konteks: Tab Browser Baru dan Sesi Login Baru Memulai dari Default

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`). Hook `after` mengembalikan sesi ke akun default suite. Langkah 9 dan 10 adalah logout dan login ulang dengan akun yang sama; keduanya objek uji TC-AC-LA-352 (bukan ganti akun).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab; Client `PT Sejahtera`) bersifat baca-saja untuk spec ini.
- Kemampuan teknis (disediakan tim FE/BE): membuka tab browser kedua dengan sesi yang sama.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-352: Tab browser baru dan logout-login memulai dari default

1. Ketik Search `Sejahtera`, tekan Enter
2. Buka tab browser baru dan buka Allocation > License Allocation
3. Verifikasi tab baru terbuka pada tab `Current`
4. Verifikasi Search kosong pada tab baru
5. Verifikasi Filter default pada tab baru
6. Verifikasi Sort default Last Updated Newest First pada tab baru
7. Verifikasi halaman 1 pada tab baru
8. Tutup tab browser baru
9. Logout
10. Login sebagai Total Control Principal (Pre-setup #1)
11. Klik menu `License Allocation` di sidebar
12. Verifikasi sesi login baru mulai dari tab `Current`
13. Verifikasi Search kosong pada sesi login baru
14. Verifikasi Filter default pada sesi login baru
15. Verifikasi Sort default Last Updated Newest First pada sesi login baru
16. Verifikasi halaman 1 pada sesi login baru

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas c (multi-konteks, bagian 3 prinsip 13c): tab browser baru adalah objek asersi (state List tidak terbawa ke tab kedua), bukan pemicu, sehingga TC-AC-LA-352 berdiri di spec sendiri dan tidak memakai `P-2`.
- Pembagian TC lintas spec: TC-AC-LA-349, 350, 351, dan 353 (preservasi state pada satu tab) ada di spec 113.
- Langkah penghubung (S-03): langkah 1 (membentuk state non-default di tab pertama sebagai Precondition TC-AC-LA-352 Langkah 1), langkah 8 (menutup tab baru), langkah 11 (membuka List lewat menu sidebar sesudah login).
- Asersi "state default" dipecah per klausa (S-01): tab `Current`, Search kosong, Filter default, Sort default, halaman 1; Sort default `Last Updated Newest First` mengikuti penulisan TC-AC-LA-351 di spec 113.
- Temuan untuk QA:
  - TC-AC-LA-352 Langkah 1 ("Terapkan Search") tidak menyebut nilai Search; spec memakai `Sejahtera` seperti TC-AC-LA-349 sampai 353.
  - TC-AC-LA-352 Langkah 2 ("Logout, login, dan buka List") tidak menyebut cara membuka List sesudah login; spec memakai klik menu `License Allocation` di sidebar.
  - TC-AC-LA-352 Expected a menyebut "state default" tanpa merinci; spec merinci menurut TC-AC-LA-351 (tab Current, Search kosong, Filter default, Sort default, halaman 1).
