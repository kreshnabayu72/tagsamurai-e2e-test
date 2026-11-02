---
id: TC-AC-ACTS-E2E-227-modal-event-log-tab-add-stock-search-kolom
title: "Modal Event Log Tab Add Stock: Search Per Kelas Kolom dan Kolom Tanpa Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-487
  - TC-AC-ACTS-488
  - TC-AC-ACTS-489
  - TC-AC-ACTS-490
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Search Per Kelas Kolom dan Kolom Tanpa Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `eventLogDateText` = nilai kolom Date salah satu sesi seed Event Log Tab Add Stock sebagaimana tampil di tabel (contoh TC: `15 Jun 2026`); `eventLogSuccessText` = angka kolom Success salah satu sesi seed Tab Add Stock sebagaimana tampil (contoh TC: `45`); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Nilai sel Date dan Success yang dicari (TC-AC-ACTS-490) berasal dari baris seed sebagaimana tampil di tabel.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-487: Search kelas teks di modal Event Log (Tab Add Stock): Hardware

4. Ketik Search `zebra`, tekan Enter
5. Verifikasi tabel memuat sesi dengan Hardware `Zebra RFD40 (SN-2201)` untuk keyword `zebra`
6. Ganti isi kotak search dengan `ZEBRA`, tekan Enter
7. Verifikasi tabel memuat sesi dengan Hardware `Zebra RFD40 (SN-2201)` untuk keyword `ZEBRA`
8. Ganti isi kotak search dengan `zzz-tidak-ada-hw`, tekan Enter
9. Verifikasi empty state `No results found` tampil
10. Klik `(←)` pada kotak Search

### TC-AC-ACTS-488: Search kelas enum di modal Event Log (Tab Add Stock): Activity

11. Ketik Search `delete`, tekan Enter
12. Verifikasi tabel memuat sesi Activity `Delete Stock` untuk keyword `delete`
13. Ganti isi kotak search dengan `DELETE`, tekan Enter
14. Verifikasi tabel memuat sesi Activity `Delete Stock` untuk keyword `DELETE`
15. Ganti isi kotak search dengan `zzz-tidak-ada-act`, tekan Enter
16. Verifikasi empty state `No results found` tampil
17. Klik `(←)` pada kotak Search

### TC-AC-ACTS-489: Search kelas user di modal Event Log (Tab Add Stock): Modified By

18. Ketik Search `sari`, tekan Enter
19. Verifikasi tabel memuat sesi Modified By Sari untuk keyword `sari`
20. Ganti isi kotak search dengan `SARI`, tekan Enter
21. Verifikasi tabel memuat sesi Modified By Sari untuk keyword `SARI`
22. Ganti isi kotak search dengan `zzz-tidak-ada-mod`, tekan Enter
23. Verifikasi empty state `No results found` tampil
24. Klik `(←)` pada kotak Search

### TC-AC-ACTS-490: Search tidak mencari kolom Date, Success, Waiting for Approval, dan Failed di modal Event Log (Tab Add Stock)

25. Verifikasi sedikitnya satu baris sesi tampil pada tabel
26. Ketik Search `Fixture.tagStock.eventLogDateText`, tekan Enter
27. Verifikasi empty state `No results found` tampil sehingga tabel tidak menemukan baris berdasarkan nilai kolom Date
28. Ganti isi kotak search dengan `Fixture.tagStock.eventLogSuccessText`, tekan Enter
29. Verifikasi empty state `No results found` tampil sehingga tabel tidak menemukan baris berdasarkan nilai kolom angka Success
30. Klik icon Filter
31. Verifikasi field `Date` tersedia di Filter Panel (penyaringan kolom Date hanya lewat Filter Panel)
32. Klik icon Filter untuk menutup panel
33. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
