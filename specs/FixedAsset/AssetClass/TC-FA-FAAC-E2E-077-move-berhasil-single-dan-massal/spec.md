---
id: TC-FA-FAAC-E2E-077-move-berhasil-single-dan-massal
title: "Move Asset Name Berhasil: Satu Asset Name dan Massal dengan Effective From Bulan Berjalan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-190
  - TC-FA-FAAC-191
  - TC-FA-FAAC-192
sourceRules: ["E-FAAC-42", "T-08", "FAAC-LOGIC-07k", "FAAC-LOGIC-13e", "§4.1.3#r5", "D-14"]
smoke: []
dependsOn: []
trace:
  "E-FAAC-42": [6, 12, 31]
  "T-08": [7, 17, 32]
  "FAAC-LOGIC-07k": [8, 11, 18, 35]
  "FAAC-LOGIC-13e": [16, 22]
  "§4.1.3#r5": 21
  "D-14": [26, 27, 28]
coverage:
  web: automated
---

# Move Asset Name Berhasil: Satu Asset Name dan Massal dengan Effective From Bulan Berjalan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke Asset Class semula oleh fixture BE di hook `before` dan `after`): Asset Class Active 'Heavy Equipment' (HEAVY-EQ) dengan "Wheel Loader" (4 aset aktif); 'Machinery' (MACHINERY) dengan "Welding Machine" (0 aset aktif); 'Construction Equipment' (CONSTR-EQ) dengan "Bulldozer D6" (5 aset aktif) dan "Concrete Mixer" (0 aset aktif); 'Vehicles' (VEHICLES) sebagai tujuan; 'Office Equipment (Legacy)' (OFFICE-OLD) berstatus Inactive (precondition TC, tidak diasersi). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; jam: M = bulan berjalan pada zona waktu General Settings client (NC-11); seed periode akuntansi, Last Posted Period, dan Last Exported Period lewat fixture (tanpa Last Posted Period dan tanpa Accounting Period Closed pada Asset Class terkait).
- State global: keanggotaan Asset Name di Asset Class berubah; dipulihkan di hook `after`.
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (seed spec lain ikut tampil), sehingga Class Code target dijangkau lewat Search kode (R-16), bukan lewat posisi baris di halaman 1.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-191: Move satu Asset Name dengan aset aktif memakai Effective From bulan berjalan

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"
3. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
4. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
5. Klik [Move] dengan "Effective From" tetap bernilai awal bulan berjalan
6. Verifikasi dialog menutup
7. Verifikasi muncul toast sukses: "Success, asset name has been moved."
8. Verifikasi "Wheel Loader" tidak lagi tampil di tab Asset Names Heavy Equipment
9. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `MACHINERY`, tekan Enter
10. Klik link Class Code "MACHINERY", lalu klik tab "Asset Names"
11. Verifikasi "Wheel Loader" tampil di tab Asset Names Machinery
12. Verifikasi keanggotaan berubah saat Confirm (tidak berstatus terjadwal)

### TC-FA-FAAC-190: Move satu Asset Name tanpa aset aktif ke Asset Class tujuan

13. Klik ikon ⋯ pada baris "Welding Machine" lalu pilih "Move"
14. Pilih "Destination Asset Class" = "VEHICLES – Vehicles"
15. Klik [Move]
16. Verifikasi dialog menutup
17. Verifikasi muncul toast sukses: "Success, asset name has been moved."
18. Verifikasi "Welding Machine" tidak lagi tampil di tab Asset Names Machinery
19. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `VEHICLES`, tekan Enter
20. Klik link Class Code "VEHICLES", lalu klik tab "Asset Names"
21. Verifikasi "Welding Machine" tampil di tab Asset Names Vehicles dengan Assigned At hari ini
22. Verifikasi "Welding Machine" langsung berlaku saat Confirm (tidak berstatus terjadwal)

### TC-FA-FAAC-192: Move massal dua Asset Name dengan salah satu memiliki aset aktif

23. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `CONSTR-EQ`, tekan Enter
24. Klik link Class Code "CONSTR-EQ", lalu klik tab "Asset Names"
25. Centang baris "Bulldozer D6" dan "Concrete Mixer", klik "Bulk Action", lalu pilih "Move to another asset class"
26. Verifikasi dialog "Move Asset Names" memuat dua bullet: "Bulldozer D6" dengan "5 active assets" dan "Concrete Mixer" dengan "0 active assets"
27. Verifikasi Effective From tampil karena ada Asset Name dengan aset aktif
28. Verifikasi pratinjau dampak berlabel "Assets affected" bernilai 5 (5 + 0 aset aktif)
29. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
30. Klik [Move]
31. Verifikasi dialog menutup
32. Verifikasi muncul toast sukses: "Success, asset name has been moved."
33. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `MACHINERY`, tekan Enter
34. Klik link Class Code "MACHINERY", lalu klik tab "Asset Names"
35. Verifikasi "Bulldozer D6" dan "Concrete Mixer" tampil di Machinery

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 191, 190, 192 (191 lebih dulu memindahkan "Wheel Loader" ke MACHINERY sehingga tab Machinery yang dibuka pada langkah 10 dipakai lagi untuk memilih "Welding Machine" pada TC-190; kedua TC memakai Asset Name yang berbeda).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class dan Asset Name seed dipakai apa adanya; dipulihkan oleh fixture BE di hook `after`.
- Langkah penghubung (S-03): langkah 1, 2, 9, 10, 19, 20, 23, 24, 33, dan 34 (Search kode untuk menemukan baris target, R-16, dan navigasi antar Asset Class lewat breadcrumb dan link Class Code).
- Langkah 5: TC-191 menyuruh membiarkan Effective From bernilai awal bulan berjalan; tidak ada aksi pada field itu.
- Temuan untuk QA: TC-190 menyebut toast "Success, asset name has been moved." tanpa membedakan Move satu dan massal; Post Condition "Seleksi bulk direset" pada TC-192 tidak memiliki langkah observasi sehingga tidak diasersi.
