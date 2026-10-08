---
id: TC-AUTH-ACT-E2E-016-dimensi-entitas-dan-plan
title: "Aktivasi pada Client Suspended, Expired, dan Berbagai Plan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-110
  - TC-AUTH-ACT-111
  - TC-AUTH-ACT-112
coverage:
  web: automated
---

# Aktivasi pada Client Suspended, Expired, dan Berbagai Plan

## Prerequisites

- Tanpa login untuk semua langkah uji: aktivasi berjalan di halaman publik tanpa sesi aktif di browser.
- Akun aktor seeding: Total Control (Admin Console), pre-setup `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (baris 2 Tabel Data Uji Pre-setup); password dari `Spectra.env.AC_TC_PASSWORD`. Akun ini dipakai hook untuk membuat Client dan Default User, bukan oleh langkah uji.
- Password user uji dari `Spectra.env.ACT_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API Admin Console) membuat Client per run beserta Default User-nya, lalu mengaktifkan term subscription pertama Client (Activate Trial lewat API oleh aktor Principal) supaya Activation Email terkirim (`admin-console/client` `ACC-LOGIC-05.2`); Default User berstatus Pending Activation, token Active, link aktivasi diambil dari mail-catcher lalu disimpan. Untuk Client Suspended dan Expired urutannya: aktifkan subscription → ambil link aktivasi → baru suspend Client (aksi Suspend, F-ACC-06) / set term subscription Client ke Expired lewat kemampuan time-travel atau fixture status subscription environment uji (tidak ada endpoint Admin Console untuk ini). Untuk TC-AUTH-ACT-112, term pertama dibuat lewat `+ Subscription` mode New (F-ACCS-02) dengan plan Starter dan plan Enterprise oleh aktor Principal dengan approval di-bypass, sehingga term langsung Active (saldo Wallet Principal harus cukup untuk Feature Pricing Charge kedua plan, F-ACCS-02); Activate Trial tidak dipakai untuk Client ini karena plan trial belum tentu Starter/Enterprise. Nama Client dari Tabel Data Uji Pre-setup baris 3 dan 4 dengan suffix `{runId}-016` karena satu Client hanya punya satu Default User:
  - TC-AUTH-ACT-110: Client `PT Maju Bersama {runId}-016` status Suspended; Default User `Tika Pangestu` (`tikapangestu+{runId}-016@qwertysystem.net`)
  - TC-AUTH-ACT-111: Client `PT Sentosa Abadi {runId}-016` status Expired; Default User `Joko Suryani` (`jokosuryani+{runId}-016@qwertysystem.net`)
  - TC-AUTH-ACT-112: Client `PT Cahaya Starter {runId}-016` plan Starter dengan Default User `Mega Kartika` (`megakartika+{runId}-016@qwertysystem.net`); Client `PT Garuda Enterprise {runId}-016` plan Enterprise dengan Default User `Arif Prasetyo` (`arifprasetyo+{runId}-016@qwertysystem.net`)
- Kemampuan teknis: mail-catcher uji (API inbox per alamat) untuk mengambil link aktivasi; time-travel atau fixture status subscription di environment uji, untuk membuat term Expired (TC-AUTH-ACT-111) dan memajukannya ke Archive saat cleanup.
- Hook `after` membersihkan keempat Client mengikuti `ACC-LOGIC-04.4`/`04.5`: Unsuspend Client Suspended lebih dulu (F-ACC-06), lalu batalkan term yang Active (Cancel Subscription, F-ACCS-04a) atau majukan term Expired ke Archive lewat kemampuan di atas; setelah semua term terminal, polling status Client sampai Archived (job Auto-Archive F-ACC-07 berjalan hourly; environment uji perlu memicu job ini atau hook menunggu hingga batas waktu); lalu hapus Client beserta Default User-nya (`DELETE /v2/enterprise-management/clients/{id}` dengan body `{companyName: <nama Client>, confirm: true}`). Tetap jalan walau seeding gagal sebagian.

## Test Steps

### TC-AUTH-ACT-110: User dari Client yang suspended tetap bisa membuka Set Password dan mengaktifkan akun

1. Buka link aktivasi user `Tika Pangestu` di browser
2. Verifikasi `Auth > Account Activation > Set Password` tampil normal
3. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
4. Klik button "Set Password"
5. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated"
6. Verifikasi Status user `Tika Pangestu` Activated; pembatasan Client Suspended berlaku saat login, bukan saat aktivasi

### TC-AUTH-ACT-111: User dari Client yang expired tetap bisa membuka Set Password dan mengaktifkan akun

7. Buka link aktivasi user `Joko Suryani` di browser
8. Verifikasi `Auth > Account Activation > Set Password` tampil normal
9. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
10. Klik button "Set Password"
11. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated"
12. Verifikasi Status user `Joko Suryani` Activated; pembatasan Client Expired berlaku saat login, bukan saat aktivasi

### TC-AUTH-ACT-112: Aktivasi berjalan identik untuk user Client plan Starter dan plan Enterprise

13. Buka link aktivasi user `Mega Kartika` (Client plan Starter)
14. Verifikasi `Auth > Account Activation > Set Password` tampil tanpa batasan atau pesan upsell
15. Lakukan Set Password dengan `Spectra.env.ACT_PASSWORD`
16. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated"
17. Buka link aktivasi user `Arif Prasetyo` (Client plan Enterprise)
18. Verifikasi `Auth > Account Activation > Set Password` tampil tanpa batasan atau pesan upsell, identik dengan langkah 14
19. Lakukan Set Password dengan `Spectra.env.ACT_PASSWORD`
20. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated", identik dengan langkah 16
21. Verifikasi Status kedua user Activated

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness h (state tenant). TC-AUTH-ACT-112 (dimensi plan) ikut di sini karena memakai harness yang sama (Client per run dibuat lewat API Admin Console) dan tidak ada plan gating.
- Client dibuat per run dengan suffix, sesuai Tabel Data Uji Pre-setup baris 3–4, karena Default User yang sudah Activated tidak bisa dipakai ulang di run berikutnya.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
