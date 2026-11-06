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

1. Catat jumlah baris tab Current sebagai baseline (Search tidak aktif)
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera {runId}-081`
4. Pilih Target term FAMS Professional Client itu
5. Pilih Type `Concurrent User`
6. Isi Additional Quantity `3`
7. Pelaku kedua (sesi API) meng-Cancel Subscription term Target hingga tersimpan
8. Tunggu aksi selesai
9. Kembali ke form dan klik `[Submit]`
10. Verifikasi pesan `This target no longer exists. Please select another.`
11. Verifikasi Target dikosongkan
12. Verifikasi Type ikut di-reset
13. Verifikasi opsi Target dimuat ulang
14. Verifikasi Client dan Additional Quantity `3` dipertahankan
15. Verifikasi tidak ada record yang dibuat (jumlah baris tab Current sama dengan baseline)
16. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-466: Dua pengajuan serentak menghasilkan Allocation ID berbeda

17. Ganti akun: logout `Hendra W`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`
18. Buka Allocation > License Allocation tab Current
19. Catat jumlah baris tab Current sebagai baseline
20. Klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `1`
21. Klik `[Submit]` pada detik yang sama dengan sesi API `Dewi Anggraini` mengirim Submit identik hingga tersimpan
22. Tunggu aksi selesai
23. Verifikasi jumlah baris tab Current bertambah dua dari baseline
24. Verifikasi dua record baru memiliki Allocation ID berbeda dan berurutan (counter harian atomik)

### TC-AC-LA-474: Submit dari dua tab dengan form identik menghasilkan dua alokasi terpisah

25. Catat jumlah baris tab Current sebagai baseline
26. Buka tab browser kedua pada Allocation > License Allocation
27. Pada tab pertama dan tab kedua, klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `1` (form identik)
28. Klik `[Submit]` pada tab pertama
29. Klik `[Submit]` pada tab kedua
30. Verifikasi jumlah baris tab Current bertambah dua dari baseline
31. Verifikasi dua alokasi terpisah memiliki Allocation ID berbeda (top-up diizinkan)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (Catat baseline jumlah baris tab Current tanpa Search sebelum membuka form, S-12), langkah 8 dan 22 (menunggu aksi selesai karena berganti sesi atau akun, 8b butir 8), 17 (ganti akun), 18 (membuka List tab Current setelah ganti akun, S-07), 19 dan 25 (baseline S-12), 26 (membuka tab kedua), dialog `Unsaved Changes` (langkah 16, S-08).
- Penyimpangan data (S-06): TC-AC-LA-139 meng-Cancel term PT Sejahtera (Pre-setup #19); spec memakai Client seed milik spec dengan bentuk yang sama.
- Pelaku kedua lewat sesi API (langkah 7, 21) tidak memakai butir `P-2` (bagian 3). Tab kedua pada langkah 26 sampai 29 adalah objek uji kelas c, bukan pemicu.
- Temuan untuk QA:
  - TC-AC-LA-139 tidak menyebut akun dan mekanisme pelaku "sesi lain" yang meng-Cancel Subscription; disediakan tim FE.
  - TC-AC-LA-466 Langkah 1 ("Dua sesi Submit alokasi pada detik yang sama") tidak menyebut akun pengirim kedua dan tidak ada cara deterministik membuat "detik yang sama"; spec memakai sesi API `Dewi Anggraini` dan hasilnya (dua Allocation ID berbeda) yang diasersi.
  - TC-AC-LA-466 dan TC-AC-LA-474 tidak menyebut Target, Type, dan Quantity; spec memakai Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan Quantity `1`.
  - TC-AC-LA-466 Expected a ("berurutan") tidak menyebut aturan urutan selain counter harian atomik; spec mengasersi dua Allocation ID berbeda dan berurutan.
  - TC-AC-LA-474 Langkah 1 tidak menyebut apakah form tab kedua dibuka sebelum Submit pertama; spec membuka keduanya sebelum Submit.
