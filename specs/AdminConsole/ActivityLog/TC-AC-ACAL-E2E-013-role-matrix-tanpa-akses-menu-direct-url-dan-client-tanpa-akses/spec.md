---
id: TC-AC-ACAL-E2E-013-role-matrix-tanpa-akses-menu-direct-url-dan-client-tanpa-akses
title: "Role Matrix: Tanpa Akses Menu, Direct URL, dan Client Tanpa Akses"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-28
  - TC-AC-ACAL-29
  - TC-AC-ACAL-30
  - TC-AC-ACAL-31
  - TC-AC-ACAL-32
coverage:
  web: automated
---

# Role Matrix: Tanpa Akses Menu, Direct URL, dan Client Tanpa Akses

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: tidak relevan untuk spec ini (akun tidak membuka halaman Activity Log); hook suite before/after tetap berjalan (lihat suite.md).
- Spec Role Matrix negatif (bagian 3a konvensi): menu Activity Log Hidden dan direct URL ditolak. Password tidak ditulis di spec atau fixture; dari nama env AC_* di bawah tidak ada yang sudah terdaftar di `.env.example` maupun `spectra.config.ts`; semuanya usulan tim FE (lihat Temuan untuk QA).

Role yang diuji, urutan baris = urutan blok:

| Role | Email | Env var password |
|---|---|---|
| Group Manager (di-assign ke beberapa group) | `groupManagerAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 4) | `Spectra.env.AC_GM_PASSWORD` |
| Capability Client Full CRUD (staf Principal, tanpa access level) | `fullCrudClient_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 5) | `Spectra.env.AC_FULLCRUD_PASSWORD` |
| Total Control (Client Sejahtera) | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `Spectra.env.AC_SEJAHTERA_TC_PASSWORD` |

- Login akun pertama (Group Manager) di hook `before` spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Halaman awal: halaman Admin Console yang terbuka setelah login. Untuk akun tanpa akses Activity Log, hook `beforeEach` suite tidak membuka halaman Activity Log (kemampuan disediakan tim FE; lihat Temuan untuk QA).
- URL halaman Admin Console > Activity Log (tanpa segmen tab) untuk langkah direct URL ditetapkan tim FE (TC tidak menulis route).
- Data Pre-setup: tiga akun pada tabel di atas, dengan hierarki entitas Pre-setup No 8 (Client Sejahtera milik Distributor Alfa). Tidak ada Data Dinamis dan tidak ada state global yang diubah.
- Direct URL dilakukan lewat address bar browser (bukan request API); asersinya toast dan tampilan, sehingga ini bukan kelas defense-in-depth (spec 020).

## Test Steps

### TC-AC-ACAL-28: Group Manager, menu Activity Log Hidden

1. Verifikasi sedikitnya satu item menu lain tampil pada sidebar Admin Console
2. Verifikasi menu Activity Log Hidden pada sidebar Admin Console

### TC-AC-ACAL-29: Group Manager, akses URL langsung ditolak

3. Ketik URL halaman Activity Log di address bar, tekan Enter
4. Verifikasi toast error `You don't have permission to do this.` tampil
5. Verifikasi tidak ada baris log dari tab Session maupun tab User Action yang tampil
6. Verifikasi menu Activity Log tetap Hidden pada sidebar Admin Console

### TC-AC-ACAL-30: Pemegang capability individual, menu Activity Log Hidden

7. Ganti akun: logout, lalu login sebagai Capability Client Full CRUD dengan `Spectra.env.AC_FULLCRUD_PASSWORD`
8. Verifikasi sedikitnya satu item menu lain tampil pada sidebar Admin Console
9. Verifikasi menu Activity Log Hidden pada sidebar Admin Console

### TC-AC-ACAL-31: Pemegang capability individual, akses URL langsung ditolak

10. Ketik URL halaman Activity Log di address bar, tekan Enter
11. Verifikasi toast error `You don't have permission to do this.` tampil
12. Verifikasi tidak ada baris log yang tampil
13. Verifikasi halaman tidak dialihkan ke halaman unauthorized

### TC-AC-ACAL-32: Client tidak punya akses Activity Log Admin Console

14. Ganti akun: logout, lalu login sebagai Total Control (Client Sejahtera) dengan `Spectra.env.AC_SEJAHTERA_TC_PASSWORD`
15. Verifikasi sedikitnya satu produk lain tampil pada produk yang tersedia setelah login
16. Verifikasi produk Admin Console dan menu Activity Log tidak tersedia
17. Ketik URL halaman Admin Console > Activity Log di address bar, tekan Enter
18. Verifikasi toast error `You don't have permission to do this.` tampil
19. Verifikasi tidak ada baris log yang tampil
20. Verifikasi halaman tidak dialihkan ke halaman unauthorized

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-28, 29, 30, 31, 32).
- Spec ditulis per blok role (bagian 3a konvensi, `[KEPUTUSAN 2026-10-30]`): ekspektasi tiap role berbeda (Client tidak punya produk Admin Console, dua role lain tidak punya menu), dan ganti akun menuntut Step eksplisit; akun pertama login di hook `before`.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun (langkah 7, 14) dan mengetik URL langsung (langkah 3, 10, 17).
- Asersi tambahan di luar Expected TC (S-03): langkah 1, 8, dan 15 membuktikan item menu atau produk lain pada surface yang sama sudah tampil, sebagai anchor positif sebelum asersi absence menu atau produk (bagian 8b butir 2). Toast error pada langkah 4, 11, dan 18 menjadi anchor untuk asersi "tidak ada baris log" pada langkah 5, 12, dan 19.
- Temuan untuk QA:
  - Email dan env password akun Pre-setup tidak lengkap: email memakai placeholder `{namaCompany}`; akun Total Control Client Sejahtera (TC-AC-ACAL-32) tidak ada di tabel Pre-setup; nama env `AC_GM_PASSWORD`, `AC_FULLCRUD_PASSWORD`, `AC_SEJAHTERA_TC_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
  - TC-AC-ACAL-29, 31, dan 32 menulis "Ketik URL halaman Activity Log" tanpa route; route ditetapkan tim FE.
  - Halaman awal akun tanpa akses Activity Log: hook `beforeEach` suite membuka Activity Log untuk akun aktor suite; untuk akun di spec ini TC tidak menyebut halaman awalnya, sehingga halaman awal diserahkan ke tim FE.
  - TC-AC-ACAL-32 ("Amati produk yang tersedia setelah login") tidak menyebut nama produk pembanding; spec memakai "sedikitnya satu produk lain".
