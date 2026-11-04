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
- Data Pre-setup #20: draf ke-1 Pre-setup #20 siap Submit di Gudang A (TC-FA-LIC-407, 408, dan 409). Fixture BE penyetel tiap blok menyiapkan draf ke-1 siap Submit sebelum blok itu, karena Submit yang berhasil pada TC-FA-LIC-407 mengubah draf menjadi aset Active.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Gudang A dan draf Pre-setup #20 bernama literal karena hierarki, kuota, dan draf tidak dapat dimiliki spec (nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dan #20 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- State yang diubah spec dan dipulihkan (kelas h, state tenant): plan client #1 diturunkan ke Starter lalu dikembalikan ke Paid; alokasi Gudang A disetel (alokasi 100 dengan Used 100 pada TC-FA-LIC-407; alokasi 100 dengan Used 98 dan Reserved 5 pada TC-FA-LIC-408 dan 409); Total Asset Capacity disetel 4.500 dengan Total Allocated 4.800 dan Kantor Pusat 1.500/Used 700/Allocated to Subgroups 600 (TC-FA-LIC-411); alokasi Kantor Pusat diubah ke 1400 pada langkah 30. Langkah 34 dan hook `after` memulihkan plan Paid, alokasi Pre-setup #12, dan Total Asset Capacity. Fixture BE penyetel plan, kuota, Used, dan Reserved serta pemulih Pre-setup #12 disediakan tim FE/BE; endpoint tidak dikarang.
- Kemampuan teknis: aksi Submit draf aset pada modul Asset sebagai pemicu registrasi (kemampuan disediakan tim FE); membaca status aset lewat fixture BE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Plan turun ke Starter (TC-FA-LIC-406 dan TC-FA-LIC-407)

1. Turunkan plan client ke Starter lewat fixture BE, lalu muat ulang halaman License
2. Verifikasi Tabs hanya `All License | Concurrent User`
3. Setel Gudang A beralokasi 100 dengan Used 100 (Total plan Starter belum penuh) lewat fixture BE
4. Submit draf ke-1 Pre-setup #20 di Gudang A
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
14. Submit draf ke-1 Pre-setup #20 di Gudang A
15. Verifikasi registrasi ditolak `Group quota exceeded. Available slots: 0. Please contact administrator to increase quota.`
16. Submit draf ke-1 Pre-setup #20 di Gudang A
17. Verifikasi registrasi ditolak karena Used + Reserved melampaui Allocated Quota (Used 98 saja belum melampaui)
18. Buka License > Allocation Quota > node `Gudang A`
19. Verifikasi `Remaining Quota` Gudang A ditampilkan 0

### Total Asset Capacity lebih kecil dari Total Allocated (TC-FA-LIC-411)

20. Setel Total Asset Capacity 4.500 dan Total Allocated 4.800 (Kantor Pusat level 1 beralokasi 1.500, Used 700, Allocated to Subgroups 600) lewat fixture BE, lalu muat ulang halaman License
21. Klik Tab `Allocation Quota`
22. Klik `[Edit]` pada baris `Kantor Pusat` di Section 2
23. Verifikasi helper `Available unallocated pool: 0 units.`
24. Isi field Allocated Quota dengan `1501`
25. Klik `[Save]`
26. Verifikasi `1501` ditolak saat klik `[Save]` dengan pesan inline `Total allocated quota exceeds organization total limit (1,500).`
27. Verifikasi modal Edit Allocated Quota tetap terbuka
28. Verifikasi Allocated Quota `Kantor Pusat` pada tabel tetap `1500` (kuota tidak berubah)
29. Isi field Allocated Quota dengan `1400`
30. Klik `[Save]`
31. Verifikasi `1400` diterima dengan toast sukses `Success, group license quota updated.`
32. Verifikasi modal Edit Allocated Quota tertutup
33. Verifikasi baris `Kantor Pusat` menampilkan Allocated Quota `1400`
34. Pulihkan plan Paid, toggle ON, alokasi Pre-setup #12, dan Total Asset Capacity lewat fixture BE

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-406, 407, 408, 409, 411). Tidak ada TC hanya-BE di spec ini. TC-FA-LIC-410 tidak ada di spec ini.
- Urutan TC diubah dari urutan nomor: TC-407 (dependensi TC-406: client turun ke Starter) dijalankan di antara Expected a dan b TC-406 (langkah 1 sampai 2, 3 sampai 5, 6 sampai 9) sehingga plan Starter tidak diturunkan dua kali (S-04, S-10). Langkah TC-406 "Kembalikan plan ke Paid" adalah langkah 6.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 7, 8, 11, 12, 18, 21 (klik tab dan node, membuka node Gudang A), langkah 34 (pemulihan state tenant).
- Temuan untuk QA:
  - TC-408 Expected c ("Penolakan berlaku sampai kuota dinaikkan atau Used dan Reserved turun") tidak punya langkah observasi untuk bagian "sampai kuota dinaikkan"; spec mengasersi penolakan berulang pada percobaan Submit kedua (langkah 16 dan 17, TC-409) dan tidak menaikkan kuota.
  - TC-407 Expected "hanya batas Total aset plan yang berlaku" tidak punya cara observasi terpisah; spec mengasersi keberhasilan registrasi saja (langkah 5).
  - TC-407 sampai TC-409 menulis "Submit draf ke-1 Pre-setup #20 di Gudang A" tanpa menyebut layar atau modul tempat Submit dijalankan (modul Asset); kemampuan disediakan tim FE. Ketiga TC memakai draf ke-1 yang sama padahal Submit yang berhasil pada TC-407 mengubahnya menjadi Active; spec mengandalkan fixture BE penyetel tiap blok untuk menyiapkan draf ke-1 siap Submit lagi.
