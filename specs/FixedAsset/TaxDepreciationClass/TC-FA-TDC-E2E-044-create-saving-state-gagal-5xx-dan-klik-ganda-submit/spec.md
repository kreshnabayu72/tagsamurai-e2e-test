---
id: TC-FA-TDC-E2E-044-create-saving-state-gagal-5xx-dan-klik-ganda-submit
title: "Create - Saving State, Gagal 5xx, dan Klik Ganda Submit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-114
  - TC-FA-TDC-115
  - TC-FA-TDC-116
coverage:
  web: automated
---

# Create - Saving State, Gagal 5xx, dan Klik Ganda Submit

## Prerequisites

- Mode: FE+BE. Respons endpoint create dimanipulasi lewat `Spectra.intercept()` di atas backend nyata; asersi atas tabel dan class tersimpan memuat state server, sehingga spec bukan `Mode: mock`.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; tabel berisi paling banyak 9 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-08` (tersimpan), `KHS-09` (tidak tersimpan), dan `KHS-10` (tersimpan) belum ada. Form valid: Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`), Class Name `Kelompok khusus uji 8`, `Kelompok khusus uji 9`, `Kelompok khusus uji 10`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line`. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Kemampuan teknis: `Spectra.intercept()` atas request create Tax Depreciation Class (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) untuk (a) menunda respons 3 detik dan (b) mengembalikan respons 500; membaca jumlah request create yang dikirim (monitor jaringan) untuk langkah klik ganda. Intercept dilepas segera setelah pemicu selesai (S-09).
- Pemulihan: hook `after` menghapus `KHS-08` dan `KHS-10` lewat API (kemampuan disediakan tim FE/BE) dan melepas intercept sebagai cadangan.

## Test Steps

### TC-FA-TDC-114: Tombol Submit masuk Saving state saat request berjalan

1. Klik `+ Class` di toolbar
2. Isi form valid dengan Class Code `KHS-08`
3. Pasang intercept: respons endpoint create ditunda 3 detik
4. Klik `[Submit]` lalu amati Drawer selama request berjalan
5. Verifikasi tombol `[Submit]` menampilkan spinner
6. Verifikasi tombol `[Submit]` tidak dapat diklik
7. Verifikasi tombol `[Clear Field]`, ikon ✕, dan semua field input tidak interaktif selama request
8. Verifikasi Drawer menutup setelah respons diterima
9. Verifikasi toast sukses: "Success, tax depreciation class has been created."
10. Lepas intercept penundaan respons

### TC-FA-TDC-115: Create gagal 5xx - toast error, Drawer tetap terbuka, input dipertahankan

11. Tunggu toast lama hilang otomatis
12. Klik `+ Class` di toolbar
13. Isi form valid dengan Class Code `KHS-09`
14. Pasang intercept: endpoint create mengembalikan 500
15. Klik `[Submit]`
16. Verifikasi muncul toast error: "Error, failed to create tax depreciation class." (tetap tampil sampai di-dismiss)
17. Verifikasi Drawer tetap terbuka
18. Verifikasi semua input dipertahankan
19. Verifikasi tombol `[Submit]` kembali enabled untuk retry manual
20. Verifikasi tabel tidak berubah (tetap berisi 8 baris: 7 seed dan `KHS-08`)
21. Lepas intercept respons 500
22. Dismiss toast error

### TC-FA-TDC-116: Klik ganda cepat pada Submit hanya membuat satu class

23. Klik ikon ✕ pada Drawer
24. Verifikasi dialog Unsaved Changes tampil
25. Klik `[Leave]`
26. Klik `+ Class` di toolbar
27. Isi form valid dengan Class Code `KHS-10`
28. Klik `[Submit]` dua kali dengan cepat
29. Verifikasi hanya satu request create yang diproses
30. Verifikasi tombol `[Submit]` disabled setelah klik pertama
31. Verifikasi muncul satu toast sukses: "Success, tax depreciation class has been created."
32. Verifikasi tabel memuat tepat satu baris `KHS-10`

## Notes

- Langkah penghubung (S-03): langkah 3 dan 14 (memasang intercept sebagai kebutuhan Pre-setup TC, tidak diasersi), langkah 10 dan 21 (melepas intercept; S-09), langkah 11 (menunggu toast sukses sebelumnya hilang otomatis), langkah 22 (dismiss toast error), langkah 23 sampai 25 (menutup Drawer dirty dengan `Unsaved Changes` sesuai S-08).
- P-5 butir (b): TC-FA-TDC-115 adalah satu-satunya TC kelas b (fault injection 5xx) di spec ini dan memakai permukaan Create yang sama dengan TC fungsional lain; TC-FA-TDC-114 hanya menahan respons untuk mengamati state UI (bukan kelas b).
- Langkah 31 (satu toast) didahului langkah 11 dan 22 yang memastikan toast sebelumnya sudah tidak ada; toast sukses TC-FA-TDC-114 sudah hilang pada saat TC-FA-TDC-116 berjalan.
- Tabel berisi 8 baris sesudah TC-FA-TDC-114 dan 9 baris sesudah TC-FA-TDC-116, sehingga langkah 20 dan 32 tidak didahului Search (8b.13, R-23).
- Pembagian TC lintas spec: tidak ada; seluruh TC sumber ada di spec ini.
- Temuan untuk QA:
  - Post Condition TC-FA-TDC-115 (tidak ada class `KHS-09` tersimpan; tidak ada entri log) dan TC-FA-TDC-116 (tepat satu entri L-01 pada tiap surface log) tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01). Tabel tidak berubah (Expected d TC-FA-TDC-115) diasersi lewat jumlah baris.
  - TC-FA-TDC-116 Expected a ("hanya satu request diproses") tidak menyebut cara mengamati; spec memakai monitor jaringan (disediakan tim FE).
  - Langkah 2, 13, dan 27 mengikuti TC ("Isi form valid"); nilai Regulation Reference, Class Name, dan seterusnya tidak ditulis TC, spec memakai nilai dasar TC-FA-TDC-105.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
