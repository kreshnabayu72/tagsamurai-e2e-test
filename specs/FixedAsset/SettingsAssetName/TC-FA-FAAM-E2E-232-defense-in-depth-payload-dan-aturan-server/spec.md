---
id: TC-FA-FAAM-E2E-232-defense-in-depth-payload-dan-aturan-server
title: "Defense-in-Depth: Payload Script-SQL pada Create dan Search Dirender atau Diperlakukan sebagai Teks"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-625
  - TC-FA-FAAM-626
  - TC-FA-FAAM-627
coverage:
  web: automated
---

# Defense-in-Depth: Payload Script-SQL pada Create dan Search Dirender atau Diperlakukan sebagai Teks

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category `IT Equipment`), No. 23 (Brand `Dell`), No. 24 (UoM `Unit`), No. 25 (Label), No. 10 (`Dell Latitude`).
- Data Dinamis (dibuat lewat UI, nama bersuffix `{runId}-232`): `<script>alert(1)</script> {runId}-232` (TC-FA-FAAM-625), `Payload Model Item {runId}-232` dengan model `<img src=x onerror=alert(1)>` dan Code `<b>` (TC-FA-FAAM-626; ditolak, tidak tersimpan), dan `x'; DROP TABLE a;-- {runId}-232` (TC-FA-FAAM-627). Field wajib lain pada Create: Category `IT Equipment`, TAG Type `QR`, Brand `Dell` (model `5420` bila model wajib), UoM `Unit`; TC tidak menyebut nilai ini (lihat Temuan untuk QA).
- Kemampuan teknis: pemantauan dialog JavaScript (alert) pada halaman untuk memastikan tidak ada script berjalan; Modal Changelog dan Search di dalamnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus Asset Name bersuffix `-232` lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-625, 626, 627: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-625: Payload script pada Asset Name dirender sebagai teks

1. Klik `[+ Asset Name]`
2. Isi Asset Name `<script>alert(1)</script> {runId}-232` dengan field wajib lain
3. Klik `[Submit]`
4. Ketik Search `{runId}-232`, tekan Enter
5. Verifikasi List menampilkan teks `<script>alert(1)</script> {runId}-232` apa adanya
6. Klik nama `<script>alert(1)</script> {runId}-232`
7. Verifikasi Detail menampilkan teks `<script>alert(1)</script> {runId}-232` apa adanya
8. Tutup Popup Detail
9. Klik icon Changelog
10. Ketik Search `{runId}-232`, tekan Enter
11. Verifikasi Changelog menampilkan teks `<script>alert(1)</script> {runId}-232` apa adanya
12. Verifikasi tidak ada script berjalan (tidak ada dialog alert pada halaman)
13. Tutup Modal Changelog

### TC-FA-FAAM-626: Payload script pada nama model dan Code ditolak atau dirender sebagai teks

14. Klik `[+ Asset Name]`
15. Isi Asset Name `Payload Model Item {runId}-232` dengan field wajib lain, model `<img src=x onerror=alert(1)>` pada Brand `Dell`, dan Code `<b>`
16. Verifikasi model tampil sebagai teks literal
17. Klik `[Submit]`
18. Verifikasi Code `<b>` ditolak dengan `Code contains invalid characters`
19. Klik `✕` pada Modal Create
20. Verifikasi dialog `Unsaved Changes`
21. Klik `[Leave]`

### TC-FA-FAAM-627: Payload SQL pada Search dan Asset Name diperlakukan sebagai teks

22. Klik icon Search, ketik `' OR 1=1 --`, tekan Enter
23. Verifikasi Search tidak menampilkan baris tambahan (empty state `No results found`)
24. Klik `(←)` pada kotak Search
25. Klik `[+ Asset Name]`
26. Isi Asset Name `x'; DROP TABLE a;-- {runId}-232` dengan field wajib lain
27. Klik `[Submit]`
28. Ketik Search `{runId}-232`, tekan Enter
29. Verifikasi baris `x'; DROP TABLE a;-- {runId}-232` tersimpan sebagai teks
30. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
31. Verifikasi baris `Dell Latitude` tetap ada (tabel tidak terpengaruh payload SQL)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 4, 10, 22, 24, 28, 30 (Search atau pengosongan Search), langkah 8 dan 13 (menutup Popup Detail atau Modal Changelog), dan langkah 9 (membuka Modal Changelog).
- Langkah 12 mengasersi absence script berjalan dengan anchor positif langkah 5, 7, dan 11 (teks payload tampil pada tiga surface). Langkah 23 adalah absence hasil Search dengan anchor empty state `No results found` (bagian 8b butir 2).
- Langkah 30 dan 31 tidak dalam Expected TC-FA-FAAM-627 secara eksplisit; ia mengamati bahwa payload SQL tidak menghapus data (Pre-setup No. 10 hanya dibaca). Ditulis sebagai asersi tambahan beralasan: "diperlakukan sebagai teks" mencakup tidak adanya efek SQL.
- Temuan untuk QA:
  - TC-FA-FAAM-625 sampai 627 tidak menyebut nilai Category, TAG Type, Brand, dan UoM untuk "field wajib lain"; spec memilih dari Pre-setup No. 22 sampai 24.
  - TC-FA-FAAM-626 tidak menyebut apakah model tampil sebagai teks literal sebelum atau sesudah Submit; karena Code ditolak sehingga record tidak tersimpan, spec mengasersi model pada form sebelum Submit.
  - TC-FA-FAAM-625 butir b ("tidak ada script berjalan") tidak menyebut cara pengamatan; spec memakai pemantauan dialog alert.
