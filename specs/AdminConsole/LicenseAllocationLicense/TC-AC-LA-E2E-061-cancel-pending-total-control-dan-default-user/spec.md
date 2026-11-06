---
id: TC-AC-LA-E2E-061-cancel-pending-total-control-dan-default-user
title: "Cancel Allocation Pending oleh Total Control Tanpa Refund dan Default User Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-221
  - TC-AC-LA-227
coverage:
  web: automated
---

# Cancel Allocation Pending oleh Total Control Tanpa Refund dan Default User Principal

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current). Ganti akun ke Sari Pratama dilakukan eksplisit pada langkah 14 sampai 16; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |
| Sari Pratama | #2 | Default User Principal PT ABC | `defaultUserLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), PT Sejahtera (Pre-setup #19), kantong wallet (Pre-setup #33), Product Price (Pre-setup #34), Require Approval ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #46 dan #60 bersama): `{idPending}` alokasi `Completed` berstatus lisensi `Pending`, Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini (Pre-setup #4), Cost $3,650.00 di-Reserve; `{idFree}` alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Sari Pratama dengan Payment `Free` tanpa Reserve.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, kemampuan membaca saldo kantong Distributor PT Maju Bersama dan kantong Principal (Balance, Reserved, Available).
- State global: saldo kantong dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Cancel Pending oleh Total Control

1. Ketik Search `{idPending}`, tekan Enter
2. Klik row action `Cancel Allocation` pada baris Pending milik Dewi Anggraini
3. Klik `[Cancel Request]`
4. Tunggu aksi selesai
5. Klik tab `History`
6. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
7. Ketik Search `{idPending}`, tekan Enter
8. Verifikasi Status `{idPending}` menjadi `Canceled`
9. Verifikasi Reserve `$3,650.00` dilepas
10. Verifikasi Balance kantong tidak berubah (tanpa refund karena dana belum di-Capture)
11. Klik row action `Allocation Log`
12. Verifikasi Allocation Log memuat entri `Allocation canceled by Fajar N`
13. Tutup modal Allocation Log

### Cancel oleh Default User Principal untuk alokasi tanpa Reserve

14. Ganti akun: Logout dari Fajar Nugroho
15. Login sebagai Sari Pratama (`defaultUserLic`, password `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`)
16. Buka Allocation > License Allocation pada tab Current
17. Catat saldo kantong Principal (Balance, Reserved, Available) sebagai baseline
18. Ketik Search `{idFree}`, tekan Enter
19. Klik row action `Cancel Allocation`
20. Klik `[Cancel Request]`
21. Verifikasi toast sukses: "Success, license allocation has been canceled."
22. Klik tab `History`
23. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
24. Ketik Search `{idFree}`, tekan Enter
25. Verifikasi Status `{idFree}` menjadi `Canceled`
26. Verifikasi tidak ada mutasi wallet: saldo kantong Principal sama dengan baseline

## Notes

- Langkah penghubung (S-03, R-16): langkah 4 (menunggu aksi selesai karena langkah berikutnya pindah tab), langkah 6 dan 23 (mengosongkan kotak search lewat `✕` dan Enter sesudah pindah tab sebelum Search berikutnya; isi kotak setelah pindah tab tidak diandaikan), langkah 1, 7, 18, dan 24 (Search untuk menemukan baris seed), langkah 5 dan 22 (pindah tab), langkah 13 (menutup modal Allocation Log), langkah 14 sampai 16 (ganti akun dan membuka halaman), langkah 17 (baseline saldo).
- Urutan TC-AC-LA-227: toast (butir b) diasersi sebelum Status dan saldo (butir a) karena toast adalah state sementara (8b butir 5).
- Temuan untuk QA:
  - TC-AC-LA-221 butir a ("Balance kantong tidak berubah", "Reserve dilepas") dan TC-AC-LA-227 butir a ("tanpa mutasi wallet") tidak menyebut halaman atau cara membaca wallet; spec memakai kemampuan baca saldo yang disediakan tim FE/BE, dengan baseline pada langkah 17 untuk kantong Principal.
  - TC-AC-LA-221 butir b ("Log `Allocation canceled by Fajar N`") tidak menyebut surface log; spec membacanya di Allocation Log record (langkah 11 dan 12).
  - TC-AC-LA-227 tidak menyebut tab asal baris saat Cancel dan tempat membaca Status akhir; spec membaca Status di tab History setelah Cancel.
  - TC-AC-LA-227: kantong yang dibaca untuk "tanpa mutasi wallet" tidak disebut; spec memakai kantong Principal karena Payment `Free` dan requester Default User Principal.
