---
id: TC-GS-IMPORT-E2E-055-kunci-sesi-edit-izin-create-dicabut-saat-sesi-edit-aktif-save-ditolak
title: "Kunci Sesi Edit: Izin Create Dicabut saat Sesi Edit Aktif, Save Ditolak 403, Dialog Draft Is Being Edited, Kunci Dilepas lewat TTL 10 Menit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-607
coverage:
  web: automated
---

# Kunci Sesi Edit: Izin Create Dicabut saat Sesi Edit Aktif, Save Ditolak 403, Dialog Draft Is Being Edited, Kunci Dilepas lewat TTL 10 Menit

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah capability role dan state kunci; lihat `suite.md`.
- Dua sesi browser (konteks kedua menjadi objek asersi): sesi Import data (Create) Client C dan sesi Total Control Client C pada konteks browser terpisah.
  - Import data (Create) Client C (Kiki Amalia) `importCreate_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_IMPORTCREATE_PASSWORD`; login di hook `before`.
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, `Spectra.env.GS_CLIENTC_TC_PASSWORD`; dibuka di sesi browser terpisah pada langkah 9.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup sesi Total Control dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client C): D-18 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`), dibuat lewat skrip fixture; pembaca status respons HTTP permintaan Save (pengamatan jaringan tanpa mock).
- Kemampuan teknis yang disediakan tim FE/BE: fixture Role & Permission untuk mencabut capability Import data (Create) dari akun uji (capability Read tetap aktif) dan memulihkannya; fixture timestamp untuk mengatur kedaluwarsa kunci sesi edit akun uji ke waktu yang sudah lewat (batas persis lewat timestamp, bukan jam server).
- State global yang diubah dan dipulihkan: capability role akun Import data (Create) Client C (dipulihkan di hook `after` walau spec gagal); kunci sesi edit.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

### TC-GS-IMPORT-607

1. [Sesi Import data (Create)] Klik `[⋯]` pada baris #1
2. [Sesi Import data (Create)] Pilih Edit
3. [Sesi Import data (Create)] Ubah Brand Name baris #1 dari `Acme Corp` menjadi `Acme Corporation` tanpa menyimpan
4. Cabut capability Import data (Create) dari akun uji lewat fixture (capability Read tetap aktif)
5. [Sesi Import data (Create)] Klik `[Save]`
6. [Sesi Import data (Create)] Verifikasi server menolak Save dengan 403 Forbidden
7. [Sesi Import data (Create)] Verifikasi toast error: "You don't have permission to do this."
8. [Sesi Import data (Create)] Muat ulang halaman Import
9. [Sesi Import data (Create)] Verifikasi baris #1 tetap berisi `Acme Corp`
10. Buka sesi browser terpisah sebagai Total Control Client C
11. [Sesi Total Control] Buka menu Import dari sidebar
12. [Sesi Total Control] Klik `[⋯]` pada baris #1
13. [Sesi Total Control] Pilih Edit
14. [Sesi Total Control] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[OK]`
15. [Sesi Total Control] Klik `[OK]`
16. Atur kedaluwarsa kunci sesi edit akun uji ke waktu yang sudah lewat lewat fixture timestamp
17. [Sesi Total Control] Klik `[⋯]` pada baris #1
18. [Sesi Total Control] Pilih Edit
19. [Sesi Total Control] Verifikasi sesi edit Total Control dimulai: baris #1 menjadi input dan footer menampilkan `[Cancel]` dan `[Save]`
20. [Sesi Total Control] Verifikasi tidak ada dialog konflik
21. [Sesi Total Control] Klik `[Cancel]` pada footer
22. [Sesi Total Control] Verifikasi sesi edit Total Control berakhir tanpa dialog
23. [Sesi Total Control] Verifikasi footer menampilkan kembali `[Import (12)]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji fixture timestamp TTL 10 menit dan perubahan capability).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 dan 16 (fixture capability dan timestamp); langkah 8 (muat ulang); langkah 10 (membuka sesi browser kedua).
- Langkah 20 (absence dialog konflik) memakai sesi edit yang dimulai pada langkah 19 sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-IMPORT-607 memuat tiga topik dalam satu TC (izin dicabut di tengah sesi edit, dialog konflik Draft Is Being Edited, pelepasan kunci lewat TTL 10 menit); spec mempertahankan satu TC satu spec.
  - Status 403 pada langkah 6 diamati dari respons permintaan Save yang dikirim FE; TC tidak menyebut cara mengamati status itu selain Expected a.
