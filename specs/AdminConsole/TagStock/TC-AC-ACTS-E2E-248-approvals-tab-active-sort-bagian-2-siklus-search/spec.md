---
id: TC-AC-ACTS-E2E-248-approvals-tab-active-sort-bagian-2-siklus-search
title: "Approvals Tab Active: Sort 3-State Per Kelas Kolom (Bagian 2); Siklus Search Toolbar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-577
  - TC-AC-ACTS-578
coverage:
  web: automated
---

# Approvals Tab Active: Sort 3-State Per Kelas Kolom (Bagian 2); Siklus Search Toolbar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-577: Sort 3-state kelas tanggal di Approvals > TAG Stock > Tab Active: Requested At

3. Verifikasi tabel memuat sedikitnya satu baris
4. Klik header kolom `Requested At` sekali
5. Verifikasi urutan kolom `Requested At` Ascending (↑) (Oldest First)
6. Klik header kolom `Requested At` kedua kali
7. Verifikasi urutan kolom `Requested At` Descending (↓), terbalik dari urutan Ascending
8. Klik header kolom `Requested At` ketiga kali
9. Verifikasi indikator sort kolom `Requested At` hilang dan tabel kembali ke urutan default Requested At Oldest First

### TC-AC-ACTS-578: Siklus Search toolbar Approvals > TAG Stock > Tab Active: reveal, Enter, clear, collapse

10. Verifikasi sedikitnya satu baris Subject dengan identifier tanpa `rfid` dan satu baris dengan `rfid` tampil pada tabel
11. Hover icon Search
12. Verifikasi tooltip `Search` tampil
13. Klik icon Search
14. Verifikasi input Search terbuka dengan fokus otomatis
15. Verifikasi input Search memiliki placeholder `Search by identifier or requester...`
16. Ketik `rfid` tanpa menekan Enter
17. Verifikasi tabel belum tersaring (baris tanpa `rfid` masih tampil)
18. Verifikasi icon (✕) muncul di dalam input
19. Tekan Enter
20. Verifikasi tabel tersaring sesuai keyword `rfid`
21. Klik icon (✕) pada input
22. Verifikasi input Search kosong
23. Verifikasi kursor tetap fokus di input Search
24. Verifikasi tabel masih menampilkan hasil search terakhir
25. Tekan Enter pada input kosong
26. Verifikasi tabel kembali menampilkan semua data
27. Ketik Search `rfid`, tekan Enter
28. Klik icon panah (←)
29. Verifikasi kotak pencarian tertutup
30. Verifikasi keyword dikosongkan
31. Verifikasi tabel langsung kembali menampilkan semua data

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup kotak Search lewat `(←)`.
- Pembanding (8b butir 2): langkah 3 memastikan tabel memuat sedikitnya satu baris sebelum asersi urutan sort pertama.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
