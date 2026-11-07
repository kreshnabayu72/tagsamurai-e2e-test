---
id: TC-FA-SU-E2E-149-sub-tab-transaction-role-perilaku-filter-panel-dan-chip-dropdown-filter
title: "Sub-tab Transaction Role: Perilaku Filter Panel dan Chip Dropdown Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-396
  - TC-FA-SU-397
coverage:
  web: automated
---

# Sub-tab Transaction Role: Perilaku Filter Panel dan Chip Dropdown Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-396: Perilaku Filter Panel Sub-tab Transaction Role: tutup tanpa Apply, indikator titik, dan nilai kosong

1. Ketik Search `Yuda Pratama`, tekan Enter
2. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
3. Klik icon Filter
4. Buka dropdown Transaction
5. Centang `Disposal`
6. Klik di luar panel Filter
7. Klik icon Filter
8. Verifikasi panel dibuka lagi menampilkan nilai ter-Apply terakhir: field Transaction kosong dengan placeholder `All transactions`
9. Verifikasi tabel tidak berubah: 7 baris tetap tampil
10. Buka dropdown Transaction
11. Verifikasi dropdown Transaction tidak memiliki opsi untuk nilai kosong
12. Centang `Disposal`
13. Klik `[Apply]`
14. Verifikasi memilih opsi menyaring keluar baris yang nilainya kosong: sedikitnya satu baris tampil dan tidak ada baris dengan Transaction kosong
15. Klik icon Filter
16. Verifikasi icon Filter menampilkan badge titik saat panel tertutup
17. Klik icon Filter
18. Verifikasi icon Filter menampilkan badge titik saat panel terbuka
19. Klik header kolom Actions (⋯)
20. Hapus centang Transaction pada overlay Column Visibility
21. Tutup overlay Column Visibility dengan Esc
22. Verifikasi field Transaction tetap ada pada panel Filter
23. Verifikasi filter ter-Apply tetap berlaku: tabel menyisakan 2 baris `Disposal`
24. Klik header kolom Actions (⋯)
25. Centang kembali Transaction pada overlay Column Visibility
26. Tutup overlay Column Visibility dengan Esc
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Verifikasi badge titik pada icon Filter hilang
30. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-397: Chip dan checkbox dropdown Filter Sub-tab Transaction Role sinkron dua arah, logika OR dalam field

31. Klik icon Filter
32. Buka dropdown Transaction
33. Centang `Disposal`
34. Centang `Transfer`
35. Klik `[Apply]`
36. Verifikasi dua chip `Disposal` dan `Transfer` tampil di dalam field Transaction
37. Verifikasi hasil adalah gabungan (OR) kedua opsi: `Disposal - Approver`, `Disposal - Staff`, `Transfer - Asset Admin`, dan `Transfer - Monitoring & Report`
38. Klik ✕ pada chip `Disposal` tanpa membuka dropdown
39. Verifikasi chip `Disposal` hilang
40. Buka dropdown Transaction
41. Verifikasi checkbox opsi `Disposal` ter-uncheck
42. Verifikasi chip `Transfer` tetap tampil
43. Centang `Missing`
44. Hapus centang `Transfer`
45. Verifikasi chip `Transfer` hilang
46. Verifikasi chip `Missing` tetap tampil
47. Hapus centang `Missing`
48. Ketik `tran` di kotak cari dropdown
49. Verifikasi pencarian di dalam dropdown mempersempit opsi menjadi `Transfer` (substring, tidak case-sensitive)
50. Ganti isi kotak cari dropdown dengan `zzz`
51. Verifikasi keyword tanpa hasil menampilkan `No results found`
52. Tutup dropdown Transaction dengan Esc
53. Klik `[Clear Field]`
54. Klik `[Apply]`
55. Tutup panel Filter dengan klik icon Filter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Yuda Pratama` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Asersi tambahan (S-03): TC-FA-SU-397: opsi `Missing` dicentang sebelum `Transfer` di-uncheck (langkah penghubung tambahan) supaya klausa c "chip lain tetap" dapat diasersi; keyword `tran` dan `zzz` pada kotak cari dropdown dipilih penulis karena Data Uji TC kosong.
- Alasan melewati sekitar 35 langkah (55 langkah tertulis, 55 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-396 butir c: Pre-setup #39 tidak memuat baris bernilai kosong, sehingga "menyaring keluar baris yang nilainya kosong" diasersi sebagai tidak ada baris dengan Transaction kosong pada hasil.
  - TC-FA-SU-397: Data Uji kosong; butir c "chip lain tetap" tidak teramati bila hanya satu chip tersisa (lihat catatan S-03 di atas).
