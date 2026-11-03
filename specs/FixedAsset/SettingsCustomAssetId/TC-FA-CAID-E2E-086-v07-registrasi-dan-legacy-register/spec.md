---
id: TC-FA-CAID-E2E-086-v07-registrasi-dan-legacy-register
title: "V-07 pada Registrasi: Quick Register, Legacy Register, dan Counter Setelah Penolakan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-271
  - TC-FA-CAID-272
  - TC-FA-CAID-325
coverage:
  web: automated
---

# V-07 pada Registrasi: Quick Register, Legacy Register, dan Counter Setelah Penolakan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company V07R (Pre-setup No 33; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email disediakan tim FE/BE menurut Pre-setup TC), password `Spectra.env.FA_V07R_TC_PASSWORD` (nama env dari kolom `Akun dan Env Var` Pre-setup No 33; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company V07R (No 33): formula Initial Company `ABCDE`, Group, Category, Asset Name, Division, Purchase Date, Increment; Group Code `GRP-LONG-000001`, Category Code `CAT-LONG-000001`, Asset Name Code `AST-LONG-000001`; Division `Procurement X` (Code `PRCX`, menghasilkan 65 karakter) dan Division `Procurement` (Code `PRC`, Asset ID 64 karakter). Hook `before` men-seed satu aset valid ber-Increment 1 dengan Division `Procurement` (Asset ID 64 karakter); aset ini dipakai sebagai precondition TC-FA-CAID-325 dan menjadi baseline TC-FA-CAID-271 dan TC-FA-CAID-272. Nilai field Quick Register pada langkah 3, 13, 22, dan 29: Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal` (Division sesuai langkah). Nilai field khusus Legacy (Tanggal Perolehan Historis, Status Berkas Dokumen Fisik, Status Label Fisik Lama) valid apa pun (G-12), tidak diasersi.
- Fixture: nilai data Pre-setup di atas (akun Company, master data, Code Division, nilai field khusus Legacy) dibaca dari `Fixture.customAssetId.<kunci>`; berkas `fixtures/customAssetId.json` belum ada (prasyarat tahap script yang disediakan tim FE/BE).
- Data Dinamis: aset valid baru hasil registrasi TC-FA-CAID-325 (Dinamis No 14 untuk aset seed); dibersihkan oleh seed reset Company.
- Kemampuan teknis: sesi API aktor, seed API (suite.md), dan kemampuan baca jumlah baris tabel Registration dan jumlah aset Active di All Assets sebelum aksi (disediakan tim FE/BE).
- State global: aset dibuat; hook `after` memulihkan Company V07R ke seed awal dan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-271: Quick Register ditolak bila Asset ID melebihi 64 karakter dan transaksi di-rollback

1. Buka Fixed Asset > Assets > Registration
2. Catat baseline jumlah baris tabel Registration dan jumlah aset Active di All Assets
3. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Division `Procurement X`, Condition `Normal`, lalu klik `[Save as Draft]`
4. Verifikasi alert inline pada form Register berbunyi `Asset ID would exceed 64 characters. Contact your administrator to adjust the Custom Asset ID format.`
5. Verifikasi jumlah baris tabel Registration sama dengan baseline (tidak ada aset baru)
6. Verifikasi Asset ID aset seed tetap 64 karakter semula
7. Verifikasi tidak ada Asset ID baru yang dipotong menjadi 64 karakter
8. Klik `✕` pada form Register
9. Verifikasi dialog `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
10. Klik `[Leave]`
11. Verifikasi form Register tertutup

### TC-FA-CAID-272: Legacy Register ditolak bila Asset ID melebihi 64 karakter

12. Klik `[+ Legacy Register]`
13. Isi field Quick Register: Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Division `Procurement X`, Condition `Normal`, dan field khusus Legacy (Tanggal Perolehan Historis, Status Berkas Dokumen Fisik, Status Label Fisik Lama) dengan nilai valid dari fixture (lihat Prerequisites), lalu simpan
14. Verifikasi alert inline pada form berbunyi `Asset ID would exceed 64 characters. Contact your administrator to adjust the Custom Asset ID format.`
15. Klik `✕` pada form Legacy Register
16. Verifikasi dialog `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
17. Klik `[Leave]`
18. Verifikasi form Legacy Register tertutup
19. Buka Fixed Asset > Assets > All Assets
20. Verifikasi jumlah aset Active sama dengan baseline (tidak ada aset Active baru)

### TC-FA-CAID-325: Registrasi yang ditolak V-07 tidak menghasilkan Increment ganda pada registrasi berikutnya

21. Buka Fixed Asset > Assets > Registration
22. Registrasi aset dengan Division `Procurement X`: klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Division `Procurement X`, Condition `Normal`, lalu klik `[Save as Draft]`
23. Verifikasi alert inline V-07 `Asset ID would exceed 64 characters. Contact your administrator to adjust the Custom Asset ID format.` tampil
24. Verifikasi jumlah baris tabel Registration sama dengan baseline (tidak ada aset baru)
25. Klik `✕` pada form Register
26. Verifikasi dialog `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
27. Klik `[Leave]`
28. Verifikasi form Register tertutup
29. Registrasi aset valid: klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Division `Procurement` (Code `PRC`), Condition `Normal`, lalu klik `[Save as Draft]` sampai berhasil
30. Tunggu aksi selesai
31. Buka Fixed Asset > Assets > All Assets
32. Verifikasi aset valid baru terbit dengan Increment 2
33. Verifikasi Asset ID aset valid baru 64 karakter
34. Verifikasi tidak ada nomor Increment terlewat maupun ganda: Increment aset berurutan 1 lalu 2, karena counter ikut di-rollback bersama registrasi yang ditolak

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 1, 21 (buka halaman), 2 (baseline jumlah, S-12), 8, 10, 15, 17, 25, 27 (menutup form dengan `✕` dan `[Leave]`; `Verifikasi` dialog `Unsaved Changes` pada langkah 9, 16, dan 26 mengikuti S-08), 19 dan 31 (buka All Assets), 30 (tunggu aksi selesai sebelum pindah surface; hasil `[Save as Draft]` pada langkah 29 tidak diasersi langsung, bagian 8b butir 8).
- Asersi "tidak ada aset baru" pada langkah 5, 20, dan 24 memakai baseline jumlah; alert penolakan pada langkah 4, 14, 23 menjadi anchor positif (konvensi bagian 8b butir 2). Asersi ini bukan kelas g.
- Langkah 6 dan 7 memisahkan dua klausa Expected TC-FA-CAID-271 b (Asset ID seed tidak berubah dan tidak ada Asset ID dipotong) per klausa (S-01).
- Temuan untuk QA:
  - Precondition TC-FA-CAID-272 menulis "Company V07R sama seperti TC sebelumnya" tanpa id TC; dibaca sebagai TC-FA-CAID-271. Pre-setup No 33 menulis aset valid ber-Increment 1 hanya untuk TC-FA-CAID-325; spec men-seed aset itu di hook `before`, sehingga ia juga ada saat TC-FA-CAID-271 dan 272.
  - TC-FA-CAID-272 tidak menyebut nilai field Quick Register selain Division `PRCX`; spec memakai nilai yang sama dengan TC-FA-CAID-271 dan TC-FA-CAID-260 (Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`).
  - Nilai literal Asset ID aset seed (separator formula Company V07R tidak tertulis) tidak diasersi; hanya panjang 64 karakter.
  - Email akun Total Control Company V07R tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}` dan "email disediakan tim FE/BE").
