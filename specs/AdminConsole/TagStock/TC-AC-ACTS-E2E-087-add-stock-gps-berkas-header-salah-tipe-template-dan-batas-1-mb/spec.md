---
id: TC-AC-ACTS-E2E-087-add-stock-gps-berkas-header-salah-tipe-template-dan-batas-1-mb
title: "Add Stock GPS: Header Berkas Salah (V-06), Tipe Tidak Didukung (V-08), Download Template, serta Batas 1 MB (V-10, Tepat 1 MB, Preview Tak Berubah)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-251
  - TC-AC-ACTS-252
  - TC-AC-ACTS-253
  - TC-AC-ACTS-737
  - TC-AC-ACTS-738
  - TC-AC-ACTS-739
coverage:
  web: automated
---

# Add Stock GPS: Header Berkas Salah (V-06), Tipe Tidak Didukung (V-08), Download Template, serta Batas 1 MB (V-10, Tepat 1 MB, Preview Tak Berubah)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. Spec ini tidak menekan `[Submit]`, sehingga tidak ada unit yang perlu dihapus.
- Kemampuan teknis disediakan tim FE (kelas f, berkas): pembuat berkas CSV berheader `IMEI` dengan ukuran tepat 1.048.576 byte dan 1.048.577 byte (sisa ukuran diisi spasi di akhir baris yang di-trim), berkas XLSX 2 MB, CSV berheader `Serial`, berkas `.pdf`, dan pembaca isi berkas template yang diunduh.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-251: Header berkas salah ditolak dengan V-06

1. Unggah file CSV dengan header `Serial`
2. Verifikasi pesan "Invalid file. Use the template with an 'IMEI' column."
3. Verifikasi Preview tidak berubah (tetap kosong)

### TC-AC-ACTS-252: Tipe berkas tidak didukung ditolak dengan V-08

4. Unggah file `.pdf`
5. Verifikasi pesan "Unsupported file type. Upload a .csv or .xlsx file."

### TC-AC-ACTS-253: Download template menghasilkan CSV berheader IMEI

6. Klik `Download template`
7. Buka file yang terunduh
8. Verifikasi file CSV terunduh dengan header `IMEI`

### TC-AC-ACTS-737: File lebih dari 1 MB ditolak dengan V-10 saat dipilih

9. Pilih file CSV berheader `IMEI` berukuran 1.048.577 byte
10. Verifikasi inline error pada dropzone "File size must not exceed 1 MB."
11. Verifikasi file tidak diparse dan tidak ada baris ditambahkan ke Preview (Preview tetap kosong)
12. Pilih file XLSX berukuran 2 MB
13. Verifikasi inline error pada dropzone "File size must not exceed 1 MB." untuk file XLSX
14. Verifikasi file XLSX tidak diparse dan tidak ada baris ditambahkan ke Preview

### TC-AC-ACTS-738: File berukuran tepat 1 MB diterima

15. Pilih file CSV berheader `IMEI` berukuran tepat 1.048.576 byte (tiga baris IMEI valid `356938035643809`, `356938035643812`, `356938035643814`; sisa ukuran diisi spasi di akhir baris yang di-trim)
16. Verifikasi file diparse dan Preview memuat 3 baris OK
17. Verifikasi tidak ada inline error V-10 pada dropzone
18. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-739: Preview tidak berubah setelah file lebih dari 1 MB ditolak

19. Tambahkan IMEI `356938035643809` dan `356938035643812` lewat Manual Entry (dua baris OK; dipakai sebagai precondition TC, tidak diasersi)
20. Pilih file CSV berukuran 1.048.577 byte berisi IMEI valid lain
21. Verifikasi inline error pada dropzone "File size must not exceed 1 MB."
22. Verifikasi Preview tetap 2 baris OK semula
23. Verifikasi Ringkasan tidak berubah `2 valid, 0 waiting approval, 0 duplicate, 0 invalid of 2 entries`
24. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

## Notes

- Mode: FE+BE. Kelas harness f (berkas) dengan batas ukuran berkas (TC-AC-ACTS-737 sampai TC-AC-ACTS-739) sebagai pembentuk berkas uji, bukan kegagalan yang dipaksa.
- Langkah penghubung tanpa Verifikasi (S-03): "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" sesudah TC-AC-ACTS-738 dan TC-AC-ACTS-739 (S-09).
- Verifikasi Preview tetap kosong pada TC-AC-ACTS-251 dan TC-AC-ACTS-737 adalah pembacaan keadaan awal Preview (S-14: Preview kosong sejak halaman dibuka).
- Temuan untuk QA:
  - TC-AC-ACTS-738 meminta tiga IMEI valid di berkas tepat 1 MB dengan sisa ukuran spasi; kemampuan membuat berkas seperti itu disediakan tim FE.
  - TC-AC-ACTS-737 tidak menyebut apakah inline error V-10 hilang saat file lain dipilih; spec tidak mengasersi hilangnya error.
