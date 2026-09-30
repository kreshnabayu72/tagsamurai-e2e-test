---
id: TC-GS-USER-E2E-064-custom-field-inline-edit
title: 'Ubah Custom Field langsung di User Detail dengan inline-edit'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-374
  - TC-GS-USER-375
  - TC-GS-USER-376
  - TC-GS-USER-377
  - TC-GS-USER-378
  - TC-GS-USER-379
  - TC-GS-USER-120
  - TC-GS-USER-119
coverage:
  web: automated
---

# Ubah Custom Field langsung di User Detail dengan inline-edit

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Budi Santoso" punya Custom Field aktif `Blood Type` (bertipe teks) dengan value existing, `Phone` (format Phone), satu Custom Field tidak Required yang belum diisi (`Hobi`), dan satu Custom Field Required yang belum diisi (`Golongan`)
- Spec ini mengubah value `Blood Type` pada langkah akhir dan mengembalikannya

## Test Steps

### State Display

1. Buka User Detail "Budi Santoso" lalu expand Section Custom Fields
2. Verifikasi `Hobi` menampilkan `—` tanpa alert dan ikon `Edit2Line` belum tampil sebelum di-hover
3. Verifikasi `Golongan` menampilkan alert "Golongan is required." menggantikan `—`, dan ikon `Edit2Line` langsung tampil tanpa hover

### Masuk state Active dan Cancel

4. Hover baris `Blood Type` lalu klik ikon `Edit2Line`
5. Verifikasi ikon muncul rata kanan saat hover, dan setelah klik baris berubah menjadi widget input sesuai Data Type dengan ikon `[✓ Save]` dan `[✕ Cancel]`
6. Ubah value lalu klik `[✕ Cancel]`
7. Verifikasi baris kembali ke state Display dengan value lama, dan tidak ada permintaan perubahan yang terkirim

### Multi-field dan validasi

8. Klik ikon `Edit2Line` pada `Blood Type`, lalu klik ikon `Edit2Line` pada `Phone` tanpa menutup `Blood Type`
9. Verifikasi kedua field berada di state Active bersamaan dengan widget, `[✓ Save]`, dan `[✕ Cancel]` masing-masing independen
10. Isi `Phone` dengan `abc123` lalu klik `[✓ Save]` pada `Phone`
11. Verifikasi inline error format Phone sesuai daftar validasi `user.md` bagian 6 muncul, value `Phone` tidak berubah, dan `Blood Type` tetap Active tanpa terganggu
12. Klik `[✕ Cancel]` pada `Phone` lalu verifikasi `Blood Type` tetap Active
13. Klik ikon `Edit2Line` pada `Golongan`, kosongkan value lalu klik `[✓ Save]`
14. Verifikasi inline error "Golongan must not be empty" muncul, field tetap Active, dan value tidak tersimpan kosong
15. Klik `[✕ Cancel]` pada `Golongan`

### Simpan (mengubah data)

16. Pada `Blood Type` yang masih Active, isi value baru `O+` lalu klik `[✓ Save]`
17. Verifikasi toast "Success, Blood Type has been updated." muncul, baris kembali ke Display dengan `O+`, dan field lain tidak berubah
18. Buka Tab Changelog user "Budi Santoso"
19. Verifikasi ada baris Action `Edit` dengan Field `Blood Type`, Old value lama, New `O+`, dan Modified By admin yang login
20. Kembalikan value `Blood Type` ke nilai awal lewat inline-edit yang sama

## Notes

- Sumber `user.md` bagian 4.1, 4.3, 6, dan 7. Aturan validasi memakai Data Type yang sama dengan definisi Custom Field, bukan validator baru.
- Teks alert Required mengikuti pola "[Field Name] is required." dari TC sumber (`TC-GS-USER-378`), dan inline error kosong mengikuti "[Field Name] must not be empty" (`TC-GS-USER-379`). Kedua teks mengikuti label field.
- Save gagal server (500) dicakup di antrean spec `Mode: mock` (`TC-GS-USER-577`). Guard aktor dicakup `TC-GS-USER-E2E-065-custom-field-inline-edit-guard-aktor`, dan race field dinonaktifkan dicakup `TC-GS-USER-E2E-066-custom-field-inline-edit-race`.
- Aksi yang mengubah data ditaruh paling akhir.
