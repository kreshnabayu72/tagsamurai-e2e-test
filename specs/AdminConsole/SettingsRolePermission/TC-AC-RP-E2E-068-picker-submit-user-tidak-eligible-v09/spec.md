---
id: TC-AC-RP-E2E-068-picker-submit-user-tidak-eligible-v09
title: "Picker Submit: User Tidak Eligible (V-09 Tunggal dan Jamak) dan Rename User Bukan Error"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-225
  - TC-AC-RP-226
  - TC-AC-RP-229
coverage:
  web: automated
---

# Picker Submit: User Tidak Eligible (V-09 Tunggal dan Jamak) dan Rename User Bukan Error

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Admin B: sesi API sesuai Hook suite "Sesi API aktor" untuk menetapkan Total Control dan me-rename user; akun Admin B disediakan tim FE. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Pelaku kedua lewat sesi API tidak membuka konteks UI kedua.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`Alex Tan`, `Sarah Kimura`, `Dewi Anggreni`), #13 (pemegang Read Only `Dewi Anggraini`, `Lisa Wong`), #24 (Admin B).
- Data Dinamis: spec ini tidak membuat Data Dinamis; user yang ditetapkan atau di-rename Admin B adalah user Pre-setup #12 (nama tampil dipakai asersi alert TC). Nilai bersuffix `+{runId}-068` tidak dipakai karena tidak ada data yang dibuat spec.
- Perubahan Pre-setup: `Alex Tan`, `Sarah Kimura`, `Dewi Anggreni` ditetapkan Total Control oleh Admin B; `Alex Tan` menjadi `Alex Tanoto` pada TC-AC-RP-229. Pemulihan (user kembali Standard dan bernama `Alex Tan`) memakai kemampuan reset baseline automation yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC. Efek: Changelog Tab Total Control dan Settings > User menerima entri; Last Updated berubah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-225: Submit picker dengan user yang menjadi tidak eligible

1. Klik tab `Read Only`
2. Klik "+ Assign"
3. Centang `Alex Tan` dan `Sarah Kimura`
4. Sesi B (sesi API Admin B): tetapkan `Alex Tan` sebagai Total Control hingga tersimpan
5. Sesi A: klik `[Assign]`
6. Verifikasi inline alert "Alex Tan is no longer eligible. Please select another."
7. Verifikasi centangan `Alex Tan` auto-clear
8. Verifikasi `Sarah Kimura` tetap tercentang
9. Klik `✕` pada popup
10. Verifikasi tabel Tab Read Only memuat baris `Dewi Anggraini`
11. Verifikasi submit ditolak seluruhnya: tabel Tab Read Only tidak memuat `Sarah Kimura`

### TC-AC-RP-226: Alert V-09 bentuk jamak

12. Pulihkan baseline automation: `Alex Tan` kembali Standard, lalu muat ulang halaman
13. Klik tab `Read Only`
14. Klik "+ Assign"
15. Centang `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni`
16. Sesi B (sesi API Admin B): tetapkan `Alex Tan` dan `Sarah Kimura` sebagai Total Control hingga tersimpan
17. Sesi A: klik `[Assign]`
18. Verifikasi alert "Alex Tan and Sarah Kimura are no longer eligible. Please select another."
19. Pulihkan baseline automation: `Alex Tan` dan `Sarah Kimura` kembali Standard, lalu muat ulang halaman
20. Klik tab `Read Only`
21. Klik "+ Assign"
22. Centang `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni`
23. Sesi B (sesi API Admin B): tetapkan `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni` sebagai Total Control hingga tersimpan
24. Sesi A: klik `[Assign]`
25. Verifikasi alert "Alex Tan, Sarah Kimura, and Dewi Anggreni are no longer eligible. Please select another."

### TC-AC-RP-229: Rename user sebelum Submit bukan error

26. Pulihkan baseline automation: ketiga user kembali Standard, lalu muat ulang halaman
27. Klik "+ Assign"
28. Centang `Alex Tan`
29. Sesi B (sesi API Admin B): rename `Alex Tan` menjadi `Alex Tanoto` (Settings > User) hingga tersimpan
30. Sesi A: klik `[Assign]`
31. Verifikasi toast "Success, Total Control has been assigned."
32. Verifikasi Tab Total Control menampilkan nama terbaru `Alex Tanoto`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Pembagian TC lintas spec: TC-AC-RP-223, TC-AC-RP-224, dan TC-AC-RP-227 ada di spec 067; TC-AC-RP-228 ada di spec 129.
- Langkah penghubung (S-03, S-09): langkah 9 (tutup popup tanpa dialog Unsaved Changes karena popup picker bukan form), 10 (anchor positif untuk asersi absence, bagian 8b butir 2), 12, 19, 26 (pemulihan baseline dan muat ulang), 13 dan 20 (pilih tab). Langkah 19 hingga 25 mengulang langkah 12 hingga 18 dengan ketiganya ditetapkan Total Control sesuai Langkah Uji TC-AC-RP-226.
- Langkah 4, 16, 23, dan 29 memakai sesi API Admin B hanya sebagai pemicu perubahan state; tidak memakai `P-2`.
- Urutan TC: 225, 226, 229. Blok negatif didahulukan, blok sukses rename di akhir (S-10).
- Temuan untuk QA:
  - TC-AC-RP-225 Expected "submit ditolak seluruhnya" tidak punya langkah observasi; spec mengamatinya dengan menutup popup dan membaca Tab Read Only (langkah 10 dan 11).
  - TC-AC-RP-225 dan TC-AC-RP-226 menyebut "dua sesi paralel" (Manual Only kriteria d) dengan Sesi B hanya memicu perubahan state; spec memakai sesi API. Bila QA menghendaki sesi UI kedua, spec dipindah ke kelas c.
  - TC-AC-RP-226 Langkah Uji 7 "Ulangi dengan ketiganya ditetapkan sebagai Total Control" tidak menyebut pemulihan antar iterasi; spec menambah langkah pemulihan baseline (langkah 19).
  - TC-AC-RP-229 Expected tidak menyebut keadaan popup sesudah Assign; tidak diasersi. Rename lewat Admin B (Settings > User) tidak punya mekanisme yang ditulis di TC, PRD, atau LLD (S-13); ditulis sebagai kemampuan yang disediakan tim FE/BE.
  - Email Admin B (Pre-setup #24) tidak tertulis; ditulis "disediakan tim FE".
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-13).
