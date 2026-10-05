---
id: TC-AUTH-ACT-E2E-018-resend-multiple-race-zero-logging
title: Multiple resend, race condition, dan zero-logging konsekuensi resend
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-64
  - TC-AUTH-ACT-65
  - TC-AUTH-ACT-66
coverage:
  web: automated
---

# Multiple resend, race condition, dan zero-logging konsekuensi resend

## Prerequisites

- User dengan status `Pending Activation` dan token `active` tersedia.
- Akses admin untuk melakukan Resend Activation Email (via UI/API).
- Kemampuan simulasi timing untuk race condition.
- Akses keempat surface log: Activity Log > Session, User Log, System Log, Changelog (count-based comparison).

## Test Steps

### A. Multiple resend berturut-turut

1. Siapkan user dengan token `active`. Lakukan Resend Activation Email sebanyak 3 kali berturut-turut.
2. Verifikasi setelah 3x resend, hanya token terakhir yang memiliki `status=active`.
3. Verifikasi **semua** token sebelumnya (pertama, kedua, dan tiap token yang di-supersede) memiliki `status=superseded`. Tidak hanya token kedua-terakhir.

### B. Race condition: submit bersamaan dengan resend

4. Siapkan user dengan token `active` (token T0). Buka halaman Set Password dengan token T0, form siap di-submit.
5. Picu race condition: lakukan Resend Activation Email (membuat token T1, supersede T0) bersamaan/segera sebelum submit form dengan token T0.
6. Amati outcome: salah satu harus menang secara atomik. Tidak ada dua-duanya "berhasil" dengan token yang sama.
7. Verifikasi salah satu terpenuhi: (a) submit tervalidasi duluan → sukses dengan T0, T1 tetap active & terpisah; atau (b) resend duluan → submit dengan T0 gagal dan redirect 404, T1 tetap active & T0 superseded.
8. Verifikasi tidak ada state campuran.

### C. Zero-logging konsekuensi resend

9. Catat baseline jumlah entri pada keempat surface log (Activity Log > Session, User Log, System Log, Changelog).
10. Admin melakukan Resend Activation Email untuk user dengan token `active`.
11. Catat ulang jumlah entri pada keempat surface log.
12. Verifikasi tidak ada entri log baru dari sisi Activation Feature terkait konsekuensi invalidasi token ini (jumlah entri tetap sama). Catatan: aksi admin resend sendiri (jika ada) bisa dicatat di modul lain, bukan scope fitur Activation.

## Notes

- Semua token sebelumnya harus di-supersede (bukan hanya terakhir).
- Race condition menjamin atomicity - submit dengan token yang sedang di-supersede harus ditolak.
