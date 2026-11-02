---
id: TC-AC-ACTS-E2E-186-tab-in-use-search-kolom-bagian-2-search-visibilitas
title: "Detail SKU Tab In Use: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-443
  - TC-AC-ACTS-444
  - TC-AC-ACTS-445
  - TC-AC-ACTS-446
coverage:
  web: automated
---

# Detail SKU Tab In Use: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data tambahan: salah satu unit memiliki Registered At atau Activated At `08 Jun 2026` (nilai yang tampil di tabel, TC-AC-ACTS-444). Search hanya menyaring saat Enter.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`
2. Verifikasi tabel memuat sedikitnya satu baris data

### TC-AC-ACTS-443: Search kelas user Registered By

3. Ketik Search `budi`, tekan Enter
4. Verifikasi tabel memuat baris yang didaftarkan Budi
5. Ganti isi kotak search dengan `BUDI`, tekan Enter
6. Verifikasi tabel memuat baris yang didaftarkan Budi
7. Ganti isi kotak search dengan `zzz-tidak-ada-reg`, tekan Enter
8. Verifikasi empty state `No results found`

### TC-AC-ACTS-444: Search tidak mencari kolom Registered At dan Activated At

9. Ganti isi kotak search dengan `08 Jun 2026`, tekan Enter
10. Verifikasi empty state `No results found` (tabel tidak menemukan baris berdasarkan nilai kolom Registered At dan Activated At)
11. Klik `(←)` pada kotak Search
12. Klik icon Filter
13. Verifikasi field `Registered At` dan `Activated At` tersedia di Filter Panel (penyaringan kolom tersebut hanya lewat Filter Panel)
14. Klik icon Filter untuk menutup panel

### TC-AC-ACTS-445: Search terikat visibilitas kolom, kolom `Client` di-hide

15. Klik header (⋯), hilangkan centang kolom `Client`
16. Verifikasi kolom `Client` tidak tampil
17. Ketik Search `maju`, tekan Enter
18. Verifikasi empty state `No results found` (keyword `maju` tidak mencocokkan baris melalui kolom `Client`)
19. Klik `(←)` pada kotak Search

### TC-AC-ACTS-446: Search terikat visibilitas kolom, kolom `Client` di-unhide kembali

20. Klik header (⋯), centang kembali kolom `Client`
21. Verifikasi kolom `Client` tampil kembali
22. Ketik Search `maju`, tekan Enter
23. Verifikasi keyword `maju` kembali mencocokkan baris melalui kolom `Client`
24. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): klik `(←)` pada kotak Search (reset tabel), menutup panel Filter. Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi absence dan hasil Search.
- Temuan untuk QA: (1) TC-AC-ACTS-444 langkah 5 memakai contoh tanggal `08 Jun 2026`; data harus memuat tanggal itu. (2) TC-AC-ACTS-443 memakai keyword tidak ada `zzz-tidak-ada-reg`.
