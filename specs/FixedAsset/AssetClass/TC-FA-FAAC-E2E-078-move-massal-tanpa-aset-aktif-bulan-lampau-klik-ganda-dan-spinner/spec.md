---
id: TC-FA-FAAC-E2E-078-move-massal-tanpa-aset-aktif-bulan-lampau-klik-ganda-dan-spinner
title: "Move Massal Tanpa Aset Aktif, Effective From Bulan Lampau, Klik Ganda, dan Spinner"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-193
  - TC-FA-FAAC-206
  - TC-FA-FAAC-626
  - TC-FA-FAAC-628
sourceRules: ["E-FAAC-42", "T-08", "FAAC-LOGIC-07k", "E-FAAC-80", "L-08", "ST-13", "FAAC-LOGIC-13e", "D-14"]
smoke: []
dependsOn: []
trace:
  "E-FAAC-42": 7
  "T-08": [8, 20, 37, 46]
  "FAAC-LOGIC-07k": [9, 12, 49]
  "E-FAAC-80": [20, 23]
  "L-08": 25
  "ST-13": [33, 34]
  "FAAC-LOGIC-13e": [36, 45]
  "D-14": [41, 42]
coverage:
  web: automated
---

# Move Massal Tanpa Aset Aktif, Effective From Bulan Lampau, Klik Ganda, dan Spinner

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke Asset Class semula oleh fixture BE di hook `before` dan `after` dan di langkah 26): 'Heavy Equipment' (HEAVY-EQ) dengan "Excavator PC200" (8 aset aktif; precondition TC, tidak diasersi), "Wheel Loader" (4 aset aktif), dan "Crane Rental Unit" (0 aset aktif); 'Office Equipment (New)' (OFFICE-NEW) dengan "Meeting Table" (0 aset aktif) dan "Whiteboard Stand" (0 aset aktif); 'Machinery' (MACHINERY) dan 'Vehicles' (VEHICLES) sebagai tujuan; 'Office Equipment (Legacy)' (OFFICE-OLD) berstatus Inactive (precondition TC, tidak diasersi); tanpa Last Posted Period pada kedua Asset Class. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; `Spectra.intercept` untuk menahan respons permintaan Move di atas backend nyata (dilepas segera di langkah 35); kemampuan baca BE untuk jumlah entri Changelog (audit trail permanen, S-12) dan Asset Class asal Asset Name; jam: M = bulan berjalan pada zona waktu General Settings client (NC-11).
- State global: keanggotaan Asset Name di Asset Class berubah; dipulihkan di hook `after`.
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (seed spec lain ikut tampil), sehingga Class Code target dijangkau lewat Search kode (R-16), bukan lewat posisi baris di halaman 1.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-206: Move dengan Effective From sebelum bulan berjalan tetap berlaku langsung

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"
3. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
4. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
5. Pilih Effective From = bulan M-1
6. Klik [Move]
7. Verifikasi dialog menutup
8. Verifikasi muncul toast sukses: "Success, asset name has been moved."
9. Verifikasi "Wheel Loader" tidak lagi tampil di tab Asset Names Heavy Equipment
10. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `MACHINERY`, tekan Enter
11. Klik link Class Code "MACHINERY", lalu klik tab "Asset Names"
12. Verifikasi "Wheel Loader" tampil di Machinery tanpa status terjadwal (langsung berpindah saat Confirm walau Effective From bulan sebelumnya)

### TC-FA-FAAC-626: Klik ganda tombol Move hanya memproses satu permintaan

13. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
14. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"
15. Tunggu toast lama hilang otomatis
16. Baca jumlah entri Changelog sebagai baseline
17. Klik ikon ⋯ pada baris "Crane Rental Unit" lalu pilih "Move"
18. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
19. Klik [Move] dua kali dengan cepat
20. Verifikasi hanya satu toast sukses "Success, asset name has been moved."
21. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `MACHINERY`, tekan Enter
22. Klik link Class Code "MACHINERY", lalu klik tab "Asset Names"
23. Verifikasi "Crane Rental Unit" tampil tepat satu kali di tab Asset Names Machinery
24. Klik breadcrumb "Asset Class", lalu klik ikon Changelog
25. Verifikasi selisih jumlah entri Changelog terhadap baseline langkah 16 adalah 2, yaitu dua entri L-08 (asal dan tujuan) untuk "Crane Rental Unit"

### TC-FA-FAAC-628: Tombol Move menampilkan spinner dan non-interaktif saat permintaan dikirim

26. Tutup modal Changelog dan pulihkan "Crane Rental Unit" ke HEAVY-EQ lewat fixture BE
27. Tunggu toast lama hilang otomatis
28. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
29. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"
30. Klik ikon ⋯ pada baris "Crane Rental Unit" lalu pilih "Move"
31. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
32. Tunda respons permintaan Move, lalu klik [Move]
33. Verifikasi tombol [Move] menampilkan spinner selama permintaan berjalan
34. Verifikasi tombol [Move] tidak dapat diklik selama permintaan berjalan
35. Lepas tahanan respons permintaan Move
36. Verifikasi dialog menutup
37. Verifikasi toast sukses "Success, asset name has been moved." tampil

### TC-FA-FAAC-193: Move massal dua Asset Name tanpa aset aktif tidak meminta Effective From

38. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `OFFICE-NEW`, tekan Enter
39. Klik link Class Code "OFFICE-NEW", lalu klik tab "Asset Names"
40. Centang baris "Meeting Table" dan "Whiteboard Stand", klik "Bulk Action", lalu pilih "Move to another asset class"
41. Verifikasi dialog memuat dua bullet "Meeting Table" dan "Whiteboard Stand" dengan "0 active assets"
42. Verifikasi Effective From dan pratinjau dampak Hidden
43. Pilih "Destination Asset Class" = "VEHICLES – Vehicles"
44. Klik [Move]
45. Verifikasi dialog menutup
46. Verifikasi muncul toast sukses: "Success, asset name has been moved."
47. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `VEHICLES`, tekan Enter
48. Klik link Class Code "VEHICLES", lalu klik tab "Asset Names"
49. Verifikasi "Meeting Table" dan "Whiteboard Stand" tampil di Vehicles

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 206, 626, 628, 193 (Move pada HEAVY-EQ lebih dulu; TC-628 memindahkan "Crane Rental Unit" yang sama dengan TC-626 sehingga langkah 26 memulihkannya di antaranya).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class dan Asset Name seed dipakai apa adanya; dipulihkan oleh fixture BE.
- Langkah penghubung (S-03): langkah 1, 2, 10, 11, 13, 14, 15, 21, 22, 24, 26, 27, 28, 29, 38, 39, 47, dan 48 (Search kode R-16, navigasi, pemulihan seed, menunggu toast lama, R-12).
- Intercept pada langkah 32 hanya menahan respons untuk mengamati state UI (bukan kelas b) dan dilepas pada langkah 35.
- Spec di atas 35 langkah (49 langkah): empat TC satu topik (Move dari Asset Class asal) dengan dataset seed yang sama; Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan empat belas langkah di antaranya adalah Search kode dan navigasi antar Asset Class untuk memeriksa tujuan; memecah lagi menggandakan seed dan pemulihan tanpa pemisah nyata.
- Temuan untuk QA: TC-626 tidak menyebut cara menghitung entri L-08; spec memakai selisih jumlah entri terhadap baseline. TC-206 tidak menyebut apakah Effective From bulan lampau tampil di Changelog.
