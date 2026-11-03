---
id: TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast
title: "Download: Opsi CSV/XLSX, Nama Berkas, Scope Baris, dan Toast"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-418
  - TC-FA-CF-420
  - TC-FA-CF-421
  - TC-FA-CF-422
  - TC-FA-CF-423
  - TC-FA-CF-425
  - TC-FA-CF-429
  - TC-FA-CF-432
coverage:
  web: automated
---

# Download: Opsi CSV/XLSX, Nama Berkas, Scope Baris, dan Toast

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Alpha (Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12: `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`) dan tab Purchasing empat field (Pre-setup #13: `Vendor Code`, `Warranty Months`, `Rated Precision`, `Long Option Field`), dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` dan `Fixture.faCustomFields.baselinePurchasing` (fixture belum ada, disediakan tim FE). Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Last Updated baseline tab General (terbaru ke terlama): `Asset Serial Tag` (17/10/26), `Storage Capacity` (16/10/26), `Equipment Class` (15/10/26), `Operating Voltage` (14/10/26), `Total Cost` (13/10/26), `Depreciated Ratio` (10/10/26), `Compliance File` (03/10/26), `Legacy Tag` (02/10/26).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data custom field.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: penangkapan berkas unduhan di browser dan pembacaan nama berkas, baris header, serta jumlah dan urutan baris data berkas CSV (disediakan tim FE). Isi sel tiap tipe kolom, BOM, dan sheet XLSX tidak diasersi di spec ini.
- State global: visibilitas kolom `Placeholder` disembunyikan pada langkah 20 dan ditampilkan kembali pada langkah 25 (Overlay Column Visibility berlaku langsung). Hook `after` suite menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-CF-418: Klik icon Download membuka overlay dengan opsi CSV dan XLSX

1. Klik icon Download
2. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`

### TC-FA-CF-423: Nama berkas mengikuti pilihan format tanpa extension di spesifikasi

3. Klik `Download as CSV`
4. Verifikasi berkas `Custom-Fields.csv` terunduh
5. Klik icon Download > `Download as XLSX`
6. Verifikasi berkas `Custom-Fields.xlsx` terunduh

### TC-FA-CF-425: Download sukses tidak menampilkan toast

7. Klik icon Download > `Download as XLSX`
8. Verifikasi tidak ada toast sukses
9. Verifikasi berkas terunduh

### TC-FA-CF-420: Download mengikuti Search, Filter, dan tab aktif

10. Ketik Search `serial`, tekan Enter
11. Klik icon Download > `Download as CSV`
12. Verifikasi berkas memuat baris `Asset Serial Tag`
13. Verifikasi berkas tidak memuat baris selain `Asset Serial Tag`
14. Klik `(←)` pada kotak Search

### TC-FA-CF-421: Download pada tab Purchasing hanya memuat field tab Purchasing

15. Klik tab `Purchasing`
16. Klik icon Download > `Download as CSV`
17. Verifikasi berkas memuat field grup Purchasing: `Vendor Code`, `Warranty Months`, `Rated Precision`, dan `Long Option Field`
18. Verifikasi berkas tidak memuat satu pun field baseline tab General
19. Klik tab `General`

### TC-FA-CF-422: Kolom yang disembunyikan tidak ikut ter-export dan kembali ikut setelah ditampilkan

20. Sembunyikan kolom `Placeholder` lewat Overlay Column Visibility pada header kolom Actions `(⋯)`
21. Klik icon Download > `Download as CSV`
22. Verifikasi tidak ada toast atau peringatan
23. Verifikasi berkas pertama memuat header kolom visible `Field Name` dan `Data Type`
24. Verifikasi berkas pertama tidak memuat kolom `Placeholder`
25. Tampilkan kembali kolom `Placeholder` lewat Overlay Column Visibility
26. Klik icon Download > `Download as CSV`
27. Verifikasi berkas kedua memuat kolom `Placeholder`

### TC-FA-CF-429: Download dengan nol baris tetap aktif dan berisi header kolom saja

28. Ketik Search `zzzxxx`, tekan Enter
29. Verifikasi tombol Download aktif
30. Klik icon Download > `Download as CSV`
31. Verifikasi tidak ada toast
32. Verifikasi berkas hanya memuat baris header kolom visible tanpa baris data
33. Klik `(←)` pada kotak Search

### TC-FA-CF-432: Urutan baris berkas mengikuti Sort aktif

34. Urutkan Last Updated Newest First (klik header kolom `Last Updated` hingga tabel berurut Newest First)
35. Klik icon Download > `Download as CSV`
36. Verifikasi baris berkas mengikuti urutan Newest First di tabel: `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`

## Notes

- Spec memuat 36 langkah, di atas smell 35 langkah. Alasan: satu topik (ekspor dari Table Tools tabel utama: opsi, nama berkas, scope baris, dan toast), satu akun, satu dataset (Company Alpha baseline) tanpa membuat atau mengubah data; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Nama berkas, header kolom, dan jumlah baris adalah asersi fungsional (bagian 3 prinsip 13 butir f); isi sel, BOM, dan sheet XLSX diasersi di spec lain yang khusus kelas binary buffer.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14 dan 33 (`(←)` menutup kotak Search dan mereset tabel), langkah 19 (kembali ke tab General), langkah 20 dan 25 (menyembunyikan lalu menampilkan kembali kolom `Placeholder` sesuai langkah uji TC-FA-CF-422), langkah 34 (Sort Newest First sesuai langkah uji TC-FA-CF-432). Search di langkah 10 dan 28 menyaring baris target (R-16).
- Urutan TC di spec: 418, 423, 425, 420, 421, 422, 429, 432. TC-FA-CF-423 dan 425 diletakkan di awal karena tidak memakai Search, Filter, atau Sort; TC-FA-CF-432 di akhir karena mengubah Sort.
- Anchor absence: langkah 8, 22, dan 31 (tidak ada toast) ditulis tepat setelah pemicu unduh dan sebelum asersi berkas (bagian 8b butir 11); berkas terunduh pada langkah 9, 23, dan 32 menjadi buktinya. Langkah 12 adalah anchor positif untuk absence langkah 13, langkah 17 untuk langkah 18, dan langkah 23 untuk langkah 24.
- Temuan untuk QA:
  - TC-FA-CF-432 menyebut "Urutkan Last Updated Newest First" tanpa jumlah klik; spec mengklik header hingga tabel berurut Newest First.
  - TC-FA-CF-420 Expected ("hanya memuat baris `Asset Serial Tag`") bergantung pada Search `serial` yang hanya cocok dengan satu baris baseline; berubah bila baseline Alpha berubah.
  - TC-FA-CF-418, 421, 423, dan 425 tidak menyebut cara membaca berkas unduhan; kemampuannya disediakan tim FE (Prerequisites).
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
