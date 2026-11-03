---
id: TC-AC-ACTS-E2E-257-approvals-tab-active-state
title: "Approvals Tab Active: State Kosong, Empty-Filtered, Error Load, dan Loading"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-603
  - TC-AC-ACTS-604
  - TC-AC-ACTS-605
  - TC-AC-ACTS-606
coverage:
  web: automated
---

# Approvals Tab Active: State Kosong, Empty-Filtered, Error Load, dan Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- TC-AC-ACTS-603 membutuhkan tidak ada Subject berstatus pending: fixture BE mengosongkan Subject pending di blok itu dan memulihkan seed di langkah penutup blok serta hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Intercept respons 5xx dan penahanan respons (delay) di atas backend nyata lewat `Spectra.intercept()`; intercept dilepas segera setelah dipakai dan hook `after` memastikan tidak ada intercept tersisa.
- State global: tidak ada yang diubah selain intercept respons yang dilepas segera setelah dipakai.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-604: Empty-filtered Approvals > TAG Stock > Tab Active: search atau filter tanpa hasil

3. Verifikasi sedikitnya satu baris Subject tampil pada tabel
4. Ketik Search `zzz-tidak-ada`, tekan Enter
5. Verifikasi empty state tampil dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
6. Verifikasi tampilan bukan tampilan error
7. Klik `(←)` pada kotak Search

### TC-AC-ACTS-605: Error load Approvals > TAG Stock > Tab Active: fetch gagal bukan empty state

8. Gagalkan request daftar data dengan intercept respons 5xx pada endpoint daftar
9. Muat ulang halaman (F5)
10. Klik Tab `Active`
11. Verifikasi area tabel menampilkan `Unable to load this data.` dan `[Try Again]`
12. Verifikasi tab bar dan toolbar tetap tampil
13. Verifikasi tampilan bukan empty state
14. Lepas intercept respons 5xx
15. Klik `[Try Again]`
16. Verifikasi tombol `[Try Again]` memuat ulang data sehingga tabel Subject tampil

### TC-AC-ACTS-606: Loading state Approvals > TAG Stock > Tab Active

17. Tahan respons daftar data (delay jaringan), lalu muat ulang halaman (F5)
18. Klik Tab `Active`
19. Verifikasi komponen loading tampil selama data diambil
20. Lepas tahanan respons daftar data
21. Verifikasi tabel menggantikan komponen loading

### TC-AC-ACTS-603: Empty state genuine Approvals > TAG Stock > Tab Active

22. Kosongkan seluruh Subject berstatus pending lewat fixture BE hingga tersimpan, lalu muat ulang halaman (F5)
23. Klik Tab `Active`
24. Verifikasi empty state tampil dengan ilustrasi, judul `No pending approvals`, dan deskripsi `You have no pending approval requests at this moment.`
25. Verifikasi tidak ada baris data pada tabel
26. Pulihkan Subject pending seed lewat fixture BE hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`; memulihkan state antar TC.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Urutan blok: TC-AC-ACTS-603 (tanpa Subject pending) diletakkan terakhir karena mengubah data bersama seluruh blok lain (S-10).
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-603 menyatakan precondition Tab Active memuat 5 baris atau lebih sekaligus meminta tidak ada Subject pending; spec memakai kemampuan fixture BE untuk mengosongkan lalu memulihkan Subject.
