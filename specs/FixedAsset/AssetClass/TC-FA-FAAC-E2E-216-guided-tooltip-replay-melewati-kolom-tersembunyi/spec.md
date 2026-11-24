---
id: TC-FA-FAAC-E2E-216-guided-tooltip-replay-melewati-kolom-tersembunyi
title: "Guided Tooltip Tab Asset Class: Replay Melewati Step yang Kolom Targetnya Disembunyikan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-754
sourceRules: ["§4.7#p1", "§4.7#r1", "§4.7#r2", "§4.7#r5", "§4.7#r6", "§4.7#r7", "§4.7#r8"]
smoke: []
dependsOn: []
trace:
  "§4.7#p1": [7, 8, 18, 19]
  "§4.7#r1": 7
  "§4.7#r2": 9
  "§4.7#r5": 11
  "§4.7#r6": 13
  "§4.7#r7": 15
  "§4.7#r8": [17, 18]
anchor: [5, 23]
coverage:
  web: automated
---

# Guided Tooltip Tab Asset Class: Replay Melewati Step yang Kolom Targetnya Disembunyikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini memakai replay lewat tombol `[?]` dan tidak mengubah flag.
- State yang diubah spec: konfigurasi kolom tabel (kolom Commercial dan Fiscal disembunyikan lalu ditampilkan kembali oleh spec ini). Dipulihkan oleh langkah 20 sampai 21 dan oleh hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data Asset Class.

## Test Steps

### TC-FA-FAAC-754: Replay Guided Tooltip melewati step yang kolom targetnya disembunyikan

1. Buka Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
2. Hilangkan centang kolom Commercial dan Fiscal
3. Klik `[Save]`
4. Verifikasi header kolom Commercial dan Fiscal tidak tampil di tabel
5. Verifikasi header kolom Class Code, Accounts, dan Asset Names tetap tampil
6. Klik icon `[?]` di sebelah kanan Breadcrumb
7. Verifikasi walkthrough dimulai dari `Step 1 of 6` dengan Title `Set Up in Order` dan spotlight pada tab bar halaman Accounting
8. Klik `[Next]`
9. Verifikasi `Step 2 of 6` dengan Title `Asset Class` dan spotlight pada header kolom Class Code
10. Klik `[Next]`
11. Verifikasi `Step 3 of 6` dengan Title `Accounts` dan spotlight pada header kolom Accounts (step `Commercial Depreciation` dan `Fiscal Depreciation` tidak tampil)
12. Klik `[Next]`
13. Verifikasi `Step 4 of 6` dengan Title `Asset Names` dan spotlight pada header kolom Asset Names
14. Klik `[Next]`
15. Verifikasi `Step 5 of 6` dengan Title `Filter Asset Classes`
16. Klik `[Next]`
17. Verifikasi `Step 6 of 6` dengan Title `Changelog` dan tombol `[Next]` berganti menjadi `[Done]`
18. Klik `[Done]`
19. Verifikasi walkthrough tertutup
20. Buka Setup Column, centang kembali kolom Commercial dan Fiscal
21. Klik `[Save]`
22. Klik icon `[?]` di sebelah kanan Breadcrumb
23. Verifikasi walkthrough dimulai dari `Step 1 of 8` dengan Title `Set Up in Order`
24. Klik link `[Skip]`

## Notes

- Langkah penghubung (S-03): langkah 1 sampai 3 (membentuk precondition d TC: kolom target disembunyikan lewat Column Visibility), langkah 20 sampai 21 (menampilkan kembali kolom untuk Expected d dan sekaligus memulihkan konfigurasi kolom), langkah 24 (menutup walkthrough hasil replay; flag sudah tersimpan sehingga tidak berubah).
- Aturan sumber: `foundation/functions/guided-tooltip.md` §16.3 baris Target tersembunyi, dirujuk PRD `asset-class.md` §4.7 (unit `§4.7#p1`).
