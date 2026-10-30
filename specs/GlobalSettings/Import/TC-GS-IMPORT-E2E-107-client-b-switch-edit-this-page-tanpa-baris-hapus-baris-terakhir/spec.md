---
id: TC-GS-IMPORT-E2E-107-client-b-switch-edit-this-page-tanpa-baris-hapus-baris-terakhir
title: "Client B: Switch Edit this page tanpa baris, hapus baris terakhir menghapus draft, Remove dari halaman basi setelah draft terhapus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-195
  - TC-GS-IMPORT-276
  - TC-GS-IMPORT-277
coverage:
  web: automated
---

# Client B: Switch Edit this page tanpa baris, hapus baris terakhir menghapus draft, Remove dari halaman basi setelah draft terhapus

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Penghapus draft kedua (hanya memicu perubahan state, P-2): sesi API dengan akun Total Control Client B yang sama pada konteks terpisah; klien HTTP disediakan tim FE/BE.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client B.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client B: tanpa data master dan tanpa draft pada keadaan awal (Kontrak Fixture R1).
- Data Dinamis: D-33 (Draft Brand 1 baris `pending` `Nikon` Client B dari `brand-1.csv`), dibuat lewat skrip fixture sebelum TC-276 dan sebelum TC-277 (Kontrak Fixture R1); nama literal karena asersi bergantung pada isi.
- Kemampuan teknis: dua tab browser pada akun yang sama (Tab 1 basi, Tab 2 tidak dipakai; pemicu penghapusan lewat sesi API), skrip seed D-33 dan reset draft (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client B dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): buang draft Brand Client B.

## Test Steps

### TC-GS-IMPORT-195: Switch Edit this page saat belum ada baris

1. Arahkan kursor ke Switch `Edit this page`
2. Verifikasi Switch `Edit this page` tampil Disabled
3. Verifikasi tooltip tidak muncul saat hover

### TC-GS-IMPORT-276: Menghapus baris terakhir menghapus draft

4. Seed draft D-33 di Client B lewat skrip fixture, lalu muat ulang halaman Import > Brand
5. Klik `⋯` pada baris #1, pilih `Remove`
6. Klik `[Delete]`
7. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
8. Verifikasi Unsaved Banner tidak tampil
9. Muat ulang halaman Import > Brand
10. Verifikasi Dropzone tetap tampil
11. Verifikasi Unsaved Banner tidak tampil

### TC-GS-IMPORT-277: Remove dari halaman basi setelah draft terhapus

12. Seed draft D-33 di Client B lewat skrip fixture, lalu muat ulang halaman Import > Brand (Tab 1)
13. Verifikasi baris #1 `Nikon` tampil pada Tab 1
14. Penghapus draft kedua menghapus baris #1 lewat sesi API hingga tersimpan
15. Pada Tab 1 (belum dimuat ulang): klik `⋯` pada baris #1, pilih `Remove`
16. Klik `[Delete]`
17. Verifikasi muncul toast netral: "This draft is no longer available."
18. Verifikasi halaman Tab 1 me-refresh ke state belum ada draft: Dropzone tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; penghapus draft kedua hanya pemicu (P-2, sesi API), Tab 1 yang diasersi hanya satu konteks UI.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-195 pertama (screening tanpa draft), TC-276 (menghapus draft) sebelum TC-277; TC-277 memakai D-33 baru.
- Langkah penghubung (tanpa `Verifikasi`): langkah 4 dan 12 menyiapkan D-33; langkah 14 menjalankan Langkah 2 sampai 5 TC-277 (Tab 2 membuka halaman dan menghapus) sebagai penghapusan lewat sesi API, bukan sesi UI kedua (P-2).
- Pembagian TC lintas spec: TC-GS-IMPORT-258 sampai 260 dan 686 (Remove baris) ada di spec 108.
- Temuan untuk QA:
  - TC-GS-IMPORT-195 Precondition menyebut Client B tanpa draft, tetapi Expected menyatakan Switch `Edit this page` tampil Disabled; state "tidak ada baris" menurut PRD §7.1 menampilkan Dropzone, bukan Staging Table, sehingga tidak jelas di mana Switch itu tampil. Perlu klarifikasi PRD; spec mengikuti Expected TC.
  - TC-GS-IMPORT-277 Langkah 2 sampai 5 memakai Tab 2 sebagai sesi UI kedua; spec menggantinya dengan sesi API (P-2) karena hasil di Tab 2 tidak diasersi.
  - Post Condition kosong; tidak ada yang diasersi.
