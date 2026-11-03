---
id: TC-AC-CS-E2E-034-payment-preview-estimated-cost-dan-saldo-kantong
title: "Payment Preview: Estimated Cost dan Saldo Kantong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-132
  - TC-AC-CS-133
  - TC-AC-CS-134
  - TC-AC-CS-136
  - TC-AC-CS-135
coverage:
  web: automated
---

# Payment Preview: Estimated Cost dan Saldo Kantong

## Prerequisites

- Mode: FE+BE (`Spectra.intercept()` parsial pada endpoint perhitungan biaya untuk TC-AC-CS-133; endpoint tidak dinamai TC dan ditentukan tim FE).
- Akun aktor pertama: Total Control Distributor PT Maju Bersama (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-034` (padanan Pre-setup #48: tanpa term dan tanpa trial). Tidak ada Submit sukses pada spec ini.
- State global yang diubah (suite serial) dan pemulihannya di hook `after` lewat fixture BE (disediakan tim FE/BE): saldo `Main Pocket` PT Maju Bersama $25,000.00 (Pre-setup #20) dikurangi hingga $5,000.00 pada TC-AC-CS-135; harga feature `Custom Report Builder` plan `Professional` dikosongkan pada TC-AC-CS-136 (harga acuan Pre-setup #27: FAMS Professional $10,000.00 per tahun, FAMS Enterprise $18,000.00 per tahun) lalu dipulihkan.
- Kemampuan teknis (disediakan tim FE/BE): membaca saldo `Main Pocket`, jumlah term Client seed, dan Reserve Wallet lewat fixture BE; menahan dan melepas respons endpoint perhitungan biaya.

## Test Steps

### TC-AC-CS-132: Preview Payment menghitung Estimated Cost dan menampilkan saldo kantong

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription+{runId}-034`, Product `FAMS`, Plan `Professional`, isi Duration `2`
3. Verifikasi tampil "Estimated Cost: $20,000.00 (2 year(s) × $10,000.00/year)" mengikuti template "Estimated Cost: $[X,XXX.XX] ([N] year(s) × $[annual_price]/year)"
4. Verifikasi tampil "Your pocket balance: $25,000.00" mengikuti template "Your pocket balance: $[Y,YYY.YY]"
5. Verifikasi tidak ada Alert Danger saldo

### TC-AC-CS-133: Estimated Cost dan Pocket Balance memakai Shimmer saat dihitung

6. Klik `[Clear Field]`
7. Tahan respons endpoint perhitungan biaya
8. Pilih Client `Client Tanpa Subscription+{runId}-034`, Product `FAMS`, Plan `Professional`, isi Duration `2`
9. Verifikasi baris Estimated Cost dan Pocket Balance menampilkan Shimmer (Form Controls) selama perhitungan
10. Lepas tahanan respons endpoint perhitungan biaya
11. Verifikasi nilai biaya dan saldo menggantikan Shimmer

### TC-AC-CS-134: Saldo kantong kurang dari Estimated Cost memblokir Submit secara real-time

12. Klik `[Clear Field]`
13. Pilih Client `Client Tanpa Subscription+{runId}-034`, Product `FAMS`, Plan `Enterprise`, isi Duration `2`
14. Verifikasi Alert Danger "Insufficient balance in your pocket. Available: $25,000.00. Required: $36,000.00." tampil mengikuti template "Insufficient balance in your pocket. Available: $[Y,YYY.YY]. Required: $[X,XXX.XX]." tepat setelah preview dimuat
15. Verifikasi tombol `[Submit]` diblok
16. Verifikasi tidak ada Reserve pada Wallet (saldo `Main Pocket` tetap $25,000.00, dibaca lewat fixture BE)

### TC-AC-CS-136: Harga feature belum di-set menampilkan tooltip dan memblokir Submit

17. Klik `[Clear Field]`
18. Kosongkan harga feature `Custom Report Builder` untuk plan `Professional` lewat fixture BE
19. Pilih Client `Client Tanpa Subscription+{runId}-034`, Product `FAMS`, Plan `Professional`, isi Duration `1`
20. Arahkan kursor ke indikator harga pada blok Payment
21. Verifikasi tooltip "Price not set for Custom Report Builder. Please configure feature pricing first." tampil mengikuti template "Price not set for [Feature Name]. Please configure feature pricing first."
22. Verifikasi tombol `[Submit]` diblok
23. Verifikasi tidak ada Reserve pada Wallet (saldo `Main Pocket` tetap $25,000.00, dibaca lewat fixture BE)
24. Pulihkan harga feature `Custom Report Builder` untuk plan `Professional` lewat fixture BE

### TC-AC-CS-135: Saldo berkurang setelah preview dimuat ditolak server saat Submit

25. Klik `[Clear Field]`
26. Pilih Client `Client Tanpa Subscription+{runId}-034`, Product `FAMS`, Plan `Professional`, isi Duration `1` dan Start Date `19/08/26`
27. Kurangi saldo `Main Pocket` hingga $5,000.00 lewat fixture BE hingga saldo tersimpan
28. Klik `[Submit]`
29. Verifikasi pesan penolakan "Insufficient wallet balance" tampil
30. Verifikasi term Client `Client Tanpa Subscription+{runId}-034` tidak masuk Waiting for Approval (jumlah term tetap 0, dibaca lewat fixture BE)
31. Verifikasi saldo `Main Pocket` tetap $5,000.00 tanpa Reserve (dibaca lewat fixture BE)
32. Verifikasi modal tetap terbuka dengan input dipertahankan
33. Pulihkan saldo `Main Pocket` ke $25,000.00 lewat fixture BE, lalu klik `[✕]` pada header modal
34. Verifikasi dialog Unsaved Changes tampil
35. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular; urutan TC-AC-CS-136 sebelum TC-AC-CS-135 agar perubahan saldo (state global) berada di akhir (S-10).
- Langkah penghubung (S-03): `[Clear Field]` antar kasus (langkah 6, 12, 17, 25), pasang dan lepas tahanan respons (langkah 7, 10), pemulihan harga dan saldo lewat fixture BE (langkah 24, 33; juga di hook `after`), serta penutupan form dirty (langkah 33 sampai 35, S-08).
- Penahanan respons pada langkah 7 sampai 10 hanya untuk mengamati state Shimmer (bukan kelas b, boleh di spec fungsional); tahanan dilepas segera (S-09) sebelum asersi hasil.
- Langkah 28 memicu server memeriksa saldo (TC-AC-CS-135 Langkah 3 menyebut "server memeriksa saldo"); pembacaan saldo lewat fixture BE hanya untuk Expected b (S-11).
- Langkah 35 nominal; spec berada pada ukuran sekitar 35 langkah dengan satu kelas (fungsional Payment Preview), satu Client seed, dan satu form yang dipakai berulang.
- Temuan untuk QA:
  - TC-AC-CS-136 Precondition menyebut harga feature `Custom Report Builder` belum di-set di Plans & Features tanpa Pre-setup; spec memakai fixture BE untuk mengosongkan dan memulihkannya.
  - TC-AC-CS-135 Expected a tidak menyatakan apakah pesan "Insufficient wallet balance" berupa toast atau inline; spec mengasersi keberadaan teksnya.
  - TC-AC-CS-136 Langkah 3 menyebut "indikator harga pada blok Payment" tanpa menamai elemen; ditulis apa adanya.
