---
id: TC-AC-ACTS-E2E-233-modal-event-log-tab-add-stock-sc-reset-tutup-bagian-1
title: "Modal Event Log Tab Add Stock: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-505
  - TC-AC-ACTS-506
  - TC-AC-ACTS-507
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Setup Column: Reset, Tutup, Satu Kolom Tersisa, dan Pin ke-4 (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-505: Setup Column modal Event Log (Tab Add Stock): Reset to Default

4. Klik header kolom Column Visibility (⋯)
5. Klik `[Setup Column]`
6. Sembunyikan kolom `Activity` dan geser `Date`, klik `[Save]`
7. Klik header kolom Column Visibility (⋯), klik `[Setup Column]`
8. Klik `[Reset to Default]`
9. Verifikasi preview kembali ke susunan default modul (bukan ke state tersimpan terakhir)
10. Klik `[Save]`
11. Muat ulang halaman (F5)
12. Verifikasi susunan default bertahan setelah F5

### TC-AC-ACTS-506: Setup Column modal Event Log (Tab Add Stock): tutup dengan (X) atau Esc membuang perubahan

13. Klik header kolom Column Visibility (⋯)
14. Klik `[Setup Column]`
15. Sembunyikan kolom `Activity` di preview
16. Klik icon (X)
17. Verifikasi Popup Setup Column tertutup tanpa dialog konfirmasi
18. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir
19. Klik header kolom Column Visibility (⋯), klik `[Setup Column]`
20. Sembunyikan kolom `Activity` di preview
21. Tekan Esc
22. Verifikasi Popup Setup Column tertutup tanpa dialog konfirmasi
23. Verifikasi perubahan preview dibuang dan tabel memakai konfigurasi tersimpan terakhir

### TC-AC-ACTS-507: Setup Column modal Event Log (Tab Add Stock): satu kolom tersisa tidak bisa di-uncheck

24. Klik header kolom Column Visibility (⋯)
25. Klik `[Setup Column]`
26. Hilangkan centang semua kolom kecuali satu
27. Arahkan kursor ke checkbox kolom terakhir
28. Verifikasi checkbox kolom terakhir disabled
29. Verifikasi tooltip `At least one column must remain visible.` tampil
30. Tutup Popup Setup Column dengan klik (X)

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
