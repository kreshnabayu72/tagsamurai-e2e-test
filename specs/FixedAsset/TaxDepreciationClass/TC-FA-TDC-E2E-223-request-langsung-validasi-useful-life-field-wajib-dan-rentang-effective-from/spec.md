---
id: TC-FA-TDC-E2E-223-request-langsung-validasi-useful-life-field-wajib-dan-rentang-effective-from
title: "Request Langsung: Validasi Useful Life, Field Wajib, dan Rentang Effective From"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-856
  - TC-FA-TDC-857
  - TC-FA-TDC-858
  - TC-FA-TDC-926
  - TC-FA-TDC-927
  - TC-FA-TDC-928
sourceRules: ["F-FATDC-01.k5a", "F-FATDC-01.k4b", "E-FATDC-77", "E-FATDC-18", "E-FATDC-21", "F-FATDC-02.k10a", "FATDC-LOGIC-04h", "FATDC-LOGIC-04p.5"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-01.k5a": [3, 6, 8, 11]
  "F-FATDC-01.k4b": [13, 16]
  "E-FATDC-77": [18, 20]
  "E-FATDC-18": [22, 24]
  "E-FATDC-21": 26
  "F-FATDC-02.k10a": 28
  "FATDC-LOGIC-04h": 28
  "FATDC-LOGIC-04p.5": 29
anchor: [5, 10, 15]
coverage:
  web: automated
---

# Request Langsung: Validasi Useful Life, Field Wajib, dan Rentang Effective From

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Langkah spec tidak memakai UI.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, seed dan pemulihan lewat API (Exported through dan versi class), dan kendali jam sistem (jam server dan jam browser diatur bersama). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Jam sistem uji: 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00); Fiscal Year Start Januari. Jam diatur di langkah 1 dan dipulihkan di langkah 31; hook `after` memulihkannya bila spec berhenti di tengah.
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb9` | `NB-9` | belum ada di daftar |
| `nb4` | `NB-4` | hanya satu versi (versi pertama tanpa Effective From) |
| `exportedThrough` | Exported through | Nov 2025 (tahun pajak 2025 belum seluruh bulannya diekspor) |

- Nilai request dasar Create (dari TC): Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`, Regulation Reference `UU HPP 7/2021` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`); Class Name `Kelompok 9 uji` untuk request yang tidak menguji Class Name.
- State global yang diubah spec: jam server dan jam browser (langkah 1 dan 31) dan versi Scheduled `NB-4` yang terbentuk di TC-FA-TDC-926 (dipulihkan langkah 30). Master Data Count Limit belum tercapai.
- Nilai awal Exported through (Nov 2025) perlu dikonfirmasi tim FE/BE: TC tidak menyebutnya, sehingga nilai ini hasil tebakan penulis spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB

### TC-FA-TDC-856: Request langsung Useful Life di luar rentang 1 sampai 100 ditolak

2. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `NB-9` (nilai request dasar) dengan Useful Life `101` tanpa melalui UI
3. Verifikasi server menolak request tanpa membuat class
4. Baca ulang daftar class lewat request baca
5. Verifikasi daftar class memuat sedikitnya satu class lain
6. Verifikasi class `NB-9` tidak ada di daftar

### TC-FA-TDC-857: Request langsung Useful Life bukan bilangan bulat ditolak

7. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `NB-9` (nilai request dasar) dengan Useful Life `7.5` tanpa melalui UI
8. Verifikasi server menolak request tanpa membuat class
9. Baca ulang daftar class lewat request baca
10. Verifikasi daftar class memuat sedikitnya satu class lain
11. Verifikasi class `NB-9` tidak ada di daftar

### TC-FA-TDC-858: Request langsung dengan field wajib hanya spasi ditolak

12. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `NB-9` (nilai request dasar) dengan Class Name berisi hanya spasi tanpa melalui UI
13. Verifikasi server menolak request tanpa membuat class
14. Baca ulang daftar class lewat request baca
15. Verifikasi daftar class memuat sedikitnya satu class lain
16. Verifikasi class `NB-9` tidak ada di daftar

### TC-FA-TDC-927: Request langsung dengan Effective From lebih dari 5 tahun pajak setelah tahun pajak berjalan ditolak

17. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Januari 2032` tanpa melalui UI
18. Verifikasi server menolak request tanpa membentuk versi baru
19. Baca ulang daftar versi `NB-4` lewat request baca
20. Verifikasi daftar versi `NB-4` tetap satu versi

### TC-FA-TDC-928: Request langsung dengan Effective From sebelum tahun pajak berjalan pada tahun pajak yang tidak tertutup ditolak

21. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Januari 2025` tanpa melalui UI
22. Verifikasi server menolak request tanpa membentuk versi baru
23. Baca ulang daftar versi `NB-4` lewat request baca
24. Verifikasi daftar versi `NB-4` tetap satu versi

### TC-FA-TDC-926: Request langsung dengan Effective From di dalam rentang pilihan (batas atas tahun pajak berjalan + 5) diterima

25. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Januari 2031` tanpa melalui UI, hingga perubahan tersimpan
26. Verifikasi server menerima request (respons sukses)
27. Baca ulang daftar versi `NB-4` lewat request baca
28. Verifikasi versi baru berstatus Scheduled dengan Effective From Jan 2031 terbentuk
29. Verifikasi daftar versi `NB-4` memuat dua versi: versi pertama Current tanpa Effective From dan versi Scheduled Jan 2031
30. Pulihkan `NB-4` ke satu versi lewat seeding API
31. Pulihkan jam server dan jam browser

## Notes

- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE; spec hanya mengasersi status respons dan state data lewat request baca (8b.1). Tidak ada tampilan UI yang diasersi.
- Klausa Expected c TC-FA-TDC-856, TC-FA-TDC-857, TC-FA-TDC-858, TC-FA-TDC-927, dan TC-FA-TDC-928 (tidak ada entri log baru) tidak diasersi di spec ini; asersinya ada di spec absence 272 (TC-FA-TDC-856, TC-FA-TDC-857, TC-FA-TDC-858), 271 (TC-FA-TDC-928), dan 270 (TC-FA-TDC-927) dengan aksi nyata dan baseline sendiri per TC (S-05).
- Urutan TC: TC-FA-TDC-856, 857, 858, 927, 928, 926. TC-FA-TDC-926 di akhir karena satu-satunya yang mengubah data (membentuk versi Scheduled `NB-4`), yang dipulihkan langkah 30.
- Langkah penghubung (S-03): langkah 1 dan 31 (mengatur dan memulihkan jam); langkah 30 (memulihkan `NB-4`); langkah 4, 9, 14, 19, 23, dan 27 (membaca state data lewat request baca). Langkah 5, 10, dan 15 adalah anchor positif untuk asersi absence langkah 6, 11, dan 16 (8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-856, 857, 858, 927, dan 928 menulis "Server menolak request" tanpa status HTTP; spec mengasersi penolakan tanpa kode status.
  - TC-FA-TDC-856 sampai 858 tidak menyebut Class Name pada request; spec memakai `Kelompok 9 uji` (nilai TC-815). TC-FA-TDC-858 tidak menyebut jumlah spasi.
  - TC-FA-TDC-928 mensyaratkan Exported through Nov 2025 (tahun pajak 2025 belum seluruh bulannya diekspor) sebagai data uji Export Journal; mekanisme penyiapannya tidak disebut TC dan disediakan tim FE/BE.
  - TC-FA-TDC-926 tidak menyebut pemulihan versi Scheduled yang terbentuk; spec memulihkan `NB-4` lewat seeding API.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
