---
id: TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0
title: "Banner Renewal: Batas N pada Hari Pengingat (31, 30, 8, 7, 2, 1, 0)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-464
  - TC-FA-LIC-465
  - TC-FA-LIC-466
  - TC-FA-LIC-467
  - TC-FA-LIC-468
  - TC-FA-LIC-469
  - TC-FA-LIC-470
coverage:
  web: automated
---

# Banner Renewal: Batas N pada Hari Pengingat (31, 30, 8, 7, 2, 1, 0)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Status term live Active pada seluruh blok; tanggal fixture hari ini berbeda per blok (30/11/26, 01/12/26, 23/12/26, 24/12/26, 29/12/26, 30/12/26, 31/12/26).
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-464: N = 31 (satu hari sebelum hari pengingat pertama) tidak dirender

1. Atur tanggal fixture hari ini ke `30/11/26` (N = 31); status term Active lewat fixture BE
2. Buka License > All License
3. Verifikasi Tabs Bar tampil
4. Verifikasi banner tidak dirender

### TC-FA-LIC-465: N = 30 (tepat hari pengingat pertama) stage Notice

5. Atur tanggal fixture hari ini ke `01/12/26` (N = 30); status term Active lewat fixture BE
6. Buka License > All License
7. Verifikasi banner stage Notice dengan Title `Subscription expires in 30 days`

### TC-FA-LIC-466: N = 8 (satu hari di atas hari pengingat kedua) tetap Notice

8. Atur tanggal fixture hari ini ke `23/12/26` (N = 8); status term Active lewat fixture BE
9. Buka License > All License
10. Verifikasi banner stage Notice dengan Title `Subscription expires in 8 days`

### TC-FA-LIC-467: N = 7 (tepat hari pengingat kedua) stage Reminder

11. Atur tanggal fixture hari ini ke `24/12/26` (N = 7); status term Active lewat fixture BE
12. Buka License > All License
13. Verifikasi banner stage Reminder (Warning) dengan Title `Subscription expires in 7 days`

### TC-FA-LIC-468: N = 2 (satu hari di atas hari pengingat final) tetap Reminder

14. Atur tanggal fixture hari ini ke `29/12/26` (N = 2); status term Active lewat fixture BE
15. Buka License > All License
16. Verifikasi banner stage Reminder dengan Title `Subscription expires in 2 days`

### TC-FA-LIC-469: N = 1 (tepat hari pengingat final) stage Final

17. Atur tanggal fixture hari ini ke `30/12/26` (N = 1); status term Active lewat fixture BE
18. Buka License > All License
19. Verifikasi banner stage Final dengan Title `Subscription expires tomorrow`
20. Verifikasi tidak ada tombol `[×]` pada banner

### TC-FA-LIC-470: N = 0 dengan status masih Active tidak dirender

21. Atur tanggal fixture hari ini ke `31/12/26` (N = 0); status term tetap Active, belum diubah Admin Console lewat fixture BE
22. Buka License > All License
23. Verifikasi Tabs Bar tampil
24. Verifikasi banner tidak dirender (modul tidak menghitung ulang status)

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): penyetelan tanggal fixture dan status term menyetel precondition TC.
- Asersi "banner tidak dirender" (TC-FA-LIC-464 dan 470) didahului `Verifikasi Tabs Bar tampil` sebagai anchor positif bahwa halaman sudah termuat.
- Temuan untuk QA:
  - TC-FA-LIC-465 sampai 468 menyatakan stage dan Title dalam satu butir Expected; spec menulisnya sebagai satu `Verifikasi` stage beserta Title. Severity stage Notice dan Reminder diasersi di spec 019.
