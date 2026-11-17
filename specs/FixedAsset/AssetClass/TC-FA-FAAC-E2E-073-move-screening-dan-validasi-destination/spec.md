---
id: TC-FA-FAAC-E2E-073-move-screening-dan-validasi-destination
title: "Screening Dialog Move Asset Names dan Validasi Destination Asset Class"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-188
  - TC-FA-FAAC-189
  - TC-FA-FAAC-196
  - TC-FA-FAAC-197
sourceRules: ["D-14", "V-31", "E-FAAC-95", "E-FAAC-37", "F-FAAC-09.k1", "FAAC-LOGIC-11c"]
smoke: []
dependsOn: []
trace:
  "D-14": [4, 5, 6, 7, 8, 9, 12, 13, 14, 21, 25]
  "V-31": 16
  "E-FAAC-95": [17, 18]
  "E-FAAC-37": 19
  "F-FAAC-09.k1": 22
  "FAAC-LOGIC-11c": 23
coverage:
  web: automated
---

# Screening Dialog Move Asset Names dan Validasi Destination Asset Class

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Class Active 'Heavy Equipment' (HEAVY-EQ) dengan Asset Name ter-assign: Excavator PC200 (8 aset aktif), Wheel Loader (4 aset aktif), Crane Rental Unit (0 aset aktif); Asset Class Active 'Machinery' (MACHINERY) dan 'Vehicles' (VEHICLES) sebagai tujuan; 'Office Equipment (Legacy)' (OFFICE-OLD) berstatus Inactive. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk Asset Class asal Asset Name; jam: bulan berjalan (M) dihitung pada zona waktu General Settings client (NC-11).
- State global: tidak ada yang diubah (dialog selalu dibatalkan).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (seed spec lain ikut tampil), sehingga Class Code target dijangkau lewat Search kode (R-16), bukan lewat posisi baris di halaman 1.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"

### TC-FA-FAAC-188: Screening Dialog Move Asset Names dari row action untuk Asset Name dengan aset aktif

3. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
4. Verifikasi Dialog Form berjudul "Move Asset Names" dengan tombol [✕]
5. Verifikasi daftar read-only "Asset Names" berisi satu bullet "Wheel Loader" disertai teks "4 active assets"
6. Verifikasi Select "Destination Asset Class" tampil dengan placeholder "Select asset class"
7. Verifikasi field "Effective From" (pemilih bulan, placeholder "Select month") tampil dengan nilai awal bulan berjalan
8. Verifikasi pratinjau dampak berlabel "Assets affected" bernilai 4
9. Verifikasi footer berisi [Cancel] dan [Move]
10. Klik [Cancel]

### TC-FA-FAAC-189: Screening Dialog Move Asset Names untuk Asset Name tanpa aset aktif menyembunyikan Effective From

11. Klik ikon ⋯ pada baris "Crane Rental Unit" lalu pilih "Move"
12. Verifikasi daftar "Asset Names" berisi bullet "Crane Rental Unit" disertai teks "0 active assets"
13. Verifikasi Select "Destination Asset Class" tampil
14. Verifikasi field "Effective From" dan pratinjau dampak Hidden

### TC-FA-FAAC-196: Klik Move tanpa memilih Destination Asset Class

15. Klik [Move] tanpa memilih tujuan
16. Verifikasi caption error tampil di field Destination Asset Class: "Destination asset class must not be empty"
17. Verifikasi dialog tetap terbuka
18. Verifikasi tidak ada toast
19. Verifikasi "Crane Rental Unit" tidak berpindah: tetap di HEAVY-EQ

### TC-FA-FAAC-197: Opsi Destination Asset Class hanya Asset Class Active selain Asset Class asal

20. Buka daftar opsi "Destination Asset Class"
21. Verifikasi opsi ditulis "[Class Code] – [Class Name]" dan memuat "MACHINERY – Machinery" serta "VEHICLES – Vehicles"
22. Verifikasi opsi tidak memuat "HEAVY-EQ – Heavy Equipment" (Asset Class asal)
23. Verifikasi opsi tidak memuat "OFFICE-OLD – Office Equipment (Legacy)" (Inactive)
24. Ketik "veh" pada pencarian opsi
25. Verifikasi pencarian "veh" menyisakan "VEHICLES – Vehicles"
26. Tutup daftar opsi lalu klik [Cancel]

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 188, 189, 196, 197 (TC-196 dan TC-197 melanjutkan dialog Move "Crane Rental Unit" dari TC-189; keduanya tidak membutuhkan dialog baru).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class dan Asset Name seed dipakai apa adanya; spec tidak mengubah data.
- Langkah penghubung (S-03): langkah 1 (Search kode, R-16), 2 (membuka Detail HEAVY-EQ), 10 dan 26 (menutup dialog).
- Langkah 21 menjadi anchor positif bagi asersi absence langkah 22 dan 23 (bagian 8b butir 2).
- Temuan untuk QA: TC-197 menyebut placeholder pencarian opsi tanpa teksnya; spec hanya mengetik "veh".
