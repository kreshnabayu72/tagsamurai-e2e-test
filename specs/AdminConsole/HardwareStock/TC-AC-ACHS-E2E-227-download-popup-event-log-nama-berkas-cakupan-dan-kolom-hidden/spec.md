---
id: TC-AC-ACHS-E2E-227-download-popup-event-log-nama-berkas-cakupan-dan-kolom-hidden
title: "Download Popup Event Log: Nama Berkas, Cakupan, dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-508
  - TC-AC-ACHS-509
  - TC-AC-ACHS-510
  - TC-AC-ACHS-513
coverage:
  web: automated
---

# Download Popup Event Log: Nama Berkas, Cakupan, dan Kolom Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Spec membuka Stock Detail dan popup Event Log sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: #20 TC (Tabel B), SKU `Fixture.hardwareStock.p16.a[4].sku` (Handheld Reader - Long Range) memiliki tepat 12 sesi Event Log; baseline read-only yang tidak diubah spec ini. Event Log adalah audit trail permanen; total 12 sesi ditetapkan Pre-setup dan berlaku sebelum spec lain menambah sesi pada SKU ini (suite.md menjalankan spec yang mengubah baseline sesudah spec baca). Baris dirujuk lewat nomor baris Tabel B: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel B (`Fixture.hardwareStock.p20.b[n]`) pada urutan default (Date terbaru lebih dulu); nilai sel dibaca dari fixture lewat kunci pada tabel Parameter Pre-setup.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU Handheld Reader Long Range | #16 Tabel A baris 4 | kode SKU Handheld Reader - Long Range (RFD40); pemilik Event Log Pre-setup #20 | `Fixture.hardwareStock.p16.a[4].sku` |
  | Date baris #n (n = 1 sampai 12) | #20 Tabel B | identitas baris hasil; urutan default Date terbaru lebih dulu; format General Settings (Pre-setup #15) | `Fixture.hardwareStock.p20.b[n].date` |
- Guided Tooltip: hook suite `before` dan `after` menyetel dan memulihkan flag halaman yang dipakai suite (lihat suite.md).
- Kemampuan teknis (disediakan tim FE/BE): menangkap berkas unduhan browser, membaca isi berkas CSV dan XLSX (header, jumlah baris data, encoding BOM, nama sheet, urutan baris), dan mengamati toast.
- State global: Column Visibility kolom Modified By disembunyikan pada langkah 34 dan dipulihkan pada langkah 41. Suite serial: `parallel: false` (lihat suite.md).
- Kolom berkas: Date, Activity, Success, Waiting for Approval, Modified By.
- Tiga baris data teratas pada sort default (kolom Date): #1, #2, #3.

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab `Available` aktif
3. Klik icon `[Event Log]` di toolbar

### TC-AC-ACHS-508: CSV dan XLSX, nama berkas, tanpa toast sukses

4. Hover icon Download
5. Verifikasi tooltip `Download`
6. Klik icon Download
7. Verifikasi overlay `Download as CSV` dan `Download as XLSX`
8. Pilih `Download as CSV`
9. Verifikasi tidak ada toast sukses
10. Verifikasi berkas `Hardware-Stock-EventLog-<Fixture.hardwareStock.p16.a[4].sku>.csv` terunduh
11. Klik icon Download
12. Pilih `Download as XLSX`
13. Verifikasi tidak ada toast sukses
14. Verifikasi berkas `Hardware-Stock-EventLog-<Fixture.hardwareStock.p16.a[4].sku>.xlsx` terunduh
15. Buka berkas CSV
16. Verifikasi kolom berkas CSV: Date, Activity, Success, Waiting for Approval, Modified By
17. Verifikasi CSV UTF-8 dengan BOM
18. Verifikasi urutan baris CSV mengikuti sort default: tiga baris pertama #1, #2, #3
19. Buka berkas XLSX
20. Verifikasi kolom berkas XLSX: Date, Activity, Success, Waiting for Approval, Modified By
21. Verifikasi XLSX satu sheet bernama `Sheet1`
22. Verifikasi urutan baris XLSX mengikuti sort default: tiga baris pertama #1, #2, #3

### TC-AC-ACHS-509: Cakupan mengikuti Search/Filter aktif dan seluruh halaman

23. Klik icon Download
24. Pilih `Download as CSV`
25. Buka berkas CSV
26. Verifikasi tanpa Search/Filter berkas berisi seluruh 12 baris data (bukan hanya 10 baris halaman pertama)
27. Ketik Search `Delete`, tekan Enter
28. Klik icon Download
29. Pilih `Download as CSV`
30. Buka berkas CSV
31. Verifikasi dengan Search berkas hanya berisi 3 baris data hasil search
32. Klik icon `(←)`

### TC-AC-ACHS-510: Kolom yang di-hide tidak ikut, ikut kembali setelah unhide

33. Klik header kolom Actions `(⋯)`
34. Uncheck `Modified By`
35. Klik icon Download
36. Pilih `Download as CSV`
37. Buka berkas CSV
38. Verifikasi berkas memuat kolom Date, Activity, Success, dan Waiting for Approval
39. Verifikasi berkas pertama tidak memuat kolom Modified By
40. Klik header kolom Actions `(⋯)`
41. Check `Modified By`
42. Klik icon Download
43. Pilih `Download as CSV`
44. Buka berkas CSV
45. Verifikasi berkas kedua memuat kolom Modified By

### TC-AC-ACHS-513: Hasil kosong, tombol Download tetap aktif dan berkas berisi header saja

46. Ketik Search `zzqx-tidak-ada`, tekan Enter
47. Verifikasi tabel menampilkan empty state `No results found`
48. Verifikasi tombol Download tetap aktif
49. Klik icon Download
50. Pilih `Download as CSV`
51. Verifikasi tidak ada toast
52. Buka berkas CSV
53. Verifikasi berkas berisi baris header kolom visible saja tanpa baris data
54. Klik icon `(←)`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-508, 509, 510, 513). Tidak ada TC hanya-BE di spec ini. TC-AC-ACHS-511 (download gagal) ada di spec resilience lain, TC-AC-ACHS-512 (isi sel) ada di spec 228.
- Langkah 1 sampai 3 membuka popup Event Log (langkah TC "Buka Hardware > Stock" dikerjakan hook `beforeEach` suite). Langkah penghubung (bukan dari langkah TC): langkah 32 dan 54 (klik `(←)` mereset Search, S-09), langkah 9 dan 13 (asersi absence toast diletakkan segera setelah pemicu dan sebelum asersi berkas, bagian 8b butir 11, dengan pemicu pilihan format sebagai anchor positif yang buktinya `Verifikasi` berkas terunduh).
- TC-508 butir f, g, dan h (BOM, nama sheet, urutan baris) ditulis di spec ini sesuai TC sumber; isi sel per tipe kolom ada di spec 228 (kelas binary buffer).
- Spec ini di atas 35 langkah (54 langkah nominal). Alasan: empat TC download berbagi satu dataset read-only (Event Log satu SKU), tiap TC berdiri sendiri (Search dan Column Visibility dipulihkan di antaranya), dan langkah membuka berkas diulang per unduhan.
- Temuan untuk QA:
  - Pengecekan BOM, nama sheet, dan urutan baris pada TC-508 adalah asersi isi berkas; bagian 3 prinsip 13f memisahkan isi berkas dari nama berkas, kolom, dan jumlah baris. Spec mengikuti TC sumber apa adanya dan menandainya untuk ditinjau.
  - Baris data hasil unduh bergantung pada format tanggal General Settings yang tidak diubah spec ini.
  - Populasi Pre-setup #20 dirujuk lewat nomor baris Tabel B (`#n` = `Fixture.hardwareStock.p20.b[n]`), kunci akun `Fixture.hardwareStock.account.*`, dan kunci turunan `Fixture.hardwareStock.derived.*` (R-06), tanpa nilai literal Pre-setup di spec dan tanpa pengecualian S-12. Total 12 sesi hanya berlaku sebelum spec lain menambah sesi pada SKU ini (audit trail permanen, lihat suite.md). Literal yang tetap ada adalah teks UI nyata (placeholder, `Add Stock`, `Delete Stock`, `Delete`, `Showing ...`) dan input milik spec (`zzqx-tidak-ada`).
