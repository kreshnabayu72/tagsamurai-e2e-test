---
id: TC-GS-UCF-E2E-004-empty-state-entitas-tanpa-custom-field
title: "Empty State Entitas Tanpa Custom Field: Illustration, CTA Tidak Ada, dan Filter dengan No options available"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-9
  - TC-GS-UCF-543
coverage:
  web: automated
---

# Empty State Entitas Tanpa Custom Field: Illustration, CTA Tidak Ada, dan Filter dengan No options available

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup, Client C tanpa Custom Field dan tanpa Changelog). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite (`Spectra.env.GS_TC_PASSWORD`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > User List untuk akun Client C; tab Custom Field dibuka oleh langkah spec karena pembukaan tab adalah langkah TC-GS-UCF-9 dan 543.
- Data Pre-setup: Client C belum memiliki Custom Field (precondition TC-GS-UCF-9 dan 543); tidak diubah spec ini. Spec tidak membuat, mengubah, atau menghapus data. Tidak ada Data Dinamis.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Client C dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan teks Illustration (Title dan Description); pembacaan isi dropdown Filter Panel.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-9: Empty state genuinely kosong saat client belum punya Custom Field

1. Klik tab Custom Field
2. Verifikasi Illustration dengan Title `No custom fields yet`
3. Verifikasi Illustration dengan Description `Get started by creating your first custom field.`
4. Verifikasi tidak ada tombol CTA di dalam empty state
5. Verifikasi `[+ Custom Field]` tetap tampil di Table Tools

### TC-GS-UCF-543: Empty state katalog kosong, tombol Filter tetap tersedia dan dropdown opsi Filter menampilkan `No options available`

6. Klik tab User List, lalu klik tab Custom Field (membuka ulang tab Custom Field)
7. Verifikasi Illustration dengan Title `No custom fields yet`
8. Verifikasi Illustration dengan Description `Get started by creating your first custom field.`
9. Verifikasi tombol Filter tampil
10. Klik Filter
11. Verifikasi Filter Panel terbuka
12. Buka dropdown Active
13. Verifikasi dropdown Active menampilkan `No options available`
14. Verifikasi dropdown Active tidak menampilkan pesan error
15. Tutup dropdown Active
16. Buka dropdown Data Type
17. Verifikasi dropdown Data Type menampilkan `No options available`
18. Verifikasi dropdown Data Type tidak menampilkan pesan error
19. Tutup dropdown Data Type
20. Buka dropdown Required
21. Verifikasi dropdown Required menampilkan `No options available`
22. Verifikasi dropdown Required tidak menampilkan pesan error
23. Tutup dropdown Required
24. Buka dropdown Modified By
25. Verifikasi dropdown Modified By menampilkan `No options available`
26. Verifikasi dropdown Modified By tidak menampilkan pesan error
27. Tutup dropdown Modified By
28. Tutup Filter Panel

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Spec ini kelas fungsional pada entitas khusus (Client C kosong); seluruh asersi baca.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti TC sumber (9, 543). Langkah 1 TC-GS-UCF-543 ("Buka tab Custom Field") dijalankan ulang pada langkah 6 lewat klik tab User List lalu Custom Field karena TC-GS-UCF-9 sudah membuka tab itu.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (membuka ulang tab), langkah 12, 16, 20, dan 24 (membuka dropdown satu per satu, sesuai langkah 3 TC-GS-UCF-543), langkah 15, 19, 23, dan 27 (menutup dropdown), dan langkah 28 (menutup Filter Panel).
- Langkah 4 (tidak ada tombol CTA di dalam empty state) beranchor langkah 2 dan 3 yang membuktikan empty state tampil; langkah 5 membuktikan Table Tools tampil. Langkah 14, 18, 22, dan 26 (tidak ada pesan error) beranchor teks `No options available` pada dropdown yang sama.
- Kolom Filterable yang dipakai TC-GS-UCF-543 (`Active`, `Data Type`, `Required`, `Modified By`) mengikuti Expected c; kolom lain pada Filter Panel tidak diasersi.
- Temuan untuk QA:
  - TC-GS-UCF-543 langkah 3 menyebut "Buka dropdown ... satu per satu" tanpa menyebut cara menutup dropdown antar-buka; spec menutup tiap dropdown sebelum membuka berikutnya.
  - TC-GS-UCF-9 dan 543 tidak menyebut email dan password akun Total Control Client C selain data Pre-setup (`totalControl_automated_qaTeam3@qwertysystem.net`); env var `GS_CLIENTC_TC_PASSWORD` sudah terdaftar di `.env.example`.
