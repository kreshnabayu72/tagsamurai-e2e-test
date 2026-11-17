---
id: TC-FA-TDC-E2E-222-request-langsung-validasi-class-name-class-code-dan-regulation-reference
title: "Request Langsung: Validasi Class Name, Class Code, dan Regulation Reference Ditolak Server"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-851
  - TC-FA-TDC-852
  - TC-FA-TDC-853
  - TC-FA-TDC-854
  - TC-FA-TDC-855
sourceRules: ["V-07", "V-06", "V-03", "V-02", "V-09"]
smoke: []
dependsOn: []
trace:
  "V-07": [2, 5]
  "V-06": [7, 10]
  "V-03": [12, 15]
  "V-02": [17, 20]
  "V-09": [22, 25]
anchor: [4, 9, 14, 19, 24]
coverage:
  web: automated
---

# Request Langsung: Validasi Class Name, Class Code, dan Regulation Reference Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Langkah spec tidak memakai UI.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca, serta seed dan pemulihan lewat API. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Data milik spec (hook `before` memastikan tidak ada class `NB-9` lewat API; hook `after` menghapus `NB-9` bila terbentuk; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb9` | `NB-9` | belum ada di daftar |

- Nilai request dasar (dari TC): Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`, Regulation Reference `UU HPP 7/2021` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`); Class Name `Kelompok 9 uji` untuk request yang tidak menguji Class Name. Nilai uji: Class Name `Kelompok 🙂`; Class Name 121 karakter (karakter `A` diulang 121 kali); Class Code `NB 9/x`; Class Code `ABCDEFGHIJKLMNOP` (16 karakter); Regulation Reference 256 karakter (karakter `A` diulang 256 kali).
- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah. Master Data Count Limit belum tercapai. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-851: Request langsung Class Name berisi emoji ditolak

1. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `NB-9` (nilai request dasar) dengan Class Name `Kelompok 🙂` tanpa melalui UI
2. Verifikasi server menolak request tanpa membuat class
3. Baca ulang daftar class lewat request baca
4. Verifikasi daftar class memuat sedikitnya satu class lain
5. Verifikasi class `NB-9` tidak ada di daftar

### TC-FA-TDC-852: Request langsung Class Name 121 karakter ditolak

6. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `NB-9` (nilai request dasar) dengan Class Name sepanjang 121 karakter tanpa melalui UI
7. Verifikasi server menolak request tanpa membuat class
8. Baca ulang daftar class lewat request baca
9. Verifikasi daftar class memuat sedikitnya satu class lain
10. Verifikasi class `NB-9` tidak ada di daftar

### TC-FA-TDC-853: Request langsung Class Code dengan karakter di luar whitelist ditolak

11. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class (nilai request dasar) dengan Class Code `NB 9/x` tanpa melalui UI
12. Verifikasi server menolak request tanpa membuat class
13. Baca ulang daftar class lewat request baca
14. Verifikasi daftar class memuat sedikitnya satu class lain
15. Verifikasi class `NB-9` tidak ada di daftar

### TC-FA-TDC-854: Request langsung Class Code 16 karakter ditolak

16. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class (nilai request dasar) dengan Class Code `ABCDEFGHIJKLMNOP` (16 karakter) tanpa melalui UI
17. Verifikasi server menolak request tanpa membuat class
18. Baca ulang daftar class lewat request baca
19. Verifikasi daftar class memuat sedikitnya satu class lain
20. Verifikasi class `NB-9` tidak ada di daftar

### TC-FA-TDC-855: Request langsung Regulation Reference 256 karakter ditolak

21. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `NB-9` (nilai request dasar) dengan Regulation Reference sepanjang 256 karakter tanpa melalui UI
22. Verifikasi server menolak request tanpa membuat class
23. Baca ulang daftar class lewat request baca
24. Verifikasi daftar class memuat sedikitnya satu class lain
25. Verifikasi class `NB-9` tidak ada di daftar

## Notes

- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE; spec hanya mengasersi status respons dan state data lewat request baca (8b.1). Tidak ada tampilan UI yang diasersi.
- Klausa Expected c TC-FA-TDC-851, TC-FA-TDC-852, TC-FA-TDC-853, TC-FA-TDC-854, dan TC-FA-TDC-855 (tidak ada entri log baru) tidak diasersi di spec ini; asersinya ada di spec absence 272 dengan aksi nyata dan baseline sendiri per TC (S-05).
- Langkah penghubung (S-03): langkah 3, 8, 13, 18, dan 23 (membaca state data lewat request baca). Langkah 4, 9, 14, 19, dan 24 adalah anchor positif untuk asersi absence langkah 5, 10, 15, 20, dan 25 (8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-851 sampai 855 menulis "Server menolak request" tanpa status HTTP; spec mengasersi penolakan tanpa kode status.
  - TC-FA-TDC-853 mengirim Class Code `NB 9/x` tetapi Expected b menulis "Class NB-9 tidak ada di daftar"; spec mengikuti TC. Hal yang sama untuk Class Code 16 karakter pada TC-FA-TDC-854.
  - TC-FA-TDC-852 sampai 855 tidak menyebut Class Name dan isi karakter string panjang; spec memakai Class Name `Kelompok 9 uji` (nilai TC-815) dan karakter `A`.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
