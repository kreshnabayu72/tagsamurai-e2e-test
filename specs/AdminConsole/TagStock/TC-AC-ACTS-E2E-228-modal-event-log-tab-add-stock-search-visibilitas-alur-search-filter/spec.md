---
id: TC-AC-ACTS-E2E-228-modal-event-log-tab-add-stock-search-visibilitas-alur-search-filter
title: "Modal Event Log Tab Add Stock: Search Terikat Visibilitas Kolom; Alur Search lalu Filter dan Filter lalu Search"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-491
  - TC-AC-ACTS-492
  - TC-AC-ACTS-493
  - TC-AC-ACTS-494
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: Search Terikat Visibilitas Kolom; Alur Search lalu Filter dan Filter lalu Search

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

### TC-AC-ACTS-491: Search terikat visibilitas kolom di modal Event Log (Tab Add Stock): kolom `Activity` di-hide

4. Klik header (⋯) lalu hilangkan centang kolom `Activity`
5. Verifikasi kolom `Activity` tidak tampil
6. Ketik Search `delete stock`, tekan Enter
7. Verifikasi keyword `delete stock` tidak mencocokkan baris melalui kolom `Activity`
8. Verifikasi baris yang cocok lewat kolom lain tetap bisa dicari
9. Klik `(←)` pada kotak Search

### TC-AC-ACTS-492: Search terikat visibilitas kolom di modal Event Log (Tab Add Stock): kolom `Activity` di-unhide kembali

10. Klik header (⋯), centang kembali kolom `Activity`
11. Verifikasi kolom `Activity` tampil kembali
12. Ketik Search `delete stock`, tekan Enter
13. Verifikasi keyword `delete stock` kembali mencocokkan baris melalui kolom `Activity`
14. Klik `(←)` pada kotak Search

### TC-AC-ACTS-493: Alur Search lalu Filter di modal Event Log (Tab Add Stock)

15. Verifikasi sedikitnya satu baris Activity `Add Stock` dan satu baris Activity `Delete Stock` tampil pada tabel
16. Ketik Search `add stock`, tekan Enter
17. Klik icon Filter, pilih `Add Stock` pada field `Activity`, klik `[Apply]`
18. Verifikasi hasil tabel adalah irisan Search `add stock` dan Filter Activity `Add Stock`
19. Verifikasi keyword `add stock` tetap berisi di kotak Search setelah Filter diterapkan
20. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
21. Klik `(←)` pada kotak Search

### TC-AC-ACTS-494: Alur Filter lalu Search di modal Event Log (Tab Add Stock)

22. Klik icon Filter, pilih `Add Stock` pada field `Activity`, klik `[Apply]`
23. Ketik Search `add stock`, tekan Enter
24. Verifikasi hasil tabel identik dengan hasil alur Search lalu Filter (langkah 18)
25. Verifikasi kriteria Filter Activity `Add Stock` tetap aktif setelah Search
26. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
27. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`; mengosongkan Filter lewat `[Clear Field]` dan `[Apply]`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
