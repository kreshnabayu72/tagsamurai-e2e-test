---
id: TC-AC-ACTS-E2E-259-approvals-tab-active-dan-history-state-per-sub-tab-dan-refresh-f5
title: "Approvals Tab Active dan Tab History: State Search, Filter, Sort, dan Paginasi Per Sub-Tab serta Dipertahankan saat Refresh F5"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-788
  - TC-AC-ACTS-802
coverage:
  web: automated
---

# Approvals Tab Active dan Tab History: State Search, Filter, Sort, dan Paginasi Per Sub-Tab serta Dipertahankan saat Refresh F5

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `historyApprovalOption` = satu opsi field Filter `Approval` Tab History yang ada pada data seed; `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Data seed Approvals > TAG Stock > Tab History: lebih dari 10 baris, termasuk Subject dengan nama pemohon yang memuat `andi`.
- Opsi filter `Approval` Tab History: `Fixture.tagStock.historyApprovalOption`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-788: State Search, Filter, Sort, dan paginasi disimpan per sub-tab di Approvals > TAG Stock

3. Di Tab `Active`: ketik Search `maju`, tekan Enter
4. Klik icon Filter, pilih `Register Duplicate` pada field `Type`, klik `[Apply]`
5. Klik header kolom `Requested By` sekali
6. Pindah ke halaman 2
7. Klik Tab `History`
8. Verifikasi Tab `History` tampil dengan state default (Search kosong, Filter tidak aktif, halaman 1)
9. Di Tab `History`: ketik Search `andi`, tekan Enter
10. Klik icon Filter, pilih `Fixture.tagStock.historyApprovalOption` pada field `Approval`, klik `[Apply]`
11. Pindah ke halaman 2
12. Klik Tab `Active`
13. Verifikasi Tab `Active` memulihkan Search `maju`
14. Verifikasi Tab `Active` memulihkan Filter Type `Register Duplicate`
15. Verifikasi Tab `Active` memulihkan Sort Requested By Ascending
16. Verifikasi Tab `Active` memulihkan halaman 2
17. Verifikasi Tab `Active` memulihkan jumlah baris per halaman miliknya
18. Klik Tab `History`
19. Verifikasi Tab `History` memulihkan Search `andi`
20. Verifikasi Tab `History` memulihkan Filter Approval yang dipilih
21. Verifikasi Tab `History` memulihkan halaman 2
22. Verifikasi Tab `History` memulihkan jumlah baris per halaman miliknya

### TC-AC-ACTS-802: State Search, Filter, Sort, dan paginasi Approvals > TAG Stock Tab Active dan Tab History dipertahankan saat refresh F5

23. Klik Tab `Active`, ketik Search `maju`, tekan Enter
24. Klik icon Filter, pilih `Register Duplicate` pada field `Type`, klik `[Apply]`
25. Klik header kolom `Requested By` sekali
26. Pindah ke halaman 2
27. Tekan F5
28. Verifikasi setelah F5 di Tab `Active`: Search `maju` sama seperti sebelum refresh
29. Verifikasi setelah F5 di Tab `Active`: Filter Type `Register Duplicate` sama seperti sebelum refresh
30. Verifikasi setelah F5 di Tab `Active`: Sort Requested By Ascending sama seperti sebelum refresh
31. Verifikasi setelah F5 di Tab `Active`: halaman aktif 2 sama seperti sebelum refresh
32. Verifikasi setelah F5 di Tab `Active`: jumlah baris per halaman sama seperti sebelum refresh
33. Klik Tab `History`, ketik Search `andi`, tekan Enter
34. Klik icon Filter, pilih `Fixture.tagStock.historyApprovalOption` pada field `Approval`, klik `[Apply]`
35. Pindah ke halaman 2
36. Tekan F5
37. Verifikasi setelah F5 di Tab `History`: Search `andi` sama seperti sebelum refresh
38. Verifikasi setelah F5 di Tab `History`: Filter Approval yang dipilih sama seperti sebelum refresh
39. Verifikasi setelah F5 di Tab `History`: halaman aktif 2 sama seperti sebelum refresh
40. Verifikasi setelah F5 di Tab `History`: jumlah baris per halaman sama seperti sebelum refresh

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 40 langkah dihitung dengan ekspansi; kedua blok membaca state dua sub-tab yang sama pada dataset yang sama dan hanya berbeda pemicunya (pindah sub-tab atau F5); sebagian besar langkah adalah `Verifikasi` per properti state yang dipulihkan (S-01).
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-788 dan 802 tidak menyebut opsi filter `Approval` Tab History dan opsi filter `Type` Tab Active; spec memakai opsi seed dan `Register Duplicate`.
  - TC-AC-ACTS-788 Expected b menyebut "jumlah baris" tanpa menyatakan nilai awal; spec mengasersi nilai yang sama seperti sebelum berpindah tab.
  - TC-AC-ACTS-788 tidak menyebut kolom yang disortir pada Tab History; spec tidak mengasersi sort di Tab History.
