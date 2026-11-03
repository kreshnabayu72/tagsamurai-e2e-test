---
id: TC-FA-SU-E2E-180-sub-tab-pending-tasks-download
title: "Sub-tab Pending Tasks: Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-531
  - TC-FA-SU-532
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Kemampuan teknis: penangkapan berkas unduhan dan pembacaan isi berkas CSV/XLSX (jumlah baris, nama kolom header, dan untuk TC dengan asersi isi: encoding BOM, pembungkus tanda kutip ganda, nama sheet) disediakan tim FE.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.
- Nama berkas: `Pending-Tasks-Budi-Santoso` (`.csv` atau `.xlsx`).

## Test Steps

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-531: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

2. Hover icon Download
3. Verifikasi tooltip `Download`
4. Klik icon Download
5. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `Pending-Tasks-Budi-Santoso.csv` terunduh
9. Klik icon Download
10. Pilih `Download as XLSX`
11. Verifikasi file `Pending-Tasks-Budi-Santoso.xlsx` terunduh
12. Buka berkas CSV
13. Verifikasi CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
15. Buka berkas XLSX
16. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-532: Cakupan baris dan kolom Download

17. Unduh CSV tanpa kontrol aktif (klik icon Download, pilih `Download as CSV`)
18. Verifikasi berkas memuat seluruh baris (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`) dalam urutan sort aktif
19. Ketik Search `ASG-2026`, tekan Enter
20. Klik icon Filter
21. Buka dropdown Transaction lalu centang `Assignment`
22. Klik `[Apply]`
23. Unduh CSV (klik icon Download, pilih `Download as CSV`)
24. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter (`ASG-20260715-0045`, `ASG-20260718-0067`)
25. Klik header kolom Actions (⋯), lalu hilangkan centang Group
26. Unduh CSV (klik icon Download, pilih `Download as CSV`)
27. Verifikasi tidak ada toast peringatan
28. Verifikasi kolom Group tidak ikut berkas
29. Klik header kolom Actions (⋯), lalu centang kembali Group
30. Unduh CSV (klik icon Download, pilih `Download as CSV`)
31. Verifikasi kolom Group ikut berkas kembali
32. Ganti isi kotak search dengan `zzz`, tekan Enter
33. Unduh CSV (klik icon Download, pilih `Download as CSV`)
34. Verifikasi tidak ada toast
35. Verifikasi berkas hanya memuat baris header kolom yang visible

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; membuka berkas unduhan (langkah TC-FA-SU-531 "Buka kedua berkas").
- Jumlah langkah: 35 tertulis, 35 dengan ekspansi iterasi.
- Temuan untuk QA:
  - TC-FA-SU-531 Expected d (encoding BOM, pembungkus tanda kutip ganda, nama sheet) adalah asersi isi berkas (kelas f, bagian 3 prinsip 13 butir f), tetapi TC ini bertipe fungsional dan memuatnya bersama nama berkas; spec mengikuti TC. Pemilik proses dapat memindahkan dua Verifikasi isi berkas ke spec kelas f.
  - TC-FA-SU-531 Expected d menyebut nilai ber-koma, tanda kutip, atau baris baru, tetapi Pre-setup #25 tidak memuat nilai seperti itu pada 5 baris Pending Tasks; tim FE perlu memastikan data yang memuatnya.
  - TC-FA-SU-532 Expected a menyebut "seluruh baris (bukan hanya halaman aktif)" padahal fixture hanya satu halaman (5 baris); spec mengasersi lima baris.
