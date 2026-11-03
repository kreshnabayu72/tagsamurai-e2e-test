---
id: TC-GS-NLU-E2E-086-list-download-fungsional-opsi-mengikuti-search-dan-filter-kolom
title: "List Download fungsional: opsi CSV dan XLSX, mengikuti Search dan Filter, kolom visible, dan nol baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-297
  - TC-GS-NLU-299
  - TC-GS-NLU-300
  - TC-GS-NLU-301
  - TC-GS-NLU-303
coverage:
  web: automated
---

# List Download fungsional: opsi CSV dan XLSX, mengikuti Search dan Filter, kolom visible, dan nol baris

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): seluruh Non-Login User Pre-setup (lebih dari 10 baris, sehingga seluruh baris tidak muat di halaman 1; precondition TC-GS-NLU-299 mengacu ke populasi TC-GS-NLU-99, tersedia lewat Pre-setup); Position `Contractor` (`Agus Salim`, `Joko Susilo`). Kolom visible default: Active, Name, Position, Division, Employee ID, Represented By, Last Update. Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: menangkap unduhan browser dan membaca nama berkas, ekstensi, nama sheet, header kolom, dan jumlah baris data dari berkas CSV dan XLSX; pembacaan jumlah total Non-Login User Client dan jumlah baris hasil Filter lewat kemampuan baca data (disediakan tim FE/BE, tanpa endpoint karangan); penghapusan preferensi kolom di browser di hook `after` (disediakan tim FE). Isi sel, BOM, dan tipe sel diasersi di spec 087.
- State global: konfigurasi kolom (kolom Division disembunyikan pada TC-GS-NLU-301), dipulihkan oleh langkah penghubung dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-297: Download overlay menawarkan CSV dan XLSX

1. Klik icon Download
2. Verifikasi overlay memuat `Download as CSV` dan `Download as XLSX`
3. Tekan `Esc` untuk menutup overlay

### TC-GS-NLU-299: Download CSV tanpa Search atau Filter mengekspor seluruh baris

4. Klik Download > `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi ekstensi file `.csv`
7. Verifikasi nama berkas `Non-Login-Users.csv`
8. Verifikasi file memuat header kolom yang visible
9. Verifikasi file memuat seluruh baris Non-Login User (jumlah baris data sama dengan jumlah total Non-Login User Client dan lebih dari 10, bukan hanya halaman 1)

### TC-GS-NLU-300: Download XLSX mengikuti Search dan Filter aktif

10. Buka Filter Panel, pilih Position `Contractor`, klik `[Apply]`
11. Klik Download > `Download as XLSX`
12. Verifikasi ekstensi `.xlsx`
13. Verifikasi file memuat satu sheet bernama `Sheet1`
14. Verifikasi file hanya memuat baris Contractor: jumlah baris data sama dengan jumlah baris hasil Filter (sedikitnya satu baris) dan seluruh baris ber-Position `Contractor`
15. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-NLU-301: Download hanya memuat kolom yang visible dan kolom yang ditampilkan kembali ikut

16. Klik `⋯` header Actions, hapus centang kolom Division, tutup overlay Column Visibility
17. Klik Download > `Download as CSV`
18. Verifikasi file pertama tanpa kolom Division
19. Klik `⋯` header Actions, centang kolom Division, tutup overlay Column Visibility
20. Klik Download > `Download as CSV`
21. Verifikasi file kedua memuat kolom Division

### TC-GS-NLU-303: Download dengan nol baris menghasilkan file berisi header saja

22. Ketik Search `zzzxxx`, tekan Enter
23. Verifikasi tombol Download tetap aktif
24. Klik Download > `Download as CSV`
25. Verifikasi tidak ada toast
26. Verifikasi file hanya berisi baris header kolom (nol baris data)
27. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): menutup overlay (`Esc`), `[Clear Field]` lalu `[Apply]`, menutup overlay Column Visibility dan memulihkan kolom Division, serta `(←)` yang mengosongkan Search. Asumsi dari TC-GS-NLU-274 dan TC-GS-NLU-275: `[Apply]` menutup Filter Panel.
- Asersi tambahan (S-03): pada TC-GS-NLU-299 dan TC-GS-NLU-303 asersi "tidak ada toast" diletakkan segera setelah pemicu unduhan (bagian 8b butir 11); anchor positifnya adalah berkas terunduh pada `Verifikasi` berikutnya. Pada TC-GS-NLU-300 asersi "hanya baris Contractor" memeriksa nilai Position sel sebagai hasil Filter; nilai, tipe, dan format sel lain ada di spec 087.
- Pembagian TC lintas spec: isi berkas (tipe sel, BOM, format tanggal; TC-GS-NLU-302, TC-GS-NLU-304, TC-GS-NLU-414) ada di spec 087 (kelas binary buffer); TC-GS-NLU-298 (kegagalan server saat Download) dan TC-GS-NLU-482 (di atas 5.000 baris) ada di spec lain.
- Temuan untuk QA:
  - TC-GS-NLU-299 precondition d merujuk TC populasi (TC-GS-NLU-99) sebagai dependensi; spec memakai Pre-setup yang memuat lebih dari 10 baris.
  - TC-GS-NLU-300 dan TC-GS-NLU-303 menyebut "buka file" tanpa menyebut cara; spec membaca berkas hasil unduhan lewat kemampuan teknis.
  - TC-GS-NLU-301 menyatakan "File kedua memuat kolom Division" tanpa posisi kolom; spec mengasersi keberadaannya.
