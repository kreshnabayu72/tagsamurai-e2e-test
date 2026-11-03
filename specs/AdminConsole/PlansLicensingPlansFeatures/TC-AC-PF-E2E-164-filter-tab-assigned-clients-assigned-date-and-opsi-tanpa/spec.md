---
id: TC-AC-PF-E2E-164-filter-tab-assigned-clients-assigned-date-and-opsi-tanpa
title: "Filter Tab Assigned Clients: Assigned Date inklusif, kombinasi dengan Search, isi opsi dropdown, dan tanpa hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-421
  - TC-AC-PF-422
  - TC-AC-PF-423
  - TC-AC-PF-424
coverage:
  web: automated
---

# Filter Tab Assigned Clients: Assigned Date inklusif, kombinasi dengan Search, isi opsi dropdown, dan tanpa hasil

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Filter Assigned Date (TC-AC-PF-421)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Verifikasi tabel menampilkan sedikitnya satu baris (footer `Showing 1–9 of 9 entries`).
4. Buka Filter Panel, pilih rentang Assigned Date `03 Jun 26` sampai `09 Jun 26`, klik `[Apply]`.
5. Verifikasi tabel menampilkan tiga baris: `PT Karya Abadi` (03 Jun), `PT Wahana Nusantara` (05 Jun), `PT Timur Jaya` (09 Jun).
6. Verifikasi baris bertanggal batas `03 Jun 26` dan `09 Jun 26` ikut tampil (batas inklusif).
7. Buka Filter Panel, kosongkan seluruh filter, klik `[Apply]`.

### Kombinasi Filter dan Search (TC-AC-PF-422)

8. Ketik Search `pt`, tekan Enter.
9. Buka Filter Panel, pilih Plan Version `Outdated` dan Assigned By `Jane Smith`, klik `[Apply]`.
10. Verifikasi tabel menampilkan empat baris: `PT Bumi Sentosa`, `PT Hak Parsial Dua`, `PT Hak Parsial Satu`, `PT Karya Abadi`.
11. Verifikasi kotak Search tetap berisi `pt`.
12. Buka Filter Panel, kosongkan seluruh filter, klik `[Apply]`.
13. Klik `(←)` pada kotak Search.

### Isi opsi dropdown Filter (TC-AC-PF-423)

14. Buka Filter Panel, buka dropdown Subscription Status.
15. Verifikasi dropdown Subscription Status memuat tujuh opsi tetap `Waiting for Approval`, `Pending`, `Active`, `Expired`, `Grace`, `Archive`, `Purge`.
16. Tutup dropdown Subscription Status, buka dropdown Plan Version.
17. Verifikasi dropdown Plan Version memuat opsi `Up to Date` dan `Outdated`.
18. Tutup dropdown Plan Version, buka dropdown Assigned By.
19. Verifikasi dropdown Assigned By memuat opsi `Jane Smith` dan `John Doe`.
20. Tutup dropdown Assigned By dan Filter Panel tanpa menerapkan filter.

### Filter tanpa hasil (TC-AC-PF-424)

21. Buka Filter Panel, pilih Subscription Status `Grace` dan Assigned By `John Doe`, klik `[Apply]`.
22. Verifikasi Illustration tampil.
23. Verifikasi Title "No results found" tampil.
24. Verifikasi Description "Try adjusting your search or filter." tampil.
25. Buka Filter Panel, kosongkan seluruh filter, klik `[Apply]`.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 7, 12, dan 25 (mengosongkan filter), 13 (mereset Search), 16, 18, dan 20 (menutup dropdown dan panel).
- Langkah 3 menjadi pembanding positif bagi asersi tabel tersaring (langkah 5, 6, dan 10) dan bagi empty state pada langkah 22 sampai 24 (bagian 8b butir 2).
- Empty state diasersi per butir (Illustration, Title, Description) mengikuti pemecahan Expected TC-AC-PF-424.
- Temuan untuk QA:
  - TC-AC-PF-421 tidak menyebut cara memilih tanggal pada date range picker; spec memakai pemilihan rentang dari kontrol `Assigned Date`.
  - TC-AC-PF-422 menyebut Search tetap `pt` tanpa menyatakan apakah isi tabel diasersi di bawah gabungan keduanya selain empat nama baris; spec mengasersi empat nama baris dan isi kotak Search.
