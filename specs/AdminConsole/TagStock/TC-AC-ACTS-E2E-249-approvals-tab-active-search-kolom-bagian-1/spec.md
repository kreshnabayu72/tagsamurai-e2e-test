---
id: TC-AC-ACTS-E2E-249-approvals-tab-active-search-kolom-bagian-1
title: "Approvals Tab Active: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-579
  - TC-AC-ACTS-580
  - TC-AC-ACTS-581
  - TC-AC-ACTS-582
coverage:
  web: automated
---

# Approvals Tab Active: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-579: Search kelas badge di Approvals > TAG Stock > Tab Active: Type

3. Ketik Search `duplicate`, tekan Enter
4. Verifikasi tabel memuat Subject Type Register Duplicate untuk keyword `duplicate`
5. Ganti isi kotak search dengan `DUPLICATE`, tekan Enter
6. Verifikasi tabel memuat Subject Type Register Duplicate untuk keyword `DUPLICATE`
7. Ganti isi kotak search dengan `zzz-tidak-ada-typ`, tekan Enter
8. Verifikasi empty state `No results found` tampil
9. Klik `(←)` pada kotak Search

### TC-AC-ACTS-580: Search kelas teks di Approvals > TAG Stock > Tab Active: Device Name (SKU), Category

10. Ketik Search `asset tag`, tekan Enter
11. Verifikasi tabel memuat Subject SKU `RFID-ASSET-CORE-R5` untuk keyword `asset tag`
12. Ganti isi kotak search dengan `ASSET TAG`, tekan Enter
13. Verifikasi tabel memuat Subject SKU `RFID-ASSET-CORE-R5` untuk keyword `ASSET TAG`
14. Ganti isi kotak search dengan `zzz-tidak-ada-dev`, tekan Enter
15. Verifikasi empty state `No results found` tampil
16. Ganti isi kotak search dengan `rfid - object`, tekan Enter
17. Verifikasi tabel memuat Subject kategori `RFID - Object TAG` untuk keyword `rfid - object`
18. Ganti isi kotak search dengan `RFID - OBJECT`, tekan Enter
19. Verifikasi tabel memuat Subject kategori `RFID - Object TAG` untuk keyword `RFID - OBJECT`
20. Ganti isi kotak search dengan `zzz-tidak-ada-cat`, tekan Enter
21. Verifikasi empty state `No results found` tampil
22. Klik `(←)` pada kotak Search

### TC-AC-ACTS-581: Search kelas id di Approvals > TAG Stock > Tab Active: Matched Identifier, Existing Record

23. Ketik Search `a1b2`, tekan Enter
24. Verifikasi tabel memuat Subject dengan identifier `A1B2...` untuk keyword `a1b2`
25. Ganti isi kotak search dengan `A1B2`, tekan Enter
26. Verifikasi tabel memuat Subject dengan identifier `A1B2...` untuk keyword `A1B2`
27. Ganti isi kotak search dengan `zzz-tidak-ada-mat`, tekan Enter
28. Verifikasi empty state `No results found` tampil
29. Ganti isi kotak search dengan `tag-4f`, tekan Enter
30. Verifikasi tabel memuat Subject dengan Existing Record `TAG-4F7K2XQ9` untuk keyword `tag-4f`
31. Ganti isi kotak search dengan `TAG-4F`, tekan Enter
32. Verifikasi tabel memuat Subject dengan Existing Record `TAG-4F7K2XQ9` untuk keyword `TAG-4F`
33. Ganti isi kotak search dengan `zzz-tidak-ada-exi`, tekan Enter
34. Verifikasi empty state `No results found` tampil
35. Klik `(←)` pada kotak Search

### TC-AC-ACTS-582: Search kelas entitas di Approvals > TAG Stock > Tab Active: Requested By

36. Ketik Search `maju`, tekan Enter
37. Verifikasi tabel memuat Subject oleh `PT Maju Bersama (Distributor)` untuk keyword `maju`
38. Ganti isi kotak search dengan `MAJU`, tekan Enter
39. Verifikasi tabel memuat Subject oleh `PT Maju Bersama (Distributor)` untuk keyword `MAJU`
40. Ganti isi kotak search dengan `zzz-tidak-ada-req`, tekan Enter
41. Verifikasi empty state `No results found` tampil
42. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 42 langkah dihitung dengan ekspansi; keempat blok adalah keluarga Search pada satu permukaan dengan satu dataset seed dan berdiri sendiri; jumlah langkah berasal dari tiga keyword per kolom (huruf kecil, huruf besar, tidak ada) dan `Verifikasi` per klausa (S-01).
- Temuan untuk QA (S-15):
