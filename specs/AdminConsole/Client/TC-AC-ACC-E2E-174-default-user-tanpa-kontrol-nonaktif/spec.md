---
id: TC-AC-ACC-E2E-174-default-user-tanpa-kontrol-nonaktif
title: "Default User Tidak Dapat Dinonaktifkan dan Detail Client Tanpa Kontrolnya"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-459
  - TC-AC-ACC-241
coverage:
  web: automated
---

# Default User Tidak Dapat Dinonaktifkan dan Detail Client Tanpa Kontrolnya

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): C-01 "PT Sejahtera Abadi" dengan Default User Activated (Sari Wulandari, akun A-16). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja; spec tidak membuat atau mengubah data. Cara membuka Global Settings > User milik tenant Client dari akun Principal tidak dijelaskan TC (lihat Temuan untuk QA); kemampuan itu disediakan tim FE.

## Test Steps

### TC-AC-ACC-459: Detail Client tidak menyediakan kontrol untuk mencabut Total Control atau menonaktifkan Default User

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Amati Section "Default User"
4. Verifikasi Section "Default User" menampilkan Name, Email, Division, Position, dan badge "Activated"
5. Verifikasi tidak ada tombol, toggle, atau menu untuk menonaktifkan Default User atau mengubah tingkat aksesnya di Section "Default User"
6. Verifikasi `[Resend Activation Email]` Hidden

### TC-AC-ACC-241: Default User tidak dapat dinonaktifkan: Toggle Active dan Delete baris Default User disabled

7. Buka Global Settings > User tenant "PT Sejahtera Abadi"
8. Verifikasi baris Default User tampil di daftar user tenant
9. Arahkan kursor ke Toggle Active baris Default User
10. Verifikasi Toggle Active tampil dan berstatus disabled dengan tooltip "Default User cannot be modified."
11. Arahkan kursor ke row action Delete baris Default User
12. Verifikasi row action Delete tampil dan berstatus disabled dengan tooltip "Default User cannot be modified."

## Notes

- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Absence pada TC-459 (tidak ada kontrol nonaktif, `[Resend Activation Email]` Hidden) memakai Verifikasi Section "Default User" (nama, email, badge) pada surface yang sama sebagai anchor positif.
- Temuan untuk QA (S-15): TC-241 menulis Langkah "Buka Global Settings > User tenant "PT Sejahtera Abadi"" tanpa menyebut mekanisme membuka Global Settings milik tenant Client dari akun Total Control (Principal); Precondition juga menyebut Detail "PT Sejahtera Abadi" sebagai lokasi awal. Spec mengikuti redaksi TC. Post Condition kedua TC `-` sehingga tidak diasersi.
