---
id: TC-AC-ACTS-E2E-238-modal-event-log-tab-audit-tag-sort-bagian-1
title: "Modal Event Log Tab Audit TAG: Sort 3-State Per Kelas Kolom (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-908
  - TC-AC-ACTS-909
  - TC-AC-ACTS-910
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: Sort 3-State Per Kelas Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Audit TAG SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Audit dengan sedikitnya dua nilai distinct pada tiap kolom (Found dan Not Found beragam; Not Found Action `Marked as Damaged/Missing` dan `Kept previous status`; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Sari D` dan pengguna lain). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Tabel "Kolom sort kelas angka Tab Audit TAG":

  | Kolom | Urutan Ascending |
  |---|---|
  | `Found` | kecil ke besar |
  | `Not Found` | kecil ke besar |

- Tabel "Kolom sort kelas teks Tab Audit TAG":

  | Kolom | Urutan Ascending |
  |---|---|
  | `Not Found Action` | A-Z |
  | `Hardware` | A-Z |

- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Klik tab `Audit TAG`
5. Verifikasi tabel memuat sedikitnya satu baris sesi

### TC-AC-ACTS-908: Sort 3-state kelas tanggal di modal Event Log (Tab Audit TAG): Date

6. Klik header kolom `Date` sekali
7. Verifikasi urutan kolom `Date` Ascending (↑) (Oldest First)
8. Klik header kolom `Date` kedua kali
9. Verifikasi urutan kolom `Date` Descending (↓), terbalik dari urutan Ascending
10. Klik header kolom `Date` ketiga kali
11. Verifikasi indikator sort kolom `Date` hilang dan tabel kembali ke urutan default Date Newest First

### TC-AC-ACTS-909: Sort 3-state kelas angka di modal Event Log (Tab Audit TAG): Found, Not Found

Langkah 12 sampai 17 diulang untuk setiap baris tabel "Kolom sort kelas angka Tab Audit TAG" pada Prerequisites (2 iterasi).

12. Klik header kolom `<Kolom>` sekali
13. Verifikasi urutan kolom `<Kolom>` Ascending (↑) (<Urutan Ascending>)
14. Klik header kolom `<Kolom>` kedua kali
15. Verifikasi urutan kolom `<Kolom>` Descending (↓), terbalik dari urutan Ascending
16. Klik header kolom `<Kolom>` ketiga kali
17. Verifikasi indikator sort kolom `<Kolom>` hilang dan tabel kembali ke urutan default Date Newest First

### TC-AC-ACTS-910: Sort 3-state kelas teks di modal Event Log (Tab Audit TAG): Not Found Action, Hardware

Langkah 18 sampai 23 diulang untuk setiap baris tabel "Kolom sort kelas teks Tab Audit TAG" pada Prerequisites (2 iterasi).

18. Klik header kolom `<Kolom>` sekali
19. Verifikasi urutan kolom `<Kolom>` Ascending (↑) (<Urutan Ascending>)
20. Klik header kolom `<Kolom>` kedua kali
21. Verifikasi urutan kolom `<Kolom>` Descending (↓), terbalik dari urutan Ascending
22. Klik header kolom `<Kolom>` ketiga kali
23. Verifikasi indikator sort kolom `<Kolom>` hilang dan tabel kembali ke urutan default Date Newest First

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), dan langkah 4 (memilih Tab `Audit TAG`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Perulangan bagian 8b butir 7: langkah 12 sampai 17 diulang untuk setiap baris tabel "Kolom sort kelas angka Tab Audit TAG" (2 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Perulangan bagian 8b butir 7: langkah 18 sampai 23 diulang untuk setiap baris tabel "Kolom sort kelas teks Tab Audit TAG" (2 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
