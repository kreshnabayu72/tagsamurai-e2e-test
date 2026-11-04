---
id: TC-FA-TDC-E2E-046-create-validasi-class-code-duplikat-debounce-dan-trim
title: "Create - Validasi Class Code Duplikat, Debounce, dan Trim"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-140
  - TC-FA-TDC-141
  - TC-FA-TDC-142
  - TC-FA-TDC-143
  - TC-FA-TDC-174
  - TC-FA-TDC-175
coverage:
  web: automated
---

# Create - Validasi Class Code Duplikat, Debounce, dan Trim

## Prerequisites

- Mode: FE+BE. Respons cek keunikan Class Code dimanipulasi lewat `Spectra.intercept()` di atas backend nyata (TC-FA-TDC-175); asersi atas class tersimpan memuat state server, sehingga spec bukan `Mode: mock`.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND; Class Code `NB-1` sudah ada. Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; sesudah satu Create tabel berisi 8 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-T1` (tersimpan ter-trim) belum ada; `KHS-429` tidak disimpan. Data Uji dasar (field selain Class Code): Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok uji validasi`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`. Nilai Class Code uji: `NB-1`, `nb-1`, `Nb-1`, ` NB-1 ` (spasi di awal dan akhir), `  KHS-T1  ` (dua spasi di awal dan akhir), `KHS-429`. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Kemampuan teknis: `Spectra.intercept()` atas request cek keunikan Class Code (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) untuk mengembalikan respons 429, serta merekam bahwa request tersebut menerima respons 429. Intercept dilepas segera setelah pemicu selesai (S-09).
- Pemulihan: hook `after` menghapus `KHS-T1` lewat API (kemampuan disediakan tim FE/BE) dan melepas intercept sebagai cadangan.

## Test Steps

### TC-FA-TDC-140: Create - Class Code sama persis dengan class lain ditolak (debounce)

1. Klik `+ Class` di toolbar
2. Ketik `NB-1` pada Class Code lalu berhenti mengetik
3. Verifikasi sekitar 500 ms setelah berhenti mengetik, caption "Class code already exists" muncul pada Class Code

### TC-FA-TDC-141: Create - Class Code berbeda kapitalisasi dari class lain ditolak

4. Ganti isi Class Code dengan `nb-1`, lalu berhenti mengetik
5. Verifikasi caption "Class code already exists" muncul pada Class Code (`nb-1`)
6. Ganti isi Class Code dengan `Nb-1`, lalu berhenti mengetik
7. Verifikasi caption "Class code already exists" muncul pada Class Code (`Nb-1`)

### TC-FA-TDC-142: Create - Class Code dengan spasi tepi yang sama dengan class lain setelah trim ditolak

8. Ganti isi Class Code dengan ` NB-1 ` (dengan spasi di awal dan akhir), lalu berhenti mengetik
9. Verifikasi caption "Class code already exists" muncul pada Class Code (pembanding setelah trim)

### TC-FA-TDC-174: Create - pengecekan keunikan Class Code berjalan setelah jeda mengetik sekitar 500 ms, bukan tiap karakter

10. Klik `[Clear Field]`
11. Ketik `NB-1` karakter demi karakter dengan jeda antar karakter di bawah 300 ms
12. Verifikasi selama mengetik tanpa jeda, caption "Class code already exists" tidak muncul
13. Berhenti mengetik dan tunggu sekitar 500 ms
14. Verifikasi caption "Class code already exists" muncul

### TC-FA-TDC-143: Create - Class Code dengan spasi tepi disimpan ter-trim

15. Klik `[Clear Field]`
16. Isi field lain sesuai Data Uji dasar
17. Ketik `  KHS-T1  ` (dua spasi di awal dan akhir) pada Class Code
18. Klik `[Submit]`
19. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
20. Verifikasi baris tabel menampilkan Class Code "KHS-T1" tanpa spasi tepi

### TC-FA-TDC-175: Create - respons 429 pada cek keunikan saat mengetik tidak menampilkan toast maupun caption

21. Tunggu toast lama hilang otomatis
22. Klik `+ Class` di toolbar
23. Pasang intercept: endpoint cek keunikan Class Code mengembalikan 429
24. Ketik `KHS-429` pada Class Code lalu berhenti mengetik
25. Verifikasi request cek keunikan Class Code menerima respons 429
26. Verifikasi tidak ada toast, tidak ada caption error, dan tidak ada state valid pada Class Code (field tetap netral)
27. Lepas intercept respons 429
28. Klik `[Clear Field]`
29. Klik ikon ✕ pada Drawer

## Notes

- Langkah penghubung (S-03): langkah 10 dan 15 (`[Clear Field]` mengosongkan Class Code dan caption sebelum kasus berikutnya; S-09), langkah 21 (menunggu toast sukses hilang otomatis), langkah 23 (memasang intercept sebagai kebutuhan Pre-setup TC, tidak diasersi), langkah 27 (melepas intercept; S-09), langkah 28 dan 29 (mengosongkan form lalu menutup Drawer yang bersih).
- Urutan TC: TC-FA-TDC-174 (Edge, tanpa submit) diletakkan sebelum TC-FA-TDC-143 (submit berhasil) dan TC-FA-TDC-175 (intercept) sesudahnya, karena kasus tanpa submit berurutan pada satu pembukaan Drawer, aksi yang menyimpan data diletakkan setelah semua validasi, dan intercept diletakkan terakhir dengan Drawer dibuka kembali.
- P-5 butir (b): TC-FA-TDC-175 adalah satu-satunya TC kelas b (respons 429 yang dipaksa) di spec ini dan memakai permukaan Create yang sama dengan TC fungsional lain.
- Asersi absence langkah 12 diletakkan sebelum jeda 500 ms dan didahului pengetikan karakter demi karakter (pemicu) pada Drawer yang sama dengan caption pada langkah 14 sebagai anchor positif sesudahnya; asersi absence langkah 26 didahului anchor positif langkah 25 (respons 429 sudah diterima).
- Pembagian TC lintas spec: validasi Class Code kosong, panjang, dan whitelist (TC-FA-TDC-135 sampai 139) ada di spec `TC-FA-TDC-E2E-045-create-validasi-class-code-kosong-panjang-dan-whitelist`.
- Temuan untuk QA:
  - TC-FA-TDC-175 Expected a menyebut "state valid" pada Class Code tanpa mendefinisikan tampilannya; spec memverifikasi field tetap netral tanpa menambah definisi sendiri.
  - TC-FA-TDC-174 Expected a ("selama mengetik tanpa jeda") tidak menyebut kapan asersi dilakukan; spec mengasersinya segera sesudah pengetikan selesai dan sebelum jeda 500 ms.
  - Post Condition TC-FA-TDC-140 sampai 142, 174, dan 175 ("Tidak ada data berubah dan tidak ada entri log") tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01). Post Condition TC-FA-TDC-143 ("Class Code tersimpan KHS-T1") sudah diasersi lewat baris tabel pada Expected b.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
