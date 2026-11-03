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
- Data Pre-setup (hanya dibaca atau aksi yang ditolak; fixture BE pemulih memulihkannya di hook `before` dan `after` serta pada langkah 12 dan 25): hierarki dan kuota #12 (Divisi Logistik beralokasi 500 dalam Kantor Pusat) dan sesi aktif #14 (sesi Budi Santoso; akun login Budi Santoso disediakan tim FE). Tidak ada entri log yang diharapkan bertambah; Last Updated alokasi tidak berubah.
- Kemampuan teknis:
  - Membaca jumlah entri Changelog Allocation Quota, Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log sebelum aksi (baseline per TC, langkah 1, 11, dan 26) disediakan tim FE/BE.
  - Mengakhiri sesi Budi Santoso lewat sesi API akun Budi (disediakan tim FE/BE) pada langkah 15.
  - `Spectra.intercept()` memaksa respons Edit Allocation menjadi 500 pada langkah 33 (endpoint sesuai openapi dan LLD modul, disediakan tim FE); intercept dilepas pada langkah 34.
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
7. Tutup modal dengan `[×]`, lalu buka Global Settings > User > Detail Rudi Hartono > Tab System Log
8. Verifikasi jumlah entri System Log tidak bertambah dari baseline
9. Buka Fixed Asset > Reports & Logs > Activity Log
10. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

### TC-FA-LIC-377: Force Logout atas sesi yang sudah berakhir menulis nol entri

11. Catat jumlah entri Changelog Concurrent User, System Log Rudi Hartono, dan Activity Log (baseline TC-FA-LIC-377)
12. Pulihkan Pre-setup #14 lewat fixture BE (sesi Budi Santoso aktif)
13. Buka License > Concurrent User, ketik Search `Budi`, tekan Enter
14. Klik `[Force Logout]` pada baris Budi Santoso
15. Akhiri sesi Budi Santoso lewat sesi API akun Budi hingga sesi berakhir tersimpan
16. Klik `[Confirm Logout]` pada dialog `Force Logout User`
17. Verifikasi dialog `Session Already Expired` tampil
18. Klik `[OK]`
19. Klik ikon Changelog pada toolbar
20. Verifikasi jumlah entri Changelog Concurrent User tidak bertambah dari baseline
21. Tutup modal dengan `[×]`, lalu buka Global Settings > User > Detail Rudi Hartono > Tab System Log
22. Verifikasi jumlah entri System Log tidak bertambah dari baseline
23. Buka Fixed Asset > Reports & Logs > Activity Log
24. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

### TC-FA-LIC-378: Validasi gagal dan kegagalan 5xx tidak menulis entri log

25. Pulihkan Pre-setup #12 lewat fixture BE (`Divisi Logistik` beralokasi 500)
26. Catat jumlah entri Changelog Allocation Quota (baseline TC-FA-LIC-378)
27. Buka License > Allocation Quota, klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik`, isi `701`, klik `[Save]`
28. Verifikasi modal Edit Allocation menampilkan pesan validasi V-FALIC-02 (penolakan nilai di atas Maximum Quota)
29. Klik `[×]` pada modal
30. Verifikasi dialog `Unsaved Changes` tampil
31. Klik `[Leave]`
32. Verifikasi baris `Divisi Logistik` tetap menampilkan Allocated Quota `500`
33. Pasang intercept respons Edit Allocation 500, klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
34. Lepas intercept
35. Verifikasi baris `Divisi Logistik` tetap menampilkan Allocated Quota `500`
36. Klik `[×]` pada modal
37. Verifikasi dialog `Unsaved Changes` tampil
38. Klik `[Leave]`
39. Klik `[Edit]` pada `Divisi Logistik`, klik `[Clear Field]`, klik `[Save]`
40. Verifikasi modal Edit Allocation menampilkan pesan validasi V-FALIC-04 (penolakan Remove Allocation)
41. Klik `[×]` pada modal
42. Verifikasi dialog `Unsaved Changes` tampil
43. Klik `[Leave]`
44. Klik ikon Changelog pada toolbar Child Groups Quota
45. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline untuk ketiga percobaan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Rujukan: spec fungsional memuat TC pencatatan terkait (TC-FA-LIC-364 sampai 375 di spec 107 dan 108). Asersi absence log hanya ada di spec ini (S-05).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 11, dan 26 mencatat baseline per TC; langkah 7, 9, 21, dan 23 berpindah surface; langkah 12 dan 25 memulihkan Pre-setup antar blok; langkah 13 menemukan baris target lewat Search `Budi` (R-16); langkah 34 melepas intercept segera setelah pemicu (S-09); langkah 29, 36, dan 41 menutup form dirty (S-08).
- Anchor absence: langkah 4 (toast `No changes to save.`), langkah 17 (dialog `Session Already Expired`), dan langkah 28, 32, 35, 40 (penolakan dan baris tetap 500) membuktikan pemicu diproses sebelum asersi jumlah entri (bagian 8b butir 2); jumlah baseline per surface menjadi pembanding agregat.
- Spec di atas 35 langkah (45 langkah): alasan dipertahankan, ketiga blok berkelas sama (absence log), berbasis baseline masing-masing, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-377 berlabel Manual Only (dua sesi paralel) dan tidak menyebut cara mengakhiri sesi Budi Santoso sebelum konfirmasi; spec memakai sesi API akun Budi (kemampuan disediakan tim FE/BE).
  - TC-FA-LIC-378 tidak menyebut teks pesan V-FALIC-02 dan V-FALIC-04 serta pesan kegagalan 5xx untuk Divisi Logistik; spec mengasersi kemunculan pesan validasi tanpa teks dan tidak mengasersi pesan 5xx.
  - TC-FA-LIC-378 langkah 3 ("Remove Divisi Logistik (V-FALIC-04)") tidak menyebut tindakan; spec memakai `[Clear Field]` lalu `[Save]` sesuai TC-FA-LIC-367.
  - TC-FA-LIC-378 hanya memeriksa Changelog Allocation Quota; spec mengikuti TC dan tidak memeriksa System Log atau Activity Log untuk blok ini.
