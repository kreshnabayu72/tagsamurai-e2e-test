---
id: TC-AC-LA-E2E-068-approve-reject-oleh-additional-approver-dan-principal
title: "Approve dan Reject oleh Additional Approver dan Total Control Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-480
  - TC-AC-LA-261
coverage:
  web: automated
---

# Approve dan Reject oleh Additional Approver dan Total Control Principal

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Maya Tanjung (akun pertama tabel "Role yang diuji"); halaman License Allocation dibuka hook `beforeEach` suite (tab Current), dan spec ini berpindah ke Approvals sebagai langkah pertama. Ganti akun ke Hendra Wijaya dilakukan eksplisit pada langkah 14 dan 15; hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji:

| Role | Pre-setup | Email | Env password | Blok TC |
|---|---|---|---|---|
| Additional Approver tanpa Manage allocation (Maya Tanjung, Distributor PT Maju Bersama) | #11 | `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD` | TC-AC-LA-480 |
| Total Control Principal (Hendra Wijaya, Principal PT ABC) | #1 | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` | TC-AC-LA-261; pengamat Allocation Log TC-AC-LA-480 butir c |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: PT Sejahtera (Pre-setup #19), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34), Require Approval ON (Pre-setup #38), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`, status `Waiting for Approval`; tidak memakai baris Pre-setup #42 dan #60 bersama): `{idMaya}` Concurrent User +10 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini (Pre-setup #4), Cost $300.00 di-Reserve (bentuk Pre-setup #42); `{idFree}` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Sari Pratama (Default User Principal, Pre-setup #2) dengan Payment `Free` tanpa Reserve (bentuk Pre-setup #60).
- Data uji: Rejection Reason `Kuota tidak sesuai`.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, kemampuan membaca saldo kantong Distributor PT Maju Bersama dan kantong Principal (Balance, Reserved), serta kuota term.
- State global: saldo kantong dan kuota berubah akibat Reject; dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Maya Tanjung (Additional Approver): Reject

1. Buka Approvals > License Allocation
2. Klik `[Review]` pada alokasi Concurrent User +10 PT Sejahtera `{idMaya}`
3. Pilih Reject
4. Isi Rejection Reason `Kuota tidak sesuai`
5. Klik Submit
6. Verifikasi toast sukses: "Success, transaction has been rejected."
7. Verifikasi Status `{idMaya}` menjadi `Rejected`
8. Verifikasi kuota term tidak berubah
9. Verifikasi Reserve dilepas
10. Verifikasi Balance kantong tidak berubah
11. Periksa sidebar Allocation
12. Verifikasi item menu `Approvals` tampil pada sidebar
13. Verifikasi menu `License Allocation` tetap Hidden

### Hendra Wijaya (Total Control Principal)

14. Ganti akun: Logout dari Maya Tanjung
15. Login sebagai Hendra Wijaya (`totalControlLic`, password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`)
16. Buka Allocation > License Allocation
17. Klik tab `History`
18. Ketik Search `{idMaya}`, tekan Enter
19. Klik row action `Allocation Log`
20. Verifikasi Allocation Log memuat entri `Allocation rejected by Maya T` dengan `Rejection Reason: Kuota tidak sesuai`
21. Tutup modal Allocation Log
22. Buka Approvals > License Allocation
23. Catat saldo kantong Principal (Balance, Reserved, Available) sebagai baseline
24. Klik `[Review]` pada alokasi `{idFree}`
25. Pilih Approve
26. Klik Submit
27. Verifikasi alokasi `{idFree}` `Completed` berstatus `Active` tanpa Capture
28. Verifikasi tidak ada transaksi wallet baru: saldo kantong Principal sama dengan baseline

## Notes

- Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan langkah tiap role berbeda.
- Langkah penghubung (S-03, R-16): langkah 1, 16, dan 22 (berpindah halaman), langkah 11 (membuka sidebar), langkah 14 dan 15 (ganti akun), langkah 17 (pindah tab), langkah 18 (Search untuk menemukan baris seed), langkah 21 (menutup modal Allocation Log), langkah 23 (baseline saldo).
- Langkah 12 adalah anchor positif sebelum asersi Hidden pada langkah 13 (8b butir 2): item sidebar `Approvals` baru dipakai langkah 1 sehingga selalu tampil bagi akun ini.
- Temuan untuk QA:
  - TC-AC-LA-480 butir c ("Allocation Log: `Allocation rejected by Maya T`") tidak dapat diamati oleh Maya Tanjung karena menu `License Allocation` Hidden bagi akunnya (butir d); spec membaca Allocation Log lewat akun Total Control Principal (Pre-setup #1, langkah 14 sampai 21) yang tidak disebut di Precondition TC-AC-LA-480.
  - TC-AC-LA-480 langkah 3 ("Periksa sidebar Allocation") tidak menyebut item menu sidebar lain yang menjadi pembanding; spec memakai item `Approvals`.
  - TC-AC-LA-480 butir b dan TC-AC-LA-261 butir b menyebut kuota, Reserve, Balance, dan transaksi wallet tanpa menyebut cara membacanya; spec memakai kemampuan baca state BE dari tim FE/BE.
  - TC-AC-LA-261 tidak menyebut kantong yang diperiksa pada langkah 2 ("Periksa Wallet"); spec memakai kantong Principal karena Payment `Free` dan requester Default User Principal.
