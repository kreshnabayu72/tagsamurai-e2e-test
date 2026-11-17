---
id: TC-FA-TDC-E2E-218-request-langsung-pemanggil-terotorisasi-tercatat-di-tiga-surface
title: "Request Langsung Pemanggil Terotorisasi Tercatat di Tiga Surface: Create, Deactivate, dan Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-832
  - TC-FA-TDC-833
  - TC-FA-TDC-909
sourceRules: ["J-04", "L-01", "FATDC-LOGIC-08g", "L-04", "FATDC-LOGIC-09d", "L-05"]
smoke: []
dependsOn: []
trace:
  "J-04": [3, 5, 7, 10, 13, 17, 21, 23, 25, 28, 32, 34, 36]
  "L-01": [7, 8, 10, 11, 13, 14]
  "FATDC-LOGIC-08g": 19
  "L-04": [21, 23, 25]
  "FATDC-LOGIC-09d": 30
  "L-05": [32, 34, 36]
coverage:
  web: automated
---

# Request Langsung Pemanggil Terotorisasi Tercatat di Tiga Surface: Create, Deactivate, dan Delete

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Sesi UI dan sesi API aktor memakai akun Total Control yang sama, sehingga System Log milik user pemanggil adalah System Log akun itu.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, serta seed dan pemulihan lewat API. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Kemampuan tambahan (disediakan tim FE/BE): membaca jumlah entri Changelog, System Log, dan Activity Log per class sebagai baseline. Changelog, System Log, dan Activity Log adalah audit trail permanen, sehingga jumlah entri tidak diasersi sebagai angka absolut (S-12).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsJ4a` | `KHS-J4A` | belum ada di daftar; dibuat langkah 2 |
| `nb4` | `NB-4` | Active, Used By 0, tanpa Last Posted Tax Year |

- Data Dinamis TC-FA-TDC-909: Class Name `Kelompok J4 uji`, Asset Type Non-building, Useful Life `8`, Allowed Methods Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`). Master Data Count Limit belum tercapai.
- Pemulihan: hook `after` menghapus `KHS-J4A` dan membuat ulang `NB-4` lewat API.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-909: Request langsung Create tercatat di tiga surface dengan dua baris per surface

1. Catat baseline jumlah entri class `KHS-J4A` di Changelog, System Log, dan Activity Log lewat kemampuan baca log
2. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `KHS-J4A` (Class Name `Kelompok J4 uji`, Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`) tanpa melalui UI, hingga class tersimpan
3. Verifikasi request berhasil (respons sukses)
4. Baca ulang class `KHS-J4A` lewat request baca
5. Verifikasi class `KHS-J4A` terbentuk
6. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class, klik ikon Changelog di toolbar, ketik Search `KHS-J4A`, tekan Enter
7. Verifikasi Changelog memuat dua baris Create baru untuk `KHS-J4A` (selisih dua dari baseline langkah 1): Field `Class Code` (Old Value `—`, New Value `KHS-J4A`) dan Field `Asset Type` (Old Value `—`, New Value `Non-building`)
8. Verifikasi Changelog tidak memuat baris untuk Class Name, Useful Life, Allowed Methods, atau Regulation Reference
9. Buka System Log milik user pemanggil, ketik Search `KHS-J4A`, tekan Enter
10. Verifikasi System Log memuat dua baris Create baru untuk `KHS-J4A` (selisih dua dari baseline langkah 1): Field `Class Code` (Old Value `—`, New Value `KHS-J4A`) dan Field `Asset Type` (Old Value `—`, New Value `Non-building`)
11. Verifikasi System Log tidak memuat baris untuk Class Name, Useful Life, Allowed Methods, atau Regulation Reference
12. Buka Activity Log (`Reports & Logs > Activity Log`, tab `User Action`), ketik Search `KHS-J4A`, tekan Enter
13. Verifikasi Activity Log memuat dua baris Create baru untuk `KHS-J4A` (selisih dua dari baseline langkah 1): Field `Class Code` (Old Value `—`, New Value `KHS-J4A`) dan Field `Asset Type` (Old Value `—`, New Value `Non-building`)
14. Verifikasi Activity Log tidak memuat baris untuk Class Name, Useful Life, Allowed Methods, atau Regulation Reference

### TC-FA-TDC-832: Request langsung Deactivate tercatat di tiga surface

15. Catat baseline jumlah entri class `NB-4` di Changelog, System Log, dan Activity Log lewat kemampuan baca log
16. Kirim request langsung dengan sesi API aktor Total Control untuk menonaktifkan class `NB-4` tanpa melalui UI, hingga perubahan tersimpan
17. Verifikasi request berhasil (respons sukses)
18. Baca ulang status `NB-4` lewat request baca
19. Verifikasi status `NB-4` menjadi Inactive
20. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class, klik ikon Changelog di toolbar, ketik Search `NB-4`, tekan Enter
21. Verifikasi Changelog memuat satu baris Status baru untuk `NB-4` (selisih satu dari baseline langkah 15) dengan Old Value `Active` dan New Value `Inactive`
22. Buka System Log milik user pemanggil, ketik Search `NB-4`, tekan Enter
23. Verifikasi System Log memuat satu baris Status baru untuk `NB-4` (selisih satu dari baseline langkah 15) dengan Old Value `Active` dan New Value `Inactive`
24. Buka Activity Log (`Reports & Logs > Activity Log`, tab `User Action`), ketik Search `NB-4`, tekan Enter
25. Verifikasi Activity Log memuat satu baris Status baru untuk `NB-4` (selisih satu dari baseline langkah 15) dengan Old Value `Active` dan New Value `Inactive`

### TC-FA-TDC-833: Request langsung Delete tercatat di tiga surface

26. Catat baseline jumlah entri class `NB-4` di Changelog, System Log, dan Activity Log lewat kemampuan baca log
27. Kirim request langsung dengan sesi API aktor Total Control untuk menghapus class `NB-4` tanpa melalui UI, hingga class terhapus
28. Verifikasi request berhasil (respons sukses)
29. Baca ulang daftar class lewat request baca
30. Verifikasi class `NB-4` tidak ada lagi di daftar
31. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class, klik ikon Changelog di toolbar, ketik Search `NB-4`, tekan Enter
32. Verifikasi Changelog memuat satu baris Delete baru untuk `NB-4` (selisih satu dari baseline langkah 26) dengan Field `Class Code`, Old Value `NB-4`, dan New Value `—`
33. Buka System Log milik user pemanggil, ketik Search `NB-4`, tekan Enter
34. Verifikasi System Log memuat satu baris Delete baru untuk `NB-4` (selisih satu dari baseline langkah 26) dengan Field `Class Code`, Old Value `NB-4`, dan New Value `—`
35. Buka Activity Log (`Reports & Logs > Activity Log`, tab `User Action`), ketik Search `NB-4`, tekan Enter
36. Verifikasi Activity Log memuat satu baris Delete baru untuk `NB-4` (selisih satu dari baseline langkah 26) dengan Field `Class Code`, Old Value `NB-4`, dan New Value `—`

## Notes

- K-1: TC kelas a dengan Expected respons API dan state data tetap masuk spec FE+BE. Request dikirim tanpa browser; asersi respons dan state data lewat request baca (8b.1), sedangkan asersi baris log dibaca di tiga surface UI.
- Spec melewati sekitar 35 langkah (36). Alasan: seluruh blok satu kelas (kelas a) dan satu pola (request langsung oleh pemanggil terotorisasi lalu baca tiga surface log); langkah 6 sampai 14, 20 sampai 25, dan 31 sampai 36 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung terhadap batas (prinsip 13 Smell); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-FA-TDC-910, 911, dan 912 (pencatatan di tiga surface untuk Edit, Cancel Scheduled Version, dan Restore default classes) ada di spec 258; tidak ada TC yang dibagi antar spec.
- Urutan TC: TC-FA-TDC-909, 832, 833 (bukan nomor naik). Delete `NB-4` (TC-FA-TDC-833) di akhir spec karena menghabisi data; TC-FA-TDC-832 menonaktifkan `NB-4` sebelum dihapus.
- Langkah penghubung (S-03): langkah 1, 15, dan 26 (baseline jumlah entri per TC, S-12); langkah 4, 18, dan 29 (membaca state data lewat request baca); langkah 6, 20, dan 31 (kembali ke modul asal sebelum membuka Changelog, S-14); Search `KHS-J4A` dan `NB-4` pada tiap surface log menemukan entri target (R-16).
- Entri baru dibaca lewat Search nama class dan selisih jumlah dari baseline; himpunan baris sebanyak selisih tanpa mengandalkan urutan di antaranya (S-14). Asersi absence pada langkah 8, 11, dan 14 didahului asersi dua baris Create milik class yang sama pada surface yang sama (anchor positif, 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-832, 833, dan 909 tidak menyebut lokasi menu System Log milik user pemanggil; spec menulis "Buka System Log milik user pemanggil" tanpa path.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
