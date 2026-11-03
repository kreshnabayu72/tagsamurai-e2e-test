---
id: TC-AC-ACHS-E2E-207-download-approvals-tab-history-nama-berkas-cakupan-dan-kolom-hidden
title: "Download Approvals > Hardware Stock Tab History: Nama Berkas, Cakupan, dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-460
  - TC-AC-ACHS-461
  - TC-AC-ACHS-462
  - TC-AC-ACHS-465
coverage:
  web: automated
---

# Download Approvals > Hardware Stock Tab History: Nama Berkas, Cakupan, dan Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Stock List). Spec membuka Approvals > Hardware Stock sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #22 TC (Tabel D), 12 Subject terputus pada Tab History, baseline read-only yang tidak diubah spec ini. Baris dirujuk lewat nomor baris Tabel D: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel D (`Fixture.hardwareStock.p22.d[n]`) pada urutan default (Resolved At terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup dan tidak ditulis di spec ini.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #22 Tabel D | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #5 dan #8 berformat MAC dengan awalan yang sama | `Fixture.hardwareStock.p22.d[n].matchedIdentifier` |
  | Requested By baris #n (n = 1 sampai 12) | #22 Tabel D | Client, Distributor, atau Principal dengan label peran dalam kurung; entitas yang sama pada #4 dan #11 serta #8 dan #12 | `Fixture.hardwareStock.p22.d[n].requestedBy` |
  | Keyword Search nama Client | #22 Tabel D | diturunkan dari `Fixture.hardwareStock.p22.d[10].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; muncul pada Existing Record atau Requested By tepat tiga baris #1, #8, #10 | `Fixture.hardwareStock.derived.clientCoreNameHistory` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman Approvals Hardware Stock (lihat suite.md).
- Kemampuan teknis (disediakan tim FE/BE): menangkap berkas unduhan browser, membaca isi berkas CSV dan XLSX (header, jumlah baris data, encoding BOM, nama sheet, urutan baris), dan mengamati toast.
- State global: Column Visibility kolom Approver disembunyikan pada langkah 33 dan dipulihkan pada langkah 40. Suite serial: `parallel: false` (lihat suite.md).
- Kolom berkas: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At.
- Tiga baris data teratas pada sort default (Matched Identifier): #1, #2, #3.

## Test Steps

1. Buka Approvals > Hardware Stock
2. Klik Tab `History`

### TC-AC-ACHS-460: CSV dan XLSX, nama berkas, tanpa toast sukses

3. Hover icon Download
4. Verifikasi tooltip `Download`
5. Klik icon Download
6. Verifikasi overlay `Download as CSV` dan `Download as XLSX`
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas `Hardware-Stock.csv` terunduh
10. Klik icon Download
11. Pilih `Download as XLSX`
12. Verifikasi tidak ada toast sukses
13. Verifikasi berkas `Hardware-Stock.xlsx` terunduh
14. Buka berkas `Hardware-Stock.csv`
15. Verifikasi kolom berkas CSV: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At
16. Verifikasi CSV UTF-8 dengan BOM
17. Verifikasi urutan baris CSV mengikuti sort default: tiga baris pertama #1, #2, #3
18. Buka berkas `Hardware-Stock.xlsx`
19. Verifikasi kolom berkas XLSX: Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Approver, Requested At, Resolved At
20. Verifikasi XLSX satu sheet bernama `Sheet1`
21. Verifikasi urutan baris XLSX mengikuti sort default: tiga baris pertama #1, #2, #3

### TC-AC-ACHS-461: Cakupan mengikuti Search/Filter aktif dan seluruh halaman

22. Klik icon Download
23. Pilih `Download as CSV`
24. Buka berkas CSV
25. Verifikasi tanpa Search/Filter berkas berisi seluruh 12 baris data (bukan hanya 10 baris halaman pertama)
26. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameHistory`, tekan Enter
27. Klik icon Download
28. Pilih `Download as CSV`
29. Buka berkas CSV
30. Verifikasi dengan Search berkas hanya berisi 3 baris data hasil search
31. Klik icon `(←)`

### TC-AC-ACHS-462: Kolom yang di-hide tidak ikut, ikut kembali setelah unhide

32. Klik header kolom Actions `(⋯)`
33. Uncheck `Approver`
34. Klik icon Download
35. Pilih `Download as CSV`
36. Buka berkas CSV
37. Verifikasi berkas memuat kolom Type, Device Name (SKU), Category, Matched Identifier, Existing Record, Requested By, Approval, Requested At, Resolved At
38. Verifikasi berkas pertama tidak memuat kolom Approver
39. Klik header kolom Actions `(⋯)`
40. Check `Approver`
41. Klik icon Download
42. Pilih `Download as CSV`
43. Buka berkas CSV
44. Verifikasi berkas kedua memuat kolom Approver

### TC-AC-ACHS-465: Hasil kosong, tombol Download tetap aktif dan berkas berisi header saja

45. Ketik Search `zzqx-tidak-ada`, tekan Enter
46. Verifikasi tabel menampilkan empty state `No results found`
47. Verifikasi tombol Download tetap aktif
48. Klik icon Download
49. Pilih `Download as CSV`
50. Verifikasi tidak ada toast
51. Buka berkas CSV
52. Verifikasi berkas berisi baris header kolom visible saja tanpa baris data
53. Klik icon `(←)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-460, 461, 462, 465). Tidak ada TC hanya-BE di spec ini. TC-AC-ACHS-463 (download gagal) ada di spec resilience lain, TC-AC-ACHS-464 (isi sel) ada di spec 208.
- Langkah penghubung (bukan dari langkah TC): langkah 31 dan 53 (klik `(←)` mereset Search, S-09), langkah 8 dan 12 (asersi absence toast diletakkan segera setelah pemicu dan sebelum asersi berkas, bagian 8b butir 11, dengan pemicu pilihan format sebagai anchor positif yang buktinya `Verifikasi` berkas terunduh).
- TC-460 butir f, g, dan h (BOM, nama sheet, urutan baris) ditulis di spec ini sesuai TC sumber; isi sel per tipe kolom ada di spec 208 (kelas binary buffer).
- Spec ini di atas 35 langkah (53 langkah nominal). Alasan: empat TC download berbagi satu dataset read-only (Tab History), tiap TC berdiri sendiri (Search dan Column Visibility dipulihkan di antaranya), dan langkah membuka berkas diulang per unduhan.
- Konfirmasi (#8): nama inti Client sama dengan substring yang ditulis TC-461 (bukan nilai kolom penuh); hasil pada Tabel D: tiga baris #1, #8, #10. Tidak ada perbedaan.
- Temuan untuk QA:
  - Pengecekan BOM, nama sheet, dan urutan baris pada TC-460 adalah asersi isi berkas; bagian 3 prinsip 13f memisahkan isi berkas dari nama berkas, kolom, dan jumlah baris. Spec mengikuti TC sumber apa adanya dan menandainya untuk ditinjau.
  - Baris data hasil unduh bergantung pada format tanggal General Settings yang tidak diubah spec ini.
  - Populasi Pre-setup #22 dirujuk lewat nomor baris Tabel D (`#n` = `Fixture.hardwareStock.p22.d[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nama literal Pre-setup di spec dan tanpa pengecualian S-12. Literal yang tetap ada adalah teks UI nyata (placeholder, nilai Type, Approval, Category, `System`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
