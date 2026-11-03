---
id: TC-AC-PF-E2E-165-sort-tab-assigned-clients-dan-warna-badge-subscription
title: "Sort Tab Assigned Clients dan warna badge Subscription Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-425
  - TC-AC-PF-426
  - TC-AC-PF-427
  - TC-AC-PF-428
  - TC-AC-PF-725
coverage:
  web: automated
---

# Sort Tab Assigned Clients dan warna badge Subscription Status

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D dan Dataset Plan E2 ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup (pengecualian S-06/S-12 butir A-14: nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`):
  - Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith.
  - Dataset Plan E2, default plan `Professional` dengan 7 client: PT Alfa Prima Waiting for Approval, PT Beta Karya Pending, PT Citra Makmur Active, PT Delta Sentosa Expired, PT Eka Jaya Grace, PT Fajar Mulia Archive, PT Gema Persada Purge.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Sort Client Name (TC-AC-PF-425)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Verifikasi tabel menampilkan sedikitnya satu baris (footer `Showing 1–9 of 9 entries`).
4. Klik header `Client Name` satu kali.
5. Verifikasi urutan ascending sama dengan default: `PT Bumi Sentosa` paling atas dan `PT Zona Nol` paling bawah.
6. Klik header `Client Name` untuk kedua kalinya.
7. Verifikasi urutan descending: `PT Zona Nol` paling atas.
8. Verifikasi urutan descending: `PT Bumi Sentosa` paling bawah.
9. Klik header `Client Name` untuk ketiga kalinya.
10. Verifikasi urutan kembali ke default: `PT Bumi Sentosa` paling atas dan `PT Zona Nol` paling bawah.

### Sort Plan Version dan Assigned Date (TC-AC-PF-427)

11. Klik header `Plan Version` satu kali.
12. Verifikasi enam baris `v1` tampil lebih dulu dengan urutan default sebagai tie-breaker: `PT Bumi Sentosa`, `PT Hak Parsial Dua`, `PT Hak Parsial Satu`, `PT Karya Abadi`, `PT Timur Jaya`, `PT Wahana Nusantara`.
13. Verifikasi tiga baris `v5` mengikutinya: `PT Cahaya Mandiri`, `PT Sejahtera Abadi`, `PT Zona Nol`.
14. Klik header `Assigned Date` satu kali.
15. Verifikasi urutan ascending Assigned Date (Oldest First): `PT Karya Abadi` (03 Jun) paling atas.
16. Verifikasi urutan ascending Assigned Date: `PT Zona Nol` (25 Jun) paling bawah.

### Sort Assigned By (TC-AC-PF-428)

17. Klik header `Assigned By` satu kali.
18. Verifikasi lima baris `Jane S` tampil lebih dulu dengan urutan default sebagai tie-breaker: `PT Bumi Sentosa`, `PT Cahaya Mandiri`, `PT Hak Parsial Dua`, `PT Hak Parsial Satu`, `PT Karya Abadi`.
19. Verifikasi empat baris `John D` mengikutinya: `PT Sejahtera Abadi`, `PT Timur Jaya`, `PT Wahana Nusantara`, `PT Zona Nol`.
20. Hover `Jane S` pada salah satu baris.
21. Verifikasi tooltip `Jane Smith` tampil.
22. Klik header `Assigned By` dua kali lagi hingga urutan kembali ke default.

### Sort Subscription Status (TC-AC-PF-426)

23. Kembali ke Plans & Licensing > Plans & Features > Default > Active.
24. Buka Plan Detail `Professional` (klik nama plan `Professional`).
25. Klik Tab Assigned Clients.
26. Klik header `Subscription Status` satu kali.
27. Verifikasi urutan ascending mengikuti lifecycle: `Waiting for Approval`, `Pending`, `Active`, `Expired`, `Grace`, `Archive`, `Purge`.
28. Klik header `Subscription Status` untuk kedua kalinya.
29. Verifikasi urutan descending berkebalikan: `Purge`, `Archive`, `Grace`, `Expired`, `Active`, `Pending`, `Waiting for Approval`.

### Warna badge Subscription Status (TC-AC-PF-725)

30. Klik header `Subscription Status` untuk ketiga kalinya hingga urutan kembali ke default.
31. Verifikasi badge `Waiting for Approval`, `Pending`, `Expired`, dan `Grace` berwarna kuning.
32. Verifikasi badge `Active` berwarna hijau.
33. Verifikasi badge `Archive` dan `Purge` berwarna hitam.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 22 dan 30 (mengembalikan sort ke default), 23 sampai 25 (berpindah ke Plan Detail `Professional`).
- Urutan TC dalam spec: TC-AC-PF-426 dan TC-AC-PF-725 (Dataset Plan E2) ditulis sesudah TC-AC-PF-428 karena keduanya memakai plan `Professional`, sedangkan TC-AC-PF-425, 427, dan 428 memakai plan `Growth`; dengan begitu perpindahan plan terjadi sekali.
- Langkah 3 menjadi pembanding positif bagi asersi urutan baris pada langkah 5 sampai 21.
- Temuan untuk QA:
  - TC-AC-PF-425 Expected a menulis rentang urutan dengan elipsis (`PT Bumi Sentosa` ... `PT Zona Nol`); spec mengasersi baris paling atas dan paling bawah.
  - TC-AC-PF-426 Expected b hanya menulis "urutan kebalikan"; spec menuliskan tujuh status dalam urutan kebalikan dari Expected a.
  - TC-AC-PF-725 tidak menyebut kode warna atau token desain untuk "kuning", "hijau", dan "hitam"; nilai warna perlu dikonfirmasi tim FE.
