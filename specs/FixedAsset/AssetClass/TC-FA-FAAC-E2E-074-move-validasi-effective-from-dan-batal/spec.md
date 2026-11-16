---
id: TC-FA-FAAC-E2E-074-move-validasi-effective-from-dan-batal
title: "Move: Validasi Pemilih Bulan Effective From serta Batal dan Tutup Dialog Move"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-194
  - TC-FA-FAAC-195
  - TC-FA-FAAC-198
  - TC-FA-FAAC-199
sourceRules: ["FAAC-LOGIC-07b", "FAAC-LOGIC-07k", "V-23", "E-FAAC-95", "D-14"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-07b": 6
  "FAAC-LOGIC-07k": [7, 16, 23, 28]
  "V-23": 13
  "E-FAAC-95": [14, 15]
  "D-14": [21, 26]
anchor: [22, 27]
coverage:
  web: automated
---

# Move: Validasi Pemilih Bulan Effective From serta Batal dan Tutup Dialog Move

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Class Active 'Heavy Equipment' (HEAVY-EQ) dengan Asset Name ter-assign: Excavator PC200 (8 aset aktif), Wheel Loader (4 aset aktif), Crane Rental Unit (0 aset aktif; precondition TC, tidak diasersi); Asset Class Active 'Machinery' (MACHINERY) sebagai tujuan; 'Vehicles' (VEHICLES) berstatus Active tersedia sebagai tujuan; 'Office Equipment (Legacy)' (OFFICE-OLD) berstatus Inactive (precondition TC, tidak diasersi). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; jam: bulan berjalan (M) dihitung pada zona waktu General Settings client (NC-11); kemampuan baca BE untuk Asset Class asal Asset Name.
- State global: tidak ada yang diubah (setiap dialog berakhir tanpa Move).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (seed spec lain ikut tampil), sehingga Class Code target dijangkau lewat Search kode (R-16), bukan lewat posisi baris di halaman 1.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"

### TC-FA-FAAC-198: Pemilih bulan Effective From tidak menawarkan bulan setelah bulan berjalan

3. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
4. Buka pemilih bulan "Effective From"
5. Coba maju ke bulan setelah bulan berjalan
6. Verifikasi bulan berjalan dan bulan sebelumnya yang memenuhi batas bawah dapat dipilih
7. Verifikasi bulan setelah bulan berjalan tidak ditawarkan (tidak dapat dipilih)
8. Tutup pemilih bulan lalu klik [Cancel]

### TC-FA-FAAC-199: Effective From dikosongkan lalu klik Move

9. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
10. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
11. Kosongkan "Effective From"
12. Klik [Move]
13. Verifikasi caption error di field Effective From: "Effective from must not be empty"
14. Verifikasi dialog tetap terbuka
15. Verifikasi tidak ada toast
16. Verifikasi "Wheel Loader" tidak berpindah: tetap di HEAVY-EQ
17. Klik [Cancel]

### TC-FA-FAAC-194: Batal Move dengan tombol Cancel

18. Klik ikon ⋯ pada baris "Excavator PC200" lalu pilih "Move"
19. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
20. Klik [Cancel]
21. Verifikasi dialog menutup
22. Verifikasi tidak ada toast
23. Verifikasi "Excavator PC200" tetap berada di Heavy Equipment

### TC-FA-FAAC-195: Tutup dialog Move dengan ikon ✕

24. Klik ikon ⋯ pada baris "Excavator PC200" lalu pilih "Move"
25. Klik ikon [✕] di header dialog
26. Verifikasi dialog menutup tanpa konfirmasi
27. Verifikasi tidak ada toast
28. Verifikasi "Excavator PC200" tetap di Heavy Equipment

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 198, 199 (validasi diblokir), lalu 194, 195 (kasus menutup dialog di akhir).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class dan Asset Name seed dipakai apa adanya; spec tidak mengubah data.
- Langkah penghubung (S-03): langkah 1 (Search kode, R-16), 2 (membuka Detail HEAVY-EQ), 8 dan 17 (menutup dialog).
- Langkah 6 menjadi anchor positif bagi asersi absence langkah 7 (bagian 8b butir 2).
- Langkah 10 pada TC-199 memilih tujuan sesuai langkah 3 TC-199 sehingga hanya Effective From yang kosong.
- Temuan untuk QA: TC-198 tidak menyebut bulan terjauh sebelum bulan berjalan yang dapat dipilih; spec hanya mengasersi bulan berjalan dan bulan sebelumnya yang memenuhi batas bawah.
