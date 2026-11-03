---
id: TC-AC-ACTS-E2E-241-modal-event-log-tab-audit-tag-sc-screening-sc-ceklis
title: "Modal Event Log Tab Audit TAG: Setup Column: Screening Overlay dan Popup; Setup Column: Ceklis dan Unceklis Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-917
  - TC-AC-ACTS-918
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: Setup Column: Screening Overlay dan Popup; Setup Column: Ceklis dan Unceklis Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Audit TAG SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Audit dengan sedikitnya dua nilai distinct pada tiap kolom (Found dan Not Found beragam; Not Found Action `Marked as Damaged/Missing` dan `Kept previous status`; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Sari D` dan pengguna lain). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Tabel "Kolom Hideable Tab Audit TAG":

  | Kolom |
  |---|
  | `Date` |
  | `Found` |
  | `Not Found` |
  | `Not Found Action` |
  | `Hardware` |
  | `Modified By` |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pemulihan Setup Column: hook `before` dan `after` menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- State global: konfigurasi kolom Setup Column yang disimpan spec dipulihkan di hook `before` dan `after` (menghapus preferensi kolom di browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Klik tab `Audit TAG`

### TC-AC-ACTS-917: Setup Column modal Event Log (Tab Audit TAG): screening Overlay dan Popup Setup Column

5. Klik header kolom Column Visibility (⋯)
6. Klik `[Setup Column]`
7. Verifikasi Overlay Setup Column tampil
8. Verifikasi daftar pada Popup Setup Column berurutan `Date`, `Found`, `Not Found`, `Not Found Action`, `Hardware`, `Modified By`
9. Verifikasi setiap kolom berstatus checkbox checked dan enabled (Hideable) dengan drag handle dan icon Pin
10. Verifikasi footer Popup memuat `[Reset to Default]` dan `[Save]` rata kanan, tanpa `[Cancel]`
11. Tutup Popup Setup Column dengan klik (X)

### TC-AC-ACTS-918: Setup Column modal Event Log (Tab Audit TAG): ceklis dan unceklis kolom (kelas Hideable) serta Reset to Default

12. Klik header kolom Column Visibility (⋯)
13. Klik `[Setup Column]`
Langkah 14 sampai 17 diulang untuk setiap baris tabel "Kolom Hideable Tab Audit TAG" pada Prerequisites (6 iterasi).

14. Hilangkan centang kolom `<Kolom>` di Setup Column
15. Verifikasi preview langsung menyembunyikan kolom `<Kolom>`
16. Centang kembali kolom `<Kolom>`
17. Verifikasi preview langsung menampilkan kolom `<Kolom>` kembali
18. Hilangkan centang kolom `Date` dan `Found`, klik `[Save]`
19. Verifikasi kolom `Date` dan `Found` hilang dari tabel
20. Muat ulang halaman (F5)
21. Verifikasi kolom `Date` dan `Found` tetap hilang setelah F5
22. Klik header kolom Column Visibility (⋯)
23. Klik `[Setup Column]`
24. Klik `[Reset to Default]`, lalu klik `[Save]`
25. Verifikasi semua kolom tampil kembali dengan susunan default

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), dan langkah 4 (memilih Tab `Audit TAG`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Perulangan bagian 8b butir 7: langkah 14 sampai 17 diulang untuk setiap baris tabel "Kolom Hideable Tab Audit TAG" (6 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Alasan di atas sekitar 35 langkah: spec ini 45 langkah dihitung dengan ekspansi; seluruh blok memakai satu kelas harness dan satu dataset seed, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang diulang per baris tabel sah menurut bagian 8b butir 7.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
