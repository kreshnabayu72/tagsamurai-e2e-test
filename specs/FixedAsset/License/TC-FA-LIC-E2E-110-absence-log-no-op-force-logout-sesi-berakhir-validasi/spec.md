---
id: TC-FA-LIC-E2E-110-absence-log-no-op-force-logout-sesi-berakhir-validasi
title: "Absence Log: Edit Tanpa Perubahan, Force Logout Sesi Berakhir, dan Validasi atau Kegagalan 5xx Tidak Menulis Entri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-376
  - TC-FA-LIC-377
  - TC-FA-LIC-378
coverage:
  web: automated
---

# Absence Log: Edit Tanpa Perubahan, Force Logout Sesi Berakhir, dan Validasi atau Kegagalan 5xx Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON, General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca atau aksi yang ditolak; fixture BE pemulih memulihkannya di hook `before` dan `after` serta pada langkah 14 dan 29): hierarki dan kuota #12 (Divisi Logistik beralokasi 500 dalam Kantor Pusat) dan sesi aktif #14 (sesi seed Budi Santoso tanpa login). Tidak ada entri log yang diharapkan bertambah; Last Updated alokasi tidak berubah.
- Kemampuan teknis:
  - Membaca jumlah entri Changelog Allocation Quota, Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log sebelum aksi (baseline per TC, langkah 1, 13, dan 30) disediakan tim FE/BE.
  - Mengakhiri sesi seed Budi Santoso lewat fixture BE (disediakan tim FE/BE; sesuai Precondition TC-FA-LIC-377) pada langkah 17.
  - `Spectra.intercept()` memaksa respons Edit Allocation menjadi 500 pada langkah 39 (endpoint sesuai openapi dan LLD modul, disediakan tim FE); intercept dilepas pada langkah 43, sesudah toast error diterima.
- Pemicu kelas lain (No-Op, sesi paralel, 5xx) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a); tiap TC punya baseline sendiri.
- Jalur menu: System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-376: Edit tanpa perubahan (No-Op) tidak menulis entri di tiga surface

1. Catat jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log (baseline TC-FA-LIC-376)
2. Buka tab Allocation Quota, klik node `Kantor Pusat`
3. Klik `[Edit]` pada `Divisi Logistik`, klik `[Save]` tanpa perubahan
4. Verifikasi toast netral `No changes to save.`
5. Klik ikon Changelog pada toolbar Child Groups Quota
6. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline
7. Tutup modal dengan `[×]`
8. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
9. Klik Name `Rudi Hartono`, buka Tab System Log
10. Verifikasi jumlah entri System Log tidak bertambah dari baseline
11. Buka Fixed Asset > Reports & Logs > Activity Log
12. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

### TC-FA-LIC-377: Force Logout atas sesi yang sudah berakhir menulis nol entri

13. Catat jumlah entri Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log (baseline TC-FA-LIC-377)
14. Pulihkan Pre-setup #14 lewat fixture BE (sesi Budi Santoso aktif)
15. Buka License > Concurrent User, ketik Search `Budi`, tekan Enter
16. Klik `[Force Logout]` pada baris Budi Santoso
17. Akhiri sesi seed Budi Santoso lewat fixture BE hingga sesi berakhir tersimpan
18. Klik `[Confirm Logout]` pada dialog `Force Logout User`
19. Verifikasi dialog `Session Already Expired` tampil
20. Klik `[OK]`
21. Klik ikon Changelog pada toolbar
22. Verifikasi jumlah entri Changelog Concurrent User tidak bertambah dari baseline
23. Tutup modal dengan `[×]`
24. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
25. Klik Name `Rudi Hartono`, buka Tab System Log
26. Verifikasi jumlah entri System Log tidak bertambah dari baseline
27. Buka Fixed Asset > Reports & Logs > Activity Log
28. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

### TC-FA-LIC-378: Validasi gagal dan kegagalan 5xx tidak menulis entri log

29. Pulihkan Pre-setup #12 lewat fixture BE (`Divisi Logistik` beralokasi 500)
30. Catat jumlah entri Changelog Allocation Quota (baseline TC-FA-LIC-378)
31. Buka License > Allocation Quota, klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik`, isi `701`, klik `[Save]`
32. Verifikasi pesan inline `Allocated quota exceeds the maximum allowed for this group (700).` tampil
33. Verifikasi pesan inline tampil di bawah field
34. Verifikasi modal Edit Allocation tetap terbuka
35. Klik `[×]` pada modal
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`
38. Verifikasi baris `Divisi Logistik` tetap menampilkan Allocated Quota `500`
39. Pasang intercept respons Edit Allocation 500, klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
40. Verifikasi toast error `Error, failed to update group license quota.`
41. Verifikasi modal Edit Allocation tetap terbuka
42. Verifikasi tombol `[Save]` aktif kembali
43. Lepas intercept
44. Verifikasi baris `Divisi Logistik` tetap menampilkan Allocated Quota `500`
45. Klik `[×]` pada modal
46. Verifikasi dialog `Unsaved Changes` tampil
47. Klik `[Leave]`
48. Klik `[Edit]` pada `Divisi Logistik`, klik `[Clear Field]`, klik `[Save]`
49. Verifikasi pesan inline `Cannot remove allocation while its subgroups have their own allocation.` tampil
50. Verifikasi modal Edit Allocation tetap terbuka
51. Klik `[×]` pada modal
52. Verifikasi dialog `Unsaved Changes` tampil
53. Klik `[Leave]`
54. Klik ikon Changelog pada toolbar Child Groups Quota
55. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline untuk ketiga percobaan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Rujukan: spec fungsional memuat TC pencatatan terkait (TC-FA-LIC-364 sampai 375 di spec 107 dan 108). Asersi absence log hanya ada di spec ini (S-05).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 13, dan 30 mencatat baseline per TC; langkah 7, 11, 23, dan 27 berpindah surface; langkah 8, 9, 24, dan 25 mencari baris `Rudi Hartono` lewat Search sebelum membuka Detail dan langkah 15 menemukan baris target lewat Search `Budi` (R-16, bagian 8b butir 13); langkah 14 dan 29 memulihkan Pre-setup antar blok; langkah 43 melepas intercept sesudah toast error diterima (8b butir 8, S-09); langkah 35, 45, dan 51 menutup form dirty (S-08).
- Anchor absence: langkah 4 (toast `No changes to save.`), langkah 19 (dialog `Session Already Expired`), dan langkah 32, 40, dan 49 (pesan penolakan dan toast error); `Verifikasi` baris tetap 500 (langkah 38 dan 44) adalah asersi tambahan sebagai pembanding agregat (S-03) membuktikan pemicu diproses sebelum asersi jumlah entri (bagian 8b butir 2); jumlah baseline per surface menjadi pembanding agregat.
- Spec di atas 35 langkah (55 langkah): alasan dipertahankan, ketiga blok berkelas sama (absence log), berbasis baseline masing-masing, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-378 langkah 3 ("Remove Divisi Logistik (V-FALIC-04)") tidak menyebut tindakan; spec memakai `[Clear Field]` lalu `[Save]` sesuai TC-FA-LIC-367.
  - TC-FA-LIC-378 hanya memeriksa Changelog Allocation Quota; spec mengikuti TC dan tidak memeriksa System Log atau Activity Log untuk blok ini.
