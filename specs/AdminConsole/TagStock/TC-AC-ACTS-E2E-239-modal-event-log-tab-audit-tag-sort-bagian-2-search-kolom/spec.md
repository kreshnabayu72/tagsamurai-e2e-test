---
id: TC-AC-ACTS-E2E-239-modal-event-log-tab-audit-tag-sort-bagian-2-search-kolom
title: "Modal Event Log Tab Audit TAG: Sort 3-State Per Kelas Kolom (Bagian 2); Search Per Kelas Kolom dan Kolom Tanpa Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-911
  - TC-AC-ACTS-912
  - TC-AC-ACTS-913
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: Sort 3-State Per Kelas Kolom (Bagian 2); Search Per Kelas Kolom dan Kolom Tanpa Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `auditDateText` = nilai kolom Date salah satu sesi seed Tab Audit TAG sebagaimana tampil (contoh TC: `12 Jun 2026`); `auditFoundText` = angka kolom Found salah satu sesi seed Tab Audit TAG sebagaimana tampil (contoh TC: `47`); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Audit TAG SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Audit dengan sedikitnya dua nilai distinct pada tiap kolom (Found dan Not Found beragam; Not Found Action `Marked as Damaged/Missing` dan `Kept previous status`; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Sari D` dan pengguna lain). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Nilai sel Date dan Found yang dicari (TC-AC-ACTS-913) berasal dari baris seed sebagaimana tampil di tabel.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Klik tab `Audit TAG`

### TC-AC-ACTS-911: Sort 3-state kelas user di modal Event Log (Tab Audit TAG): Modified By

5. Verifikasi tabel memuat sedikitnya satu baris
6. Klik header kolom `Modified By` sekali
7. Verifikasi urutan kolom `Modified By` Ascending (↑) (A-Z menurut nama lengkap user)
8. Klik header kolom `Modified By` kedua kali
9. Verifikasi urutan kolom `Modified By` Descending (↓), terbalik dari urutan Ascending
10. Klik header kolom `Modified By` ketiga kali
11. Verifikasi indikator sort kolom `Modified By` hilang dan tabel kembali ke urutan default Date Newest First

### TC-AC-ACTS-912: Search kelas teks di modal Event Log (Tab Audit TAG): Not Found Action, Hardware, Modified By

12. Ketik Search `marked`, tekan Enter
13. Verifikasi placeholder kotak Search adalah `Search by action, hardware, or modified by...`
14. Verifikasi tabel memuat sesi `Marked as Damaged/Missing` untuk keyword `marked`
15. Ganti isi kotak search dengan `MARKED`, tekan Enter
16. Verifikasi tabel memuat sesi `Marked as Damaged/Missing` untuk keyword `MARKED`
17. Ganti isi kotak search dengan `zebra`, tekan Enter
18. Verifikasi tabel memuat sesi dengan reader `Zebra RFD40 (SN-2201)`
19. Ganti isi kotak search dengan `sari`, tekan Enter
20. Verifikasi tabel memuat sesi oleh Sari
21. Ganti isi kotak search dengan `zzz-tidak-ada`, tekan Enter
22. Verifikasi empty state `No results found` tampil
23. Klik `(←)` pada kotak Search

### TC-AC-ACTS-913: Search tidak mencari kolom Date, Found, dan Not Found di modal Event Log (Tab Audit TAG)

24. Verifikasi sedikitnya satu baris sesi tampil pada tabel
25. Ketik Search `Fixture.tagStock.auditDateText`, tekan Enter
26. Verifikasi empty state `No results found` tampil sehingga tabel tidak menemukan baris berdasarkan nilai kolom Date
27. Ganti isi kotak search dengan `Fixture.tagStock.auditFoundText`, tekan Enter
28. Verifikasi empty state `No results found` tampil sehingga tabel tidak menemukan baris berdasarkan nilai kolom angka Found
29. Klik icon Filter
30. Verifikasi field `Date` tersedia di Filter Panel (penyaringan kolom Date hanya lewat Filter Panel)
31. Klik icon Filter untuk menutup panel
32. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), dan langkah 4 (memilih Tab `Audit TAG`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`.
- Pembanding (8b butir 2): langkah 5 memastikan tabel memuat sedikitnya satu baris sebelum asersi urutan sort pertama.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
