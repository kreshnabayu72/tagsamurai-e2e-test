---
id: TC-FA-LIC-E2E-018-state-tenant-toggle-license-allocation-per-group-off
title: "State Tenant: Toggle License Allocation per Group OFF"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-593
  - TC-FA-LIC-594
coverage:
  web: automated
---

# State Tenant: Toggle License Allocation per Group OFF

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control client Paid dengan `License allocation per group` OFF Pre-setup #35 `totalControlToggleOff_automated_{namaCompany}@qwertysystem.net` (data kuota dan hierarki Pre-setup #12 dengan baris alokasi grup dipertahankan: Divisi Logistik 500; kredensial `Spectra.env.FA_TOGGLEOFF_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit di langkah 9 sampai 11): Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; data kuota #12; kredensial `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite (#1).
- Data Pre-setup #12: Total Asset License 5.000; Kantor Pusat (alokasi 1500, Used 700, Allocated to Subgroups 600), Divisi Logistik 500, Gudang A. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan (kelas h, state tenant): `License allocation per group` client #1 dimatikan pada langkah 13 lalu dinyalakan kembali pada langkah 19 lewat fixture BE; hook `after` memulihkan toggle ON dan alokasi Pre-setup #12. Fixture BE penyetel toggle serta pemulih Pre-setup #12 disediakan tim FE/BE; endpoint tidak dikarang.
- Kemampuan teknis: membuka route Tab Allocation Quota langsung lewat URL dan muat ulang halaman (F5).
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Client Paid dengan toggle OFF (TC-FA-LIC-593)

1. Verifikasi Tabs: `All License | Concurrent User`
2. Verifikasi Tab `Allocation Quota` tidak dirender (bukan disabled, tanpa chip Upgrade)
3. Buka route Tab `Allocation Quota` langsung (tempel URL tab)
4. Verifikasi route Tab `Allocation Quota` dialihkan ke Tab `All License` dengan Breadcrumb `License > All License`
5. Verifikasi tidak ada toast
6. Verifikasi tidak ada dialog
7. Verifikasi tidak ada toolbar Section 2 Tab `Allocation Quota` di halaman mana pun sehingga tombol Download Allocation Quota tidak tersedia
8. Verifikasi tombol Download License Summary di Tab `All License` tetap tampil
9. Ganti akun: Logout
10. Login sebagai Total Control Pre-setup #1 (`Spectra.env.FA_TC_PASSWORD`)
11. Klik menu License pada sidebar

### Toggle dimatikan saat Tab Allocation Quota terbuka (TC-FA-LIC-594)

12. Klik Tab `Allocation Quota`
13. Matikan `License allocation per group` lewat fixture BE
14. Tekan F5
15. Verifikasi halaman dialihkan ke Tab `All License` dengan Breadcrumb `License > All License`
16. Verifikasi tidak ada toast
17. Verifikasi tidak ada dialog
18. Verifikasi Tabs: `All License | Concurrent User` (Tab `Allocation Quota` tidak dirender)
19. Kembalikan `License allocation per group` ke ON lewat fixture BE
20. Muat ulang halaman License
21. Verifikasi Tab `Allocation Quota` tampil
22. Klik Tab `Allocation Quota`
23. Klik node `Kantor Pusat`
24. Verifikasi `Allocated Quota` Divisi Logistik tetap 500 (baris alokasi dipertahankan)

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-593, 594). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-593 (akun #35) di awal agar hanya satu kali ganti akun (S-07).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 9 sampai 11 (ganti akun dan membuka License), langkah 22 dan 23 (membuka Tab dan node).
- Variasi pada Data Uji TC-594 (plan turun ke Starter sebagai pengganti toggle OFF; pemicu muat ulang berupa pindah Tab License atau fokus jendela kembali) tidak diulang; langkah memakai pemicu utama F5 dan plan Starter diuji pada TC-406.
