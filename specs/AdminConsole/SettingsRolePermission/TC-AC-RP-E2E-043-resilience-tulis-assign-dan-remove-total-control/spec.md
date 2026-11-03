---
id: TC-AC-RP-E2E-043-resilience-tulis-assign-dan-remove-total-control
title: "Resilience Tulis: Assign Total Control Gagal 5xx atau Jaringan dan Remove Total Control Gagal 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-131
  - TC-AC-RP-137
  - TC-AC-RP-415
coverage:
  web: automated
---

# Resilience Tulis: Assign Total Control Gagal 5xx atau Jaringan dan Remove Total Control Gagal 5xx

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons submit dipaksa lewat `Spectra.intercept()` dan state tabel diasersi)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan state: intercept dilepas setelah tiap pemicu dan dipulihkan di hook `after`; kegagalan yang dipaksa tidak menyimpan perubahan sehingga data Pre-setup tidak berubah. Kemampuan reset baseline (suite.md) tetap dijalankan di hook `before` dan `after`.
- Failure injection lewat `Spectra.intercept()` pada respons jaringan (Tabel Data Uji Pre-setup #23): respons 5xx, penahanan respons, dan timeout atau koneksi terputus. Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Tunggu waktu nyata: 10 detik pada langkah "Amati toast selama 10 detik" untuk memastikan toast error persisten tetap tampil (jeda pendek, bagian 6 konvensi).
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-131: Assign Total Control gagal 5xx mempertahankan popup dan seleksi

1. Klik tombol "+ Assign"
2. Ketik Search `Alex Tan`, tekan Enter
3. Centang `Alex Tan`
4. Ganti isi kotak search dengan `Sarah Kimura`, tekan Enter
5. Centang `Sarah Kimura`
6. Atur intercept respons submit Assign Total Control menjadi 5xx
7. Klik `[Assign]`
8. Verifikasi toast "Error, failed to assign Total Control."
9. Amati toast selama 10 detik tanpa men-dismiss
10. Verifikasi toast tetap tampil sampai di-dismiss
11. Verifikasi popup tetap terbuka
12. Verifikasi kedua centangan (`Alex Tan` dan `Sarah Kimura`) dipertahankan
13. Lepas intercept 5xx
14. Dismiss toast error secara manual

### TC-AC-RP-415: Assign Total Control gagal jaringan atau timeout menampilkan toast koneksi

15. Atur intercept respons submit Assign Total Control menjadi timeout atau koneksi terputus
16. Klik `[Assign]`
17. Verifikasi toast "Connection problem. Please try again."
18. Verifikasi toast tanpa tombol aksi
19. Verifikasi popup tetap terbuka
20. Verifikasi kedua centangan (`Alex Tan` dan `Sarah Kimura`) dipertahankan
21. Lepas intercept timeout
22. Klik `[Cancel]`
23. Verifikasi Tab Total Control memuat baris `Siti Nurhaliza`
24. Verifikasi tidak ada status parsial: `Alex Tan` dan `Sarah Kimura` tidak ada di Tab Total Control

### TC-AC-RP-137: Remove Total Control gagal 5xx

25. Klik `⋯` baris `John Doe` lalu klik `Remove`
26. Atur intercept respons Remove Total Control menjadi 5xx
27. Klik `[Remove]`
28. Verifikasi toast "Error, failed to remove Total Control."
29. Verifikasi dialog tetap terbuka tanpa perubahan
30. Verifikasi `[Remove]` aktif kembali
31. Lepas intercept 5xx
32. Klik `[Cancel]`
33. Verifikasi `John Doe` tetap di Tab Total Control

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 9, 13, 14, 21, 22, 31, 32 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 2, 4.
- Popup yang dibuka di langkah 1 dipakai bersama TC-AC-RP-131 dan 415 (seleksi dipertahankan oleh kegagalan pertama dan dipakai ulang oleh kegagalan kedua); asersi "tidak ada status parsial" untuk keduanya diamati sekali di langkah 24 sesudah kedua pemicu, karena popup harus tetap terbuka di antara keduanya.
- Alasan sekitar 35 langkah: ketiga blok satu kelas harness (b, fault injection tulis Total Control), berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; blok TC-AC-RP-137 dan blok Assign tidak saling bergantung.
- Temuan untuk QA:
  - TC-AC-RP-131 Expected "tidak ada status parsial" tidak memberi cara cek; spec mengamati Tab Total Control sesudah popup ditutup (langkah 24).
  - TC-AC-RP-415 Data Uji menyebut "timeout/koneksi terputus" tanpa memilih satu; spec memakai satu intercept timeout atau koneksi terputus sesuai kemampuan Pre-setup #23.
