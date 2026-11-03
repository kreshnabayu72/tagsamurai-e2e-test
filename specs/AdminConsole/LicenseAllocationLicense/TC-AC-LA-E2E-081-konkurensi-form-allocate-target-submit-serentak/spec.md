---
id: TC-AC-LA-E2E-081-konkurensi-form-allocate-target-submit-serentak
title: "Konkurensi Form Allocate: Term Target Berubah dan Submit Serentak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-139
  - TC-AC-LA-466
  - TC-AC-LA-474
coverage:
  web: automated
---

# Konkurensi Form Allocate: Term Target Berubah dan Submit Serentak

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19) untuk TC-AC-LA-466 dan TC-AC-LA-474, kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation OFF (#39) untuk TC-AC-LA-466 dan TC-AC-LA-474.
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): satu Client bersuffix `PT Sejahtera {runId}-081` binaan Distributor PT Maju Bersama dengan term FAMS Professional Paid Active (bentuk PT Sejahtera #19) yang term-nya di-Cancel oleh sesi lain pada blok TC-AC-LA-139, sehingga Pre-setup #19 bersama tidak berubah. Nama dan ID Subscription dibaca dari hasil seeding. Alokasi yang dibuat blok TC-AC-LA-466 dan TC-AC-LA-474 berstatus `Completed` (toggle OFF) dan dipulihkan oleh baseline automation.
- Pelaku kedua: sesi API aktor (login API tidak dihitung sebagai sesi web, `suite.md`). Pada TC-AC-LA-139 akun pelaku yang meng-Cancel Subscription tidak ditulis di TC (disediakan tim FE). Pada TC-AC-LA-466 pengirim kedua memakai sesi API `Dewi Anggraini`.
- Kemampuan teknis (disediakan tim FE/BE): mengirim Submit alokasi lewat sesi API pada saat yang sama dengan klik `[Submit]` UI; membuka tab kedua browser dengan sesi yang sama.
- State global yang diubah: saldo kantong wallet dan Client seed; dipulihkan oleh baseline automation dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-139: Term Target berubah status oleh sesi lain, V-07, Target dikosongkan

1. Klik `[+ Allocation]`
2. Pilih Client `PT Sejahtera {runId}-081`
3. Pilih Target term FAMS Professional Client itu
4. Pilih Type `Concurrent User`
5. Isi Additional Quantity `3`
6. Pelaku kedua (sesi API) meng-Cancel Subscription term Target hingga tersimpan
7. Tunggu aksi selesai
8. Kembali ke form dan klik `[Submit]`
9. Verifikasi pesan `This target no longer exists. Please select another.`
10. Verifikasi Target dikosongkan
11. Verifikasi Type ikut di-reset
12. Verifikasi opsi Target dimuat ulang
13. Verifikasi Client dan Additional Quantity `3` dipertahankan
14. Verifikasi tidak ada record yang dibuat
15. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-466: Dua pengajuan serentak menghasilkan Allocation ID berbeda

16. Ganti akun: logout `Hendra W`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`
17. Catat jumlah baris tab Current sebagai baseline
18. Klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `1`
19. Klik `[Submit]` pada detik yang sama dengan sesi API `Dewi Anggraini` mengirim Submit identik hingga tersimpan
20. Tunggu aksi selesai
21. Verifikasi jumlah baris tab Current bertambah dua dari baseline
22. Verifikasi dua record baru memiliki Allocation ID berbeda dan berurutan (counter harian atomik)

### TC-AC-LA-474: Submit dari dua tab dengan form identik menghasilkan dua alokasi terpisah

23. Catat jumlah baris tab Current sebagai baseline
24. Buka tab browser kedua pada Allocation > License Allocation
25. Pada tab pertama dan tab kedua, klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `1` (form identik)
26. Klik `[Submit]` pada tab pertama
27. Klik `[Submit]` pada tab kedua
28. Verifikasi jumlah baris tab Current bertambah dua dari baseline
29. Verifikasi dua alokasi terpisah memiliki Allocation ID berbeda (top-up diizinkan)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7 dan 20 (menunggu aksi selesai karena berganti sesi atau akun, 8b butir 8), 16 (ganti akun), 17 dan 23 (baseline S-12), 24 (membuka tab kedua), dialog `Unsaved Changes` (langkah 15, S-08).
- Penyimpangan data (S-06): TC-AC-LA-139 meng-Cancel term PT Sejahtera (Pre-setup #19); spec memakai Client seed milik spec dengan bentuk yang sama.
- Pelaku kedua lewat sesi API (langkah 6, 19) tidak memakai butir `P-2` (bagian 3). Tab kedua pada langkah 24 sampai 27 adalah objek uji kelas c, bukan pemicu.
- Temuan untuk QA:
  - TC-AC-LA-139 tidak menyebut akun dan mekanisme pelaku "sesi lain" yang meng-Cancel Subscription; disediakan tim FE.
  - TC-AC-LA-466 Langkah 1 ("Dua sesi Submit alokasi pada detik yang sama") tidak menyebut akun pengirim kedua dan tidak ada cara deterministik membuat "detik yang sama"; spec memakai sesi API `Dewi Anggraini` dan hasilnya (dua Allocation ID berbeda) yang diasersi.
  - TC-AC-LA-466 dan TC-AC-LA-474 tidak menyebut Target, Type, dan Quantity; spec memakai Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan Quantity `1`.
  - TC-AC-LA-466 Expected a ("berurutan") tidak menyebut aturan urutan selain counter harian atomik; spec mengasersi dua Allocation ID berbeda dan berurutan.
  - TC-AC-LA-474 Langkah 1 tidak menyebut apakah form tab kedua dibuka sebelum Submit pertama; spec membuka keduanya sebelum Submit.
