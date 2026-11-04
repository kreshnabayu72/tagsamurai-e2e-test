---
id: TC-FA-TDC-E2E-071-d-09-pratinjau-angka-hitung-ulang-shimmer-dan-apply-disabled
title: "Pratinjau Dampak D-09: Daftar Asset Class Terdampak, Angka Bernilai Strip, Hitung Ulang, dan Shimmer dengan Apply Disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-251
  - TC-FA-TDC-252
  - TC-FA-TDC-254
  - TC-FA-TDC-255
coverage:
  web: automated
---

# Pratinjau Dampak D-09: Daftar Asset Class Terdampak, Angka Bernilai Strip, Hitung Ulang, dan Shimmer dengan Apply Disabled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Kondisi mesin kalkulasi penyusutan fiskal: belum tersedia atau mengembalikan error (TC-252); kondisi ini disediakan tim FE/BE.
- Kemampuan intercept jaringan (`Spectra.intercept()`) di atas backend nyata untuk menunda respons endpoint pratinjau selama 3 detik (TC-255); nama endpoint pratinjau tidak tertulis di TC dan disediakan tim FE/BE (S-13). Intercept dilepas segera setelah pemicu selesai (langkah 25).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`):

| TC | Class (Class Code bersuffix) | Used By | Keterangan |
|---|---|---|---|
| TC-251, 252, 254, 255 | `KHS-V9-{runId}-071` | 3 | Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, satu versi; Asset Class pemakai `AC-DB1`, `AC-DB2`, `AC-SL1` dengan total 18 aset aktif (disediakan tim FE/BE) |

- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `KHS-V9-{runId}-071`, tekan Enter
2. Klik link Class Code `KHS-V9-{runId}-071` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`

### TC-FA-TDC-251: Klik jumlah Asset Class membuka daftar bullet inline lalu klik lagi menutupnya

5. Klik angka `3` pada baris `Asset classes affected`
6. Verifikasi daftar read-only terbuka di dalam dialog yang sama berisi tiga bullet `• [Class Code] – [Class Name]` untuk `AC-DB1`, `AC-DB2`, dan `AC-SL1`
7. Verifikasi dialog Save Changes tidak tertutup
8. Verifikasi nilai Effective From tidak berubah (`Jan 2026`)
9. Klik angka `3` lagi pada baris `Asset classes affected`
10. Verifikasi daftar bullet tertutup
11. Verifikasi Effective From tetap `Jan 2026`
12. Verifikasi dialog Save Changes tetap terbuka

### TC-FA-TDC-252: Angka penyusutan bernilai `-` bila mesin kalkulasi belum tersedia

13. Verifikasi baris `Fiscal depreciation, tax year 2026` bernilai `-`
14. Verifikasi baris `Fiscal book value at year end` bernilai `-`
15. Verifikasi baris `Asset classes affected` tetap menampilkan jumlah `3`
16. Verifikasi tombol `[Apply]` enabled

### TC-FA-TDC-254: Pratinjau dihitung ulang saat Effective From berubah

17. Pilih Effective From `Jan 2028`
18. Verifikasi label baris angka berubah menjadi `Fiscal depreciation, tax year 2028`
19. Verifikasi jumlah `Asset classes affected` tetap `3`
20. Verifikasi jumlah `Active assets affected` tetap `18`

### TC-FA-TDC-255: Blok pratinjau menampilkan Shimmer dan Apply Disabled selama dihitung ulang

21. Tahan respons endpoint pratinjau selama 3 detik (intercept jaringan)
22. Pilih Effective From `Jan 2027`
23. Verifikasi blok pratinjau menampilkan Loading component (Shimmer) selama dihitung ulang
24. Verifikasi tombol `[Apply]` tampil tetapi Disabled selama dihitung ulang
25. Lepas tahanan respons endpoint pratinjau dan tunggu penghitungan selesai
26. Verifikasi tombol `[Apply]` enabled kembali setelah penghitungan selesai
27. Klik `[Cancel]` pada dialog Save Changes
28. Klik `[×]` pada Drawer Edit
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 21 dan 25 (menahan dan melepas respons endpoint pratinjau; pemicu untuk TC-255), langkah 27 sampai 30 (menutup dialog dan Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- Keempat TC memakai satu class dan satu sesi dialog Save Changes yang dibuka pada langkah 2 sampai 4 (langkah 1 sampai 3 tiap TC identik dengan keadaan yang sudah terbentuk). Urutan TC: 251, 252, 254, 255, karena TC-254 dan TC-255 mengubah pilihan Effective From.
- Asersi state sementara (Shimmer, Disabled) pada langkah 23 dan 24 ditulis sebelum respons dilepas (8b.5); langkah 26 memuat anchor bahwa penghitungan sudah selesai.
- Temuan untuk QA:
  - TC-252 mensyaratkan mesin kalkulasi belum tersedia atau mengembalikan error, sedangkan TC-254 dan TC-255 tidak menyebut kondisi mesin; spec menjalankan keempatnya pada kondisi mesin yang sama (belum tersedia) dan hanya mengasersi label dan jumlah pada TC-254, sehingga tidak bergantung pada nilai angka.
  - TC-251 menyebut Class Name pada bullet `• [Class Code] – [Class Name]` tetapi tidak memberi nama Asset Class pemakai; spec mengasersi Class Code `AC-DB1`, `AC-DB2`, `AC-SL1` saja.
  - TC-255 tidak menyebut endpoint pratinjau yang ditunda; disediakan tim FE/BE.
  - Kode class milik spec bersuffix `{runId}-071` (S-12); batas panjang Class Code tidak tertulis di TC.
