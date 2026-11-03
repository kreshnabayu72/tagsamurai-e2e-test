---
id: TC-FA-SU-E2E-191-tab-non-login-user-tooltip-icon-dan-download
title: "Tab Non-Login User: Tooltip Icon dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-569
  - TC-FA-SU-570
  - TC-FA-SU-573
coverage:
  web: automated
---

# Tab Non-Login User: Tooltip Icon dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Kemampuan teknis: penangkapan berkas unduhan dan pembacaan isi berkas CSV/XLSX (jumlah baris, nama kolom header, dan untuk TC dengan asersi isi: encoding BOM, pembungkus tanda kutip ganda, nama sheet) disediakan tim FE.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Nama berkas: `Non-Login-User-Budi-Santoso` (`.csv` atau `.xlsx`).
- Tabel parameter "Ikon dan header tooltip":

| Ikon | Tooltip |
|---|---|
| `Search` | `Search` |
| `Filter` | `Filter` |
| `Download` | `Download` |
| header kolom Actions (⋯) | `Column Visibility` |

## Test Steps

1. Buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-569: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

2. Hover icon Download
3. Verifikasi tooltip `Download`
4. Klik icon Download
5. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `Non-Login-User-Budi-Santoso.csv` terunduh
9. Klik icon Download
10. Pilih `Download as XLSX`
11. Verifikasi file `Non-Login-User-Budi-Santoso.xlsx` terunduh
12. Buka berkas CSV
13. Verifikasi CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
15. Buka berkas XLSX
16. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-570: Cakupan baris dan kolom Download

17. Unduh CSV tanpa kontrol aktif (klik icon Download, pilih `Download as CSV`)
18. Verifikasi berkas memuat seluruh baris (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`) dalam urutan sort aktif
19. Ketik Search `Printer`, tekan Enter
20. Klik icon Filter
21. Buka dropdown Status lalu centang `Inactive`
22. Klik `[Apply]`
23. Unduh CSV (klik icon Download, pilih `Download as CSV`)
24. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter (`Printer Lantai 5`)
25. Klik header kolom Actions (⋯), lalu hilangkan centang Division
26. Unduh CSV (klik icon Download, pilih `Download as CSV`)
27. Verifikasi tidak ada toast peringatan
28. Verifikasi kolom Division tidak ikut berkas
29. Klik header kolom Actions (⋯), lalu centang kembali Division
30. Unduh CSV (klik icon Download, pilih `Download as CSV`)
31. Verifikasi kolom Division ikut berkas kembali
32. Ganti isi kotak search dengan `zzz`, tekan Enter
33. Unduh CSV (klik icon Download, pilih `Download as CSV`)
34. Verifikasi tidak ada toast
35. Verifikasi berkas hanya memuat baris header kolom yang visible

### TC-FA-SU-573: Tooltip icon Table Tools dan header Actions

36. Klik `←` pada kotak Search
37. Klik icon Filter
38. Klik `[Clear Field]` pada field Status
39. Klik `[Apply]`
40. Untuk setiap baris tabel "Ikon dan header tooltip" (langkah 40 sampai 41): hover ikon baris itu
41. Verifikasi tooltip sama dengan kolom "Tooltip" baris itu

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; membuka berkas unduhan (langkah TC-FA-SU-569 "Buka kedua berkas"); pemulihan Search dan Filter sebelum TC-FA-SU-573 (S-09).
- Langkah berulang per baris tabel parameter: tabel "Ikon dan header tooltip" pada langkah 40 sampai 41 (4 iterasi).
- Jumlah langkah: 41 tertulis, 47 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (47 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-569 Expected d (encoding BOM, pembungkus tanda kutip ganda, nama sheet) adalah asersi isi berkas (kelas f, bagian 3 prinsip 13 butir f), tetapi TC ini bertipe fungsional; spec mengikuti TC. Pemilik proses dapat memindahkan dua Verifikasi isi berkas ke spec kelas f.
  - TC-FA-SU-569 Expected d menyebut nilai ber-koma, tanda kutip, atau baris baru, tetapi Pre-setup #26 tidak memuat nilai seperti itu; tim FE perlu memastikan data yang memuatnya.
  - TC-FA-SU-570 tidak menyebut Search dan Filter yang diterapkan; spec memakai Search `Printer` dan Filter Status `Inactive` (hasil `Printer Lantai 5`).
