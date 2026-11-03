---
id: TC-AC-ACHS-E2E-161-filter-tab-in-use-screening-opsi-dan-apply-per-field
title: "Filter Tab In Use Screening Opsi dan Apply per Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-327
  - TC-AC-ACHS-328
  - TC-AC-ACHS-329
  - TC-AC-ACHS-330
coverage:
  web: automated
---

# Filter Tab In Use Screening Opsi dan Apply per Field

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): SKU `Fixture.hardwareStock.p18.sku` dengan 7 unit In Use (Pre-setup #18, Tabel F TC); baris unit dirujuk `Fixture.hardwareStock.p18.f[n].<kolom>` dengan n = nilai kolom N Tabel F (kolom: deviceName, serialNumber, client, status, registeredBy, registeredAt, activatedAt, minPower, maxPower, currentPower); pada langkah dan tabel, sebuah baris unit ditulis dengan kunci `.deviceName`-nya. Client sama pada baris 1 sampai 3 (`Fixture.hardwareStock.p18.f[1].client`), baris 4 dan 5 (`Fixture.hardwareStock.p18.f[4].client`), baris 6 (`Fixture.hardwareStock.p18.f[6].client`), baris 7 (`Fixture.hardwareStock.p18.f[7].client`). Pendaftar sama pada baris 1, 4, 7 (`Fixture.hardwareStock.p18.f[1].registeredBy`), baris 2 dan 5 (`Fixture.hardwareStock.p18.f[2].registeredBy`), baris 3 dan 6 (`Fixture.hardwareStock.p18.f[3].registeredBy`). Urutan tampil default: `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`. Status unit 1 sampai 7: Damaged, Active, Missing, Active, Active, Damaged, Active (label UI). Registered At dan Activated At naik mengikuti N (baris 1 paling awal).
- Parameter field yang diuji pada langkah 24 sampai 28 (TC-329) dan 30 sampai 34 (TC-330):

| Field | Nilai | Hasil (baris, urutan tampil) |
|---|---|---|
| Client | `Fixture.hardwareStock.p18.f[4].client` | 2 baris: `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName` |
| Status | `Damaged` | 2 baris: `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` |
| Registered By | `Fixture.hardwareStock.p18.f[1].registeredBy` | 3 baris: `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` |
| Registered At | Start = tanggal `Fixture.hardwareStock.p18.f[2].registeredAt`, End = tanggal `Fixture.hardwareStock.p18.f[5].registeredAt` | 4 baris: `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName` |
| Activated At | Start = tanggal `Fixture.hardwareStock.p18.f[2].activatedAt` dikurangi 1 hari, End = tanggal `Fixture.hardwareStock.p18.f[5].activatedAt` ditambah 2 hari (`Fixture.hardwareStock.p18.f[6].deviceName` tetap di luar rentang) | 4 baris: `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName` |

- Opsi dropdown (langkah 16): Client (All clients): empat opsi, yaitu `Fixture.hardwareStock.p18.f[1].client`, `Fixture.hardwareStock.p18.f[4].client`, `Fixture.hardwareStock.p18.f[6].client`, dan `Fixture.hardwareStock.p18.f[7].client` (urutan A-Z); Status (All statuses): `Active`, `Damaged`, `Missing` (3 opsi); Registered By (All users): tiga opsi `Fixture.hardwareStock.p18.f[1].registeredBy`, `Fixture.hardwareStock.p18.f[2].registeredBy`, `Fixture.hardwareStock.p18.f[3].registeredBy` (urutan A-Z).
- Pilihan spec (bukan nilai TC): pencarian internal dropdown memakai keyword `Fixture.hardwareStock.derived.dropdownSearchRegisteredByF1` (3 huruf pertama opsi `Fixture.hardwareStock.p18.f[1].registeredBy` dalam huruf kecil, dikecilkan untuk menguji case-insensitive) dan keyword tanpa kecocokan `zzqx`.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |
  | Client baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].client` |
  | Device Name baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 1, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[1].deviceName` |
  | Registered By baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].registeredBy` |
  | Activated At baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Activated At unit nomor 2, Tabel F (#18) | `Fixture.hardwareStock.p18.f[2].activatedAt` |
  | Device Name baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 2, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[2].deviceName` |
  | Registered At baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered At unit nomor 2, Tabel F (#18) | `Fixture.hardwareStock.p18.f[2].registeredAt` |
  | Registered By baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 2, Tabel F (#18) | `Fixture.hardwareStock.p18.f[2].registeredBy` |
  | Device Name baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 3, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[3].deviceName` |
  | Registered By baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 3, Tabel F (#18) | `Fixture.hardwareStock.p18.f[3].registeredBy` |
  | Client baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 4, Tabel F (#18) | `Fixture.hardwareStock.p18.f[4].client` |
  | Device Name baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 4, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[4].deviceName` |
  | Activated At baris 5 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Activated At unit nomor 5, Tabel F (#18) | `Fixture.hardwareStock.p18.f[5].activatedAt` |
  | Device Name baris 5 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 5, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[5].deviceName` |
  | Registered At baris 5 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered At unit nomor 5, Tabel F (#18) | `Fixture.hardwareStock.p18.f[5].registeredAt` |
  | Client baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 6, Tabel F (#18) | `Fixture.hardwareStock.p18.f[6].client` |
  | Device Name baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 6, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[6].deviceName` |
  | Client baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 7, Tabel F (#18) | `Fixture.hardwareStock.p18.f[7].client` |
  | Device Name baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 7, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[7].deviceName` |
  | Nilai turunan dropdownSearchRegisteredByF1 | turunan dari `Fixture.hardwareStock.p18.f[1].registeredBy` | keyword pencarian internal dropdown Registered By: 3 huruf pertama Registered By baris 1 Tabel F dalam huruf kecil (`bud`; pilihan spec TC-AC-ACHS-328) | `Fixture.hardwareStock.derived.dropdownSearchRegisteredByF1` |

## Test Steps

### Screening Filter Panel (TC-AC-ACHS-327)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Hover icon Filter
4. Verifikasi tooltip `Filter`
5. Klik icon Filter
6. Verifikasi ikon Filter menjadi gelap saat panel terbuka
7. Verifikasi field pertama Client: multi-select searchable, placeholder `All clients`
8. Verifikasi field kedua Status: multi-select searchable, placeholder `All statuses`
9. Verifikasi field ketiga Registered At: date range picker, placeholder `Select date`
10. Verifikasi field keempat Registered By: multi-select searchable, placeholder `All users`
11. Verifikasi field kelima Activated At: date range picker, placeholder `Select date`
12. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
13. Verifikasi tidak ada field Photo atau identifier teks di Filter Panel

### Screening isi opsi dropdown (TC-AC-ACHS-328)

14. Untuk setiap field Client, Status, Registered By (langkah 15 sampai 17): lakukan langkah berikut
15. Buka dropdown field
16. Verifikasi daftar opsi sesuai tabel "Opsi dropdown" di bawah
17. Verifikasi kotak pencarian internal ada di dropdown
18. Ketik di kotak pencarian internal dropdown Registered By keyword `Fixture.hardwareStock.derived.dropdownSearchRegisteredByF1`
19. Verifikasi daftar opsi menyempit menjadi opsi `Fixture.hardwareStock.p18.f[1].registeredBy` saja (substring, case-insensitive)
20. Ganti isi kotak pencarian internal dengan `zzqx`
21. Verifikasi teks `No results found` di daftar opsi
22. Tutup dropdown

### Apply per field kelas multi (TC-AC-ACHS-329)

23. Untuk setiap baris Client, Status, Registered By pada tabel parameter (langkah 24 sampai 28): lakukan langkah berikut
24. Isi field dengan nilai pada tabel parameter, klik `[Apply]`
25. Verifikasi tabel menampilkan hasil sesuai tabel parameter
26. Klik `[Clear Field]`
27. Klik `[Apply]`
28. Verifikasi tabel kembali menampilkan seluruh 7 baris

### Apply per field kelas date (TC-AC-ACHS-330)

29. Untuk setiap baris Registered At dan Activated At pada tabel parameter (langkah 30 sampai 34): lakukan langkah berikut
30. Isi field dengan rentang tanggal pada tabel parameter (Start dan End berbeda), klik `[Apply]`
31. Verifikasi tabel menampilkan hasil sesuai tabel parameter
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Verifikasi tabel kembali menampilkan seluruh 7 baris

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-327 sampai 330). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung: langkah 22 (tutup dropdown) dan klik `[Apply]` setelah `[Clear Field]` yang menjadi bagian langkah TC. Langkah 14 dan 23 serta 29 adalah kepala idiom "Untuk setiap ..."; rujukan "langkah 24 sampai 28" dan "30 sampai 34" menunjuk isi iterasi.
- Idiom ulang dipakai pada langkah 14 sampai 17, 23 sampai 28, 29 sampai 34 dengan parameter di Prerequisites; tiap iterasi memuat `Verifikasi` per klausa.
- Spec memuat sekitar 34 langkah nominal, dengan ekspansi sekitar 60: semua blok satu surface (Filter Panel Tab In Use), satu dataset; blok Apply per field memulihkan Filter dengan `[Clear Field]` + `[Apply]` sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Topik satu dataset tetap satu spec (prinsip 1).
- Filter Panel tetap terbuka dari langkah 5 sampai akhir spec karena TC-329 dan TC-330 melanjutkan di panel yang sama (langkah 4 TC).
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state, label Status) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-328 langkah 6 ("Ketik 3 huruf pertama salah satu opsi") tidak menyebut dropdown mana dan Expected h ("keyword tanpa kecocokan") tidak punya keyword; spec memilih dropdown Registered By, `Fixture.hardwareStock.derived.dropdownSearchRegisteredByF1` dan `zzqx` (Prerequisites).
  - TC-329 dan TC-330 tidak menyebut cara mengisi date range picker (ketik atau pilih di kalender); spec menulis "isi field dengan rentang tanggal".
