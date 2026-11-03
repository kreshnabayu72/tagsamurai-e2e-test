---
id: TC-FA-CF-E2E-174-filter-chip-opsi-terpilih-diringkas-menjadi-n-more
title: "Filter: Chip Opsi Terpilih Diringkas Menjadi +N more"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-671
coverage:
  web: automated
---

# Filter: Chip Opsi Terpilih Diringkas Menjadi +N more

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena opsi Data Type dihitung dari baseline; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12) delapan field dengan enam Data Type: `Document`, `Dropdown`, `Formula`, `Numeric`, `Percentage`, `Text`.
- Data Dinamis milik spec (di-seed lewat API oleh akun Total Control Company Alpha di hook `before`, mekanisme disediakan tim FE/BE dan endpoint tidak ditulis di spec; fixture baru belum ada, `Fixture.faCustomFields.chipSeed174`): delapan field tab General Active, Scope kosong (agar tidak menambah hitungan cap per Asset Name), Placeholder dikosongkan, satu per Data Type yang belum ada di baseline, nama bersuffix per run: `Seed Text Area {runId}-174` (Text Area), `Seed Multi {runId}-174` (Multi-Dropdown, opsi `Charger` dan `Cable`), `Seed Date {runId}-174` (Date), `Seed DateTime {runId}-174` (DateTime), `Seed Currency {runId}-174` (Currency), `Seed Phone {runId}-174` (Phone), `Seed Email {runId}-174` (Email), dan `Seed URL {runId}-174` (URL). Dengan baseline, dropdown Data Type memuat 14 opsi (Pre-setup TC menyebut "seluruh 14 opsi Data Type"): `Currency`, `Date`, `DateTime`, `Document`, `Dropdown`, `Email`, `Formula`, `Multi-Dropdown`, `Numeric`, `Percentage`, `Phone`, `Text`, `Text Area`, `URL`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedelapan field `Seed ... {runId}-174`.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan jumlah chip yang tampil dan angka `N` pada chip `+N more`, serta lebar field Data Type terhadap lebar Filter Panel dan ada tidaknya gulir horizontal.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-671: Chip opsi terpilih yang melebihi lebar field filter Data Type diringkas menjadi `+N more`

1. Klik ikon Filter
2. Buka dropdown Data Type
3. Verifikasi dropdown Data Type memuat 14 opsi
4. Pilih seluruh 14 opsi Data Type (centang satu per satu sesuai daftar pada `## Prerequisites`)
5. Tutup dropdown Data Type
6. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field dan sisanya diringkas dalam satu chip `+N more`
7. Verifikasi jumlah chip tampil ditambah N sama dengan 14
8. Verifikasi field Data Type tidak melebar keluar panel Filter
9. Verifikasi field Data Type tidak digulir horizontal
10. Klik `✕` pada satu chip yang tampil
11. Verifikasi jumlah chip tampil ditambah N sama dengan 13

## Notes

- Spec memuat 11 langkah, di bawah ambang sekitar 35 langkah. Spec berdiri sendiri karena memerlukan dataset khusus (14 Data Type pada satu tab) yang tidak dimiliki baseline Company Alpha dan tidak boleh mengubah tabel yang dipakai spec Filter lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (menutup dropdown agar field Data Type teramati dalam keadaan tertutup, sesuai langkah TC "Perhatikan field Data Type dalam keadaan tertutup").
- Langkah 3 adalah `Verifikasi` tambahan di luar Expected TC (S-03): pembuktian bahwa dropdown memuat 14 opsi, yaitu precondition "Seluruh 14 opsi Data Type" pada Data Uji TC, supaya `N` pada langkah 7 dan 11 bermakna.
- Temuan untuk QA:
  - TC-FA-CF-671 Data Uji menyebut "seluruh 14 opsi Data Type" pada tab General, tetapi baseline Company Alpha (Pre-setup #12) hanya memiliki enam Data Type, dan TC-FA-CF-375 menetapkan opsi dropdown diambil dari tabel tab aktif. Pre-setup #35 (14 field `Sample Item`) berada di tab Purchasing dan dipakai untuk Create. Spec menambah delapan field Dinamis agar 14 Data Type ada pada tab General; Pre-setup TC perlu menyatakan dataset ini.
  - TC-FA-CF-671 tidak menyebut jumlah chip yang muat; spec mengasersi hubungan "jumlah chip tampil ditambah N" saja.
  - TC-FA-CF-671 tidak menyebut cara memeriksa "tidak melebar keluar panel" dan "tidak digulir horizontal"; keduanya dibaca lewat Page Object dan dipecah satu `Verifikasi` per klausa (langkah 8 dan 9).
  - TC-FA-CF-671 tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
