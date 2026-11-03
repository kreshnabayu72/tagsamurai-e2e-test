---
id: TC-FA-CAID-E2E-090-edit-asset-dan-code-division-tanpa-cascade
title: "Edit Asset dan Edit Code Division: Tidak Memperbarui Asset ID Sampai Save Berikutnya"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-279
  - TC-FA-CAID-280
  - TC-FA-CAID-289
  - TC-FA-CAID-290
coverage:
  web: automated
---

# Edit Asset dan Edit Code Division: Tidak Memperbarui Asset ID Sampai Save Berikutnya

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (TC-FA-CAID-279 dan 280): Total Control Company Targeted (Pre-setup No 29; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email disediakan tim FE/BE menurut Pre-setup TC), password `Spectra.env.FA_TARGETED_TC_PASSWORD` (nama env dari kolom `Akun dan Env Var` Pre-setup No 29; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (TC-FA-CAID-289 dan 290, ganti akun eksplisit pada langkah 18): Total Control Company Code Edit Division (Pre-setup No 36; akun sendiri, bukan akun Pre-setup No 1; email dan env var password disediakan tim FE/BE, nama env tidak tertulis di TC), password `Spectra.env.FA_CODEEDITDIV_TC_PASSWORD` (nama usulan, perlu konfirmasi tim FE; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Targeted (No 29): hook `before` men-seed konfigurasi B3 (Slash; Group, Category, Asset Name, Division, Purchase Date, Increment) dan aset Draft D1 sampai D3, Active D4, Waiting for Approval D5 (D3 `JKT/LAP/T490/HR/0926/3`, D4 `JKT/LAP/T490/HR/0926/4`); master data Asset Name `LaserJet Pro` (Code `LJP`) dengan Category `Printer` (Code `PRN`), Group `Warehouse`, Division `Human Resources` (Code `HR`). TC-FA-CAID-279 dan 280 berjalan di Company ini.
- Data Pre-setup Company Code Edit Division (No 36; milik spec ini, terpisah dari Company Alpha dan Company Targeted): master Group `Jakarta Office` (Code `JKT`), Category `IT Equipment > Laptop` (Code `LAP`), Asset Name `ThinkPad T490` (Code `T490`), dan Division `Human Resources` (Code `HR`); hook `before` men-seed konfigurasi B3 (Slash; Group, Category, Asset Name, Division, Purchase Date, Increment), aset Draft D3 `JKT/LAP/T490/HR/0926/3` dan Active D4 `JKT/LAP/T490/HR/0926/4`. TC-FA-CAID-289 dan 290 berjalan di Company ini, sehingga tidak mengubah master Pre-setup bersama.
- Fixture: nilai data Pre-setup di atas (akun Company, master data, Code Division, Asset ID seed) dibaca dari `Fixture.customAssetId.<kunci>`; berkas `fixtures/customAssetId.json` belum ada (prasyarat tahap script yang disediakan tim FE/BE).
- Data Dinamis: Code Division `Human Resources` diubah menjadi `PPL` dengan nama `People Operations` pada Company Code Edit Division (Dinamis No 12); dibersihkan oleh seed reset Company sebelum TC berikutnya.
- Efek permanen dan pemulihan Company Code Edit Division (S-06): Last Updated Division `Human Resources` berubah dan entri audit trail perubahan Division bertambah (entri log tidak dapat dihapus); Code Division, konfigurasi, dan aset dipulihkan ke `HR`, B3, D3, dan D4 lewat seed API (kemampuan pemulihan Code master disediakan tim FE/BE) di hook `before` dan `after` spec ini; seed Company khusus ini juga dikembalikan tim FE/BE sebelum tiap run (`suite.md`).
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: master data Company Targeted dan Company Code Edit Division diubah; hook `after` memulihkan Company Targeted ke konfigurasi B3 dan aset D1 sampai D5, serta Company Code Edit Division ke Code Division `HR`, konfigurasi B3, dan aset D3 dan D4. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-279: Asset Name berubah tidak memperbarui Asset ID sampai Save berikutnya me-resolve ulang

1. Buka Fixed Asset > Assets > Registration
2. Edit Draft aset D3: ganti Asset Name menjadi `LaserJet Pro` (Category `Printer`) dengan Brand `HP` dan Model/Type `M404` lalu simpan
3. Tunggu aksi selesai
4. Buka Fixed Asset > Assets > All Assets > Detail D3 > tab `Histori Aset`
5. Verifikasi Asset ID D3 tetap `JKT/LAP/T490/HR/0926/3`
6. Verifikasi tidak ada entri riwayat baru dan tidak ada banner
7. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, pilih Separator `- (Dash)` lalu klik `[Save]`
8. Tunggu aksi selesai
9. Buka Fixed Asset > Assets > All Assets > Detail D3
10. Verifikasi Asset ID D3 menjadi `JKT-PRN-LJP-HR-0926-3` karena segmen di-resolve ulang dari data aset terkini

### TC-FA-CAID-280: Group diubah di luar Transfer tidak memperbarui Asset ID

11. Pulihkan Company Targeted ke konfigurasi B3 dan aset D1 sampai D5 (seed API)
12. Buka Fixed Asset > Assets > Registration
13. Edit Draft aset D3: ganti Group menjadi `Warehouse` lalu simpan
14. Tunggu aksi selesai
15. Buka Fixed Asset > Assets > All Assets > Detail D3 > tab `Histori Aset`
16. Verifikasi Asset ID D3 tetap `JKT/LAP/T490/HR/0926/3`
17. Verifikasi tidak ada entri riwayat baru dan tidak ada banner

### TC-FA-CAID-289: Edit nama atau Code Division tidak memicu cascade ke Asset ID yang sudah terbit

18. Ganti akun: logout dari akun Total Control Company Targeted, lalu login sebagai Total Control Company Code Edit Division (password dari `Spectra.env.FA_CODEEDITDIV_TC_PASSWORD`)
19. Buka Global Settings > User > Division
20. Ubah Division `Human Resources` menjadi nama `People Operations` dengan Code `PPL` lalu simpan
21. Tunggu aksi selesai
22. Buka Fixed Asset > Assets > All Assets dan perhatikan D3, D4
23. Verifikasi Asset ID D3 tetap `JKT/LAP/T490/HR/0926/3` dan D4 tetap `JKT/LAP/T490/HR/0926/4`
24. Buka Detail D3 > tab `Histori Aset`
25. Verifikasi Asset ID D3 `JKT/LAP/T490/HR/0926/3` tampil pada Detail D3
26. Verifikasi tidak ada entri riwayat baru

### TC-FA-CAID-290: Save berikutnya me-resolve ulang Code Division terkini dari master

27. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, pilih Separator `- (Dash)` lalu klik `[Save]`
28. Tunggu aksi selesai
29. Buka Fixed Asset > Assets > All Assets
30. Verifikasi D3 menjadi `JKT-LAP-T490-PPL-0926-3` dan D4 menjadi `JKT-LAP-T490-PPL-0926-4` karena mass update me-resolve ulang dari Code master terkini

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1, 12 (buka halaman), 3, 8, 14, 21, 28 (tunggu aksi selesai sebelum pindah surface), 11 (pemulihan Company Targeted antar TC lewat seed), 18 (ganti akun eksplisit ke Company Code Edit Division, S-07; TC-FA-CAID-290 melanjutkan state TC-FA-CAID-289 tanpa pemulihan).
- Langkah 24 membuka tab `Histori Aset` D3 agar Expected "tidak ada entri riwayat baru" TC-FA-CAID-289 teramati; langkah itu tidak ada di TC (S-14) dan dicatat di Temuan. Langkah 25 (`Verifikasi` Asset ID D3 pada Detail D3) adalah anchor positif untuk asersi absence pada langkah 26 (bagian 8b butir 2): anchor pada langkah 23 berada di All Assets, bukan di Detail D3; asersi tambahan ini tidak ada di Expected TC dan dicatat di sini beserta alasannya (S-03).
- Temuan untuk QA:
  - TC-FA-CAID-289 tidak punya langkah membuka `Histori Aset`; spec menambah langkah penghubung (langkah 24) dan hanya memeriksa D3, tidak D4.
  - TC-FA-CAID-289 dan 290 kini berjalan di Company Code Edit Division (Pre-setup No 36) dengan akun sendiri; TC tidak menyebut email maupun nama env var password akun itu, nama env di Prerequisites adalah usulan. TC juga tidak menyebut Asset ID D1, D2, dan D5 pada Company itu (hanya D3 dan D4).
  - Email akun Total Control Company Targeted tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}` dan "email disediakan tim FE/BE").
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
