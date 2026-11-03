---
id: TC-FA-LIC-E2E-043-edit-allocation-simpan-sukses-child-remaining-parent-muat
title: "Edit Allocation: Simpan Sukses Child, Remaining Parent, dan Muat Ulang Section"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-118
  - TC-FA-LIC-119
  - TC-FA-LIC-120
  - TC-FA-LIC-121
coverage:
  web: automated
---

# Edit Allocation: Simpan Sukses Child, Remaining Parent, dan Muat Ulang Section

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #12: Divisi Logistik beralokasi 500 (Used 350, Allocated to Subgroups 100), Remaining Kantor Pusat 200, Divisi Keuangan belum beralokasi, Cabang Surabaya level 1 (Allocated Quota 900 menghasilkan Remaining Quota 110).
- Data: Intercept jaringan mengamati permintaan ulang data License Summary (Section 1) dan Level 1 Groups Quota (Section 2) setelah Save.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Intercept jaringan mengamati permintaan data Section 1 dan Section 2 (asersi dimuat ulang).

## Test Steps

### TC-FA-LIC-119: Setelah Save sukses kedua section dimuat ulang

1. Klik tab `Allocation Quota`
2. Klik node `All Groups` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Cabang Surabaya`
4. Pasang intercept jaringan yang mencatat permintaan data Section 1 dan Section 2
5. Isi New Allocated Quota `900`
6. Klik `[Save]`
7. Verifikasi Section 1 (License Summary) dan Section 2 (Level 1 Groups Quota) dimuat ulang
8. Verifikasi baris `Cabang Surabaya`: Allocated Quota `900` dan Remaining Quota `110`
9. Lepas intercept jaringan

### TC-FA-LIC-118: Simpan alokasi child dari 500 ke 600

10. Klik node `Kantor Pusat` di Sidebar
11. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
12. Isi New Allocated Quota `600`
13. Klik `[Save]`
14. Verifikasi modal tertutup
15. Verifikasi toast sukses `Success, group license quota updated.`
16. Verifikasi baris `Divisi Logistik`: Allocated Quota `600`, Allocated to Subgroups `100`, Used `350`, Reserved `0`, Remaining Quota `150`
17. Verifikasi Group Quota Summary Kantor Pusat: Total `1500`, Allocated to Subgroups `700`, Used `700`, Reserved `0`, Remaining `100`
18. Muat ulang halaman License, lalu klik tab `Allocation Quota`
19. Klik node `Kantor Pusat` di Sidebar
20. Verifikasi nilai tersimpan setelah muat ulang: Allocated Quota baris `Divisi Logistik` `600`

### TC-FA-LIC-120: Alokasi pertama pada grup belum beralokasi

21. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan
22. Muat ulang halaman License, lalu klik tab `Allocation Quota`
23. Klik node `Kantor Pusat` di Sidebar
24. Klik tombol ikon `[Edit]` pada baris `Divisi Keuangan`
25. Isi New Allocated Quota `50`
26. Klik `[Save]`
27. Verifikasi toast sukses `Success, group license quota updated.`
28. Klik node `Divisi Keuangan` di Sidebar
29. Verifikasi Context Header `Divisi Keuangan (GRP-FIN)` tanpa badge `Not Allocated`
30. Verifikasi Group Quota Summary: Total `50`, Allocated to Subgroups `0`, Used `0`, Reserved `0`, Remaining `50`
31. Klik node `Kantor Pusat` di Sidebar
32. Verifikasi Group Quota Summary Kantor Pusat: Allocated to Subgroups `650` dan Remaining `150`

### TC-FA-LIC-121: Alokasi level 1 dinaikkan mengambil dari pool organisasi

33. Klik node `All Groups` di Sidebar
34. Klik tombol ikon `[Edit]` di samping Allocated Quota baris `Kantor Pusat`
35. Isi New Allocated Quota `1600`
36. Klik `[Save]`
37. Verifikasi toast sukses `Success, group license quota updated.`
38. Verifikasi Allocated Quota baris `Kantor Pusat` `1600`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): klik node Sidebar memilih node blok; fixture BE pemulih, muat ulang halaman, dan klik tab mengembalikan Pre-setup #12 sebelum TC-FA-LIC-120 karena TC-FA-LIC-118 mengubah Divisi Logistik dan asersi Allocated to Subgroups 650 bergantung pada Divisi Logistik 500.
- Urutan TC: TC-FA-LIC-119 dan TC-FA-LIC-118 (state Pre-setup #12), pemulihan, TC-FA-LIC-120, lalu TC-FA-LIC-121 (tidak bergantung pada Divisi Keuangan 50) (S-10).
- Temuan untuk QA:
  - TC-FA-LIC-119: `dimuat ulang` tidak punya cara observasi di TC; spec mengasersinya lewat permintaan ulang data Section 1 dan Section 2 pada intercept jaringan.
- Alasan di atas sekitar 35 langkah (38 langkah): semua blok satu topik (Save sukses Edit Allocation) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pemulihan fixture dan muat ulang.
