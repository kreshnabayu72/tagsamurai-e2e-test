---
id: TC-AC-ACC-E2E-283-filter-screening-panel-dan-opsi-dropdown
title: "Filter Client List: Screening Panel, Isi Opsi Dropdown, Cascading Country-State-City, dan Opsi Modified By System"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-375
  - TC-AC-ACC-707
  - TC-AC-ACC-388
  - TC-AC-ACC-932
coverage:
  web: automated
---

# Filter Client List: Screening Panel, Isi Opsi Dropdown, Cascading Country-State-City, dan Opsi Modified By System

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-LST-1 sampai C-LST-3 (`PT Sortir Alfa`, `PT Sortir Beta`, `PT Sortir Gamma`) dan C-W3LST-1 `PT Arsip Sistem Uji` (Archived, Modified By `System`) serta C-W3LST-2 `PT Arsip Manusia Uji` (Archived, Modified By Citra Dewi) tersedia dan hanya dibaca.
- Tidak ada data yang dibuat atau diubah; tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Screening Filter Panel (TC-AC-ACC-375)

1. Klik tombol Filter
2. Verifikasi Header: Overlay Filter dengan field berlabel Partner, Distributor, FAMS, SAMS, SIEM, Modified By, Last Updated, Industry, Country, State, City
3. Verifikasi Body: placeholder `All partners`, `All distributors`, `All statuses`, `All users`, `Select date`, `All industries`, `All countries`, `All states`, `All cities`
4. Verifikasi Body: field Group tidak ada di Filter Panel (Group lewat Sidebar)
5. Verifikasi Footer: `[Clear Field]` (kiri) dan `[Apply]` (kanan)
6. Verifikasi Footer: Status sub-tab tidak ada sebagai filter

### Isi opsi dropdown kelas DISTINCT (TC-AC-ACC-707)

7. Buka dropdown Partner dan baca opsi
8. Verifikasi opsi Partner memuat `CV Mitra Sejati`, `CV Mitra Lestari`, dan `CV Mitra Timur`
9. Buka dropdown Distributor dan baca opsi
10. Verifikasi opsi Distributor memuat `PT Distribusi Nusantara` dan `PT Distribusi Timur`
11. Buka dropdown Industry dan baca opsi
12. Verifikasi opsi Industry memuat `Healthcare`, `Manufacturing`, dan `Retail`
13. Buka dropdown Country dan baca opsi
14. Verifikasi opsi Country memuat `Indonesia`, `Malaysia`, dan `Singapore`

### Cascading Country, State, City (TC-AC-ACC-388)

15. Klik [Clear Field], lalu buka dropdown State dan baca opsi (Country kosong)
16. Verifikasi opsi State memuat `Jawa Barat`, `Selangor`, dan `Central Region`
17. Pilih Country `Indonesia`, lalu buka dropdown State dan baca opsi
18. Verifikasi opsi State memuat `Jawa Barat`
19. Verifikasi opsi State tidak memuat `Selangor` maupun `Central Region`
20. Pilih State `Jawa Barat`, lalu buka dropdown City dan baca opsi
21. Verifikasi opsi City memuat `Bandung`
22. Verifikasi opsi City tidak memuat `Shah Alam` maupun `Singapore`
23. Hapus Country `Indonesia`, lalu pilih Country `Malaysia`
24. Verifikasi pilihan State dan City ter-reset (kosong)
25. Verifikasi field State dan City tetap enabled
26. Buka dropdown State dan baca opsi
27. Verifikasi opsi State memuat `Selangor`
28. Verifikasi opsi State tidak memuat `Jawa Barat`
29. Klik [Clear Field], lalu klik ikon Filter untuk menutup panel

### Opsi Modified By memuat System (TC-AC-ACC-932)

30. Klik sub-tab Archived
31. Klik Filter, buka dropdown Modified By dan baca opsi
32. Verifikasi placeholder field Modified By `All users`
33. Verifikasi opsi Modified By memuat `System`
34. Pilih opsi `System`, lalu klik [Apply]
35. Ketik Search `PT Arsip Sistem Uji`, tekan Enter
36. Verifikasi baris `PT Arsip Sistem Uji` tampil
37. Ganti isi kotak search dengan `PT Arsip Manusia Uji`, tekan Enter
38. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
39. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], klik [Apply], dan klik sub-tab Active

## Notes

- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness dan satu dataset (Filter Panel List), blok berurutan tanpa state bersama dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): [Clear Field] dan penutupan panel Filter, `(←)` pada kotak Search, dan perpindahan sub-tab adalah pemulihan state tanpa asersi (S-09).
- Langkah buka dropdown Country/State/City mengikuti TC-AC-ACC-388; Expected butir (e) `opsi State memuat Selangor dan tidak memuat Jawa Barat` ditulis sebagai dua `Verifikasi` karena dua klausa.
- Temuan untuk QA
  - TC-AC-ACC-375: Langkah hanya `Klik tombol Filter`; kondisi awal `Filter belum ter-Apply` tidak ditulis di Precondition. Spec mengasumsikan hook `beforeEach` membuka List dengan filter kosong.
  - TC-AC-ACC-707: opsi Industry dan Country `nilai Industry/Country Client pada Tabel A3` hanya diverifikasi untuk nilai yang disebut TC; tidak diasersi bahwa opsi lain tidak ada.
