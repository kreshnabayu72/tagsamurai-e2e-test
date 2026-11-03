---
id: TC-AC-PF-E2E-161-search-tab-assigned-clients-siklus-trim-tanpa-hasil
title: "Search Tab Assigned Clients: siklus input, trim spasi, dan tanpa hasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-411
  - TC-AC-PF-412
  - TC-AC-PF-413
coverage:
  web: automated
---

# Search Tab Assigned Clients: siklus input, trim spasi, dan tanpa hasil

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Siklus interaksi Search (TC-AC-PF-411)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Hover ikon Search.
4. Verifikasi tooltip `Search` tampil.
5. Klik ikon Search.
6. Verifikasi input Search muncul dengan placeholder `Search client name, subscription status...`.
7. Verifikasi input Search langsung berfokus.
8. Ketik `abadi` pada input Search tanpa menekan Enter.
9. Verifikasi ikon `x` muncul di dalam input.
10. Verifikasi tabel belum tersaring (footer `Showing 1–9 of 9 entries`).
11. Tekan Enter.
12. Verifikasi tabel tersaring menjadi baris `PT Karya Abadi` dan `PT Sejahtera Abadi`.
13. Klik ikon `x` di dalam input.
14. Verifikasi input Search kosong.
15. Verifikasi tabel tetap menampilkan hasil Search terakhir (`PT Karya Abadi` dan `PT Sejahtera Abadi`).
16. Tekan Enter pada input kosong.
17. Verifikasi tabel kembali menampilkan seluruh data (footer `Showing 1–9 of 9 entries`).
18. Ketik Search `abadi`, tekan Enter.
19. Verifikasi tabel tersaring menjadi baris `PT Karya Abadi` dan `PT Sejahtera Abadi`.
20. Klik ikon panah collapse di kiri toolbar.
21. Verifikasi input Search tertutup.
22. Verifikasi kata kunci Search dikosongkan.
23. Verifikasi tabel langsung kembali menampilkan seluruh data (footer `Showing 1–9 of 9 entries`).

### Trim spasi (TC-AC-PF-412)

24. Ketik Search ` abadi ` (spasi di awal dan di akhir), tekan Enter.
25. Verifikasi hasil pencarian sama dengan pencarian `abadi` tanpa spasi: `PT Karya Abadi` dan `PT Sejahtera Abadi`.
26. Verifikasi isi kotak Search tetap ` abadi ` seperti diketik.
27. Kosongkan isi kotak search, ketik tiga spasi, tekan Enter.
28. Verifikasi tabel kembali menampilkan seluruh data (footer `Showing 1–9 of 9 entries`).

### Tanpa hasil (TC-AC-PF-413)

29. Klik `(←)` pada kotak Search.
30. Ketik Search `zzzzz`, tekan Enter.
31. Verifikasi tabel menampilkan Illustration, Title "No results found", dan Description "Try adjusting your search or filter.".
32. Kosongkan isi kotak search, tekan Enter.
33. Verifikasi seluruh baris tampil kembali (footer `Showing 1–9 of 9 entries`).

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 29 (menutup input Search dan mereset tabel sebelum Search `zzzzz`).
- Urutan Expected TC-AC-PF-411 mengikuti urutan state UI (bagian 8b butir 5): tooltip pada langkah 4 diasersi sebelum klik ikon Search.
- Langkah 10, 17, 23, 28, dan 33 memakai footer `Showing 1–9 of 9 entries` sebagai pembanding bahwa tabel menampilkan seluruh sembilan baris.
- Temuan untuk QA:
  - TC-AC-PF-412 Expected a menyebut "isi kotak Search tetap seperti diketik" sementara TC-AC-PF-411 Expected f menyebut collapse "mengosongkan kata kunci"; kedua perilaku diasersi apa adanya.
  - TC-AC-PF-413 menulis langkah "Klik ikon Search" padahal kotak Search masih terbuka pada rangkaian ini; spec memakai langkah 29 sebagai pengganti pembuka input.
