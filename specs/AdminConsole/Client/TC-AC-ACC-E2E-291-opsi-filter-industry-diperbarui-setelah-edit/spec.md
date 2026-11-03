---
id: TC-AC-ACC-E2E-291-opsi-filter-industry-diperbarui-setelah-edit
title: "Filter Client List: Opsi Dropdown Industry Diperbarui Setelah Client Diedit Tanpa Reload"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-716
coverage:
  web: automated
---

# Filter Client List: Opsi Dropdown Industry Diperbarui Setelah Client Diedit Tanpa Reload

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture A3 C-LST-4 `PT Opsi Dinamis` (Industry awal `Telecommunications`; Industry `Oil & Gas` dan `Telecommunications` hanya dipakai C-LST-4) tersedia. Spec ini mengubah Industry fixture itu dan mengembalikannya ke `Telecommunications` di akhir spec dan di hook `after` (Last Updated dan baris Changelog Client untuk `PT Opsi Dinamis` bertambah; Post Condition TC meminta pemulihan).
- Kemampuan teknis: Fixture BE untuk memulihkan Industry ke `Telecommunications` bila spec gagal di tengah. Tidak butuh klien HTTP selain itu, intercept, atau jam server.

## Test Steps

### Opsi Industry diperbarui setelah Edit (TC-AC-ACC-716)

1. Klik Filter, buka dropdown Industry, lalu baca opsi dan tutup panel Filter
2. Verifikasi opsi Industry memuat `Telecommunications`
3. Verifikasi opsi Industry tidak memuat `Oil & Gas`
4. Ketik Search "PT Opsi Dinamis", tekan Enter
5. Buka menu `⋯` baris `PT Opsi Dinamis` lalu klik Edit
6. Pilih Industry `Oil & Gas` lalu klik [Save]
7. Verifikasi toast `Success, client has been updated.`
8. Klik Filter lalu buka dropdown Industry dan baca opsi (tanpa reload)
9. Verifikasi opsi Industry memuat `Oil & Gas`
10. Verifikasi opsi Industry tidak memuat `Telecommunications`
11. Klik ikon Filter untuk menutup panel
12. Ketik Search "PT Opsi Dinamis", tekan Enter
13. Buka menu `⋯` baris `PT Opsi Dinamis`, klik Edit, pilih Industry `Telecommunications`, lalu klik [Save] (pemulihan)

## Notes

- Langkah penghubung (S-03, R-16): langkah 4 dan 12 (Ketik Search "PT Opsi Dinamis", tekan Enter) menemukan baris `PT Opsi Dinamis` karena sub-tab Active memuat lebih dari 10 Client; langkah 11 menutup panel Filter; langkah terakhir memulihkan Industry (Post Condition TC); hook `after` menjadi cadangan.
- Pengecualian S-06 (diterima user 2026-11-03): Client target Edit tetap fixture A3 C-LST-4 `PT Opsi Dinamis` dan tidak direplika. Alasan objektif dari TC-AC-ACC-716 Precondition d dan Tabel A3: Industry `Oil & Gas` dan `Telecommunications` hanya dipakai C-LST-4; asersi langkah 3 dan 10 (opsi hilang atau muncul) hanya benar bila tidak ada Client lain ber-Industry itu, sehingga replika bersuffix dengan Industry yang sama akan membuat C-LST-4 menahan opsi `Telecommunications` dan langkah 10 gagal. Pemulihan Industry di langkah 13 dan hook `after` dipertahankan.
- Temuan untuk QA
  - TC-AC-ACC-716: Langkah 2 `Buka menu ⋯ baris PT Opsi Dinamis` tidak menyebut cara menemukan baris (Search/halaman); spec menambah langkah penghubung Search `PT Opsi Dinamis` sebelum membuka menu `⋯`. Perlu diperjelas.
  - TC-AC-ACC-716: Langkah pemulihan Industry tidak diberi toast Expected; spec tidak mengasersinya.
