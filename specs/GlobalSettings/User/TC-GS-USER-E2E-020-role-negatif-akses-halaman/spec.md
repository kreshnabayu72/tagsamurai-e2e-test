---
id: TC-GS-USER-E2E-020-role-negatif-akses-halaman
title: Visibilitas menu dan akses halaman User menurut role
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-486
  - TC-GS-USER-10
  - TC-GS-USER-12
  - TC-GS-USER-11
coverage:
  web: automated
---

# Visibilitas menu dan akses halaman User menurut role

## Prerequisites

Bagian pertama spec ini dijalankan untuk setiap role pada tabel. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji pada bagian visibilitas menu:

| Role | Akun | Menu `User` di sidebar |
|---|---|---|
| Read Only | `readOnlyGlobalSettings_automated_qaTeam1` | Tampil |
| No Role | `noRoleGlobalSettings_automated_qaTeam1` | Hidden |

- Entity Client
- Akun `noRoleGlobalSettings_automated_qaTeam1` punya Access yang mencakup Global Settings, tetapi belum diberi role apa pun dan bukan Total Control maupun Read Only
- URL User List diketahui

## Test Steps

### Visibilitas menu

Lakukan langkah 1–2 untuk setiap role pada tabel "Role yang diuji".

1. Login sebagai role yang diuji
2. Verifikasi item sidebar `User` sesuai kolom "Menu `User` di sidebar" pada tabel

### Landing state dan akses langsung (role No Role)

3. Login sebagai `noRoleGlobalSettings_automated_qaTeam1`
4. Verifikasi login berhasil
5. Verifikasi sidebar Global Settings menampilkan 0 menu
6. Verifikasi area konten menampilkan illustration dan pesan akses kosong
7. Ketik atau tempel URL User List langsung di address bar, tanpa klik menu
8. Verifikasi server membalas 403 Forbidden
9. Verifikasi toast error "You don't have permission to do this." muncul
10. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tetap tersembunyi
11. Verifikasi halaman tidak dialihkan ke halaman unauthorized yang terpisah

## Notes

- Ini spec negatif akses halaman dari Role Matrix (`docs/e2e-conventions.md` bagian 3a).
- TC-GS-USER-10 dan TC-GS-USER-12 diperlakukan sebagai kondisi akun yang sama (Access mencakup Global Settings, tanpa role): TC-10 melihat item `User`, TC-12 melihat seluruh sidebar dan isi halaman. Kondisi ketiga, user tanpa Access Global Settings sama sekali, tidak diuji karena tidak bisa masuk halaman ini.
- Ekspektasi TC-GS-USER-11 mengikuti default `error-handling-convention.md` bagian 2, karena PRD modul diam soal ini.
- Cara skrip menjalankan banyak role diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-020, 021, 022). TC-GS-USER-486 tidak punya padanan frontend. TC-GS-USER-10 dan 11 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.
