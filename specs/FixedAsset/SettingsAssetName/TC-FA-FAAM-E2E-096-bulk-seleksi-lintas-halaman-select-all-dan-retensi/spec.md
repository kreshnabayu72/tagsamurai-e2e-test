---
id: TC-FA-FAAM-E2E-096-bulk-seleksi-lintas-halaman-select-all-dan-retensi
title: "Bulk: Select All Lintas Halaman, Uncheck Satu Baris, dan Seleksi Bertahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-279
  - TC-FA-FAAM-280
  - TC-FA-FAAM-295
coverage:
  web: automated
---

# Bulk: Select All Lintas Halaman, Uncheck Satu Baris, dan Seleksi Bertahan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control client `AutoBulk35` (Pre-setup #15g). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password dari `Spectra.env.FA_BULK35_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`).
- Data Pre-setup #15g (hanya dibaca): client `AutoBulk35` berisi tepat 35 Asset Name tanpa filter, yaitu `Seed Item 01` sampai `Seed Item 30` (Total Asset 0, UoM `Unit`) serta `Dell Latitude`, `Ergonomic Chair`, `MacBook Pro`, `Warehouse Pallet`, `Service Vehicle`; ukuran halaman 10 sehingga ada 4 halaman. Seleksi pada spec ini tidak pernah dikonfirmasi menjadi Delete; tidak ada data yang diubah.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-279: Select All ([N] records) memilih lintas halaman lalu berubah menjadi Unselect All

1. Centang 1 baris
2. Klik `Select All (35 records)`
3. Verifikasi teks `35 asset names selected`
4. Verifikasi tombol berubah menjadi `Unselect All`
5. Pindah ke halaman 2
6. Verifikasi seluruh baris halaman 2 tercentang
7. Klik `Unselect All`
8. Verifikasi seluruh baris halaman 2 tidak tercentang
9. Verifikasi bar bulk tidak tampil
10. Pindah ke halaman 1

### TC-FA-FAAM-280: Uncheck satu baris dari kondisi terpilih penuh mengembalikan tombol Select All

11. Centang 1 baris
12. Klik `Select All (35 records)`
13. Uncheck satu baris
14. Verifikasi tombol kembali `Select All (34 records)`
15. Verifikasi bar bulk tetap tampil
16. Klik icon `×`

### TC-FA-FAAM-295: Seleksi dipertahankan saat berpindah halaman dan mengubah Search, Filter, atau Sort

17. Centang `Seed Item 01`
18. Pindah ke halaman 2
19. Ketik `Item 3` di Search, tekan Enter
20. Verifikasi baris `Seed Item 30` tampil pada hasil Search
21. Verifikasi baris `Seed Item 01` tidak tampil
22. Verifikasi teks `1 asset name selected` tetap tampil
23. Klik header Code
24. Verifikasi teks `1 asset name selected` tetap tampil sesudah Sort
25. Klik icon `×`
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): kembali ke halaman 1 (langkah 10), mencentang satu baris agar bar bulk tampil sebelum `Select All (35 records)` (langkah 11), membatalkan seleksi dan mengosongkan Search sesudah asersi (langkah 16, 25, 26; S-09).
- Asersi absence pada langkah 9 memakai tabel yang sudah menampilkan baris (langkah 8) sebagai anchor; absence pada langkah 21 memakai langkah 20 sebagai anchor.
- Temuan untuk QA:
  - TC-FA-FAAM-279 sampai TC-FA-FAAM-295 memakai client `AutoBulk35` (Pre-setup #15g) tetapi akun aktornya dan emailnya tidak tertulis di Pre-setup; spec menulisnya sebagai akun yang disediakan tim FE.
  - TC-FA-FAAM-280 langkah 1 mengklik `Select All (35 records)` tanpa menyebut baris yang dicentang lebih dulu agar bar bulk tampil; spec menambah langkah mencentang satu baris (langkah 11).
  - TC-FA-FAAM-295 langkah 1 mencentang `Seed Item 01` pada halaman pertama tanpa menyebut sort default; spec mengikuti TC dan mengandaikan `Seed Item 01` tampil di halaman 1.
