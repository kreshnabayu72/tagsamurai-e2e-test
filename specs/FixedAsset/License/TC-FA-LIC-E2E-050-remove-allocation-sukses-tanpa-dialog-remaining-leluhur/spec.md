---
id: TC-FA-LIC-E2E-050-remove-allocation-sukses-tanpa-dialog-remaining-leluhur
title: "Remove Allocation: Sukses Tanpa Dialog, Remaining Leluhur, dan Double-click Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-160
  - TC-FA-LIC-164
  - TC-FA-LIC-168
  - TC-FA-LIC-496
  - TC-FA-LIC-518
coverage:
  web: automated
---

# Remove Allocation: Sukses Tanpa Dialog, Remaining Leluhur, dan Double-click Save

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
- Data: Pre-setup #12: Divisi IT beralokasi 100 tanpa subgroup (Used 60, Reserved 0); Kantor Pusat dengan Remaining 200 (menjadi 240 setelah alokasi Divisi IT dihapus; Allocated to Subgroups 560).
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Kemampuan membaca jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12).
- Kemampuan teknis: Intercept jaringan menghitung request Save (asersi satu request pada double-click).

## Test Steps

### TC-FA-LIC-496: Remove Allocation langsung tanpa dialog, lalu diberikan kembali

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
4. Klik `[Clear Field]`
5. Klik `[Save]`
6. Verifikasi toast sukses `Success, group license allocation removed.`
7. Verifikasi tidak ada dialog konfirmasi
8. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
9. Isi New Allocated Quota `100`
10. Klik `[Save]`
11. Verifikasi toast sukses `Success, group license quota updated.`

### TC-FA-LIC-160: Remove Allocation child tanpa subgroup

12. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
13. Klik `[Clear Field]`
14. Klik `[Save]`
15. Verifikasi tidak ada dialog konfirmasi
16. Verifikasi modal tertutup
17. Verifikasi toast sukses `Success, group license allocation removed.`
18. Verifikasi baris `Divisi IT`: Allocated Quota `—`, Allocated to Subgroups `—`, Remaining Quota `—`, Used `60`
19. Verifikasi Group Quota Summary Kantor Pusat: Allocated to Subgroups `560` dan Remaining `240`

### TC-FA-LIC-164: Grup yang alokasinya dihapus memakai Remaining leluhur beralokasi terdekat

20. Klik node `Divisi IT` di Sidebar
21. Verifikasi Context Header memuat badge `Not Allocated`
22. Verifikasi Remaining pada Group Quota Summary sama dengan Remaining Kantor Pusat (`240`)
23. Arahkan kursor ke nilai Remaining
24. Verifikasi tooltip `Shared from Kantor Pusat`

### TC-FA-LIC-518: Remove lewat ikon Edit di samping Total pada Group Quota Summary

25. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan
26. Muat ulang halaman License, lalu klik tab `Allocation Quota`
27. Klik node `Divisi IT` di Sidebar
28. Pada Group Quota Summary klik tombol ikon `[Edit]` di samping nilai `Total` (100)
29. Klik `[Clear Field]`
30. Klik `[Save]`
31. Verifikasi tidak ada dialog konfirmasi
32. Verifikasi modal tertutup
33. Verifikasi toast sukses `Success, group license allocation removed.`
34. Verifikasi Context Header `Divisi IT (GRP-IT)` memuat badge `Not Allocated`
35. Verifikasi Group Quota Summary: Total `—`, Allocated to Subgroups `—`, Used by This Group `60`, Reserved by This Group `0`, Remaining `240`
36. Arahkan kursor ke nilai Remaining
37. Verifikasi tooltip `Shared from Kantor Pusat`

### TC-FA-LIC-168: Double-click Save pada Remove Allocation hanya memproses satu request

38. Jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan
39. Muat ulang halaman License, lalu klik tab `Allocation Quota`
40. Klik node `Kantor Pusat` di Sidebar
41. Catat jumlah entri `Changelog: Allocation Quota` sebagai baseline
42. Pasang intercept jaringan yang menghitung request Save
43. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
44. Klik `[Clear Field]`
45. Klik `[Save]` dua kali cepat
46. Verifikasi hanya satu request dikirim
47. Verifikasi satu toast `Success, group license allocation removed.`
48. Klik ikon Changelog pada toolbar
49. Verifikasi `Changelog: Allocation Quota` bertambah tepat satu entri dibanding baseline
50. Tutup modal `Changelog: Allocation Quota`
51. Lepas intercept jaringan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih, muat ulang halaman, dan klik tab mengembalikan Pre-setup #12 sebelum TC-FA-LIC-518 dan TC-FA-LIC-168 (keduanya membutuhkan Divisi IT beralokasi 100); menutup modal Changelog; melepas intercept.
- Urutan TC: TC-FA-LIC-496 (hapus lalu beri kembali 100), TC-FA-LIC-160, TC-FA-LIC-164 (bergantung pada TC-FA-LIC-160: node Divisi IT sesudah alokasinya dihapus), TC-FA-LIC-518, lalu TC-FA-LIC-168 (S-10).
- TC-FA-LIC-168: hanya `Changelog: Allocation Quota` yang dihitung karena Expected TC menyebut satu entri Changelog.
- Alasan di atas sekitar 35 langkah (51 langkah): semua blok satu topik (Remove Allocation sukses) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pemulihan fixture, muat ulang, dan hover tooltip.
