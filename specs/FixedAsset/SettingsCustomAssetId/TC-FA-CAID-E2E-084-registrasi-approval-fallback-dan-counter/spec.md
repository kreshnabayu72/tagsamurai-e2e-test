---
id: TC-FA-CAID-E2E-084-registrasi-approval-fallback-dan-counter
title: "Registrasi Aset: Approval Tanpa Increment Baru, Fallback Master Switch OFF, dan Counter Switch OFF/ON"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-261
  - TC-FA-CAID-263
  - TC-FA-CAID-264
coverage:
  web: automated
---

# Registrasi Aset: Approval Tanpa Increment Baru, Fallback Master Switch OFF, dan Counter Switch OFF/ON

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Company Register (Pre-setup No 24; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE), password `Spectra.env.FA_REGISTER_TC_PASSWORD` (nama env dari kolom `Akun dan Env Var` Pre-setup No 24; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (approver TC-FA-CAID-261, ganti akun eksplisit di tengah spec): Total Control sesi 2 (Pre-setup No 8; pola `totalControlSecond_automated_{namaCompany}@qwertysystem.net`; email pada Company Register disediakan tim FE), password `Spectra.env.FA_TC2_PASSWORD`. Setelah approval, spec login kembali sebagai akun aktor pertama.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Register (No 24): plan Professional; master data Division `Human Resources` (`HR`), Asset Name `ThinkPad T490` (`T490`), Group `Jakarta Office` (`JKT`), Category `Laptop` (`LAP`), Brand `Lenovo`. Seed awal (hook `before`): konfigurasi B1 dan satu aset Draft ber-Asset ID `JKT/LAP/T490/0000/1` (dipakai TC-FA-CAID-261). Seed antar TC lewat seed API: B1 dengan Master Switch OFF tanpa aset (TC-FA-CAID-263), B1 tanpa aset (TC-FA-CAID-264).
- Data Dinamis: aset hasil registrasi (Dinamis No 5 dan 6, aset A, B, C); dibersihkan oleh seed reset Company sebelum TC berikutnya.
- Fixture: nilai data Pre-setup di atas (akun Company, master data, Asset ID seed) dibaca dari `Fixture.customAssetId.<kunci>`; berkas `fixtures/customAssetId.json` belum ada (prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: konfigurasi singleton Company Register (Master Switch) diubah dan aset dibuat; hook `after` memulihkan Company Register ke konfigurasi B1 tanpa aset dan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-261: Submit for Approval dan Approve tidak mengalokasikan Increment baru

1. Buka Fixed Asset > Assets > Registration
2. Klik `[Submit for Approval]` pada aset Draft
3. Verifikasi aset berstatus Waiting for Approval
4. Verifikasi Asset ID aset tetap `JKT/LAP/T490/0000/1`
5. Logout dari akun Total Control Company Register
6. Login sebagai Total Control sesi kedua (password dari `Spectra.env.FA_TC2_PASSWORD`)
7. Buka Approvals > Registration dan klik `[Approve]` pada tiket
8. Tunggu aksi selesai
9. Logout dari akun Total Control sesi kedua
10. Login sebagai Total Control Company Register (password dari `Spectra.env.FA_REGISTER_TC_PASSWORD`)
11. Buka Fixed Asset > Assets > All Assets
12. Verifikasi aset berstatus Active
13. Verifikasi Asset ID aset tetap `JKT/LAP/T490/0000/1`
14. Buka Fixed Asset > Assets > Registration, klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
15. Verifikasi aset baru mendapat Asset ID `JKT/LAP/T490/0000/2`, membuktikan tidak ada Increment ganda untuk aset pertama

### TC-FA-CAID-263: Master Switch OFF: registrasi memakai Increment polos

16. Pulihkan Company Register ke konfigurasi B1 dengan Master Switch OFF tanpa aset (seed API)
17. Buka Fixed Asset > Assets > Registration
18. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
19. Ulangi registrasi kedua
20. Verifikasi Asset ID aset pertama `1` dan aset kedua `2` tanpa recipe format kustom

### TC-FA-CAID-264: Increment melanjutkan posisi terakhir saat Switch OFF lalu ON dan aset fallback ikut di-reformat

21. Pulihkan Company Register ke konfigurasi B1 (Master Switch ON) tanpa aset (seed API)
22. Buka Fixed Asset > Assets > Registration, klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]` (aset A)
23. Tunggu aksi selesai
24. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, geser Master Switch ke OFF dan klik `[Disable]`
25. Tunggu aksi selesai
26. Buka Fixed Asset > Assets > Registration dan registrasi aset B: klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
27. Perhatikan Asset ID aset A dan aset B
28. Verifikasi setelah OFF: aset A menjadi `1`
29. Verifikasi setelah OFF: aset B terbit `2`
30. Kembali ke tab Custom Asset ID dan geser Master Switch ke ON
31. Tunggu aksi selesai
32. Buka Fixed Asset > Assets > Registration dan perhatikan Asset ID aset A dan aset B
33. Verifikasi setelah ON: aset A kembali `JKT/LAP/T490/0000/1`
34. Verifikasi setelah ON: aset B di-reformat `JKT/LAP/T490/0000/2`
35. Registrasi aset C: klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
36. Verifikasi aset C terbit `JKT/LAP/T490/0000/3`
37. Verifikasi counter tidak di-reset ke 1
38. Verifikasi konfigurasi tidak hilang: Asset ID aset C memakai format kustom B1 (Group, Category, Asset Name, Purchase Date, Increment dengan Separator Slash)

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1, 11, 17, 32 (buka halaman), 5, 6, 9, 10 (ganti akun eksplisit, S-07; langkah 5 sampai 10 hanya memicu approval oleh akun kedua), 8, 23, 25, 31 (tunggu aksi selesai sebelum pindah surface atau ganti akun; hasil `[Save as Draft]` aset A pada langkah 22 tidak diasersi langsung, bagian 8b butir 8), 16 dan 21 (pemulihan Company Register antar TC lewat seed), 27 (perhatikan).
- Spec ini 38 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik (penerbitan Asset ID saat registrasi: approval tanpa Increment baru, fallback Master Switch OFF, dan counter OFF lalu ON), semua kelas fungsional registrasi, dan tiap blok TC di-seed ulang sendiri (langkah 16 dan 21) sehingga berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Empat langkah di atas 34 berasal dari pemisahan klausa per aset (S-01) dan satu langkah tunggu aksi selesai (bagian 8b butir 8).
- Langkah 28 dan 29, 33 dan 34, serta 36 dan 37 memisahkan klausa Expected TC-FA-CAID-264 a, b, dan c per aset atau per pernyataan (S-01).
- Pembagian TC lintas spec: TC-FA-CAID-265 dan TC-FA-CAID-266 ada di spec 096 (`TC-FA-CAID-E2E-096-registrasi-hapus-draft-dan-counter-setelah-save`).
- Temuan untuk QA:
  - Email akun Total Control Company Register dan akun sesi 2 pada Company Register tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}` dan "email disediakan tim FE/BE"); Pre-setup No 8 kini menyatakan akun sesi 2 yang sama menjadi approver pada Company Register.
  - TC-FA-CAID-261 tidak menyebut halaman pengamatan status Waiting for Approval (dipakai tabel Registration) dan tidak menyebut pelaku registrasi aset baru pada langkah ketiga TC; spec memakai akun aktor pertama.
  - TC-FA-CAID-264 tidak menyebut apakah geser Master Switch ke ON menampilkan dialog atau toast, dan Expected "konfigurasi tidak hilang" tidak punya langkah observasi; diasersi lewat format kustom Asset ID aset C.
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
