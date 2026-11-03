---
id: TC-FA-LIC-E2E-147-state-tenant-plan-starter-paid-kuota-grup-dan-total-asset-capacity
title: "State Tenant: Plan Turun ke Starter, Kembali ke Paid, dan Total Asset Capacity Lebih Kecil dari Total Allocated"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-406
  - TC-FA-LIC-407
  - TC-FA-LIC-408
  - TC-FA-LIC-409
  - TC-FA-LIC-411
coverage:
  web: automated
---

# State Tenant: Plan Turun ke Starter, Kembali ke Paid, dan Total Asset Capacity Lebih Kecil dari Total Allocated

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; data kuota #12; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Tidak ada ganti akun.
- Data Pre-setup #12: Total Asset License 5.000; Kantor Pusat (alokasi 1500, Used 700, Allocated to Subgroups 600), Divisi Logistik 500, Gudang A. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- Data milik spec (S-06): tiga draf aset siap Submit di Gudang A bersuffix `{runId}-147` (untuk TC-FA-LIC-407, 408, 409), di-seed di hook `before` dan dihapus di hook `after`.
- State yang diubah spec dan dipulihkan (kelas h, state tenant): plan client #1 diturunkan ke Starter lalu dikembalikan ke Paid; alokasi Gudang A disetel (alokasi 100 dengan Used 100 pada TC-FA-LIC-407; alokasi 100 dengan Used 98 dan Reserved 5 pada TC-FA-LIC-408 dan 409); Total Asset Capacity disetel 4.500 dengan Total Allocated 4.800 dan Kantor Pusat 1.500/Used 700/Allocated to Subgroups 600 (TC-FA-LIC-411); alokasi Kantor Pusat diubah ke 1400 pada langkah 27. Langkah 29 dan hook `after` memulihkan plan Paid, alokasi Pre-setup #12, dan Total Asset Capacity. Fixture BE penyetel plan, kuota, Used, dan Reserved serta pemulih Pre-setup #12 disediakan tim FE/BE; endpoint tidak dikarang.
- Kemampuan teknis: aksi Submit draf aset pada modul Asset sebagai pemicu registrasi (kemampuan disediakan tim FE); membaca status aset lewat fixture BE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Plan turun ke Starter (TC-FA-LIC-406 dan TC-FA-LIC-407)

1. Turunkan plan client ke Starter lewat fixture BE, lalu muat ulang halaman License
2. Verifikasi Tabs hanya `All License | Concurrent User`
3. Setel Gudang A beralokasi 100 dengan Used 100 (Total plan Starter belum penuh) lewat fixture BE
4. Submit 1 draf aset di Gudang A
5. Verifikasi registrasi berhasil walau Used Gudang A melampaui Allocated Quota lama (status aset dibaca lewat fixture BE)
6. Kembalikan plan ke Paid lewat fixture BE, lalu muat ulang halaman License
7. Klik Tab `Allocation Quota`
8. Klik node `Kantor Pusat`
9. Verifikasi `Allocated Quota` Divisi Logistik tetap 500 (nilai sama)

### Plan kembali ke Paid dengan Used + Reserved melampaui Allocated Quota (TC-FA-LIC-408 dan TC-FA-LIC-409)

10. Setel Gudang A beralokasi 100 dengan Used 98 dan Reserved 5 lewat fixture BE, lalu muat ulang halaman License
11. Klik Tab `Allocation Quota`
12. Klik node `Gudang A`
13. Verifikasi `Remaining Quota` Gudang A ditampilkan 0
14. Submit 1 draf aset di Gudang A
15. Verifikasi registrasi ditolak `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
16. Submit 1 draf aset lain di Gudang A
17. Verifikasi registrasi ditolak karena Used + Reserved melampaui Allocated Quota (Used 98 saja belum melampaui)
18. Verifikasi `Remaining Quota` Gudang A ditampilkan 0

### Total Asset Capacity lebih kecil dari Total Allocated (TC-FA-LIC-411)

19. Setel Total Asset Capacity 4.500 dan Total Allocated 4.800 (Kantor Pusat level 1 beralokasi 1.500, Used 700, Allocated to Subgroups 600) lewat fixture BE, lalu muat ulang halaman License
20. Klik Tab `Allocation Quota`
21. Klik `[Edit]` pada baris `Kantor Pusat` di Section 2
22. Verifikasi helper `Available unallocated pool: 0 units.`
23. Isi field Allocated Quota dengan `1501`
24. Klik `[Save]`
25. Verifikasi `1501` ditolak dengan pesan `Total allocated quota exceeds organization total limit (1,500).`
26. Isi field Allocated Quota dengan `1400`
27. Klik `[Save]`
28. Verifikasi `1400` diterima dengan toast `Success, group license quota updated.`
29. Pulihkan plan Paid, toggle ON, alokasi Pre-setup #12, dan Total Asset Capacity lewat fixture BE

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-406, 407, 408, 409, 411). Tidak ada TC hanya-BE di spec ini. TC-FA-LIC-410 tidak ada di spec ini.
- Urutan TC diubah dari urutan nomor: TC-407 (dependensi TC-406: client turun ke Starter) dijalankan di antara Expected a dan b TC-406 (langkah 1 sampai 2, 3 sampai 5, 6 sampai 9) sehingga plan Starter tidak diturunkan dua kali (S-04, S-10). Langkah TC-406 "Kembalikan plan ke Paid" adalah langkah 6.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 7, 8, 11, 12, 20 (klik tab dan node), langkah 29 (pemulihan state tenant).
- Temuan untuk QA:
  - TC-408 Expected c ("Penolakan berlaku sampai kuota dinaikkan atau Used dan Reserved turun") tidak punya langkah observasi untuk bagian "sampai kuota dinaikkan"; spec mengasersi penolakan berulang pada percobaan Submit kedua (langkah 16 dan 17, TC-409) dan tidak menaikkan kuota.
  - TC-407 Expected "hanya batas Total aset plan yang berlaku" tidak punya cara observasi terpisah; spec mengasersi keberhasilan registrasi saja (langkah 5).
  - TC-411 Expected b menulis "ditolak V-FALIC-03 dengan `(1,500)`" tanpa teks pesan penuh dan Expected c menulis "1400 diterima" tanpa teks toast; spec memakai teks V-FALIC-03 (`Total allocated quota exceeds organization total limit ([Total]).`) dan TS-FALIC-02 (`Success, group license quota updated.`) dari PRD `license.md` §6 dan §8 serta `(1,500)` dari TC.
  - TC-407 sampai TC-409 menulis "Submit 1 draf aset" tanpa menyebut layar atau modul tempat Submit dijalankan (modul Asset); kemampuan disediakan tim FE.
  - TC-407 Precondition "Login sbg Role: Total Control client Starter hasil downgrade" tidak menyebut akun; spec memakai akun #1 dengan fixture downgrade.
