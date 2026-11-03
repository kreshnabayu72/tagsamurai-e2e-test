---
id: TC-AC-ACHS-E2E-163-sort-tab-in-use
title: "Sort Tab In Use"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-341
  - TC-AC-ACHS-342
  - TC-AC-ACHS-343
  - TC-AC-ACHS-344
  - TC-AC-ACHS-345
  - TC-AC-ACHS-346
  - TC-AC-ACHS-347
  - TC-AC-ACHS-348
coverage:
  web: automated
---

# Sort Tab In Use

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): SKU `Fixture.hardwareStock.p18.sku` dengan 7 unit In Use (Pre-setup #18, Tabel F TC); baris unit dirujuk `Fixture.hardwareStock.p18.f[n].<kolom>` dengan n = nilai kolom N Tabel F (kolom: deviceName, serialNumber, client, status, registeredBy, registeredAt, activatedAt, minPower, maxPower, currentPower); pada langkah dan tabel, sebuah baris unit ditulis dengan kunci `.deviceName`-nya. Client sama pada baris 1 sampai 3 (`Fixture.hardwareStock.p18.f[1].client`), baris 4 dan 5 (`Fixture.hardwareStock.p18.f[4].client`), baris 6 (`Fixture.hardwareStock.p18.f[6].client`), baris 7 (`Fixture.hardwareStock.p18.f[7].client`). Urutan tampil default: `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`. Pendaftar sama pada baris 1, 4, 7 (`Fixture.hardwareStock.p18.f[1].registeredBy`), baris 2 dan 5 (`Fixture.hardwareStock.p18.f[2].registeredBy`), baris 3 dan 6 (`Fixture.hardwareStock.p18.f[3].registeredBy`). Nilai kolom yang berbeda sehingga sort bermakna: Client (empat nilai: `Fixture.hardwareStock.p18.f[1].client`, `Fixture.hardwareStock.p18.f[4].client`, `Fixture.hardwareStock.p18.f[6].client`, `Fixture.hardwareStock.p18.f[7].client`), Status (Damaged, Active, Missing; label UI), Registered By (tiga pendaftar: `Fixture.hardwareStock.p18.f[1].registeredBy`, `Fixture.hardwareStock.p18.f[2].registeredBy`, `Fixture.hardwareStock.p18.f[3].registeredBy`), Registered At dan Activated At (tiap unit berbeda), Current Power (tiap unit berbeda dan naik mengikuti N untuk unit 1 sampai 7 per Tabel F); Min Power seluruh unit sama (`Fixture.hardwareStock.p18.f[1].minPower`) dan Max Power seluruh unit sama (`Fixture.hardwareStock.p18.f[1].maxPower`), sehingga urutan mengikuti urutan default.
- Parameter sort per kolom (dipakai langkah 4 sampai 12; "teratas" = tiga baris pertama tabel):

| Kolom | Klik 1 (Ascending) teratas | Klik 2 (Descending) teratas |
|---|---|---|
| Device Name | `Fixture.hardwareStock.p18.f[1].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName` | `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName` |
| Serial Number | `Fixture.hardwareStock.p18.f[1].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName` | `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName` |
| Client | `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName` | `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` |
| Status | `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName` | `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` |
| Registered At | `Fixture.hardwareStock.p18.f[1].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName` | `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName` |
| Activated At | `Fixture.hardwareStock.p18.f[1].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName` | `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName` |
| Registered By | `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` | `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName` |
| Min Power | indikator Ascending aktif; urutan tetap default (`Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`) | indikator Descending aktif; urutan tetap default (`Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`) |
| Max Power | indikator Ascending aktif; urutan tetap default (`Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`) | indikator Descending aktif; urutan tetap default (`Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`) |
| Current Power | `Fixture.hardwareStock.p18.f[1].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName` | `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName` |

- Urutan default (klik 3, netral, dan sebelum sort apa pun): Activated At terbaru di atas, teratas `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |
  | Client baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].client` |
  | Device Name baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 1, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[1].deviceName` |
  | Max Power baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Max Power unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].maxPower` |
  | Min Power baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Min Power unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].minPower` |
  | Registered By baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].registeredBy` |
  | Device Name baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 2, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[2].deviceName` |
  | Registered By baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 2, Tabel F (#18) | `Fixture.hardwareStock.p18.f[2].registeredBy` |
  | Device Name baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 3, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[3].deviceName` |
  | Registered By baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 3, Tabel F (#18) | `Fixture.hardwareStock.p18.f[3].registeredBy` |
  | Client baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 4, Tabel F (#18) | `Fixture.hardwareStock.p18.f[4].client` |
  | Device Name baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 4, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[4].deviceName` |
  | Device Name baris 5 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 5, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[5].deviceName` |
  | Client baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 6, Tabel F (#18) | `Fixture.hardwareStock.p18.f[6].client` |
  | Device Name baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 6, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[6].deviceName` |
  | Client baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 7, Tabel F (#18) | `Fixture.hardwareStock.p18.f[7].client` |
  | Device Name baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 7, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[7].deviceName` |
  | Nilai turunan inUseClientA | turunan dari `Fixture.hardwareStock.p18.f[1].client` | keyword Search: kata nama Client baris 1 Tabel F setelah awalan badan usaha (`Sejahtera`; substring Client baris 1 sampai 3; sama dengan keyword TC-AC-ACHS-318) | `Fixture.hardwareStock.derived.inUseClientA` |

## Test Steps

### Siklus 3-state per kolom (TC-AC-ACHS-341, 342, 343, 344, 345)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Untuk setiap baris tabel "Parameter sort per kolom" (langkah 4 sampai 12): lakukan langkah berikut
4. Klik header kolom (klik 1)
5. Verifikasi indikator Ascending (`↑`) aktif pada kolom
6. Verifikasi urutan teratas sesuai kolom "Klik 1" tabel parameter
7. Klik header kolom lagi (klik 2)
8. Verifikasi indikator Descending (`↓`) aktif pada kolom
9. Verifikasi urutan teratas sesuai kolom "Klik 2" tabel parameter
10. Klik header kolom lagi (klik 3)
11. Verifikasi indikator sort kolom netral
12. Verifikasi urutan kembali ke urutan default (teratas `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`)

### Sort default Activated At Newest First (TC-AC-ACHS-346)

13. Verifikasi urutan default tanpa menyentuh header sort: teratas `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`
14. Klik header Activated At tiga kali sampai netral
15. Verifikasi urutan sama dengan default: teratas `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`

### Guard kolom non-sortable (TC-AC-ACHS-347)

16. Verifikasi kolom Device Name memiliki ikon sort (anchor header tabel termuat)
17. Verifikasi kolom Actions tidak punya ikon sort
18. Klik header kolom Actions `(⋯)`
19. Verifikasi overlay `Column Visibility` terbuka
20. Verifikasi urutan baris tidak berubah (teratas `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`)
21. Tutup overlay `Column Visibility`

### Sort tidak mereset Search dan Filter (TC-AC-ACHS-348)

22. Ketik Search `Fixture.hardwareStock.derived.inUseClientA` (`Fixture.hardwareStock.derived.inUseClientA` = kata nama `Fixture.hardwareStock.p18.f[1].client` setelah awalan badan usaha), tekan Enter
23. Klik header Activated At (Ascending)
24. Klik header Client (Ascending)
25. Verifikasi keyword `Fixture.hardwareStock.derived.inUseClientA` tetap terisi
26. Verifikasi tabel hanya berisi hasil search: 3 baris `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` (himpunan baris, urutan tidak diasersi)
27. Verifikasi indikator Activated At kembali netral
28. Verifikasi indikator Client Ascending
29. Klik header Client dua kali sampai netral
30. Klik icon `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-341 sampai 348). Tidak ada TC hanya-BE di spec ini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Sejahtera` (TC-AC-ACHS-318). Dicocokkan dengan Tabel F Pre-setup #18 (Client baris 1 sampai 3 = 3 baris); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- Langkah penghubung (bukan dari langkah TC): langkah 21 (tutup overlay), 29 (kembalikan sort Client ke netral), 30 (klik `(←)` mereset Search), dan langkah 16 (anchor positif untuk asersi absence ikon sort pada langkah 17, bagian 8b butir 2).
- Idiom ulang "Untuk setiap baris tabel" pada langkah 3 sampai 12 (10 iterasi, ekspansi sekitar 100 langkah); parameter di Prerequisites, `Verifikasi` per klausa (indikator dan urutan dipecah), tanpa langkah bersyarat. Isi iterasi adalah langkah 4 sampai 12.
- Spec melewati sekitar 35 langkah dengan ekspansi: alasan, semua blok satu surface (Tab In Use) dan satu dataset read-only; tiap blok TC mengembalikan sort ke netral sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; topik satu dataset tetap satu spec (prinsip 1).
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state, label Status) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-345 Min Power dan Max Power: seluruh unit bernilai sama, sehingga asersi sort hanya mengamati indikator dan urutan default, bukan hasil sort bermakna (tidak ada dua nilai distinct, S-11).
  - TC-348 Expected b menulis urutan `3, 2, 1` dengan sort Client Ascending (semua `Fixture.hardwareStock.p18.f[1].client`, imbang); spec mengasersi himpunan baris saja.
  - TC-346 menyebut "klik berulang hingga netral" tanpa jumlah klik; spec memakai tiga klik (Ascending, Descending, netral) sesuai siklus 3-state.
