---
id: TC-GS-IMPORT-E2E-216-draft-dibagikan-ke-seluruh-admin-berkapabilitas-dalam-organisasi-yang
title: "Draft dibagikan ke seluruh admin berkapabilitas dalam organisasi yang sama (Import data Create dan Total Control melihat draft yang sama)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-535
coverage:
  web: automated
---

# Draft dibagikan ke seluruh admin berkapabilitas dalam organisasi yang sama (Import data Create dan Total Control melihat draft yang sama)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memundurkan umur draft lewat fixture timestamp atau jam server (state global) dan menghapus baris draft Client A (lihat `suite.md`).
- Akun aktor pertama (login di hook `before`): Import data (Create) Client A (Rina Marlina) `importCreate_automated_qaTeam1@qwertysystem.net` (kapabilitas Import data: C dan R, tanpa capability Division/Position), password `Spectra.env.GS_IMPORTCREATE_PASSWORD` (nama env baru, didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script). Akun kedua (ganti akun eksplisit di langkah): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Layar awal: hook `beforeEach` membuka Import > Brand Client A untuk akun pertama.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun (nilai awal dicatat dan dipulihkan hook suite `after`), lihat `suite.md`.
- Data Dinamis: D-01 (draft Brand 12 baris `pending` dari `brand-12.csv`: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus) pada Client A, dibuat oleh Total Control lewat skrip seed pada langkah 1 (dipakai sebagai precondition TC, tidak diasersi pembuatnya). D-76 varian 1: umur draft >= 24 jam (`created_at` dimundurkan 25 jam lewat fixture timestamp atau jam server yang dimajukan; mekanisme disediakan tim FE/BE) oleh langkah 1 sebelum halaman dimuat ulang di langkah 2, sehingga Unsaved Banner tampil. Bila jam server dimajukan, jam server dan jam browser diatur bersama dan dipulihkan lewat langkah aksi sebelum asersi lain yang bergantung jam.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): draft Brand Client A dipulihkan ke 12 baris (Kontrak Fixture R2); umur draft atau jam server dipulihkan.
- Kemampuan teknis: skrip seed D-01; hook umur draft D-76.
- State global: umur draft atau jam server (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Import data (Create) melihat dan menghapus baris draft

1. Reset Client A lewat skrip fixture, seed draft Brand D-01 (12 baris `pending`), dan mundurkan umur draft 25 jam lewat hook umur draft (D-76 varian 1)
2. Muat ulang halaman Import > Brand
3. Verifikasi Unsaved Banner tampil pada halaman Import > Brand Import data (Create)
4. Verifikasi Staging Metric Cards Total Rows 12
5. Klik halaman 2 pada Pagination
6. Klik row action `⋯` pada Row # 12 lalu Remove
7. Klik `[Delete]` pada Dialog Delete Row
8. Verifikasi muncul toast sukses: "Success, row has been deleted."

### Total Control melihat hasilnya

9. Ganti akun: logout dari Import data (Create), lalu login sebagai Total Control Client A (Sari Dewi)
10. Buka halaman Import > Brand
11. Verifikasi Staging Metric Cards Total Rows 11
12. Klik halaman 2 pada Pagination
13. Verifikasi halaman 2 menampilkan Row # 11 `Cisco` saja ("Showing 11 - 11 of 11 items")
14. Verifikasi halaman 2 tidak memuat `Asus`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1 dan 2 (reset, seed D-01, umur draft D-76, muat ulang halaman) adalah langkah pembuka penghubung (S-03); langkah 3 mengasersi layar. Langkah 9 dan 10 adalah ganti akun eksplisit dan pembukaan layar akun kedua (S-07).
- Hasil aksi penghapusan (langkah 7) dipakai sebagai anchor bagi asersi Total Rows 11 di sesi kedua: toast sukses diasersi di langkah 8 sebelum ganti akun.
- Temuan untuk QA:
  - TC-GS-IMPORT-535 berada di Section 8a (security/defense-in-depth) namun bertipe Positive dan berupa alur fungsional (hapus baris oleh Create, dibaca Total Control); penempatan section meragukan.
  - TC-GS-IMPORT-535 Precondition d mensyaratkan umur draft >= 24 jam agar Unsaved Banner tampil, tetapi Expected hanya mengasersi banner di sesi Import data (Create); banner tidak diasersi di sesi Total Control.
  - TC-GS-IMPORT-535 Post Condition ("Draft Brand Client A dipulihkan ke 12 baris") tidak punya langkah observasi; ditulis sebagai cleanup di hook `after`, tanpa asersi.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
