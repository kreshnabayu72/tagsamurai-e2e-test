---
id: TC-FA-FAAM-E2E-123-sort-kelas-badge-addon-dan-total-asset
title: "Sort: Kelas Brand, Model/Type, Default Label, Default Addon, dan Total Asset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-392
  - TC-FA-FAAM-393
  - TC-FA-FAAM-394
coverage:
  web: automated
---

# Sort: Kelas Brand, Model/Type, Default Label, Default Addon, dan Total Asset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Total Asset enam Asset Name contoh: 0, 3, 8, 15, 42, 120 (Pre-setup #10 sampai #14).
- Kolom yang diuji untuk TC-FA-FAAM-392 (diulang pada langkah 1 sampai 8):

  | Kolom |
  |---|
  | Brand |
  | Model/Type |
  | Default Label |
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-392: Sort kelas Brand, Model/Type, Default Label (kolom +N more): siklus tiga state
1. Untuk setiap baris tabel "Kolom yang diuji", klik header kolom tersebut satu kali
2. Verifikasi klik 1 Ascending: jumlah nilai paling sedikit dulu
3. Verifikasi klik 1 Ascending: jumlah sama dengan tiebreaker nilai pertama A-Z
4. Klik header kolom yang sama kedua kali
5. Verifikasi klik 2 Descending: jumlah nilai terbanyak dulu
6. Verifikasi klik 2 Descending: tiebreaker nilai pertama Z-A
7. Klik header kolom yang sama ketiga kali
8. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z
### TC-FA-FAAM-393: Sort kelas Default Addon (urutan enum tetap): siklus tiga state
9. Klik header kolom Default Addon satu kali
10. Verifikasi klik 1 Ascending: jumlah addon paling sedikit dulu
11. Verifikasi klik 1 Ascending: tiebreaker nilai pertama menurut urutan enum tetap (`Audit`, `Maintenance`, `Tracking`, `Maps`)
12. Klik header kolom Default Addon kedua kali
13. Verifikasi klik 2 Descending: jumlah addon terbanyak dulu
14. Klik header kolom Default Addon ketiga kali
15. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z
### TC-FA-FAAM-394: Sort kelas Total Asset (numerik): siklus tiga state
16. Klik header kolom Total Asset satu kali
17. Verifikasi klik 1 Ascending: numerik natural 0, 3, 8, 15, 42, 120 (bukan urutan teks)
18. Klik header kolom Total Asset kedua kali
19. Verifikasi klik 2 Descending: 120, 42, 15, 8, 3, 0
20. Klik header kolom Total Asset ketiga kali
21. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z

## Notes

- Langkah yang diulang per kolom pada TC-FA-FAAM-392: langkah 1 sampai 8; parameter tiap iterasi ada di tabel "Kolom yang diuji" pada Prerequisites. Verifikasi diulang satu per klausa (bagian 8b butir 7). Ekspansi: 3 kolom x 7 langkah = 21 langkah; jumlah langkah spec setelah ekspansi 35.
- Tiap blok diakhiri klik ketiga yang mengembalikan sort ke netral (S-09).
- Urutan numerik pada TC-FA-FAAM-394 mengasersi enam baris fixture bernama; baris `Seed Item` (Total Asset 0) tidak diasersi posisinya.
- Temuan untuk QA: Total Asset 3 pada urutan TC-FA-FAAM-394 berasal dari Asset Name keenam yang tidak diberi nama di Pre-setup.
