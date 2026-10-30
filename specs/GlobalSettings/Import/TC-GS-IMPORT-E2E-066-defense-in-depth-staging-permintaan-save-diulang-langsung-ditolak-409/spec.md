---
id: TC-GS-IMPORT-E2E-066-defense-in-depth-staging-permintaan-save-diulang-langsung-ditolak-409
title: "Defense-in-depth Staging: Permintaan Save Diulang Langsung Ditolak 409 dan Nilai Melebihi Batas yang Disuntikkan Melewati Validasi FE Tidak Tersimpan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-667
  - TC-GS-IMPORT-677
coverage:
  web: automated
---

# Defense-in-depth Staging: Permintaan Save Diulang Langsung Ditolak 409 dan Nilai Melebihi Batas yang Disuntikkan Melewati Validasi FE Tidak Tersimpan

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Klien HTTP: permintaan langsung ke server dengan token sesi akun uji; token diperoleh lewat login API yang disediakan tim FE/BE. Kemampuan teknis lain: menangkap permintaan Save beserta id sesi edit dari lalu lintas jaringan halaman, dan menyetel nilai input langsung ke DOM (melewati validasi FE).
- Akun: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, Row # 2 `Lenovo`). Nama baris salinan TC-GS-IMPORT-667 bersuffix per run: `Lenovo Group {runId}-066`.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft D-01 dipulihkan sesudah TC-GS-IMPORT-667 yang menambah satu baris (Kontrak Fixture R2).

## Test Steps

### TC-GS-IMPORT-677: Nilai melebihi batas disuntikkan melewati validasi FE

1. Klik `⋯` pada baris #1
2. Pilih Edit
3. Ubah nilai input Brand Name baris #1 menjadi `A` diulang 121 kali lewat injeksi nilai langsung ke DOM (melewati validasi FE)
4. Klik `[Save]`
5. Verifikasi sel Brand Name baris #1 berborder `danger`
6. Verifikasi sel Brand Name baris #1 menampilkan pesan "Max. 120 characters"
7. Verifikasi toast sukses tidak tampil
8. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes
9. Muat ulang halaman Import > Brand
10. Verifikasi baris #1 menampilkan `Acme Corp` (nilai 121 karakter tidak tersimpan)

### TC-GS-IMPORT-667: Permintaan Save sesi Duplicate yang diulang ditolak 409

11. Klik `⋯` pada baris #2
12. Pilih Duplicate
13. Ubah Brand Name salinan menjadi `Lenovo Group {runId}-066`
14. Klik `[Save]` dan tangkap permintaan Save beserta id sesi edit
15. Kirim ulang permintaan Save yang sama (id sesi edit sama) langsung ke server dengan token akun Total Control Client A
16. Verifikasi respons permintaan kedua berupa penolakan 409 Conflict
17. Muat ulang halaman Import > Brand
18. Verifikasi draft tetap 13 baris dengan tepat satu baris `Lenovo Group {runId}-066`
19. Verifikasi footer `[Import (13)]`
20. Pulihkan draft Client A ke D-01 (hapus baris `Lenovo Group {runId}-066`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (kelas a, prinsip 13a); TC-GS-IMPORT-677 menyuntikkan nilai ke DOM, TC-GS-IMPORT-667 mengirim ulang permintaan langsung ke server (hanya status respons dan state data diasersi).
- Urutan blok: TC-GS-IMPORT-677 lebih dulu karena tidak mengubah draft; TC-GS-IMPORT-667 menambah satu baris sehingga di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 (`[Cancel]` lalu `[Discard]`), langkah 9 dan 17 (muat ulang), langkah 20 (pemulihan draft).
- Sesi edit TC-GS-IMPORT-677 ditutup di langkah 8 sebelum muat ulang (S-08, S-09): nilai 121 karakter yang tidak tersimpan dibuang lewat dialog Discard Changes sehingga muat ulang tidak berjalan dengan sesi edit dirty dan tidak membutuhkan penanganan dialog `beforeunload`.
- Langkah 7 (absence toast sukses) memakai border `danger` dan pesan error langkah 5 dan 6 sebagai anchor.
- Temuan untuk QA:
  - Nama baris salinan `Lenovo Group` pada TC-GS-IMPORT-667 ditulis bersuffix per run di spec; Expected TC menyebut nama tanpa suffix.
  - TC-GS-IMPORT-667 menyebut "id sesi edit" tanpa menyebut sumbernya; spec menuliskannya sebagai id yang ditangkap dari lalu lintas jaringan halaman.
