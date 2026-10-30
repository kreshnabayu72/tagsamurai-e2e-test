---
id: TC-GS-DIV-E2E-049-isolasi-konfigurasi-kolom-tabel-division-dan-modal-changelog
title: "Isolasi Konfigurasi Kolom: Tabel Division dan Modal Changelog"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-179
  - TC-GS-DIV-234
coverage:
  web: automated
---

# Isolasi Konfigurasi Kolom: Tabel Division dan Modal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Asersi spec ini menyangkut kolom, bukan kumpulan nama atau jumlah baris, sehingga Population D-02 tidak di-seed.
- Data Dinamis milik spec: Division `Isolasi Kolom {runId}-049` (Code auto-generate, tidak diasersi) dibuat lewat kemampuan seeding Division lewat API di hook `before` oleh akun Total Control (Sari D) agar Riwayat Changelog Division terisi (Modal Changelog menampilkan tabel, bukan empty state). Hook `after` menghapus Division tersebut lewat API tanpa berasumsi seeding berhasil penuh. Entri Changelog tidak dihapus (immutable).
- Kolom tabel Division: `Name`, `Code`, `Last Updated`. Kolom Modal Changelog (7 kolom default): `Date`, `Action`, `Division Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Preferensi kolom tiap tabel tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (PRD division.md §4.2e; prd-conventions.md §9.3).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Division dan Modal Changelog dikembalikan ke default (semua kolom tampil, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom di browser.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membuka Popup Setup Column pada tabel di dalam Modal Changelog lewat header kolom Actions (⋯); membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-DIV-179: Konfigurasi kolom tabel Division tidak memengaruhi tabel Changelog

1. Buka Popup Setup Column tabel Division lewat header Actions (⋯) lalu `Setup Column...`
2. Hilangkan centang `Code` (kolom lain tetap tercentang)
3. Klik `[Save]`
4. Klik icon Changelog di Table Tools
5. Verifikasi Modal Changelog tetap menampilkan seluruh 7 kolom: `Date`, `Action`, `Division Name`, `Field`, `Old Value`, `New Value`, `Modified By`
6. Tutup Modal Changelog lewat `[✕]`
7. Buka Popup Setup Column tabel Division lewat header Actions (⋯) lalu `Setup Column...`
8. Centang kembali `Code`
9. Klik `[Save]`

### TC-GS-DIV-234: Konfigurasi kolom Modal Changelog tidak memengaruhi tabel Division

10. Klik icon Changelog di Table Tools
11. Buka Popup Setup Column pada tabel Modal Changelog lewat header kolom Actions (⋯) lalu `Setup Column...`
12. Hilangkan centang `Field` (kolom lain tetap tercentang)
13. Klik `[Save]`
14. Tutup Modal Changelog lewat `[✕]`
15. Verifikasi tabel Division tetap menampilkan kolom `Name`, `Code`, `Last Updated`
16. Klik icon Changelog di Table Tools
17. Buka Popup Setup Column pada tabel Modal Changelog lewat header kolom Actions (⋯) lalu `Setup Column...`
18. Centang kembali `Field`
19. Klik `[Save]`
20. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE (Modal Changelog dimuat dari backend nyata; preferensi kolom disimpan di browser).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (179, 234) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 sampai 9 (menutup Modal Changelog dan mengembalikan kolom `Code` tabel Division yang di-hide pada TC-GS-DIV-179, supaya Expected TC-GS-DIV-234 "tabel Division tetap menampilkan `Name`, `Code`, `Last Updated`" berlaku pada konfigurasi default), serta langkah 16 sampai 20 (memulihkan kolom `Field` Modal Changelog dan menutup modal). Hook `after` sebagai cadangan.
- Langkah 1 sampai 3 TC-GS-DIV-179 menyembunyikan kolom lewat Popup Setup Column dan `[Save]` sesuai TC ("lalu Save"); langkah 11 sampai 13 TC-GS-DIV-234 memakai Setup Column pada Modal Changelog.
- Pembagian TC lintas spec: Setup Column tabel Division (TC-GS-DIV-171 sampai 178) ada di spec 047 dan 048; Setup Column Modal Changelog (TC-GS-DIV-213 sampai 220) ada di spec 061 dan 062.
- Temuan untuk QA:
  - TC-GS-DIV-179 dan 234: Precondition TC-GS-DIV-234 ("Riwayat Changelog terisi dengan Modified By Sari D, Rina M, Agus W, Dewi L") tidak diperlukan oleh asersinya; spec hanya memerlukan riwayat tidak kosong dan menyediakannya lewat satu Division seeding oleh Sari D. Spec mengasumsikan seeding Division lewat API menghasilkan entri Create di Changelog seperti Create lewat UI; TC dan PRD tidak menyatakannya.
  - TC-GS-DIV-179 dan 234: TC-GS-DIV-179 menyembunyikan kolom `Code` sedangkan Expected TC-GS-DIV-234 menyebut `Code` tampil; spec memulihkan `Code` di antara kedua TC (langkah 7 sampai 9) karena TC tidak menyatakan pemulihan itu.
  - Hasil TC-GS-DIV-179 tidak mengasersi tabel Division menyembunyikan `Code` setelah `[Save]` (tidak ada di Expected); hanya isolasi ke Modal Changelog yang diasersi.
  - Mekanisme menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
