---
id: TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division
title: "Cascade Dilewati: Purchase Date dan Division saat Formula Tanpa Segmen atau Master Switch OFF"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-281
  - TC-FA-CAID-282
  - TC-FA-CAID-287
  - TC-FA-CAID-301
coverage:
  web: automated
---

# Cascade Dilewati: Purchase Date dan Division saat Formula Tanpa Segmen atau Master Switch OFF

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Targeted (Pre-setup No 29; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE), password `Spectra.env.FA_TARGETED_TC_PASSWORD` (nama usulan; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Targeted (No 29). Hook `before` men-seed konfigurasi B5 (tanpa Purchase Date; Slash) dan aset Draft D1 ber-Asset ID `JKT/LAP/T490/1` (TC-FA-CAID-281). Seed antar TC lewat seed API: Master Switch OFF dengan D1 Draft Asset ID `1` (TC-FA-CAID-282); B1 (tanpa segmen Division) dengan D2 Draft `JKT/LAP/T490/0926/2` (TC-FA-CAID-287); B3 dengan Master Switch OFF dan D2 Draft Asset ID `2` (TC-FA-CAID-301). Master data Division `Human Resources` (Code `HR`). Purchase Date `15/09/26`, Purchase Price `15000000`, dan faktur `invoice.pdf` (berkas dari fixture, belum ada; prasyarat tahap script yang disediakan tim FE/BE) sesuai Data Uji.
- Data Dinamis: Purchase Date `15/09/26` pada D1 dan Division `Human Resources` pada D2; dibersihkan oleh seed reset Company sebelum TC berikutnya.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: konfigurasi dan aset Company Targeted diubah; hook `after` memulihkan Company Targeted ke konfigurasi B3 dan aset D1 sampai D5. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-281: Purchase Date diisi saat formula tanpa segmen Purchase Date dilewati

1. Buka Fixed Asset > Assets > Registration
2. Klik `[Complete Detail]` pada aset D1
3. Isi Purchase Date `15/09/26`, Purchase Price `15000000`, dan unggah faktur `invoice.pdf` lalu klik `[Save Details]`
4. Verifikasi toast sukses `Success, asset details completed.` tampil
5. Buka Fixed Asset > Assets > All Assets > Detail D1 > tab `Histori Aset`
6. Verifikasi Purchase Date `15/09/26` tersimpan pada aset
7. Verifikasi Asset ID D1 tetap `JKT/LAP/T490/1`
8. Verifikasi tidak ada entri riwayat dan tidak ada banner

### TC-FA-CAID-282: Purchase Date diisi saat Master Switch OFF dilewati tanpa mutasi Asset ID

9. Pulihkan Company Targeted ke Master Switch OFF dengan aset Draft D1 ber-Asset ID `1` (seed API)
10. Buka Fixed Asset > Assets > Registration
11. Klik `[Complete Detail]` pada aset D1
12. Isi Purchase Date `15/09/26`, Purchase Price `15000000`, dan unggah faktur `invoice.pdf` lalu klik `[Save Details]`
13. Tunggu aksi selesai
14. Buka Fixed Asset > Assets > All Assets > Detail D1 > tab `Histori Aset`
15. Verifikasi Purchase Date `15/09/26` tersimpan pada aset
16. Verifikasi Asset ID D1 tetap `1`
17. Verifikasi tidak ada entri riwayat dan tidak ada banner

### TC-FA-CAID-287: Mutasi Division saat formula tanpa segmen Division dilewati

18. Pulihkan Company Targeted ke baseline B1 (tanpa segmen Division) dengan aset Draft D2 ber-Asset ID `JKT/LAP/T490/0926/2` (seed API)
19. Buka Fixed Asset > Assets > Registration
20. Edit Draft aset D2: pilih Division `Human Resources` lalu simpan
21. Tunggu aksi selesai
22. Buka Fixed Asset > Assets > All Assets > Detail D2 > tab `Histori Aset`
23. Verifikasi Asset ID D2 tetap `JKT/LAP/T490/0926/2`
24. Verifikasi tidak ada entri riwayat dan tidak ada banner

### TC-FA-CAID-301: Mutasi Division saat Master Switch OFF dilewati tanpa mutasi Asset ID

25. Pulihkan Company Targeted ke konfigurasi B3 dengan Master Switch OFF dan aset Draft D2 ber-Asset ID `2` (seed API)
26. Buka Fixed Asset > Assets > Registration
27. Edit Draft aset D2: pilih Division `Human Resources` lalu simpan
28. Tunggu aksi selesai
29. Buka Fixed Asset > Assets > All Assets > Detail D2 > tab `Histori Aset`
30. Verifikasi Division D2 tersimpan `Human Resources`
31. Verifikasi Asset ID D2 tetap `2`
32. Verifikasi tidak ada entri riwayat dan tidak ada banner

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1, 10, 19, 26 (buka halaman), 9, 18, 25 (pemulihan Company Targeted antar TC lewat seed), 13, 21, 28 (tunggu aksi selesai sebelum pindah surface).
- Asersi "tidak ada entri riwayat dan tidak ada banner" didahului Verifikasi Asset ID aset pada Detail yang sama sebagai anchor positif; Detail dan tab `Histori Aset` dibuka dengan data aset sendiri.
- Pembagian TC lintas spec: TC-FA-CAID-277, 278, 254, dan 283 (Purchase Date) ada di spec 089 (`TC-FA-CAID-E2E-089-purchase-date-diisi-update-segmen`); TC-FA-CAID-285, 255, 286, dan 302 (Division) ada di spec 092 (`TC-FA-CAID-E2E-092-mutasi-division-segmen-isi-ganti-dan-idempoten`).
- Temuan untuk QA:
  - Expected TC-FA-CAID-281, 282, 287, dan 301 mengasersi "tidak ada entri riwayat dan tidak ada banner" tetapi langkah TC tidak membuka tab `Histori Aset`; spec membukanya sebagai langkah penghubung (S-14).
  - Langkah TC-FA-CAID-281 dan 282 mengisi Purchase Price dan faktur; spec mengikuti TC.
  - Email akun Total Control Company Targeted tidak tertulis di Pre-setup TC.
