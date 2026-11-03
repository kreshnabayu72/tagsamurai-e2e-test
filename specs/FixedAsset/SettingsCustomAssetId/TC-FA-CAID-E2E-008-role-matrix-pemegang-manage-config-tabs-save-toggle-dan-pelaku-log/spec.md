---
id: TC-FA-CAID-E2E-008-role-matrix-pemegang-manage-config-tabs-save-toggle-dan-pelaku-log
title: "Role Matrix: Pemegang Manage asset ID configuration: Tabs Bar, Account Codes, Save, Toggle, dan Pelaku Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-29
  - TC-FA-CAID-43
  - TC-FA-CAID-30
  - TC-FA-CAID-31
  - TC-FA-CAID-251
coverage:
  web: automated
---

# Role Matrix: Pemegang Manage asset ID configuration: Tabs Bar, Account Codes, Save, Toggle, dan Pelaku Log

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Config-Update) di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite untuk akun itu. Akun kedua login lewat langkah ganti akun eksplisit.
- Role yang diuji (Company Alpha; email `<prefix>_automated_{namaCompany}@qwertysystem.net`, password dari env, tidak ditulis di spec atau fixture):

| Blok | TC | Role | Pre-setup | Prefix email | Env password |
|---|---|---|---|---|---|
| 1 | TC-FA-CAID-43, 30, 251, 31 | Config-Update (Manage asset ID configuration dengan Read dan Update, tanpa Manage asset master data; pengguna Rina Putri) | No 3 | `configUpdate` | `Spectra.env.FA_CFGUPD_PASSWORD` |
| 2 | TC-FA-CAID-29 | Config-Read (Manage asset ID configuration hanya Read, tanpa Manage accounting) | No 4 | `configRead` | `Spectra.env.FA_CFGREAD_PASSWORD` |

  Nama env password mengikuti kolom Akun dan Env Var Pre-setup No 3 dan 4 TC. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk semua akun UI suite; konfigurasi Company Alpha dan aset A1 sampai A5 dipulihkan ke baseline B1 di `beforeEach` lewat sesi API Total Control Company Alpha (kemampuan disediakan tim FE).
- Data Pre-setup: No 10 baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company); No 27 General Settings Company Alpha (Date Format `dd/MM/yy`, Time Format 24 jam; dipakai sebagai precondition TC-FA-CAID-251, tidak diasersi); No 28 master data Code List (Accounts Active ber-Code `Computer Equipment` 1210 dan `Office Furniture` 1220). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis: pembacaan jumlah entri Changelog Custom Asset ID sebelum dan sesudah aksi (disediakan tim FE/BE, mekanisme tidak tertulis di TC, PRD, atau LLD); restore baseline B1 lewat sesi API Total Control.
- State global: Save Separator `- (Dash)` (TC-FA-CAID-30 dan 251) dan Master Switch OFF (TC-FA-CAID-31) mengubah konfigurasi Company Alpha dan menambah entri audit trail permanen yang tidak dihapus; konfigurasi dipulihkan ke B1 lewat sesi API di langkah 9, 20, 26 dan hook `after` suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-43: Pemegang hanya Manage asset ID configuration: Tabs Bar dan breadcrumb (blok 1)

1. Verifikasi Tabs Bar hanya memuat tab `Custom Asset ID`
2. Klik segmen `Asset Master` pada Breadcrumb
3. Verifikasi tab pertama yang boleh diakses, yaitu tab `Custom Asset ID`, terbuka

### TC-FA-CAID-30: Pemegang Update saja menjalankan Save sampai sukses

4. Pilih Separator `- (Dash)`
5. Klik `[Save]`
6. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
7. Verifikasi Separator tersimpan `- (Dash)`
8. Verifikasi `[Save]` kembali disabled
9. Pulihkan konfigurasi Company Alpha ke baseline B1 lewat sesi API hingga konfigurasi tersimpan, lalu muat ulang halaman (F5)

### TC-FA-CAID-251: Pelaku pada log memakai pengguna yang menyimpan konfigurasi

10. Catat jumlah entri Changelog Custom Asset ID sebagai baseline
11. Pilih Separator `- (Dash)`
12. Klik `[Save]`
13. Tunggu aksi selesai: tombol `[Save]` kembali disabled
14. Klik tombol `[Changelog]`
15. Verifikasi jumlah entri Changelog bertambah dari baseline sehingga entri Edit Separator hasil langkah 12 tampil di baris teratas
16. Verifikasi baris Edit Separator tersebut menampilkan Modified By `Rina P`
17. Hover Modified By `Rina P` pada baris itu
18. Verifikasi tooltip hover berbunyi `Rina Putri`
19. Tutup modal `Changelog: Custom Asset ID` dengan `✕`
20. Pulihkan konfigurasi Company Alpha ke baseline B1 lewat sesi API hingga konfigurasi tersimpan, lalu muat ulang halaman (F5)

### TC-FA-CAID-31: Pemegang Update saja menjalankan Toggle sampai sukses

21. Geser Master Switch ke OFF
22. Klik `[Disable]` pada dialog `Disable Custom Asset ID`
23. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
24. Verifikasi Master Switch berada pada posisi OFF
25. Verifikasi kontrol form di-dim dan disabled
26. Pulihkan konfigurasi Company Alpha ke baseline B1 lewat sesi API hingga konfigurasi tersimpan

### TC-FA-CAID-29: Tab Account Codes tampil tanpa capability Manage accounting (blok 2)

27. Ganti akun: logout akun Config-Update, lalu login sebagai Config-Read (Pre-setup No 4)
28. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
29. Klik tautan `[View Code List]`
30. Klik tab `Account Codes`
31. Verifikasi tab `Account Codes` tampil dan terbuka
32. Verifikasi tabel memuat kolom `Account Name` dan `Code`
33. Verifikasi tabel memuat Account berstatus Active `Computer Equipment` (1210) dan `Office Furniture` (1220)
34. Tutup modal `Code List Reference` dengan `✕`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena langkah dan Expected tiap role berbeda dan ganti akun menuntut langkah eksplisit (langkah 27). Langkah pembuka TC-FA-CAID-43, 30, 251, 31 dipenuhi hook `beforeEach` suite.
- Urutan TC di spec: TC-FA-CAID-43, 30, 251, 31, lalu 29 (blok 2). Alasan: empat TC pemegang Update berurutan pada akun yang login di hook, TC-FA-CAID-29 butuh ganti akun sehingga terakhir, dan TC-FA-CAID-251 mengulang Save Separator `- (Dash)` dari B1 yang dipulihkan di langkah 9 (S-10).
- Langkah penghubung (tanpa `Verifikasi`): langkah 2, 4, 5, 11, 12, 14, 17, 21, 22, 29, 30 (aksi TC sebagai pemicu), langkah 9, 20, 26 (memulihkan B1 lewat sesi API; langkah 9 dan 20 diikuti muat ulang), langkah 10 (baseline jumlah entri, S-12), langkah 13 (Tunggu aksi selesai; langkah berikutnya membuka modal), langkah 19 dan 34 (menutup modal), dan langkah 27 dan 28 (ganti akun dan membuka halaman).
- Langkah 15 adalah asersi tambahan di luar Expected TC-FA-CAID-251 dan dipakai sebagai anchor positif entri baru berbaseline (S-12): jumlah entri naik dari baseline membuktikan baris teratas adalah hasil aksi langkah 12, bukan baris seed. Baseline langkah 10 mengikuti Precondition TC-FA-CAID-251 (baseline jumlah entri dicatat sebelum aksi).
- Pecahan Expected TC-FA-CAID-31 b: "Master Switch OFF" dan "kontrol form di-dim dan disabled" masing-masing klausa sendiri (langkah 24 dan 25). Pecahan TC-FA-CAID-29: "tab tampil dan terbuka berisi tabel dengan kolom ... untuk Account berstatus Active" menjadi langkah 31 sampai 33.
- Temuan untuk QA:
  - Nama pengguna Pre-setup No 3 (Rina Putri) hanya tersirat dari Expected TC-FA-CAID-251; Pre-setup TC tidak menyebutnya.
  - TC-FA-CAID-29 tidak menyebut baris Account yang dicek; spec memakai Account Active Pre-setup No 28 dan tidak mengasersi baris Inactive atau tanpa Code karena bukan bagian Expected.
  - Post Condition TC-FA-CAID-29, 30, 31, 43, 251 kosong; tidak ada yang diasersi.
