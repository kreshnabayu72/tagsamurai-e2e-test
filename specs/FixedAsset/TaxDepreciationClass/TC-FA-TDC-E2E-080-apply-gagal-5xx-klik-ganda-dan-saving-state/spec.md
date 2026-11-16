---
id: TC-FA-TDC-E2E-080-apply-gagal-5xx-klik-ganda-dan-saving-state
title: "Apply D-09: Gagal 5xx Mempertahankan Input, Klik Ganda Hanya Membentuk Satu Versi, dan Tombol Apply Masuk Saving State"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-279
  - TC-FA-TDC-280
  - TC-FA-TDC-281
sourceRules: ["T-02d", "R-02", "§7.3#b1", "ST-13", "T-02c", "§4.1.6#r5"]
smoke: []
dependsOn: []
trace:
  "T-02d": 8
  "R-02": [9, 15, 18]
  "§7.3#b1": 10
  "ST-13": [11, 26, 27, 28, 29]
  "T-02c": 15
  "§4.1.6#r5": 18
coverage:
  web: automated
---

# Apply D-09: Gagal 5xx Mempertahankan Input, Klik Ganda Hanya Membentuk Satu Versi, dan Tombol Apply Masuk Saving State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Kemampuan intercept jaringan (`Spectra.intercept()`) di atas backend nyata (Mode FE+BE karena asersi memuat state server) untuk (1) mengembalikan 500 pada endpoint apply versi (TC-279) dan (2) menunda respons endpoint apply versi 3 detik (TC-281); nama endpoint apply versi tidak tertulis di TC dan disediakan tim FE/BE (S-13). Intercept dilepas segera setelah pemicu selesai (langkah 12 dan 30).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, Used By 0, satu versi Current tanpa Effective From, tanpa versi Scheduled):

| TC | Class (Class Code bersuffix) | Keterangan |
|---|---|---|
| TC-279, 280 | `KHS-V1-{runId}-080` | TC-279 gagal sehingga class tidak berubah; TC-280 melanjutkan class yang sama |
| TC-281 | `KHS-V1B-{runId}-080` | Apply berhasil setelah tahanan respons dilepas, sehingga memakai class sendiri |

- Pencarian baris target memakai kata kunci `{runId}-080` yang menampilkan kedua class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-080`, tekan Enter
2. Klik link Class Code `KHS-V1-{runId}-080` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Pilih Effective From `Jan 2027`

### TC-FA-TDC-279: Apply gagal 5xx

6. Atur endpoint apply versi mengembalikan 500 (intercept jaringan)
7. Klik `[Apply]`
8. Verifikasi toast error `Error, failed to update tax depreciation class.`
9. Verifikasi dialog Save Changes tetap terbuka
10. Verifikasi Effective From `Jan 2027` dipertahankan pada dialog Save Changes
11. Verifikasi tombol `[Apply]` enabled kembali
12. Lepas intercept endpoint apply versi
13. Dismiss toast error

### TC-FA-TDC-280: Klik ganda cepat pada Apply hanya membentuk satu versi

14. Klik `[Apply]` dua kali dengan cepat
15. Verifikasi satu toast sukses `Success, tax depreciation class has been updated.`
16. Klik link Class Code `KHS-V1-{runId}-080` pada tabel
17. Klik tautan View versions
18. Verifikasi modal Versions memuat tepat satu versi `Jan 2027` berstatus `Scheduled`
19. Tutup modal Versions
20. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-281: Tombol Apply masuk Saving state saat request berjalan

21. Klik link Class Code `KHS-V1B-{runId}-080` pada tabel
22. Ganti Useful Life menjadi `10`
23. Klik `[Save]`
24. Tahan respons endpoint apply versi selama 3 detik (intercept jaringan)
25. Klik `[Apply]`
26. Verifikasi tombol `[Apply]` menampilkan spinner
27. Verifikasi tombol `[Apply]` tidak dapat diklik
28. Verifikasi tombol `[Cancel]` tidak interaktif selama request
29. Verifikasi Select Effective From tidak interaktif selama request
30. Lepas tahanan respons endpoint apply versi
31. Tunggu aksi selesai (dialog Save Changes dan Drawer Edit tertutup)

## Notes

- P-5 butir (b): TC-279 adalah satu TC kelas b (kegagalan 5xx dipaksa lewat intercept) yang ringan, tanpa harness eksternal dan tanpa state berat, pada permukaan yang sama (Apply D-09) dengan TC-280 dan TC-281; ini satu-satunya TC kelas b di spec ini.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 12 (melepas intercept segera setelah pemicu; S-09), langkah 13 (R-12: toast error TC-279 persisten, jadi di-dismiss sebelum hitungan "satu toast sukses" langkah 15), langkah 16 dan 17 (membuka Drawer Edit dan tautan View versions untuk mengamati modal Versions), langkah 19 dan 20 (menutup modal Versions dan Drawer Edit yang tidak dirty), langkah 31 (menunggu aksi yang hasilnya tidak diasersi; 8b.8).
- TC-279 dan TC-280 memakai satu class dan satu sesi dialog Save Changes yang dibuka pada langkah 2 sampai 5; langkah 1 sampai 4 TC-280 identik dengan keadaan yang tersisa sesudah TC-279 gagal (dialog terbuka dengan Effective From `Jan 2027`, intercept sudah dilepas). Urutan TC: 279, 280, 281.
- Asersi state sementara pada langkah 26 sampai 29 ditulis sebelum respons dilepas (8b.5).
- Temuan untuk QA:
  - TC-279 Post Condition ("tidak ada versi baru", "tidak ada entri log") tidak punya langkah observasi di TC dan tidak diasersi (S-01); keberhasilan TC-280 pada class yang sama (hanya satu versi `Jan 2027`) mengamati sebagian.
  - TC-281 tidak menyebut Effective From yang dipilih; Apply memakai nilai awal.
  - TC-281 Expected b menyebut "Select Effective From tidak interaktif" tetapi tidak menyebut cara mengamati status itu (Disabled atau atribut lain); disediakan tim FE.
  - TC-279 dan TC-281 tidak menyebut endpoint yang di-intercept; disediakan tim FE/BE.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-080` (S-12); batas panjang Class Code tidak tertulis di TC.
