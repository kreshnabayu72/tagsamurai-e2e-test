---
id: TC-AC-ACC-E2E-290-distributor-filter-sort-sel-tanda-hubung
title: "Client List oleh Distributor: Filter SAMS dan SIEM Tidak Mencocokkan Sel Tanda Hubung, dan Sort FAMS-SAMS-SIEM Menempatkan Tanda Hubung"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-405
  - TC-AC-ACC-686
  - TC-AC-ACC-931
coverage:
  web: automated
---

# Client List oleh Distributor: Filter SAMS dan SIEM Tidak Mencocokkan Sel Tanda Hubung, dan Sort FAMS-SAMS-SIEM Menempatkan Tanda Hubung

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Total Control (PT Distribusi Nusantara) `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net` (A-13), password dari `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script). Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 hanya dibaca: C-W3LST-5 `PT Urut Dash Alfa` (bagi viewer jaringan PT Distribusi Nusantara: FAMS Active, SAMS `—`, SIEM `—`) dan C-W3LST-6 `PT Urut Dash Beta` (FAMS `—`, SAMS Active, SIEM Active); C-10 `PT Lintas Jaringan` (SAMS dan SIEM berplan owner CV Mitra Timur, di luar jaringan PT Distribusi Nusantara) dan C-01 `PT Sejahtera Abadi`.
- Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Filter SAMS dan SIEM tidak mencocokkan sel tanda hubung (TC-AC-ACC-686 dan TC-AC-ACC-931)

1. Klik Filter, pilih SAMS `Active`, lalu klik [Apply]
2. Verifikasi baris `PT Sejahtera Abadi` (SAMS Active) tampil
3. Verifikasi baris `PT Lintas Jaringan` (SAMS `—`) tidak tampil
4. Ketik Search `PT Urut Dash Alfa`, tekan Enter
5. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
6. Ganti isi kotak search dengan `PT Urut Dash Beta`, tekan Enter
7. Verifikasi baris `PT Urut Dash Beta` tampil dengan SAMS `Active`
8. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], klik [Apply]
9. Klik Filter, pilih SIEM `Active`, lalu klik [Apply]
10. Verifikasi baris `PT Sejahtera Abadi` (SIEM Active) tampil
11. Verifikasi baris `PT Lintas Jaringan` (SIEM `—`) tidak tampil
12. Klik Filter, klik [Clear Field], lalu klik [Apply]

### Sort FAMS, SAMS, SIEM dengan sel tanda hubung (TC-AC-ACC-405)

13. Ketik Search `PT Urut Dash`, tekan Enter
14. Klik header kolom FAMS satu kali lalu baca urutan baris
15. Verifikasi FAMS ascending: `PT Urut Dash Alfa` (Active), lalu `PT Urut Dash Beta` (`—`)
16. Klik header kolom FAMS untuk kedua kali lalu baca urutan baris
17. Verifikasi FAMS descending: `PT Urut Dash Beta` (`—`), lalu `PT Urut Dash Alfa` (Active)
18. Klik header kolom SAMS satu kali lalu baca urutan baris
19. Verifikasi SAMS ascending: `PT Urut Dash Beta` (Active), lalu `PT Urut Dash Alfa` (`—`)
20. Klik header kolom SAMS untuk kedua kali lalu baca urutan baris
21. Verifikasi SAMS descending: `PT Urut Dash Alfa` (`—`), lalu `PT Urut Dash Beta` (Active)
22. Klik header kolom SIEM satu kali lalu baca urutan baris
23. Verifikasi SIEM ascending: `PT Urut Dash Beta` (Active), lalu `PT Urut Dash Alfa` (`—`)
24. Klik header kolom SIEM untuk kedua kali lalu baca urutan baris
25. Verifikasi SIEM descending: `PT Urut Dash Alfa` (`—`), lalu `PT Urut Dash Beta` (Active)
26. Klik header kolom SIEM sekali lagi sampai indikator sort nonaktif, lalu klik `(←)` pada kotak Search

## Notes

- Urutan TC disusun ulang: blok Filter (TC-AC-ACC-686, 931) lebih dulu, lalu blok Sort (TC-AC-ACC-405), supaya Search `PT Urut Dash` tidak mempersempit blok Filter; pemulihan state sebagai langkah penghubung (S-03, S-09).
- Sel `—` di Expected adalah tampilan sel kosong produk di luar jaringan viewer; data milik Pre-setup A3 sehingga nama literal dipakai sebagai pengecualian S-12 (asersi urutan/jumlah/badge) dan seeding fixture dijamin tim FE.
- Temuan untuk QA
  - TC-AC-ACC-686: `lihat baris PT Sejahtera Abadi dan PT Lintas Jaringan` dijalankan bersama filter SAMS dan SIEM di sub-tab Active; tidak disebut sub-tab, spec memakai sub-tab Active.
  - TC-AC-ACC-405: Expected butir (a)-(f) menyebut arah ascending/descending tanpa menyebut klik ketiga; spec menambah satu klik ketiga pada SIEM sebagai langkah pemulihan sort.
