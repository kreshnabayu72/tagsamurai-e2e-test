---
id: TC-FA-TDC-E2E-258-request-langsung-pemanggil-terotorisasi-tercatat-di-tiga-surface-edit-cancel-version-dan-restore
title: "Request Langsung Pemanggil Terotorisasi Tercatat di Tiga Surface: Edit, Cancel Scheduled Version, dan Restore default classes"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-910
  - TC-FA-TDC-911
  - TC-FA-TDC-912
coverage:
  web: automated
---

# Request Langsung Pemanggil Terotorisasi Tercatat di Tiga Surface: Edit, Cancel Scheduled Version, dan Restore default classes

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Sesi UI dan sesi API aktor memakai akun Total Control yang sama, sehingga System Log milik user pemanggil adalah System Log akun itu.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, seed dan pemulihan lewat API, serta kendali jam sistem (jam server dan jam browser diatur bersama, dipulihkan setelah request). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Kemampuan tambahan (disediakan tim FE/BE): membaca jumlah entri Changelog, System Log, dan Activity Log per class sebagai baseline. Ketiganya adalah audit trail permanen, sehingga jumlah entri tidak diasersi sebagai angka absolut (S-12).
- Jam sistem uji: 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) untuk TC-FA-TDC-910 dan TC-FA-TDC-911; Fiscal Year Start Januari. Jam dipulihkan sebelum membuka Activity Log (S-09); entri dicari lewat Search nama class dan selisih dari baseline, bukan posisi teratas, karena entri bercap waktu jam yang digeser (S-12).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khsJ4b` | `KHS-J4B` | Non-building, Useful Life 8, Straight Line dan Declining Balance, satu versi (Current tanpa Effective From), Active, Used By 0, tanpa versi Scheduled |
| `khsJ4c` | `KHS-J4C` | versi Current tanpa Effective From dan versi Scheduled Effective From Jan 2027, Active, Used By 0 |
| `seedTujuh` | NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND | tujuh class seed bawaan; dikosongkan sebelum TC-FA-TDC-912 (tabel tanpa class sama sekali) dan terbentuk lagi oleh Restore default classes |

- Master Data Count Limit belum tercapai.
- State global yang diubah spec: jam server dan jam browser (langkah 1 dan 17, dipulihkan langkah 4 dan 20) serta isi tabel (dikosongkan langkah 30); hook `after` memulihkan jam, membuat ulang sembilan class Example Data, dan menghapus `KHS-J4B` dan `KHS-J4C`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-910: Request langsung Edit yang membentuk versi Current baru tercatat di tiga surface

1. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB
2. Catat baseline jumlah entri class `KHS-J4B` di Changelog, System Log, dan Activity Log lewat kemampuan baca log
3. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Useful Life `KHS-J4B` menjadi `10` dengan Effective From `Jan 2026` tanpa melalui UI, hingga perubahan tersimpan
4. Pulihkan jam server dan jam browser
5. Verifikasi request berhasil (respons sukses)
6. Baca ulang daftar versi `KHS-J4B` lewat request baca
7. Verifikasi versi baru Current terbentuk dengan Effective From pada atau sebelum hari ini
8. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class, klik ikon Changelog di toolbar, ketik Search `KHS-J4B`, tekan Enter
9. Verifikasi Changelog memuat dua baris Edit baru untuk `KHS-J4B` (selisih dua dari baseline langkah 2): Field `Useful Life` (Old Value `8`, New Value `10`) dan Field `Effective From` (Old Value `—`, New Value `Jan 2026`)
10. Verifikasi Changelog tidak memuat baris untuk Allowed Methods, Regulation Reference, Straight Line Rate, atau Declining Balance Rate
11. Buka System Log milik user pemanggil, ketik Search `KHS-J4B`, tekan Enter
12. Verifikasi System Log memuat dua baris Edit baru untuk `KHS-J4B` (selisih dua dari baseline langkah 2): Field `Useful Life` (Old Value `8`, New Value `10`) dan Field `Effective From` (Old Value `—`, New Value `Jan 2026`)
13. Verifikasi System Log tidak memuat baris untuk Allowed Methods, Regulation Reference, Straight Line Rate, atau Declining Balance Rate
14. Buka Activity Log (`Reports & Logs > Activity Log`, tab `User Action`), ketik Search `KHS-J4B`, tekan Enter
15. Verifikasi Activity Log memuat dua baris Edit baru untuk `KHS-J4B` (selisih dua dari baseline langkah 2): Field `Useful Life` (Old Value `8`, New Value `10`) dan Field `Effective From` (Old Value `—`, New Value `Jan 2026`)
16. Verifikasi Activity Log tidak memuat baris untuk Allowed Methods, Regulation Reference, Straight Line Rate, atau Declining Balance Rate

### TC-FA-TDC-911: Request langsung Cancel Scheduled Version tercatat di tiga surface

17. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB
18. Catat baseline jumlah entri class `KHS-J4C` di Changelog, System Log, dan Activity Log lewat kemampuan baca log
19. Kirim request langsung dengan sesi API aktor Total Control untuk membatalkan versi Scheduled Jan 2027 class `KHS-J4C` tanpa melalui UI, hingga perubahan tersimpan
20. Pulihkan jam server dan jam browser
21. Verifikasi request berhasil (respons sukses)
22. Baca ulang daftar versi `KHS-J4C` lewat request baca
23. Verifikasi versi Jan 2027 berstatus Cancelled
24. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class, klik ikon Changelog di toolbar, ketik Search `KHS-J4C`, tekan Enter
25. Verifikasi Changelog memuat satu baris baru (selisih satu dari baseline langkah 18): Action `Edit` | Class Code `KHS-J4C (Jan 2027)` | Field `Scheduled Version` | Old Value `Jan 2027` | New Value `—`
26. Buka System Log milik user pemanggil, ketik Search `KHS-J4C`, tekan Enter
27. Verifikasi System Log memuat satu baris baru (selisih satu dari baseline langkah 18): Action `Edit` | Object `Tax Depreciation Class` | Name `KHS-J4C` | Field `Scheduled Version` | Old Value `Jan 2027` | New Value `—`
28. Buka Activity Log (`Reports & Logs > Activity Log`, tab `User Action`), ketik Search `KHS-J4C`, tekan Enter
29. Verifikasi Activity Log memuat satu baris baru (selisih satu dari baseline langkah 18): Action `Edit` | Object `Tax Depreciation Class` | Name `KHS-J4C` | Field `Scheduled Version` | Old Value `Jan 2027` | New Value `—`

### TC-FA-TDC-912: Request langsung Restore default classes tercatat di tiga surface

30. Kosongkan seluruh class (semua status) lewat API hingga tabel tanpa class tersimpan
31. Catat baseline jumlah entri Create dan Status class seed (`NB-1`, `NB-2`, `NB-3`, `NB-4`, `BLD-P`, `BLD-NP`, `LAND`) di Changelog, System Log, dan Activity Log lewat kemampuan baca log
32. Kirim request langsung Restore default classes dengan sesi API aktor Total Control tanpa melalui UI, hingga ketujuh class tersimpan
33. Verifikasi request berhasil (respons sukses)
34. Baca ulang daftar class lewat request baca
35. Verifikasi ketujuh class seed `NB-1`, `NB-2`, `NB-3`, `NB-4`, `BLD-P`, `BLD-NP`, dan `LAND` terbentuk
36. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class, klik ikon Changelog di toolbar
37. Verifikasi Changelog memuat 14 baris Create baru (selisih 14 dari baseline langkah 31, dua per class seed): Field `Class Code` dan Field `Asset Type`, Old Value `—`
38. Verifikasi Changelog tidak memuat baris Status baru untuk class seed
39. Buka System Log milik user pemanggil
40. Verifikasi System Log memuat 14 baris Create baru (selisih 14 dari baseline langkah 31, dua per class seed): Field `Class Code` dan Field `Asset Type`, Old Value `—`
41. Verifikasi System Log tidak memuat baris Status baru untuk class seed
42. Buka Activity Log (`Reports & Logs > Activity Log`, tab `User Action`)
43. Verifikasi Activity Log memuat 14 baris Create baru (selisih 14 dari baseline langkah 31, dua per class seed): Field `Class Code` dan Field `Asset Type`, Old Value `—`
44. Verifikasi Activity Log tidak memuat baris Status baru untuk class seed

## Notes

- K-1: TC kelas a dengan Expected respons API dan state data tetap masuk spec FE+BE. Request dikirim tanpa browser; asersi respons dan state data lewat request baca (8b.1), sedangkan asersi baris log dibaca di tiga surface UI.
- Spec melewati sekitar 35 langkah (44). Alasan: seluruh blok satu kelas (kelas a) dan satu pola (request langsung oleh pemanggil terotorisasi lalu baca tiga surface log); langkah 8 sampai 16, 24 sampai 29, dan 36 sampai 44 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung terhadap batas (prinsip 13 Smell); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-FA-TDC-832, 833, dan 909 (pencatatan di tiga surface untuk Deactivate, Delete, dan Create) ada di spec 218.
- Urutan TC: TC-FA-TDC-910, 911, 912. TC-FA-TDC-912 di akhir karena mengosongkan seluruh class.
- Langkah penghubung (S-03): langkah 1, 4, 17, dan 20 (mengatur dan memulihkan jam sebelum membuka log, S-09); langkah 2, 18, dan 31 (baseline jumlah entri per TC, S-12); langkah 6, 22, dan 34 (membaca state data lewat request baca); langkah 8, 24, dan 36 (kembali ke modul asal sebelum membuka Changelog, S-14); langkah 30 (precondition tabel tanpa class, tidak diasersi); Search nama class pada surface log menemukan entri target (R-16).
- Entri baru dibaca lewat selisih dari baseline; himpunan baris sebanyak selisih dibaca tanpa mengandalkan urutan di antaranya (S-14). Asersi absence pada langkah 10, 13, 16, 38, 41, dan 44 didahului asersi baris yang diharapkan pada surface yang sama (anchor positif, 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-910, 911, dan 912 tidak menyebut lokasi menu System Log milik user pemanggil; spec menulis "Buka System Log milik user pemanggil" tanpa path.
  - TC-FA-TDC-912 Expected b tidak menyebut cara mengisolasi 14 baris Create dari entri log lain; spec memakai selisih dari baseline entri Create dan Status class seed.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
