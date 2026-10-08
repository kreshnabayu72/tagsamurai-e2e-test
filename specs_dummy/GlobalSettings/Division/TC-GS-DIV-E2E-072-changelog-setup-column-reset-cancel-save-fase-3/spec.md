---
id: TC-GS-DIV-E2E-072-changelog-setup-column-reset-cancel-save-fase-3
title: "Setup Column Modal Changelog Fase 3: Reset to Default, Pembatalan Cancel/X, Penyimpanan Browser, dan Independensi dari Tabel Utama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-218
  - TC-GS-DIV-219
  - TC-GS-DIV-234
coverage:
  web: automated
---

# Setup Column Modal Changelog Fase 3: Reset to Default, Pembatalan Cancel/X, Penyimpanan Browser, dan Independensi dari Tabel Utama

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Modal Changelog terbuka
- Konfigurasi kolom Changelog sudah diubah
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)
- Konfigurasi kolom Changelog sudah diubah dan disimpan

## Test Steps

### Setup Column Modal Changelog: Reset to Default (TC-GS-DIV-218)

1. Klik icon Changelog di Table Tools
2. Buka Popup Setup Column
3. Klik `[Reset to Default]`
4. Klik `[Save]`
5. Verifikasi Susunan kolom kembali ke default 7 kolom visible tanpa pin

### Setup Column Modal Changelog: Cancel dan X membuang perubahan (TC-GS-DIV-219)

6. Klik icon Changelog di Table Tools
7. Buka Popup Setup Column
8. Hilangkan centang `Field`
9. Klik `[✕]`
10. Verifikasi Setelah ditutup tanpa Save kolom `Field` tetap tampil

### Konfigurasi kolom Modal Changelog tidak memengaruhi tabel Division (TC-GS-DIV-234)

11. Klik icon Changelog di Table Tools
12. Sembunyikan kolom `Field` lewat Setup Column lalu Save
13. Tutup modal dan lihat kolom tabel Division
14. Verifikasi Tabel Division tetap menampilkan `Name`, `Code`, `Last Updated` (cache per tabel independen)

## Notes

- Memvalidasi Fase 3 Setup Column Modal Changelog: tombol [Reset to Default] mengembalikan 7 kolom ke default tanpa pin, tombol Cancel / icon [✕] membuang perubahan draft, tombol [Save] menyimpan konfigurasi ke browser storage per user, dan jaminan independensi konfigurasi kolom Changelog dari tabel utama Division (PRD §4.1.2, §4.2e).
- Sumber pemetaan test case granular: TC-GS-DIV-218, TC-GS-DIV-219, TC-GS-DIV-234.
