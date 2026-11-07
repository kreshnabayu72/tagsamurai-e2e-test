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

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-569: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

3. Hover icon Download
4. Verifikasi tooltip `Download`
5. Klik icon Download
6. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi file `Non-Login-User-Budi-Santoso.csv` terunduh
10. Klik icon Download
11. Pilih `Download as XLSX`
12. Verifikasi file `Non-Login-User-Budi-Santoso.xlsx` terunduh
13. Buka berkas CSV
14. Verifikasi CSV berencoding UTF-8 dengan BOM
15. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
16. Buka berkas XLSX
17. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-570: Cakupan baris dan kolom Download

18. Unduh CSV tanpa kontrol aktif (klik icon Download, pilih `Download as CSV`)
19. Verifikasi berkas memuat seluruh baris (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`) dalam urutan sort aktif
20. Ketik Search `Printer`, tekan Enter
21. Klik icon Filter
22. Buka dropdown Status lalu centang `Inactive`
23. Klik `[Apply]`
24. Unduh CSV (klik icon Download, pilih `Download as CSV`)
25. Verifikasi berkas hanya memuat baris yang cocok dengan Search dan Filter (`Printer Lantai 5`)
26. Klik header kolom Actions (⋯), lalu hilangkan centang Division
27. Unduh CSV (klik icon Download, pilih `Download as CSV`)
28. Verifikasi tidak ada toast peringatan
29. Verifikasi kolom Division tidak ikut berkas
30. Klik header kolom Actions (⋯), lalu centang kembali Division
31. Unduh CSV (klik icon Download, pilih `Download as CSV`)
32. Verifikasi kolom Division ikut berkas kembali
33. Ganti isi kotak search dengan `zzz`, tekan Enter
34. Unduh CSV (klik icon Download, pilih `Download as CSV`)
35. Verifikasi tidak ada toast
36. Verifikasi berkas hanya memuat baris header kolom yang visible

### TC-FA-SU-573: Tooltip icon Table Tools dan header Actions

37. Klik `←` pada kotak Search
38. Klik icon Filter
39. Klik `[Clear Field]` pada field Status
40. Klik `[Apply]`
41. Untuk setiap baris tabel "Ikon dan header tooltip" (langkah 41 sampai 42): hover ikon baris itu
42. Verifikasi tooltip sama dengan kolom "Tooltip" baris itu

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; membuka berkas unduhan (langkah TC-FA-SU-569 "Buka kedua berkas"); pemulihan Search dan Filter sebelum TC-FA-SU-573 (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- Langkah berulang per baris tabel parameter: tabel "Ikon dan header tooltip" pada langkah 41 sampai 42 (4 iterasi).
- Jumlah langkah: 42 tertulis, 48 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (48 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-569 Expected d (encoding BOM, pembungkus tanda kutip ganda, nama sheet) adalah asersi isi berkas (kelas f, bagian 3 prinsip 13 butir f), tetapi TC ini bertipe fungsional; spec mengikuti TC. Pemilik proses dapat memindahkan dua Verifikasi isi berkas ke spec kelas f.
  - TC-FA-SU-569 Expected d menyebut nilai ber-koma, tanda kutip, atau baris baru, tetapi Pre-setup #26 tidak memuat nilai seperti itu; tim FE perlu memastikan data yang memuatnya.
  - TC-FA-SU-570 tidak menyebut Search dan Filter yang diterapkan; spec memakai Search `Printer` dan Filter Status `Inactive` (hasil `Printer Lantai 5`).
