---
id: TC-GS-IMPORT-E2E-214-client-e-custom-field-nonaktif-dihapus-sebelum-import-tetap-terkomit
title: "Client E: Custom Field nonaktif/dihapus sebelum Import tetap terkomit, nilai ditulis ke User; record hasil commit muncul di modul Brand, Division, form Create User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-528
  - TC-GS-IMPORT-801
  - TC-GS-IMPORT-802
  - TC-GS-IMPORT-954
coverage:
  web: automated
---

# Client E: Custom Field nonaktif/dihapus sebelum Import tetap terkomit, nilai ditulis ke User; record hasil commit muncul di modul Brand, Division, form Create User

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit sungguhan di Client E (pembuat data, destruktif), memutasi Custom Field Client E (state global), dan menunggu worker commit nyata (batas tunggu 2 menit per commit) (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC2_PASSWORD` (nama env baru). Sesi API menonaktifkan, mengaktifkan kembali, dan menghapus Custom Field di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > Brand Client E; Sub-Tab User Login dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Produk organisasi Client E: Global Settings dan Fixed Asset. Pre-setup Client E: Brand `Samsung`; Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`; Position `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor`, `Store Manager`; Custom Field Shift (Dropdown Pagi/Siang/Malam), Overtime Hours, Shift Notes, Emergency Phone, Join Date (Optional, Active).
- Data Dinamis:
  - D-50 (Brand 12: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus) dan D-53 (Division 6: Finance & Accounting/FIN, Operations/(kosong), IT Support/ITS, Procurement/PRC, Sales/SLS, Legal/LGL) untuk TC-GS-IMPORT-528: hasil commit kedua draft itu disiapkan oleh langkah 1 (reset Client E, lalu skrip seed; dipakai sebagai precondition TC, tidak diasersi oleh langkah commit; TC-GS-IMPORT-352 dan 355 adalah dependensi di TC sumber).
  - D-54 (draft User Login 8 baris `pending` di Client E dari `user-login-commit-8.csv`: Rizky Pratama Shift `Siang`, Sinta Maharani Shift `Siang`, Doni Kurniawan Shift `Pagi`, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, Indah Permata; Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3; Email dengan suffix per run `+{runId}-214`), disiapkan lewat skrip seed sebelum tiap TC commit (Client E direset tanpa draft, Kontrak Fixture R1) untuk TC-GS-IMPORT-801, 802, 954.
  - Nama literal dipakai karena Client E khusus commit dan record hasil commit dihapus di hook `after`; nama Custom Field `Shift` literal (pengecualian S-12 butir (ii): nama field menentukan teks yang diasersi).
- Urutan TC: 528, 801, 954, 802 (TC-802 menghapus Custom Field `Shift` paling akhir). Pemulihan dan pembersihan dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2, D-47) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh, D-47): hapus Brand (D-50) dan Division (D-53) hasil seed; hapus 8 User Login hasil commit D-54; `Shift` diaktifkan kembali atau dibuat ulang (Dropdown Pagi/Siang/Malam, Optional, Active); hapus draft; reset hasil commit terakhir dan penanda Banner Hasil Commit.
- Kemampuan teknis: skrip seed D-50, D-53, D-54; skrip reset Client E (D-47); sesi API Admin kedua; worker commit berjalan normal.
- State global: Custom Field Client E (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Record hasil commit di modul master data dan form Create User (TC-GS-IMPORT-528)

1. Reset Client E lewat skrip reset (D-47), lalu seed hasil commit Brand D-50 dan Division D-53 lewat skrip seed
2. Buka halaman Master Reference > Brand
3. Atur Rows per page 100
4. Verifikasi daftar Brand memuat ke-12 Brand hasil commit D-50 (Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus)
5. Buka halaman User > Division
6. Atur Rows per page 100
7. Verifikasi daftar Division memuat `Finance & Accounting`, `Operations`, `IT Support`, `Procurement`, `Sales`, dan `Legal` hasil commit D-53
8. Buka form Create User di User > User List
9. Buka dropdown Division
10. Verifikasi dropdown Division pada form Create User memuat `Finance & Accounting`, `Operations`, `IT Support`, `Procurement`, `Sales`, dan `Legal` hasil commit D-53
11. Tutup dropdown dan form Create User lewat `✕`

### Custom Field dinonaktifkan sebelum Import (TC-GS-IMPORT-801)

12. Seed draft D-54 lewat skrip seed, lalu buka Import > User Login
13. Admin kedua Client E (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan (halaman Import tidak dimuat ulang)
14. Klik `[Import (8)]`
15. Tunggu aksi selesai (permintaan mendapat respons)
16. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
17. Verifikasi Banner Hasil Commit bertone success: "Success, record has been imported. Duplicate records were ignored."
18. Verifikasi halaman kembali ke Dropzone tanpa baris error
19. Buka halaman User > User List > Login User
20. Atur Rows per page 100
21. Verifikasi daftar Login User memuat 8 user baru termasuk `Rizky Pratama`
22. Buka Detail user `Rizky Pratama`
23. Verifikasi Detail user `Rizky Pratama` menampilkan nama `Rizky Pratama`
24. Verifikasi Detail user `Rizky Pratama` tidak menampilkan Custom Field Shift selama field nonaktif
25. Admin kedua Client E (sesi API) mengaktifkan kembali Custom Field `Shift` hingga tersimpan
26. Muat ulang Detail user `Rizky Pratama` (`F5`)
27. Verifikasi Detail user `Rizky Pratama` menampilkan Custom Field Shift bernilai `Siang`
28. Pulihkan: hapus 8 user hasil commit dari Client E, reset hasil commit terakhir dan Banner Hasil Commit

### Custom Field dinonaktifkan sebelum halaman dimuat ulang (TC-GS-IMPORT-954)

29. Seed draft D-54 lewat skrip seed, lalu buka Import > User Login
30. Admin kedua Client E (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
31. Tekan `F5` pada halaman Import > User Login
32. Verifikasi kolom Shift tampil tanpa lencana dengan nilai tersimpan
33. Verifikasi Banner Custom Field Deactivated tampil
34. Verifikasi Staging Metric Cards: Ready to Import 8, Errors 0
35. Klik `[Import (8)]`
36. Tunggu aksi selesai (permintaan mendapat respons)
37. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
38. Verifikasi Banner Hasil Commit bertone success: "Success, record has been imported. Duplicate records were ignored." dan halaman kembali ke Dropzone tanpa baris error
39. Buka halaman User > User List > Login User dan atur Rows per page 100
40. Buka Detail user `Doni Kurniawan`
41. Verifikasi Detail user `Doni Kurniawan` menampilkan nama `Doni Kurniawan`
42. Verifikasi Detail user `Doni Kurniawan` tidak menampilkan Custom Field Shift selama field nonaktif
43. Admin kedua Client E (sesi API) mengaktifkan kembali Custom Field `Shift` hingga tersimpan
44. Muat ulang Detail user `Doni Kurniawan` (`F5`)
45. Verifikasi Detail user `Doni Kurniawan` menampilkan Custom Field Shift bernilai `Pagi`
46. Pulihkan: hapus 8 user hasil commit dari Client E, reset hasil commit terakhir dan Banner Hasil Commit

### Custom Field dihapus sebelum Import (TC-GS-IMPORT-802)

47. Seed draft D-54 lewat skrip seed, lalu buka Import > User Login
48. Admin kedua Client E (sesi API) menghapus Custom Field `Shift` hingga tersimpan (halaman Import tidak dimuat ulang)
49. Klik `[Import (8)]`
50. Tunggu aksi selesai (permintaan mendapat respons)
51. Muat ulang halaman Import > User Login setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
52. Verifikasi Banner Hasil Commit bertone success: "Success, record has been imported. Duplicate records were ignored." dan halaman kembali ke Dropzone tanpa baris error
53. Buka halaman User > User List > Login User dan atur Rows per page 100
54. Verifikasi daftar Login User memuat 8 user baru: Rizky Pratama, Sinta Maharani, Doni Kurniawan, Eka Putri, Fajar Hidayat, Gita Savitri, Hendra Gunawan, dan Indah Permata
55. Buka Detail user `Rizky Pratama`
56. Verifikasi Detail user `Rizky Pratama` menampilkan nama `Rizky Pratama`
57. Verifikasi Detail user `Rizky Pratama` tidak menampilkan Custom Field Shift
58. Verifikasi Detail user `Rizky Pratama` tidak menampilkan nilai `Siang`
59. Pulihkan: Admin kedua membuat ulang Custom Field `Shift` (Dropdown Pagi/Siang/Malam, Optional, Active), hapus 8 user hasil commit dari Client E, reset hasil commit terakhir dan Banner Hasil Commit

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 59 langkah, di atas 35 langkah. Alasan: empat blok berdiri sendiri (satu blok baca master data, tiga blok commit User Login dengan pola sama: seed draft, mutasi Custom Field lewat sesi API, commit, tunggu worker, baca daftar dan Detail user) pada satu client dan satu akun; tiap blok dipulihkan eksplisit (langkah 28, 46, 59), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-2: Admin kedua hanya memicu perubahan status Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 15, 36, dan 50 (Tunggu aksi selesai, permintaan mendapat respons) adalah langkah penghubung tanpa `Verifikasi` sesudah klik `[Import (8)]` (D-1) sebelum polling.
- Langkah pemulihan (28, 46, 59) adalah aksi tanpa `Verifikasi` (S-09); hook `after` adalah cadangan. Langkah 1 (reset Client E dan seed D-50 serta D-53) adalah langkah pembuka penghubung (S-03). Langkah 23, 41, dan 56 (nama user tampil) adalah anchor positif untuk asersi absence Custom Field Shift pada Detail user (bagian 8b butir 2, S-03). Langkah 11 menutup form Create User yang dibuka untuk asersi dropdown dan tidak punya isi dirty.
- Urutan 528, 801, 954, 802 menempatkan penghapusan Custom Field (TC-802) paling akhir; nomor TC di sourceTc tetap (S-05).
- Temuan untuk QA:
  - TC-GS-IMPORT-528 mensyaratkan commit Brand dan Division selesai (D-50 dan D-53) tanpa langkah penyiapannya; spec menyiapkan record hasil commit lewat skrip seed (dependensi TC-GS-IMPORT-352 dan 355 tidak disalin utuh karena hanya state hasilnya yang dibutuhkan).
  - TC-GS-IMPORT-801, 802, 954 bergantung pada D-54 yang dibuat TC-GS-IMPORT-356 (kolom TC dependensi); spec menyiapkan D-54 lewat skrip seed.
  - TC-GS-IMPORT-801 dan 954 mengasersi Custom Field `Shift` tidak tampil di Detail user selama nonaktif lalu bernilai `Siang` atau `Pagi` setelah diaktifkan; TC tidak menyebut lokasi Custom Field pada Detail user, spec mengasersi tampil atau tidaknya Custom Field Shift saja.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
