---
id: TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama
title: "Download CSV dan XLSX Tabel Position: Screening Overlay, Isi Berkas, Mengikuti Search, dan Kolom Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-192
  - TC-GS-POS-193
  - TC-GS-POS-194
  - TC-GS-POS-195
  - TC-GS-POS-196
  - TC-GS-POS-197
  - TC-GS-POS-198
coverage:
  web: automated
---

# Download CSV dan XLSX Tabel Position: Screening Overlay, Isi Berkas, Mengikuti Search, dan Kolom Tersembunyi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record); selain `Sales Coordinator` (diasersi langkah 29), dipakai sebagai precondition TC, tidak diasersi.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.populationSeed033`): 13 Position `HR Business Partner {runId}-033`, `IT Support Specialist {runId}-033`, `Temporary Staff {runId}-033`, `iOS Developer {runId}-033`, `Legal Counsel {runId}-033`, `Marketing Executive {runId}-033`, `Quality Assurance Analyst {runId}-033`, `Data Engineer {runId}-033`, `Office Administrator {runId}-033`, `Logistics Coordinator {runId}-033`, `Payroll Specialist {runId}-033`, `Security Officer {runId}-033`, `Training Coordinator {runId}-033`. Dengan 7 record Pre-setup, jumlah seluruh record N = 20 (lebih dari satu halaman pada ukuran halaman 10). N dibaca hook `before` lewat API seeding (disediakan tim FE/BE, tanpa mengarang endpoint) setelah seeding dan dipakai pada TC-GS-POS-195 (N diturunkan dari seeding). Position yang tidak diasersi langkah dipakai sebagai precondition TC (Data Dinamis No. 1-13), tidak diasersi.
- General Settings Date/Time Format dan Time Zone tidak diubah spec ini; format tanggal yang berlaku dibaca dari General Settings untuk memeriksa kolom Last Updated di berkas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-033` yang masih ada; hapus berkas hasil unduhan (`Position.csv`, `Position.xlsx`) dari direktori unduhan uji; pulihkan preferensi visibilitas kolom tabel Position di browser ke default (Name dan Last Updated tampil).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: menangkap berkas hasil unduhan browser (nama berkas) dan membaca isinya (CSV dan XLSX: baris data, header kolom, nilai sel); pembacaan keberadaan toast.
- State global: preferensi kolom tabel Position tersimpan di browser per pengguna; spec memulihkannya di langkah akhir TC-GS-POS-198 dan hook `after` sebagai cadangan. Tidak ada state lain yang diubah.

## Test Steps

### TC-GS-POS-192: Screening Overlay Download tabel utama

1. Hover ikon Download
2. Verifikasi Tooltip "Download"
3. Klik ikon Download
4. Verifikasi Overlay Download memuat opsi `Download as CSV`
5. Verifikasi Overlay Download memuat opsi `Download as XLSX`
6. Tutup Overlay Download

### TC-GS-POS-193: Download CSV tabel utama

7. Klik ikon Download
8. Pilih opsi `Download as CSV`
9. Verifikasi tidak ada toast sukses
10. Verifikasi berkas `Position.csv` terunduh

### TC-GS-POS-194: Download XLSX tabel utama

11. Klik ikon Download
12. Pilih opsi `Download as XLSX`
13. Verifikasi tidak ada toast sukses
14. Verifikasi berkas `Position.xlsx` terunduh

### TC-GS-POS-195: Download tanpa Search/Filter berisi seluruh baris lintas halaman

15. Verifikasi tabel tanpa Search aktif
16. Verifikasi tabel tanpa Filter aktif
17. Verifikasi ukuran halaman tabel 10
18. Klik ikon Download
19. Pilih opsi `Download as CSV`
20. Buka berkas `Position.csv` hasil unduhan
21. Verifikasi berkas memuat N baris data (seluruh record, bukan hanya 10 baris halaman 1)
22. Verifikasi berkas memuat kolom `Name`
23. Verifikasi berkas memuat kolom `Last Updated`
24. Verifikasi nilai kolom Last Updated di berkas mengikuti format tanggal General Settings

### TC-GS-POS-196: Download mengikuti Search aktif

25. Ketik Search `Coordinator`, tekan Enter
26. Klik ikon Download
27. Pilih opsi `Download as CSV`
28. Buka berkas `Position.csv` hasil unduhan
29. Verifikasi berkas memuat baris `Sales Coordinator`, `Logistics Coordinator {runId}-033`, dan `Training Coordinator {runId}-033`
30. Verifikasi setiap baris data di berkas memuat `Coordinator` pada Name
31. Klik `✕` pada Search, tekan Enter

### TC-GS-POS-197: Download tidak menyertakan kolom yang disembunyikan

32. Klik ikon `⋯` pada header kolom Actions
33. Uncheck `Last Updated`
34. Tutup Overlay Column Visibility
35. Klik ikon Download
36. Pilih opsi `Download as CSV`
37. Verifikasi tidak ada toast atau peringatan bahwa kolom tidak ikut
38. Buka berkas `Position.csv` hasil unduhan
39. Verifikasi berkas memuat kolom `Name`
40. Verifikasi berkas hanya memuat kolom `Name`

### TC-GS-POS-198: Download kembali menyertakan kolom setelah ditampilkan lagi

41. Klik ikon `⋯` pada header kolom Actions
42. Centang `Last Updated`
43. Tutup Overlay Column Visibility
44. Klik ikon Download
45. Pilih opsi `Download as CSV`
46. Buka berkas `Position.csv` hasil unduhan
47. Verifikasi berkas memuat kolom `Name`
48. Verifikasi berkas memuat kolom `Last Updated`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 48 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas (binary buffer: isi berkas unduhan tabel utama), satu akun, tanpa mengubah data Position; langkah membuka berkas unduhan mendominasi jumlah langkah. TC-GS-POS-198 melanjutkan state kolom tersembunyi dari TC-GS-POS-197, sehingga bagian itu tidak berdiri sendiri.
- Urutan TC dalam spec mengikuti urutan TC sumber (192 sampai 198). Layar awal Global Settings > User > Position dibuka di hook `beforeEach` dan dipakai bersama semua TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (tutup Overlay Download), langkah 20, 28, 38, dan 46 (membuka berkas hasil unduhan agar isinya dapat diasersi), langkah 31 (lepas Search sebelum TC-GS-POS-197), dan langkah 34 dan 43 (menutup Overlay Column Visibility). Langkah 15 sampai 17 adalah `Verifikasi` baseline (bukan aksi): state awal spec ini belum memakai Search, Filter, atau ukuran halaman lain, sehingga langkah "Pastikan" TC-GS-POS-195 dipenuhi dengan asersi keadaan itu, satu `Verifikasi` per klausa.
- TC-GS-POS-198 bergantung pada TC-GS-POS-197 ("Sembunyikan Last Updated lalu tampilkan lagi"); langkah sembunyikan (langkah 32 sampai 34) dijalankan di TC-GS-POS-197 dan Last Updated langsung ditampilkan kembali di langkah 41 sampai 43, sehingga TC-GS-POS-198 melanjutkan state tersembunyi dari TC-GS-POS-197 dan tidak menyembunyikannya dua kali. Preferensi kolom kembali ke default di akhir TC-GS-POS-198.
- Asersi tidak adanya toast pada TC-GS-POS-193 (langkah 9), TC-GS-POS-194 (langkah 13), dan TC-GS-POS-197 (langkah 37) ditaruh tepat sesudah pemicu download dan sebelum asersi berkas (terunduh atau dibuka) supaya toast yang bersifat sementara tidak terlewat; urutan ini berbeda dari urutan Expected TC (file lalu toast) dan mengikuti bagian 8b butir 5 dan 11 konvensi.
- Langkah 29 (tiga baris yang memuat `Coordinator` ada di berkas) ditaruh sebelum asersi "setiap baris data memuat `Coordinator`" pada langkah 30, dan langkah 39 (berkas memuat kolom `Name`) ditaruh sebelum asersi "hanya memuat kolom `Name`" pada langkah 40; keduanya anchor positif tambahan di luar Expected TC supaya asersi universal tidak lolos pada berkas kosong.
- Kegagalan ekspor (download gagal) tidak termasuk spec ini: TC-GS-POS-199 dan 240 ada di spec 037. Download Popup Changelog (TC-GS-POS-237 sampai 239) ada di spec 043.
- Temuan untuk QA:
  - Judul TC-GS-POS-196 menyebut "Search dan Filter aktif", tetapi langkah dan Expected hanya memuat Search `Coordinator`; spec mengikuti langkah TC (hanya Search).
  - TC-GS-POS-193 dan 194 hanya memverifikasi nama berkas; isi berkas diasersi hanya pada TC-GS-POS-195 sampai 198 (CSV), dan isi berkas XLSX tidak diasersi oleh TC mana pun.
  - TC-GS-POS-192 sampai 198 tidak menyebut format tanggal General Settings yang berlaku; spec memakai format yang dibaca dari General Settings saat run.
