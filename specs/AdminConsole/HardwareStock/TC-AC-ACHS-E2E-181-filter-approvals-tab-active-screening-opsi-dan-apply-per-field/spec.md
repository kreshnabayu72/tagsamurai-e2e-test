---
id: TC-AC-ACHS-E2E-181-filter-approvals-tab-active-screening-opsi-dan-apply-per-field
title: "Filter Approvals Tab Active Screening Opsi dan Apply per Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-376
  - TC-AC-ACHS-377
  - TC-AC-ACHS-378
  - TC-AC-ACHS-379
coverage:
  web: automated
---

# Filter Approvals Tab Active Screening Opsi dan Apply per Field

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Baris dirujuk lewat nomor baris Tabel C: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel C (`Fixture.hardwareStock.p21.c[n]`). Urutan default FIFO (Requested At terlama di atas) sama dengan urutan Tabel C (#1 teratas, #12 terbawah). Nilai sel tidak ditulis di spec ini; penulis script membaca nilainya dari fixture lewat kunci pada tabel Parameter Pre-setup (R-06).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #21 Tabel C | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #3, #9, #12 berformat MAC | `Fixture.hardwareStock.p21.c[n].matchedIdentifier` |
  | Device Name (SKU) baris #n (n = 1 sampai 12) | #21 Tabel C | Device Name diikuti kode SKU dalam kurung; #9 adalah Subject BYO tanpa SKU (Device Name (SKU) tanpa kode SKU, Category `—`) | `Fixture.hardwareStock.p21.c[n].deviceName` |
  | Requested By baris #n (n = 1 sampai 12) | #21 Tabel C | Client, Distributor, atau Principal (Pre-setup #23) dengan label peran dalam kurung; Distributor pada #3, #6, #8, #10 | `Fixture.hardwareStock.p21.c[n].requestedBy` |
  | Requested At baris #n (n = 1 sampai 12) | #21 Tabel C | naik menurut n (FIFO); bulan dan tahun sama pada seluruh baris | `Fixture.hardwareStock.p21.c[n].requestedAt` |
  | Keyword pencarian internal dropdown Requested By | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[12].requestedBy`: tiga huruf pertama dalam huruf kecil; hanya opsi #12 yang memuatnya | `Fixture.hardwareStock.derived.requestedByPrefixLower` |
- Opsi dropdown Filter (dipakai langkah 16; nilai opsi Pre-setup dirujuk lewat nomor baris Tabel C, urut sesuai urutan opsi di dropdown): Type (All types): `Activation Collision`, `Register Duplicate` (2 opsi); Device Name (SKU) (All device names): nilai `Fixture.hardwareStock.p21.c[n].deviceName` distinct untuk n = 12, 4, 9, 2, 1, 6 (6 opsi, urutan itu); Category (All categories): `BLE Gateway`, `Handheld Reader - Long Range`, `Handheld Reader - Short Range`, `Smart Fixed Reader` (4 opsi); Requested By (All requesters): nilai `Fixture.hardwareStock.p21.c[n].requestedBy` distinct untuk n = 12, 1, 4, 2, 3, 8, 5, 10, 9 (9 opsi, urutan itu).
- Parameter Apply per field (dipakai langkah 24 sampai 28 dan 30 sampai 34; baris hasil dirujuk lewat nomor baris Tabel C):

| Field | Nilai | Hasil |
|---|---|---|
| Type | `Activation Collision` | 6 baris: #1, #4, #5, #9, #11, #12 |
| Device Name (SKU) | `Fixture.hardwareStock.p21.c[9].deviceName` | 1 baris: #9 |
| Category | `BLE Gateway` | 1 baris: #12 |
| Requested By | `Fixture.hardwareStock.p21.c[3].requestedBy` (Distributor) | 2 baris: #3, #6 |
| Requested At | rentang tanggal dari tanggal `Fixture.hardwareStock.p21.c[4].requestedAt` sampai tanggal `Fixture.hardwareStock.p21.c[8].requestedAt` | 5 baris: #4, #5, #6, #7, #8 |

- Pilihan spec (bukan nilai TC): pencarian internal dropdown memakai keyword huruf kecil `Fixture.hardwareStock.derived.requestedByPrefixLower` (3 huruf pertama opsi Requested By baris #12, dikecilkan untuk menguji case-insensitive; lihat tabel Parameter Pre-setup) dan keyword tanpa kecocokan `zzqx`, pada dropdown Requested By.

## Test Steps

### Screening Filter Panel (TC-AC-ACHS-376)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Hover icon Filter
4. Verifikasi tooltip `Filter`
5. Klik icon Filter
6. Verifikasi ikon Filter menjadi gelap saat panel terbuka
7. Verifikasi field pertama Type: multi-select searchable, placeholder `All types`
8. Verifikasi field kedua Device Name (SKU): multi-select searchable, placeholder `All device names`
9. Verifikasi field ketiga Category: multi-select searchable, placeholder `All categories`
10. Verifikasi field keempat Requested By: multi-select searchable, placeholder `All requesters`
11. Verifikasi field kelima Requested At: date range picker, placeholder `Select date`
12. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
13. Verifikasi tidak ada field Photo atau identifier teks di Filter Panel

### Screening isi opsi dropdown (TC-AC-ACHS-377)

14. Untuk setiap field Type, Device Name (SKU), Category, Requested By (langkah 15 sampai 17): lakukan langkah berikut
15. Buka dropdown field
16. Verifikasi daftar opsi sesuai "Opsi dropdown Filter" di Prerequisites
17. Verifikasi kotak pencarian internal ada di dropdown
18. Ketik di kotak pencarian internal dropdown Requested By keyword `Fixture.hardwareStock.derived.requestedByPrefixLower`
19. Verifikasi daftar opsi menyempit menjadi satu opsi: nilai Requested By baris #12 (substring, case-insensitive)
20. Ganti isi kotak pencarian internal dengan `zzqx`
21. Verifikasi teks `No results found` di daftar opsi
22. Tutup dropdown

### Apply per field kelas multi (TC-AC-ACHS-378)

23. Untuk setiap baris Type, Device Name (SKU), Category, Requested By pada tabel parameter (langkah 24 sampai 28): lakukan langkah berikut
24. Isi field dengan nilai pada tabel parameter, klik `[Apply]`
25. Verifikasi tabel menampilkan hasil sesuai tabel parameter
26. Klik `[Clear Field]`
27. Klik `[Apply]`
28. Verifikasi tabel kembali menampilkan seluruh 12 baris

### Apply per field kelas date (TC-AC-ACHS-379)

29. Untuk setiap baris Requested At pada tabel parameter (langkah 30 sampai 34): lakukan langkah berikut
30. Isi field dengan rentang tanggal pada tabel parameter (Start dan End berbeda), klik `[Apply]`
31. Verifikasi tabel menampilkan hasil sesuai tabel parameter
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Verifikasi tabel kembali menampilkan seluruh 12 baris

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-376 sampai 379). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Langkah penghubung (bukan dari langkah TC): langkah 22 (tutup dropdown); langkah 2 (klik Tab `Active` untuk "Pastikan Tab Active aktif"). Filter Panel tetap terbuka dari langkah 5 sampai akhir spec karena TC-378 dan TC-379 melanjutkan di panel yang sama.
- Idiom ulang "Untuk setiap ..." pada langkah 14 sampai 17, 23 sampai 28, 29 sampai 34; parameter di Prerequisites; tiap iterasi memuat `Verifikasi` per klausa.
- Spec 34 langkah nominal dengan ekspansi sekitar 70: semua blok satu surface (Filter Panel Approvals Tab Active) dan satu dataset read-only; tiap blok memulihkan Filter dengan `[Clear Field]` + `[Apply]` sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; topik satu dataset tetap satu spec (prinsip 1).
- Konfirmasi (#8): `Fixture.hardwareStock.derived.requestedByPrefixLower` diturunkan dari tiga huruf pertama opsi Requested By #12 (sesuai TC-377 langkah 5, "3 huruf pertama salah satu opsi"), bukan nilai kolom penuh; pada 9 opsi distinct Tabel C hanya opsi #12 yang memuatnya (substring, case-insensitive), sehingga daftar menyempit menjadi satu opsi. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-377 langkah 5 ("Ketik 3 huruf pertama salah satu opsi") tidak menyebut dropdown mana, dan Expected j ("keyword tanpa kecocokan") tidak punya keyword; spec memilih dropdown Requested By, `Fixture.hardwareStock.derived.requestedByPrefixLower` dan `zzqx` (Prerequisites).
  - TC-378 dan TC-379 tidak menyebut cara mengisi date range picker; spec menulis "isi field dengan rentang tanggal".
  - TC-377 opsi Device Name (SKU) baris #9 (tanpa SKU) dan TC-378 memakai Category `BLE Gateway`; untuk Subject BYO tanpa SKU (Matched Identifier #9) kolom Category tertulis `—` pada Tabel C, sedangkan daftar opsi Category TC-377 tidak memuat `—`; spec mengikuti TC.
