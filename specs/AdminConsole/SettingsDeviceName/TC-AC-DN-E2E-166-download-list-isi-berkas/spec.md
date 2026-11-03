---
id: TC-AC-DN-E2E-166-download-list-isi-berkas
title: "Download List: Isi Berkas (Category Jalur Penuh, Brand/Model, Hyphen, Last Modified, BOM CSV, Sheet1 XLSX)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-374
  - TC-AC-DN-375
  - TC-AC-DN-376
  - TC-AC-DN-377
  - TC-AC-DN-379
  - TC-AC-DN-380
coverage:
  web: automated
---

# Download List: Isi Berkas (Category Jalur Penuh, Brand/Model, Hyphen, Last Modified, BOM CSV, Sheet1 XLSX)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #14, #15, #16 (`Barcode Station`, `Gate Antenna`, `RFID Reader`, `Cable Tester`), #17, #19 (Last Modified `Cable Tester` `10/09/26 12:25`), #20 (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- Kemampuan teknis (disediakan tim FE): pembaca berkas CSV dan XLSX (isi sel, byte awal BOM, struktur workbook). Kelas harness f: isi berkas.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-374: Kolom Category diekspor sebagai jalur penuh dari root tanpa pemotongan
2. Ketik Search `Barcode`, tekan Enter
3. Klik ikon Download lalu klik `Download as CSV`
4. Buka file hasil unduhan dengan pembaca berkas CSV
5. Verifikasi baris Barcode Station: Category `TAG > NFC > Perangkat Pemindai Kode Batang Industri` utuh (tanpa `..`)
6. Ganti isi kotak Search dengan `Antenna`, tekan Enter
7. Klik ikon Download lalu klik `Download as CSV`
8. Buka file hasil unduhan dengan pembaca berkas CSV
9. Verifikasi baris Gate Antenna: Category `Hardware > Smart Fixed Reader > Antenna`
10. Ganti isi kotak Search dengan `RFID Reader`, tekan Enter
11. Klik ikon Download lalu klik `Download as CSV`
12. Buka file hasil unduhan dengan pembaca berkas CSV
13. Verifikasi baris RFID Reader: Category `Hardware > Handheld Reader > UHF Handheld`
14. TC-AC-DN-375: Kolom Brand dan Model/Type diekspor penuh dipisah koma dan spasi
15. Ganti isi kotak Search dengan `RFID Reader`, tekan Enter
16. Klik ikon Download lalu klik `Download as CSV`
17. Buka file hasil unduhan dengan pembaca berkas CSV
18. Verifikasi baris RFID Reader: Brand `Brand A, Brand B, Brand C` (ketiga nilai penuh, tanpa `+1 more`)
19. Verifikasi baris RFID Reader: Model/Type `Model R1, Model R2, Model R3`
20. Verifikasi nilai Brand dan Model/Type tidak memuat hierarki
21. TC-AC-DN-376: Nilai kosong Brand dan Model/Type diekspor sebagai hyphen
22. Ganti isi kotak Search dengan `Cable Tester`, tekan Enter
23. Klik ikon Download lalu klik `Download as CSV`
24. Buka file hasil unduhan dengan pembaca berkas CSV
25. Verifikasi baris Cable Tester: Brand `-` dan Model/Type `-` (hyphen tunggal, bukan sel kosong dan bukan `—`)
26. TC-AC-DN-377: Kolom Last Modified diekspor mengikuti General Settings
27. Klik ikon Download lalu klik `Download as CSV`
28. Buka file hasil unduhan dengan pembaca berkas CSV
29. Verifikasi baris Cable Tester: Last Modified `10/09/26 12:25` (Date Format `dd/MM/yy`, Time Format 24 jam)
30. Verifikasi kolom teks Device Name `Cable Tester` dan Measurement `Unit` ditulis polos
31. TC-AC-DN-379: Format file CSV: pemisah koma dan encoding UTF-8 dengan BOM
32. Ganti isi kotak Search dengan `RFID Reader`, tekan Enter
33. Klik ikon Download lalu klik `Download as CSV`
34. Periksa byte awal dan pemisah kolom file hasil unduhan
35. Verifikasi file diawali BOM UTF-8
36. Verifikasi kolom dipisah koma dan nilai yang memuat koma (Brand `Brand A, Brand B, Brand C`) dibungkus tanda kutip ganda
37. Klik `(←)` pada kotak Search
38. TC-AC-DN-380: Format file XLSX: satu sheet bernama Sheet1
39. Klik ikon Download lalu klik `Download as XLSX`
40. Buka struktur workbook file hasil unduhan dengan pembaca berkas XLSX
41. Verifikasi workbook memuat tepat satu sheet bernama `Sheet1`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search menemukan baris sasaran sebelum unduh; langkah TC-AC-DN-377 memakai Search `Cable Tester` yang masih aktif dari TC-AC-DN-376; langkah terakhir TC-AC-DN-379 mengosongkan Search.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Urutan: mengikuti sourceTc; TC-AC-DN-380 di akhir.
- Ukuran spec (41 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3); langkah unduh dan buka berkas diulang per TC karena tiap TC memeriksa berkas hasil Search yang berbeda.
- Temuan untuk QA:
  - TC-AC-DN-374 meminta unduh ulang Gate Antenna dan RFID Reader dengan Search `Antenna` dan `RFID Reader`; spec mengikutinya, Search `Antenna` juga memuat `Door Antenna` dan baris sasaran diidentifikasi lewat nama.
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
