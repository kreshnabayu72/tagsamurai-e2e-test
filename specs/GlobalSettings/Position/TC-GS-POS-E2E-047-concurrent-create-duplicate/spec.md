---
id: TC-GS-POS-E2E-047-concurrent-create-duplicate
title: Concurrent Create Duplicate Antar Dua Aktor
priority: High
caseType: Edge Case
status: draft
sourceTc:
  - TC-GS-POS-83
coverage:
  web: automated
---

# Concurrent Create Duplicate Antar Dua Aktor

## Prerequisites

- Dua sesi browser bersamaan (`adminA`, `adminB`), keduanya login sebagai Role Total Control (kredensial sama dari `Spectra.env.ADMIN_USERNAME`/`ADMIN_PASSWORD`).
- Nama Position unik yang belum ada: `P-Dup-Race`.

## Test Steps

### A. Persiapan

1. Verifikasi `P-Dup-Race` belum ada di tabel Position.

### B. Create bersamaan (race)

2. Di sesi `adminA`, buka form Create Position, isi Name = `P-Dup-Race`, belum Submit.
3. Di sesi `adminB`, buka form Create Position, isi Name = `P-Dup-Race`, belum Submit.
4. Submit form di `adminA` terlebih dahulu (atau hampir bersamaan). Amati hasil.
5. Segera Submit form di `adminB` (setelah `adminA` submit, dalam waktu sangat dekat).
6. Amati hasil kedua submit.

### C. Verifikasi hasil

7. Verifikasi hanya ada **satu** record `P-Dup-Race` di tabel Position (tidak ada duplikat).
8. Verifikasi salah satu submit menghasilkan sukses, submit lainnya menghasilkan validasi duplikat (atau pesan error duplikat sesuai aplikasi).
9. Verifikasi tidak ada partial state, toast sesuai hasil masing-masing sesi.
10. Verifikasi logging konsisten (hanya Create pertama yang tercatat di tiga surface, atau sesuai perilaku transaksi).

## Notes

- Menguji proteksi unik pada level DB/API saat create bersamaan (race condition). Harus ada guard uniqueness (constraint) yang mencegah duplikasi.
