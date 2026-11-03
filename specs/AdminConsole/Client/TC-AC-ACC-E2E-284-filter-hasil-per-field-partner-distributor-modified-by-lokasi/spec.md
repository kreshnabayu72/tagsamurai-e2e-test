---
id: TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi
title: "Filter Client List: Hasil Filter per Field Partner, Distributor, Modified By, Industry, Country, State, dan City"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-376
  - TC-AC-ACC-377
  - TC-AC-ACC-381
  - TC-AC-ACC-383
  - TC-AC-ACC-384
  - TC-AC-ACC-385
  - TC-AC-ACC-386
coverage:
  web: automated
---

# Filter Client List: Hasil Filter per Field Partner, Distributor, Modified By, Industry, Country, State, dan City

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya. Dipakai langkah: C-12 `PT Timur Perkasa` (Partner `CV Mitra Timur`, jaringan Distributor `PT Distribusi Timur`) dan C-10 `PT Lintas Jaringan` (jaringan `PT Distribusi Timur`) untuk Filter Partner dan Distributor; C-01 `PT Sejahtera Abadi` (Partner `CV Mitra Sejati`) sebagai baris yang tidak cocok.
- Fixture residen Tabel A3 C-LST-1 sampai C-LST-3 tersedia dan hanya dibaca (precondition d TC-AC-ACC-381, 383, 384, 385, 386): C-LST-1 `PT Sortir Alfa` (Industry `Healthcare`; Country / State / City `Malaysia` / `Selangor` / `Shah Alam`; Modified By `Citra Santoso`); C-LST-2 `PT Sortir Beta` (Industry `Retail`; `Indonesia` / `Jawa Barat` / `Bandung`; Modified By `Andi Wijaya`); C-LST-3 `PT Sortir Gamma` (Industry `Manufacturing`; `Singapore` / `Central Region` / `Singapore`; Modified By `Citra Sanjaya`).
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Tabel parameter A (dipakai langkah 2 sampai 12; TC-AC-ACC-376 dan 377): kolom Field / Placeholder / Opsi yang dimuat / Nilai dipilih / Search tampil (baris tampil) / Search kosong (Empty state `No results found`):
  - Partner / `All partners` / `CV Mitra Sejati`, `CV Mitra Lestari`, `CV Mitra Timur` / `CV Mitra Timur` / `PT Timur Perkasa` / `PT Sejahtera Abadi`.
  - Distributor / `All distributors` / `PT Distribusi Nusantara`, `PT Distribusi Timur` / `PT Distribusi Timur` / `PT Timur Perkasa` / `PT Sejahtera Abadi`.
- Tabel parameter B (dipakai langkah 13 sampai 22; TC-AC-ACC-381, 383, 384, 385, 386; Search selalu `Sortir`): kolom Field / Placeholder / Opsi yang dimuat / Nilai dipilih / Baris tampil / Baris tidak tampil:
  - Modified By / `All users` / `Citra Santoso`, `Andi Wijaya`, `Citra Sanjaya` / `Andi Wijaya` / `PT Sortir Beta` / `PT Sortir Alfa` dan `PT Sortir Gamma`.
  - Industry / `All industries` / `Healthcare`, `Retail`, `Manufacturing`, `Telecommunications` / `Healthcare` / `PT Sortir Alfa` / `PT Sortir Beta`.
  - Country / `All countries` / `Malaysia`, `Indonesia`, `Singapore` / `Malaysia` / `PT Sortir Alfa` / `PT Sortir Beta` dan `PT Sortir Gamma`.
  - State / `All states` / `Selangor`, `Jawa Barat`, `Central Region` / `Selangor` / `PT Sortir Alfa` / `PT Sortir Beta` dan `PT Sortir Gamma`.
  - City / `All cities` / `Shah Alam`, `Bandung`, `Singapore` / `Shah Alam` / `PT Sortir Alfa` / `PT Sortir Beta` dan `PT Sortir Gamma`.
- Ukuran halaman diubah menjadi 100 baris di awal spec agar semua baris Pre-setup berada pada satu halaman. Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Hasil filter Partner dan Distributor (TC-AC-ACC-376, 377)

1. Ubah ukuran halaman menjadi 100 baris, lalu catat angka badge sub-tab Active (baseline)
2. Untuk setiap baris tabel parameter A: klik Filter dan lihat placeholder field itu
3. Verifikasi placeholder field sesuai kolom Placeholder
4. Klik field itu untuk membuka dropdown opsi
5. Verifikasi opsi dropdown memuat nilai pada kolom Opsi yang dimuat
6. Pilih nilai pada kolom Nilai dipilih, lalu klik [Apply]
7. Ketik Search nilai pada kolom Search tampil, tekan Enter
8. Verifikasi baris pada kolom Search tampil muncul di tabel
9. Ganti isi Search dengan nilai pada kolom Search kosong, tekan Enter
10. Verifikasi Empty state `No results found`
11. Verifikasi angka badge sub-tab Active sama dengan baseline (badge jumlah sub-tab tidak berubah)
12. Klik `(←)` pada kotak Search, klik Filter, klik [Clear Field], lalu klik [Apply]

### Hasil filter Modified By, Industry, Country, State, dan City (TC-AC-ACC-381, 383, 384, 385, 386)

13. Untuk setiap baris tabel parameter B: klik Filter dan lihat placeholder field itu
14. Verifikasi placeholder field sesuai kolom Placeholder
15. Klik field itu untuk membuka dropdown opsi
16. Verifikasi opsi dropdown memuat nilai pada kolom Opsi yang dimuat
17. Pilih nilai pada kolom Nilai dipilih, lalu klik [Apply]
18. Ketik Search `Sortir`, tekan Enter
19. Verifikasi baris pada kolom Baris tampil muncul di tabel
20. Verifikasi baris pada kolom Baris tidak tampil tidak muncul di tabel
21. Verifikasi angka badge sub-tab Active sama dengan baseline (badge jumlah sub-tab tidak berubah)
22. Klik `(←)` pada kotak Search, klik Filter, klik [Clear Field], lalu klik [Apply]

## Notes

- Langkah 2 sampai 12 diulang per baris tabel parameter A (2 iterasi) dan langkah 13 sampai 22 per baris tabel parameter B (5 iterasi). Spec melewati sekitar 35 langkah setelah ekspansi (sekitar 73 langkah); alasan: semua blok satu kelas harness dan satu dataset (Filter Panel List), blok tidak saling bergantung, dan kegagalan satu field tidak membuat field lain kehilangan makna.
- Langkah penghubung (S-03): langkah 12 dan 22 (`(←)` pada kotak Search, [Clear Field], dan [Apply] di akhir tiap iterasi, S-09 dan bagian 8b butir 9). Pembanding `baris tampil` ditulis sebelum `Empty state` atau `baris tidak tampil` sebagai anchor absence (bagian 8b butir 2).
- Klausa `Tabel hanya menampilkan Client yang cocok` pada Expected a TC-AC-ACC-376 sampai 386 diasersi lewat baris tampil dan baris tidak tampil atau Empty state yang disebut TC pada setiap field; pada field yang TC tulis dengan kata `hanya` (TC-AC-ACC-381, 384, 385, 386), baris lain di luar yang tampil dicek tidak muncul.
