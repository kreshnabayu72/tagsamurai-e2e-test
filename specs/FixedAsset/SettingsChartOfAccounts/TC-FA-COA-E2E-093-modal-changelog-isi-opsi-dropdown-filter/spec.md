---
id: TC-FA-COA-E2E-093-modal-changelog-isi-opsi-dropdown-filter
title: "Modal Changelog: Isi Opsi Dropdown Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-203
coverage:
  web: automated
---

# Modal Changelog: Isi Opsi Dropdown Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Riwayat Changelog P41 (asumsi pre-setup, bukan data PRD): empat baris Example Data Modal Changelog (PRD §4.1.1; tanggal contoh 20 sampai 23 Oct 2026; kode 5-6001, 6-2001, 1-1002, 5-6000; Modified By Rina P) ditambah satu baris Create, satu baris Delete, satu baris Activate (Status Inactive menjadi Active), dan satu entri oleh user B. Changelog adalah audit trail permanen yang tumbuh sehingga daftar opsi dropdown dibaca dari log saat ini lewat kemampuan baca BE (disediakan tim FE/BE); asersi membandingkan opsi dengan nilai DISTINCT log tersebut.
- Opsi untuk langkah berulang 20 sampai 22 (opsi seed P41 minimal; opsi lain yang dibaca dari log saat ini mengikuti pola yang sama):

  | Dropdown | Opsi |
  |---|---|
  | `Action` | `Create` |
  | `Action` | `Edit` |
  | `Action` | `Delete` |
  | `Account Code` | `1-1002` |
  | `Account Code` | `5-6000` |
  | `Account Code` | `5-6001` |
  | `Account Code` | `6-2001` |
  | `Field` | `Account Code` |
  | `Field` | `Account Name` |
  | `Field` | `Last Used in Journal` |
  | `Field` | `Status` |
  | `Modified By` | `Rina P` |
  | `Modified By` | user B |

- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-203: Isi opsi dropdown filter bersumber dari data log

1. Klik ikon Changelog di toolbar
2. Klik ikon Filter di modal Changelog
3. Buka dropdown Action dan catat opsinya
4. Verifikasi opsi Action adalah Create, Edit, dan Delete (DISTINCT Action pada log saat ini)
5. Verifikasi tidak ada opsi untuk nilai kosong pada dropdown Action
6. Tutup dropdown Action
7. Buka dropdown Account Code dan catat opsinya
8. Verifikasi opsi Account Code memuat 1-1002, 5-6000, 5-6001, dan 6-2001
9. Verifikasi opsi Account Code tidak memuat kode yang tidak ada di log (sama dengan DISTINCT Account Code log saat ini)
10. Verifikasi tidak ada opsi untuk nilai kosong pada dropdown Account Code
11. Tutup dropdown Account Code
12. Buka dropdown Field dan catat opsinya
13. Verifikasi opsi Field memuat Account Code, Account Name, Last Used in Journal, dan Status
14. Verifikasi tidak ada opsi untuk nilai kosong pada dropdown Field
15. Tutup dropdown Field
16. Buka dropdown Modified By dan catat opsinya
17. Verifikasi opsi Modified By berupa nama user pengubah di log, termasuk Rina P dan user B
18. Verifikasi tidak ada opsi untuk nilai kosong pada dropdown Modified By
19. Tutup dropdown Modified By
20. Pilih opsi `Create` pada dropdown `Action` saja, lalu klik Apply
21. Verifikasi jumlah baris yang tampil minimal satu
22. Klik Clear Field pada dropdown `Action`
23. Ulangi langkah 20 sampai 22 untuk setiap baris lain pada tabel Prerequisites (dropdown dan opsi sesuai kolom tabel)
24. Tutup modal dengan ikon ✕

## Notes

- Alasan spec di atas sekitar 35 langkah (24 langkah nominal, sekitar 61 dengan ekspansi langkah 23): satu pengecekan opsi dropdown diulang untuk 13 opsi (idiom 8b.7, parameter pada tabel Prerequisites, tanpa langkah bersyarat, `Verifikasi` tetap satu per klausa); seluruh blok memakai satu Filter Panel dan satu kelas harness (fungsional) dan tiap opsi berdiri sendiri.
- Langkah 23 mengulang langkah 20 sampai 22 untuk 12 opsi lain pada tabel Prerequisites.
- Langkah penghubung (S-03): langkah 6, 11, 15, dan 19 (menutup dropdown), langkah 22 dan Clear Field pada iterasi (membersihkan filter antar opsi, S-09), langkah 24 (menutup modal).
- Asersi "tidak ada opsi untuk nilai kosong" (langkah 5, 10, 14, dan 18) ditulis saat dropdown terbuka, sebelum langkah menutupnya, dan sesudah `Verifikasi` yang membuktikan opsi lain pada dropdown itu tampil (8b butir 5 dan butir 2).
- Kemampuan baca BE untuk DISTINCT nilai log (langkah 4, 9, dan 17) disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Spec ini hanya memuat TC-FA-COA-203.
- Temuan untuk QA:
  - TC-203 butir b dan butir d memuat "tidak berisi kode yang tidak ada di log" dan "nama user yang tercatat sebagai pengubah" yang bergantung pada isi log saat ini; audit trail tumbuh oleh spec lain, sehingga spec membandingkan opsi dengan DISTINCT log yang dibaca lewat BE.
  - TC-203 butir e menulis "setiap opsi bila dipilih sendiri menghasilkan minimal satu baris"; daftar opsi dinamis, sehingga tabel Prerequisites hanya memuat opsi seed P41.
  - P41 adalah asumsi pre-setup, bukan data PRD.
