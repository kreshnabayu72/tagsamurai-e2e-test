---
id: TC-GS-GSET-E2E-045-client-suspended-write-diblokir
title: "Client suspended/expired: form terlihat, write diblokir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-146
coverage:
  web: automated
---

# Client suspended/expired: form tampil namun aksi tulis 403

## Prerequisites

- Environment menyediakan tenant dalam status `suspended`/`expired` (capability account) yang
  dijadikan objek.
- Admin pada tenant tersebut masih dapat login (state auth konsisten).

## Test Steps

1. Buka `Global Settings > General Settings` sebagai admin tenant suspended
2. Verifikasi halaman form masih tampil dan kelima field dapat dibaca
3. Ubah nilai salah satu field (misal `Session Idle Timeout` menjadi `1 hour`)
4. Klik `[Save]`
5. Verifikasi respons server menolak (403/error), tampil toast error yang sesuai (misal
   `Error, failed to save general settings.`)
6. Verifikasi perubahan tidak tersimpan: muat ulang halaman dan nilai field kembali nilai lama
7. Verifikasi tidak ada kerusakan UI saat error (halaman tetap tersusun, tombol `[Save]` kembali
   aktif)
8. Verifikasi Modal Changelog tetap dapat dibuka untuk data tersimpan sebelumnya

## Notes

- Perilaku read-only karena capability status account berbeda dengan Role Matrix (spec 008) dan tidak
  tercampur: di sini akses baca tetap boleh, tetapi write-terlarang.