---
id: TC-GS-USER-E2E-048-user-hasil-import
title: User hasil Import tampil dan bisa di-Edit sama seperti user buatan manual
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-417
  - TC-GS-USER-418
coverage:
  web: automated
---

# User hasil Import tampil dan bisa di-Edit sama seperti user buatan manual

## Prerequisites

- Login sebagai Role: Total Control, entity Client, dengan akses ke modul Import
- Berkas import Type "User Login" berisi satu baris valid untuk user "Contractor Import A" (First Name, Last Name, Email unik, Division, Access, dan Position atau Employee ID sesuai template)
- User manual "Budi Pembanding" yang dibuat lewat Create dengan struktur field yang setara, sebagai pembanding
- Spec ini membuat user "Contractor Import A" lewat Import dan mengubah Last Name-nya, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### User hasil Import di List dan Detail

1. Di modul Import, unggah berkas Type "User Login" dan proses sampai selesai
2. Buka User List dan cari "Contractor Import A"
3. Verifikasi baris tampil dengan kolom dan badge yang sama seperti baris "Budi Pembanding"
4. Klik nama "Contractor Import A" untuk membuka User Detail
5. Verifikasi User Detail terbuka dengan Header, Status Badge, dan section yang utuh, sama strukturnya dengan Detail "Budi Pembanding"

### Edit user hasil Import

6. Klik row action `Edit` pada baris "Contractor Import A"
7. Verifikasi Modal Edit pre-filled benar dan ter-normalisasi sama seperti record manual untuk First Name, Last Name, Division, Access, Position atau Employee ID, dan Custom Field
8. Ubah Last Name lalu klik `[Save]`
9. Verifikasi toast "Success, user has been updated." muncul
10. Buka Changelog "Contractor Import A"
11. Verifikasi ada satu baris Action "Edit", Field "Last Name", Old Value nama lama, dan New Value nama baru, dengan format yang sama seperti record manual

## Notes

- Alur unggah dan validasi Import diuji di modul Import. Spec ini hanya memastikan hasilnya perilaku operasional yang sama dengan user manual (`GAP-041`, prinsip P7-7b).
- Butuh berkas import yang dibuat tim FE sesuai template Import Type "User Login".
