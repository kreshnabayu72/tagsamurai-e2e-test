---
id: TC-AC-DC-E2E-027-add-urutan-dan-parent-hardcoded
title: "Add Subcategory: Urutan A-Z, Parent Hardcoded, Parent Dirujuk Device Name, dan Sub-tab Device SKU"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-66
  - TC-AC-DC-67
  - TC-AC-DC-68
  - TC-AC-DC-269
coverage:
  web: automated
---

# Add Subcategory: Urutan A-Z, Parent Hardcoded, Parent Dirujuk Device Name, dan Sub-tab Device SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware`, `Handheld Reader` (induk TC-66), `bluetooth Reader` dan `Dipakai Leaf` (sibling pembanding urutan, anak `Handheld Reader`), `TAG` dan `RFID` (induk hardcoded TC-67). Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-027`): `Dirujuk {runId}-027` (leaf di bawah `Handheld Reader`, dirujuk Device Name `HR-{runId}-027`; TC-68) dan `Induk SKU {runId}-027` (leaf di bawah `Handheld Reader`; TC-269). Node hasil Add spec (`carrier Scanner {runId}-027`, `RFID Passive {runId}-027`, `Anak Baru {runId}-027`, `SKU Surface Add {runId}-027`) juga dihapus di hook `after`, bersama Device Name `HR-{runId}-027`, lewat sesi API aktor. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: pembuatan Device Name `HR-{runId}-027` dengan Category `Dirujuk {runId}-027` lewat sesi API aktor (kolom wajib Device Name selain Category tidak disebut TC; disediakan tim FE/BE tanpa endpoint karangan). Search pada modal Changelog dan Search tabel Device Name dipakai sebagai langkah penghubung untuk menemukan entri atau baris berdasarkan nama bersuffix unik.

## Test Steps

### Node baru masuk urutan A-Z case-insensitive (TC-66)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Handheld Reader`, klik aksi `+ Subcategory`
3. Ketik `carrier Scanner {runId}-027`, klik `[Submit]`
4. Verifikasi toast sukses "Success, category has been created."
5. Verifikasi node `carrier Scanner {runId}-027` tampil di antara `bluetooth Reader` dan `Dipakai Leaf` pada anak `Handheld Reader`, tanpa muat ulang halaman

### Add di bawah node hardcoded cabang TAG (TC-67)

6. Expand `TAG`
7. Hover node `RFID`, klik aksi `+ Subcategory`
8. Ketik `RFID Passive {runId}-027`, klik `[Submit]`
9. Verifikasi toast sukses "Success, category has been created."
10. Verifikasi node `RFID Passive {runId}-027` muncul sebagai anak `RFID`

### Add di bawah node yang sudah dirujuk Device Name (TC-68)

11. Klik ikon Changelog pada header Sidebar Category
12. Ketik Search `Anak Baru {runId}-027`, tekan Enter
13. Verifikasi empty state "No results found" (baseline nol entri untuk nama `Anak Baru {runId}-027`)
14. Klik `[×]` pada modal Changelog
15. Hover node `Dirujuk {runId}-027`, klik aksi `+ Subcategory`
16. Ketik `Anak Baru {runId}-027`, klik `[Submit]`
17. Verifikasi toast sukses "Success, category has been created."
18. Verifikasi node `Anak Baru {runId}-027` muncul di bawah `Dirujuk {runId}-027`
19. Ketik Search tabel Device Name `HR-{runId}-027`, tekan Enter
20. Verifikasi Device Name `HR-{runId}-027` tetap tampil pada tabel Device Name
21. Klik ikon Changelog pada header Sidebar Category
22. Ketik Search `Anak Baru {runId}-027`, tekan Enter
23. Verifikasi tepat satu entri untuk Category `Anak Baru {runId}-027` dengan Action `Create`
24. Klik `[×]` pada modal Changelog

### Add lewat sub-tab Device SKU (TC-269)

25. Buka sub-tab `Device SKU` pada Settings > Device
26. Expand `Hardware` lalu `Handheld Reader`
27. Hover node `Induk SKU {runId}-027`, klik aksi `+ Subcategory`
28. Ketik `SKU Surface Add {runId}-027`, klik `[Submit]`
29. Verifikasi toast sukses "Success, category has been created."
30. Verifikasi node `SKU Surface Add {runId}-027` muncul sebagai anak `Induk SKU {runId}-027` pada sidebar Device SKU

## Notes

- S-03, langkah penghubung: langkah 1, 6, 26 (membuka cabang tree), langkah 14 dan 24 (menutup modal Changelog), langkah 19 (Search tabel Device Name untuk menemukan baris target), langkah 25 (membuka sub-tab Device SKU). Search pada modal Changelog (langkah 12, 22) menemukan entri berdasarkan nama bersuffix unik.
- Frasa "tanpa refresh halaman" (TC-66) dipenuhi dengan tidak memuat ulang halaman antara langkah 3 dan 5.
- Klausa "tidak ada entri log selain satu entri Create" (TC-68) dinyatakan sebagai Verifikasi baseline nol (langkah 13) dan tepat satu entri `Create` setelah aksi (langkah 23) untuk Category `Anak Baru {runId}-027`.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`, `Dipakai Leaf`) dan Device Name `HR-100` sebagai target tulis atau induk Add. Spec memakai node dan Device Name milik spec bersuffix `{runId}-027` dan hanya membaca node Pre-setup `bluetooth Reader`, `Dipakai Leaf`, dan `RFID` sebagai pembanding urutan atau induk hardcoded. Asersi urutan TC-66 tetap bergantung pada nama literal `bluetooth Reader` dan `Dipakai Leaf`.
  - TC-68 tidak menyebut cara menemukan baris Device Name pada tabel; spec memakai Search tabel Device Name.
  - Post Condition TC-269 (node tampil di Sidebar Category sub-tab Device Name dan satu entri Create pada Changelog) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
