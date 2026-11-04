---
id: TC-FA-COA-E2E-012-mobile-android-selection-mode-popup-used-by-dan-switch-disabled
title: "Mobile Android: Selection Mode, Popup Used By, dan Switch Disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-101
  - TC-FA-COA-366
  - TC-FA-COA-344
  - TC-FA-COA-345
coverage:
  mobile: automated
---

# Mobile Android: Selection Mode, Popup Used By, dan Switch Disabled

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi Android native pada emulator atau perangkat yang disediakan tim FE. `parallel: false` karena perangkat fisik bersama.
- Role yang diuji (bagian 3a; spec ditulis per blok role, urutan blok = urutan tabel):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Total Control (akun pertama, login di hook `before`) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` (terdaftar) | TC-FA-COA-101, 366, 344 |
| Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` (terdaftar) | TC-FA-COA-345 |

- Login akun pertama (Total Control) di hook `before` spec ini. Pengecualian atas hook `beforeEach` suite: layar web tidak berlaku di Android, sehingga spec membuka layar Chart of Accounts sendiri lewat langkah spec. Hook `after` spec mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak diubah): akun P1 `5-6001 – Depreciation Expense – Admin` (Active) sampai P5, dan P7 `4-7002 – Gain and Loss on Disposal` (Active, Used By 2: Asset Class `Delivery Vehicles` 3 Asset Name dan `Heavy Equipment` 12 Asset Name).
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-101: Long-press card masuk selection mode tanpa checkbox permanen dan menampilkan Floating Bottom Bulk Bar

1. Buka Settings > Accounting, pilih tab Chart of Accounts
2. Gulir card list sampai card P1 tampil
3. Tekan lama card P1
4. Verifikasi selection mode aktif tanpa checkbox permanen
5. Verifikasi Floating Bottom Bulk Bar memuat `[✕]`, counter, `[Select All]`, dan aksi bulk sesuai komposisi seleksi
6. Tekan `[Select All]`
7. Verifikasi `[Select All]` hanya memilih card yang sudah dimuat
8. Tekan `[✕]` pada Floating Bottom Bulk Bar

### TC-FA-COA-366: Mobile: selection mode berakhir lewat `[✕]`, lewat seleksi 0, dan lewat Back

9. Tekan lama card P1 sehingga selection mode aktif
10. Tekan `[✕]` pada Floating Bottom Bulk Bar
11. Verifikasi selection mode berakhir
12. Verifikasi centang hilang dan Floating Bottom Bulk Bar hilang
13. Tekan lama card P1 lagi
14. Tap card P1 untuk menghapus centang sehingga seleksi menjadi 0
15. Verifikasi selection mode berakhir dan Floating Bottom Bulk Bar hilang
16. Tekan lama card P1 lagi
17. Tekan tombol Back perangkat Android
18. Verifikasi selection mode berakhir dan Floating Bottom Bulk Bar hilang

### TC-FA-COA-344: Popup Used By tampil sebagai bottom sheet di Android

19. Gulir card list sampai card P7 tampil
20. Ketuk angka Used By `2` pada card P7
21. Verifikasi popup `Used By` tampil sebagai bottom sheet
22. Verifikasi bottom sheet memuat teks polos satu baris `4-7002 – Gain and Loss on Disposal (2)` di bawah judul
23. Verifikasi bottom sheet memuat dua bullet Asset Class `Delivery Vehicles` dengan 3 Asset Name dan `Heavy Equipment` dengan 12 Asset Name
24. Tutup bottom sheet `Used By`

### TC-FA-COA-345: Ketuk Switch Status yang Disabled menampilkan alasan sebagai tooltip yang hilang otomatis

25. Logout dari akun Total Control di Android
26. Login sebagai Read Only di Android
27. Buka Settings > Accounting, pilih tab Chart of Accounts
28. Gulir card list sampai card P1 tampil
29. Ketuk Switch Status pada card P1
30. Verifikasi tooltip `You don't have permission to edit.` tampil
31. Verifikasi tooltip hilang otomatis tanpa interaksi tambahan

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix Android (bagian 3a): blok Total Control lalu Read Only; spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Urutan (S-10): TC-FA-COA-366 mengikuti TC-FA-COA-101 (dependensi 101, langkah masuk selection mode disalin utuh pada langkah 9, 13, 16 per S-04).
- Langkah penghubung (S-03): langkah 2, 19, 28 (menggulir card list sampai card target; S-14); langkah 8 (keluar dari selection mode sebelum TC berikutnya, S-09); langkah 24 (menutup bottom sheet); langkah 25 sampai 27 (ganti akun eksplisit, S-07).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Pembagian TC lintas spec: TC-FA-COA-367 (selection mode berakhir setelah bulk) ada di spec 084.
- Temuan untuk QA:
  - TC-FA-COA-101 butir b menyebut "aksi bulk sesuai komposisi seleksi" tanpa menyebut aksi untuk seleksi P1 (Active); spec mengasersi keberadaan elemen bar sesuai Expected tanpa menyebut nama aksi bulk.
  - TC-FA-COA-101 butir c ("hanya memilih card yang sudah dimuat") tidak menyebut jumlah card yang dimuat; counter dibandingkan dengan jumlah card yang termuat saat langkah 6 (dibaca dari card list).
  - Cara menutup bottom sheet (langkah 24) tidak disebut TC; ditetapkan tim FE.
  - TC-FA-COA-345 butir b tidak menyebut durasi hilang otomatis; ditetapkan tim FE.
