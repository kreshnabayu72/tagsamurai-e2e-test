---
id: TC-FA-TDC-E2E-287-request-langsung-declining-balance-rate-end-of-life-treatment-dan-land-ditolak
title: "Request Langsung: Declining Balance Rate Kosong atau di Luar Rentang, End-of-Life Treatment Kosong atau di Luar Opsi, serta Land dengan Rate Terisi Ditolak"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-955
  - TC-FA-TDC-956
  - TC-FA-TDC-957
  - TC-FA-TDC-959
sourceRules: ["V-16", "F-FATDC-01.k4h", "FATDC-LOGIC-03f.2", "V-17", "F-FATDC-01.k14", "E-FATDC-93", "V-23", "F-FATDC-01.k4i", "FATDC-LOGIC-03g.1", "FATDC-LOGIC-03g.5", "V-18", "F-FATDC-01.k6", "E-FATDC-06", "FATDC-LOGIC-03b"]
smoke: []
dependsOn: []
trace:
  "V-16": 2
  "F-FATDC-01.k4h": 2
  "FATDC-LOGIC-03f.2": [2, 7, 9, 11]
  "V-17": [7, 9, 11]
  "F-FATDC-01.k14": [7, 9, 11]
  "E-FATDC-93": [7, 9, 11]
  "V-23": 16
  "F-FATDC-01.k4i": [16, 18]
  "FATDC-LOGIC-03g.1": [16, 18]
  "FATDC-LOGIC-03g.5": [16, 18]
  "V-18": 23
  "F-FATDC-01.k6": 23
  "E-FATDC-06": 23
  "FATDC-LOGIC-03b": 23
anchor: [4, 13, 20, 25]
coverage:
  web: automated
---

# Request Langsung: Declining Balance Rate Kosong atau di Luar Rentang, End-of-Life Treatment Kosong atau di Luar Opsi, serta Land dengan Rate Terisi Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Langkah spec tidak memakai UI.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Data milik spec (kode literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; hook `before` menghapus sisa class berkode sama dari run sebelumnya lewat API; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Keadaan |
|---|---|---|
| `rApi1` | `R-API1` | belum ada di daftar |
| `rApi2` | `R-API2` | belum ada di daftar |
| `rApi3` | `R-API3` | belum ada di daftar |
| `land3` | `LAND3` | belum ada di daftar |

- Tabel memuat sedikitnya satu class lain (tujuh class seed bawaan) sebagai pembanding untuk asersi absence (8b.2).
- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-955: Request langsung membuat class dengan Declining Balance tanpa Declining Balance Rate ditolak

1. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `R-API1` bertipe Non-building dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Useful Life 8, Allowed Methods Straight Line dan Declining Balance, dan End-of-Life Treatment Charge in final period, tanpa Declining Balance Rate
2. Verifikasi server menolak request tanpa membuat class dengan pesan V-16 "Declining rate must not be empty"
3. Baca ulang daftar class lewat request baca
4. Verifikasi daftar class memuat sedikitnya satu class lain
5. Verifikasi class `R-API1` tidak ada di daftar

### TC-FA-TDC-956: Request langsung dengan Declining Balance Rate di luar rentang atau lebih dari 2 desimal ditolak

6. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `R-API2` bertipe Non-building dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Useful Life 8, Allowed Methods Declining Balance, End-of-Life Treatment Charge in final period, dan Declining Balance Rate 0
7. Verifikasi server menolak request tanpa membuat class dengan pesan V-17 "Declining rate must be between 0 and 100"
8. Kirim request langsung yang sama dengan Declining Balance Rate 100.01
9. Verifikasi server menolak request tanpa membuat class dengan pesan V-17 "Declining rate must be between 0 and 100"
10. Kirim request langsung yang sama dengan Declining Balance Rate 12.345
11. Verifikasi server menolak request tanpa membuat class dengan pesan V-17 "Declining rate must be between 0 and 100"
12. Baca ulang daftar class lewat request baca
13. Verifikasi daftar class memuat sedikitnya satu class lain
14. Verifikasi class `R-API2` tidak ada di daftar

### TC-FA-TDC-957: Request langsung dengan Declining Balance tanpa End-of-Life Treatment atau dengan nilai di luar opsi ditolak

15. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `R-API3` bertipe Non-building dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Useful Life 8, Allowed Methods Declining Balance, Declining Balance Rate 25, tanpa End-of-Life Treatment
16. Verifikasi server menolak request tanpa membuat class dengan pesan V-23 "End-of-life treatment must not be empty"
17. Kirim request langsung yang sama dengan End-of-Life Treatment bernilai "Switch to declining"
18. Verifikasi server menolak request tanpa membuat class
19. Baca ulang daftar class lewat request baca
20. Verifikasi daftar class memuat sedikitnya satu class lain
21. Verifikasi class `R-API3` tidak ada di daftar

### TC-FA-TDC-959: Request langsung membuat class Land dengan Declining Balance Rate atau End-of-Life Treatment terisi ditolak

22. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `LAND3` bertipe Land dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, tanpa Useful Life dan Allowed Methods, dengan Declining Balance Rate 25 dan End-of-Life Treatment Charge in final period
23. Verifikasi server menolak request tanpa membuat class dengan pesan V-18 "Land is not depreciated."
24. Baca ulang daftar class lewat request baca
25. Verifikasi daftar class memuat sedikitnya satu class lain
26. Verifikasi class `LAND3` tidak ada di daftar

## Notes

- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE; spec hanya mengasersi status respons dan state data lewat request baca (8b.1). Tidak ada tampilan UI yang diasersi.
- Klausa Expected c TC-FA-TDC-955, TC-FA-TDC-956, TC-FA-TDC-957, dan TC-FA-TDC-959 (tidak ada entri log baru di Changelog, System Log aktor, dan Activity Log) tidak diasersi di spec ini; asersinya ada di spec absence 288 dengan aksi nyata dan baseline sendiri per TC (S-05).
- Langkah penghubung (S-03): langkah 3, 12, 19, dan 24 (membaca state data lewat request baca). Langkah 4, 13, 20, dan 25 adalah anchor positif untuk asersi absence langkah 5, 14, 21, dan 26 (8b.2).
- TC-FA-TDC-956 mengirim tiga request dengan data yang sama kecuali Declining Balance Rate; langkah 8 dan 10 menulis "yang sama" merujuk langkah 6 (S-04: nilai data lengkap ditulis di langkah 6).
- Temuan untuk QA:
  - TC-FA-TDC-955 sampai 959 menulis "Server menolak request" tanpa status HTTP; spec mengasersi penolakan dan pesan validasi tanpa kode status.
  - TC-FA-TDC-957 Expected a menyebut pesan V-23 hanya untuk nilai kosong; untuk nilai "Switch to declining" pesan tidak disebut, sehingga langkah 18 hanya mengasersi penolakan.
  - TC-FA-TDC-956 menyebut pesan V-17 untuk nilai 12.345 (lebih dari 2 desimal) sama dengan rentang 0 sampai 100; spec mengikuti TC (S-02), perlu konfirmasi QA apakah pesan itu untuk lebih dari 2 desimal.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
