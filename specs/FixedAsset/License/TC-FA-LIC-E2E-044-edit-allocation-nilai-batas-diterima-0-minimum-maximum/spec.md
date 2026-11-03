---
id: TC-FA-LIC-E2E-044-edit-allocation-nilai-batas-diterima-0-minimum-maximum
title: "Edit Allocation: Nilai Batas Diterima (0, Minimum, Maximum, Enter, Double-click Save)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-122
  - TC-FA-LIC-123
  - TC-FA-LIC-127
  - TC-FA-LIC-146
  - TC-FA-LIC-159
coverage:
  web: automated
---

# Edit Allocation: Nilai Batas Diterima (0, Minimum, Maximum, Enter, Double-click Save)

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
- Data: Pre-setup #12: Divisi Keuangan belum beralokasi dengan Used 0 dan Reserved 0; Divisi Logistik beralokasi 500 (Minimum Quota 450, Maximum Quota 700); Divisi IT beralokasi 100; Remaining Kantor Pusat 200.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Kemampuan membaca jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12).
- Kemampuan teknis: Intercept jaringan menghitung request Save (asersi satu request pada double-click).

## Test Steps

### TC-FA-LIC-122: Nilai 0 sah untuk grup tanpa pemakaian

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi Keuangan`
4. Isi New Allocated Quota `0`
5. Klik `[Save]`
6. Verifikasi toast sukses `Success, group license quota updated.`
7. Verifikasi Allocated Quota baris `Divisi Keuangan` `0` (bukan `—`) dan Remaining Quota `0`
8. Verifikasi nilai `0` diperlakukan sebagai alokasi, bukan Remove Allocation: toast sukses bukan `Success, group license allocation removed.`

### TC-FA-LIC-123: Nilai tepat Minimum Quota (450) diterima

9. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
10. Isi New Allocated Quota `450`
11. Klik `[Save]`
12. Verifikasi toast sukses `Success, group license quota updated.`
13. Verifikasi Allocated Quota baris `Divisi Logistik` `450` dan Remaining Quota `0`

### TC-FA-LIC-127: Nilai tepat Maximum Quota (700) diterima

14. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
15. Isi New Allocated Quota `700`
16. Klik `[Save]`
17. Verifikasi toast sukses `Success, group license quota updated.`
18. Verifikasi Allocated Quota baris `Divisi Logistik` `700`
19. Verifikasi Group Quota Summary Kantor Pusat: Remaining `0`

### TC-FA-LIC-146: Enter pada input kuota menyimpan

20. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan
21. Muat ulang halaman License, lalu klik tab `Allocation Quota`
22. Klik node `Kantor Pusat` di Sidebar
23. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
24. Isi New Allocated Quota `120`
25. Tekan Enter saat fokus di input
26. Verifikasi form tersimpan dengan toast `Success, group license quota updated.`

### TC-FA-LIC-159: Double-click Save hanya memproses satu request

27. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan
28. Muat ulang halaman License, lalu klik tab `Allocation Quota`
29. Klik node `Kantor Pusat` di Sidebar
30. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
31. Catat jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline
32. Pasang intercept jaringan yang menghitung request Save
33. Isi New Allocated Quota `120`
34. Klik `[Save]` dua kali cepat
35. Verifikasi hanya satu request dikirim
36. Verifikasi satu toast sukses `Success, group license quota updated.`
37. Klik ikon Changelog pada toolbar
38. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding baseline
39. Tutup modal `Changelog: Allocation Quota`
40. Lepas intercept jaringan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih, muat ulang halaman, dan klik tab mengembalikan Pre-setup #12 sebelum TC-FA-LIC-146 (Maximum Quota Divisi IT bergantung pada Remaining Kantor Pusat 200 yang dihabiskan TC-FA-LIC-127) dan sebelum TC-FA-LIC-159 (Divisi IT harus 100 agar `120` bukan no-op); menutup modal Changelog; melepas intercept.
- Urutan TC: TC-FA-LIC-122, TC-FA-LIC-123, TC-FA-LIC-127 (Maximum Quota Divisi Logistik = alokasi saat ini + Remaining Kantor Pusat tetap 700 setelah TC-FA-LIC-123), TC-FA-LIC-146, lalu TC-FA-LIC-159 (S-10).
- TC-FA-LIC-122 klausa c (`diperlakukan sebagai alokasi, bukan Remove Allocation`) diasersi lewat teks toast yang berbeda dari toast Remove Allocation.
- Temuan untuk QA:
  - TC-FA-LIC-159: `tepat satu entri baru` hanya diasersi di `Changelog: Allocation Quota`; TC tidak menyebut System Log dan Activity Log pada klausa itu.
- Alasan di atas sekitar 35 langkah (40 langkah): semua blok satu topik (nilai batas yang diterima Edit Allocation) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pemulihan fixture dan muat ulang.
