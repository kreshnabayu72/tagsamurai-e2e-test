---
id: TC-FA-TDC-E2E-221-request-langsung-class-code-kembar-effective-from-dan-cancel-version
title: "Request Langsung: Class Code Kembar, Effective From Tidak Valid, dan Cancel Version Ditolak"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-844
  - TC-FA-TDC-845
  - TC-FA-TDC-846
  - TC-FA-TDC-847
  - TC-FA-TDC-848
  - TC-FA-TDC-849
sourceRules: ["V-04", "F-FATDC-02.k7a", "V-22", "F-FATDC-03.k1", "FATDC-LOGIC-04i", "V-21", "FATDC-LOGIC-04e"]
smoke: []
dependsOn: []
trace:
  "V-04": [3, 5]
  "F-FATDC-02.k7a": [7, 9]
  "V-22": [12, 14]
  "F-FATDC-03.k1": [16, 18]
  "FATDC-LOGIC-04i": [20, 22]
  "V-21": [25, 27]
  "FATDC-LOGIC-04e": 25
coverage:
  web: automated
---

# Request Langsung: Class Code Kembar, Effective From Tidak Valid, dan Cancel Version Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Langkah spec tidak memakai UI.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, seed dan pemulihan lewat API (versi Scheduled, Current, dan Past, serta Exported through), dan kendali jam sistem (jam server dan jam browser diatur bersama). Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Jam sistem uji: 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00); Fiscal Year Start Januari. Jam diatur di langkah 1 dan dipulihkan di langkah 29; hook `after` memulihkannya bila spec berhenti di tengah.
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | hanya satu versi (versi pertama tanpa Effective From); tidak ada class lain berkode `nb-4` |
| `nb2` | `NB-2` | versi Current dan versi Scheduled mulai Jan 2028 sebagai versi terakhir |
| `nb1` | `NB-1` | versi dengan Effective From Jan 2026 yang sudah Current |
| `bldNp` | `BLD-NP` | versi Past (Jan 2025) dan versi Current |
| `exportedThrough` | Exported through | belum mencapai Des 2026 (nilai awal); dimajukan ke Des 2026 (seluruh 12 bulan tahun pajak 2026 sudah diekspor) di langkah 23 dan dikembalikan di langkah 28 |

- State global yang diubah spec: jam server dan jam browser (langkah 1 dan 29) serta Exported through (langkah 23 dan 28); hook `after` memulihkan keduanya.
- Nilai awal Exported through (belum mencapai Des 2026) perlu dikonfirmasi tim FE/BE: TC tidak menyebutnya, sehingga nilai ini hasil tebakan penulis spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur jam server dan jam browser ke 15 Okt 2026 10:00 WIB

### TC-FA-TDC-844: Request langsung membuat class dengan Class Code kembar berbeda kapital ditolak

2. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class dengan Class Code `nb-4` (Class Name `Kelompok kembar`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`) tanpa melalui UI
3. Verifikasi server menolak request tanpa membuat class
4. Baca ulang daftar class lewat request baca
5. Verifikasi hanya satu class `NB-4` di daftar

### TC-FA-TDC-845: Request langsung dengan Effective From bukan awal tahun pajak ditolak

6. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Maret 2027` tanpa melalui UI
7. Verifikasi server menolak request tanpa membentuk versi baru
8. Baca ulang daftar versi `NB-4` lewat request baca
9. Verifikasi daftar versi `NB-4` tetap satu versi

### TC-FA-TDC-846: Request langsung dengan Effective From lebih awal dari versi terakhir ditolak

10. Baca daftar versi `NB-2` lewat request baca dan catat sebagai baseline
11. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Useful Life `NB-2` menjadi `12` dengan Effective From `1 Januari 2027` tanpa melalui UI
12. Verifikasi server menolak request tanpa membentuk versi baru
13. Baca ulang daftar versi `NB-2` lewat request baca
14. Verifikasi daftar versi `NB-2` tidak berubah dari baseline langkah 10

### TC-FA-TDC-848: Request langsung membatalkan versi yang tahun pajaknya sudah dimulai ditolak

15. Kirim request langsung dengan sesi API aktor Total Control untuk membatalkan versi Jan 2026 `NB-1` tanpa melalui UI
16. Verifikasi server menolak request tanpa mutasi
17. Baca ulang daftar versi `NB-1` lewat request baca
18. Verifikasi status versi Jan 2026 `NB-1` tetap Current

### TC-FA-TDC-849: Request langsung membatalkan versi yang sudah tidak berstatus Scheduled ditolak tanpa mutasi

19. Kirim request langsung dengan sesi API aktor Total Control untuk membatalkan versi Past `BLD-NP` tanpa melalui UI
20. Verifikasi server menolak request tanpa mutasi
21. Baca ulang daftar versi `BLD-NP` lewat request baca
22. Verifikasi status versi Past `BLD-NP` tidak berubah (tetap Past)

### TC-FA-TDC-847: Request langsung dengan Effective From pada tahun pajak tertutup ditolak

23. Atur Exported through menjadi Des 2026 (seluruh 12 bulan tahun pajak 2026 sudah diekspor) lewat data uji Export Journal
24. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah Useful Life `NB-4` menjadi `10` dengan Effective From `1 Januari 2026` tanpa melalui UI
25. Verifikasi server menolak request tanpa membentuk versi baru
26. Baca ulang daftar versi `NB-4` lewat request baca
27. Verifikasi daftar versi `NB-4` tetap satu versi
28. Kembalikan Exported through ke nilai awal
29. Pulihkan jam server dan jam browser

## Notes

- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE; spec hanya mengasersi status respons dan state data lewat request baca (8b.1). Tidak ada tampilan UI yang diasersi.
- Klausa Expected c TC-FA-TDC-844, TC-FA-TDC-845, TC-FA-TDC-846, TC-FA-TDC-847, TC-FA-TDC-848, dan TC-FA-TDC-849 (tidak ada entri log baru) tidak diasersi di spec ini; asersinya ada di spec absence 270 (TC-FA-TDC-845, TC-FA-TDC-846), 271 (TC-FA-TDC-848, TC-FA-TDC-849), 273 (TC-FA-TDC-844), dan 262 (TC-FA-TDC-847) dengan aksi nyata dan baseline sendiri per TC (S-05).
- Urutan TC: TC-FA-TDC-844, 845, 846, 848, 849, 847. TC-FA-TDC-847 di akhir karena mengubah state global (Exported through) yang dipulihkan langkah 28.
- Langkah penghubung (S-03): langkah 1 dan 29 (mengatur dan memulihkan jam); langkah 10 (baseline daftar versi untuk asersi "tidak berubah"); langkah 23 dan 28 (membentuk dan memulihkan precondition tahun pajak tertutup lewat Exported through, tidak diasersi); langkah 4, 8, 13, 17, 21, dan 26 (membaca state data lewat request baca).
- Temuan untuk QA:
  - TC-FA-TDC-844 sampai 849 menulis "Server menolak request" tanpa status HTTP; spec mengasersi penolakan tanpa kode status.
  - TC-FA-TDC-844 tidak menyebut Regulation Reference pada request Create; spec mengirim field yang disebut TC.
  - TC-FA-TDC-846 dan TC-FA-TDC-847 mensyaratkan data uji Export Journal untuk Exported through yang disediakan tim FE/BE; TC-FA-TDC-847 menyebut "Exported through Des 2026" tanpa menyebut mekanismenya.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
