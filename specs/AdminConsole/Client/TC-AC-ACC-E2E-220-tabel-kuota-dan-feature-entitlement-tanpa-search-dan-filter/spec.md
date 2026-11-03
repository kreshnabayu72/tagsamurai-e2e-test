---
id: TC-AC-ACC-E2E-220-tabel-kuota-dan-feature-entitlement-tanpa-search-dan-filter
title: "Tabel Kuota, Feature Entitlement, Station Quota, dan Tablet List Tanpa Ikon Search dan Tombol Filter"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-826
coverage:
  web: automated
---

# Tabel Kuota, Feature Entitlement, Station Quota, dan Tablet List Tanpa Ikon Search dan Tombol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (Station "Gerbang Gudang A" dengan Tablet List) dan C-DTL-2 "PT Uji Free" (SAMS Free, Section Platform Core). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-826: Tabel kuota dan Feature Entitlement tanpa ikon Search maupun tombol Filter; Tablet List tanpa ikon Search maupun tombol Filter

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Klik Tab `Subscription`, sub-tab `FAMS`
4. Lihat section License Quota, Fixed Asset Module, Feature Suites, dan Addon Features
5. Verifikasi tabel License Quota menampilkan kolom License Type, Total, Used, Available
6. Verifikasi tabel License Quota tanpa ikon Search dan tanpa tombol Filter
7. Verifikasi tabel Fixed Asset Module menampilkan kolom Feature, Value, Source
8. Verifikasi tabel Fixed Asset Module tanpa ikon Search dan tanpa tombol Filter
9. Verifikasi tabel Feature Suites menampilkan kolom Feature, Value, Source
10. Verifikasi tabel Feature Suites tanpa ikon Search dan tanpa tombol Filter
11. Verifikasi tabel Addon Features menampilkan kolom Feature, Qty
12. Verifikasi tabel Addon Features tanpa ikon Search dan tanpa tombol Filter
13. Klik Tab `TAG` lalu lihat section Quota
14. Verifikasi tabel Quota TAG menampilkan kolom Type, Total Quota, Used, Available dengan toolbar hanya `Download`
15. Verifikasi tabel Quota TAG tanpa ikon Search dan tanpa tombol Filter
16. Klik Tab `Hardware` lalu lihat section Quota
17. Verifikasi tabel Quota Hardware menampilkan kolom Category, Type, Total Quota, Used, Available dengan toolbar hanya `Download`
18. Verifikasi tabel Quota Hardware tanpa ikon Search dan tanpa tombol Filter
19. Klik Tab `Asset Control` lalu lihat section Station Quota
20. Verifikasi tabel Station Quota menampilkan kolom Total, Used, Available
21. Verifikasi tabel Station Quota tanpa ikon Search dan tanpa tombol Filter
22. Klik baris "Gerbang Gudang A" lalu lihat Tablet List
23. Verifikasi tabel Tablet List menampilkan kolom Device Name, Brand, Device ID, App Version, Enrolled Date, Last Active, Status
24. Verifikasi tabel Tablet List tanpa ikon Search dan tanpa tombol Filter
25. Klik Tab `Storage` lalu lihat section Quota
26. Verifikasi tabel Quota Storage menampilkan kolom Total (GB), Used (GB), Available (GB)
27. Verifikasi tabel Quota Storage tanpa ikon Search dan tanpa tombol Filter
28. Kembali ke List lewat breadcrumb Client
29. Ketik Search `PT Uji Free`, tekan Enter
30. Klik Company Name "PT Uji Free" untuk membuka Detail
31. Klik Tab `Subscription` lalu sub-tab `SAMS`, lalu lihat section Platform Core
32. Verifikasi tabel Platform Core menampilkan kolom Feature, Value, Source
33. Verifikasi tabel Platform Core tanpa ikon Search dan tanpa tombol Filter

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan beberapa tabel pada satu role, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Absence ikon Search dan tombol Filter pada tiap tabel didahului Verifikasi kolom tabel yang sama sebagai anchor positif (bagian 8b butir 2).
- Pembagian TC lintas spec: Search dan Filter pada tabel Purchase History dan Hardware List ada di spec lain; TC-826 hanya tabel tanpa Search dan Filter.
- Temuan untuk QA (S-15): TC-826 Langkah 5 menyebut "Klik baris "Gerbang Gudang A"" pada Tab Asset Control tanpa menyebut cara membuka Tablet List selain klik baris; spec mengikuti redaksi TC. Post Condition `-`.
