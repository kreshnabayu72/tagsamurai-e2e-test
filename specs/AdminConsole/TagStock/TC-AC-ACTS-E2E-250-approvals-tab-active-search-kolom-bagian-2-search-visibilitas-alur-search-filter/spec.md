---
id: TC-AC-ACTS-E2E-250-approvals-tab-active-search-kolom-bagian-2-search-visibilitas-alur-search-filter
title: "Approvals Tab Active: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom; Alur Search lalu Filter dan Filter lalu Search"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-583
  - TC-AC-ACTS-584
  - TC-AC-ACTS-585
  - TC-AC-ACTS-586
  - TC-AC-ACTS-587
coverage:
  web: automated
---

# Approvals Tab Active: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom; Alur Search lalu Filter dan Filter lalu Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `approvalDateText` = nilai kolom Requested At salah satu Subject seed Tab Active sebagaimana tampil (contoh TC: `18 Jun 2026`); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Nilai sel Requested At yang dicari (TC-AC-ACTS-583) berasal dari baris seed sebagaimana tampil di tabel.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-583: Search tidak mencari kolom Requested At di Approvals > TAG Stock > Tab Active

3. Verifikasi sedikitnya satu baris Subject tampil pada tabel
4. Ketik Search `Fixture.tagStock.approvalDateText`, tekan Enter
5. Verifikasi empty state `No results found` tampil sehingga tabel tidak menemukan baris berdasarkan nilai kolom Requested At
6. Klik icon Filter
7. Verifikasi field `Requested At` tersedia di Filter Panel (penyaringan kolom Requested At hanya lewat Filter Panel)
8. Klik icon Filter untuk menutup panel
9. Klik `(←)` pada kotak Search

### TC-AC-ACTS-584: Search terikat visibilitas kolom di Approvals > TAG Stock > Tab Active: kolom `Type` di-hide

10. Klik header (⋯) lalu hilangkan centang kolom `Type`
11. Verifikasi kolom `Type` tidak tampil
12. Ketik Search `duplicate`, tekan Enter
13. Verifikasi keyword `duplicate` tidak mencocokkan baris melalui kolom `Type`
14. Verifikasi baris yang cocok lewat kolom lain tetap bisa dicari
15. Klik `(←)` pada kotak Search

### TC-AC-ACTS-585: Search terikat visibilitas kolom di Approvals > TAG Stock > Tab Active: kolom `Type` di-unhide kembali

16. Klik header (⋯), centang kembali kolom `Type`
17. Verifikasi kolom `Type` tampil kembali
18. Ketik Search `duplicate`, tekan Enter
19. Verifikasi keyword `duplicate` kembali mencocokkan baris melalui kolom `Type`
20. Klik `(←)` pada kotak Search

### TC-AC-ACTS-586: Alur Search lalu Filter di Approvals > TAG Stock > Tab Active

21. Verifikasi sedikitnya satu baris Type `Register Duplicate` dan satu baris Type `Activation Collision` tampil pada tabel
22. Ketik Search `rfid`, tekan Enter
23. Klik icon Filter, pilih `Register Duplicate` pada field `Type`, klik `[Apply]`
24. Verifikasi hasil tabel adalah irisan Search `rfid` dan Filter Type `Register Duplicate`
25. Verifikasi keyword `rfid` tetap berisi di kotak Search setelah Filter diterapkan
26. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
27. Klik `(←)` pada kotak Search

### TC-AC-ACTS-587: Alur Filter lalu Search di Approvals > TAG Stock > Tab Active

28. Klik icon Filter, pilih `Register Duplicate` pada field `Type`, klik `[Apply]`
29. Ketik Search `rfid`, tekan Enter
30. Verifikasi hasil tabel identik dengan hasil alur Search lalu Filter (langkah 24)
31. Verifikasi kriteria Filter Type `Register Duplicate` tetap aktif setelah Search
32. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
33. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`; mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
