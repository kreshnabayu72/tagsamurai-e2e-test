---
id: TC-AC-ACC-E2E-265-changelog-dan-activity-log-retry-access-setup-principal-vs-distributor
title: "Retry Access Setup: Baris Tampil bagi Principal di Changelog Client dan Activity Log, Disaring Seluruhnya bagi Distributor"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-1040
coverage:
  web: automated
---

# Retry Access Setup: Baris Tampil bagi Principal di Changelog Client dan Activity Log, Disaring Seluruhnya bagi Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite. Akun kedua (langkah ganti akun): Distributor Total Control A-13 (PT Distribusi Nusantara) `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`, password `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): C-FX18-12 "PT Akses Gagal Plan Owner Principal" (relasi Distributor-langsung PT Distribusi Nusantara; FAMS plan owner Principal); riwayat Changelog Client dan Activity Log masing-masing memuat satu baris `Retry Access Setup` (Client Name atau Name "PT Akses Gagal Plan Owner Principal", Field `Product`, Old Value `—`, New Value `FAMS`).
- Kemampuan teknis: Changelog dan Activity Log adalah audit trail permanen; baris seed dicari lewat Search nama Client (S-14).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-1040: Principal melihat baris, Distributor di luar jaringan plan owner tidak

1. [Principal] Klik [Changelog] di toolbar List
2. [Principal] Ketik "PT Akses Gagal Plan Owner Principal" di Search modal, tekan Enter
3. Verifikasi (Principal) tepat satu baris Action `Retry Access Setup`: Client Name "PT Akses Gagal Plan Owner Principal", Field `Product`, Old Value `—`, New Value `FAMS`
4. [Principal] Tutup modal, lalu buka Admin Console > Activity Log dan saring Object `Client`
5. [Principal] Cari baris dengan Name "PT Akses Gagal Plan Owner Principal" (ketik Search, tekan Enter)
6. Verifikasi (Principal) Activity Log memuat tepat satu baris Action `Retry Access Setup`, Object `Client`, Name "PT Akses Gagal Plan Owner Principal", Field `Product`, Old Value `—`, New Value `FAMS`
7. Logout, lalu login sebagai Total Control Distributor A-13 (PT Distribusi Nusantara) dan buka Admin Console > Client
8. [A-13] Klik [Changelog] di toolbar List
9. [A-13] Ketik "PT Akses Gagal Plan Owner Principal" di Search modal, tekan Enter
10. Verifikasi (A-13) empty state hasil Search: Title "No results found" dan Description "Try adjusting your search or filter."
11. Verifikasi (A-13) baris Action `Retry Access Setup` tidak tampil sama sekali (plan owner term FAMS = Principal, di luar jaringan Distributor)
12. Verifikasi (A-13) tidak ada baris placeholder
13. Verifikasi (A-13) jumlah baris pada Pagination hanya menghitung baris yang tampil
14. [A-13] Tutup modal, lalu buka Admin Console > Activity Log dan saring Object `Client`
15. [A-13] Cari baris dengan Name "PT Akses Gagal Plan Owner Principal" (ketik Search, tekan Enter)
16. Verifikasi (A-13) empty state hasil Search: Title "No results found" dan Description "Try adjusting your search or filter."
17. Verifikasi (A-13) Activity Log tidak memuat baris Action `Retry Access Setup` untuk Name "PT Akses Gagal Plan Owner Principal"
18. Verifikasi (A-13) tidak ada baris placeholder

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`.
- Langkah penghubung (S-03, R-16): langkah 4 dan 14 (menutup modal dan menyaring Activity Log lewat Object `Client`), langkah 5 dan 15 (Search nama Client agar baris seed berada di halaman teramati, S-14).
- Ganti akun (langkah 7) memakai Step eksplisit; asersi absence memakai anchor positif empty state "No results found" hasil Search (bagian 8b butir 2); scope exclusion dengan data seed milik TC (bukan kelas g).
- Temuan untuk QA:
  - TC-AC-ACC-1040 menyebut "saring Object Client" di Activity Log tanpa menyebut kontrol Filter yang dipakai; spec memakai Filter Object `Client` dan Search Name.
