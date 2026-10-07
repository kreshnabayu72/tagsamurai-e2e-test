---
id: TC-GS-DIV-E2E-059-tabel-utama-setup-column-reset-cancel-save-fase-3
title: "Setup Column Tabel Utama Fase 3: Reset to Default, Pembatalan Cancel/Esc, dan Penyimpanan Permanen di Browser per Pengguna"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-175
  - TC-GS-DIV-176
  - TC-GS-DIV-177
coverage:
  web: automated
---

# Setup Column Tabel Utama Fase 3: Reset to Default, Pembatalan Cancel/Esc, dan Penyimpanan Permanen di Browser per Pengguna

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Modal Setup Column terbuka dengan perubahan staged
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)
- Susunan kolom sudah diubah dan disimpan

## Test Steps

### Setup Column: pin dan unpin tiap kolom lalu Save (TC-GS-DIV-175)

1. Buka Popup Setup Column
2. Klik icon pin pada `Name`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Name` dan Save
3. Klik icon pin pada `Code`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Code` dan Save
4. Klik icon pin pada `Last Updated`, klik `[Save]`, scroll tabel horizontal, lalu unpin `Last Updated` dan Save
5. Verifikasi Name: kolom `Name` membeku (sticky) saat scroll horizontal setelah Save
6. Verifikasi Code: kolom `Code` membeku (sticky) saat scroll horizontal setelah Save
7. Verifikasi Last Updated: kolom `Last Updated` membeku (sticky) saat scroll horizontal setelah Save
8. Verifikasi Setelah F5 pin terakhir yang disimpan tetap berlaku

### Setup Column: Reset to Default mengembalikan susunan default (TC-GS-DIV-176)

9. Buka Popup Setup Column
10. Klik `[Reset to Default]`
11. Klik `[Save]`
12. Muat ulang halaman (F5)
13. Verifikasi Preview kembali ke default: `Name`, `Code`, `Last Updated` seluruhnya visible tanpa pin
14. Verifikasi Setelah Save dan F5 susunan default bertahan

### Setup Column: Cancel dan X membuang perubahan preview (TC-GS-DIV-177)

15. Buka Popup Setup Column
16. Hilangkan centang `Code`
17. Klik `[✕]`
18. Buka kembali Popup Setup Column, hilangkan centang `Code`, tutup lewat tombol Esc
19. Verifikasi Setelah ditutup tanpa Save tabel kembali memakai konfigurasi tersimpan terakhir (kolom `Code` tampil)

## Notes

- Memvalidasi Fase 3 Setup Column: tombol [Reset to Default], pembatalan tanpa menyimpan via [✕]/Esc membuang perubahan staged, dan klik [Save] menyimpan konfigurasi kolom secara permanen di browser local storage (PRD §4.2e).
- Sumber pemetaan test case granular: TC-GS-DIV-175, TC-GS-DIV-176, TC-GS-DIV-177.
