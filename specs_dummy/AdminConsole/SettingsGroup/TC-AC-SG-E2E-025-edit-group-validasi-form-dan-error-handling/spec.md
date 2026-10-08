---
id: TC-AC-SG-E2E-025-edit-group-validasi-form-dan-error-handling
title: "Validasi form Edit Group: nama kosong, duplikat sibling, dan penanganan kegagalan simpan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-52
  - TC-AC-SG-53
  - TC-AC-SG-55
coverage:
  web: automated
---

# Validasi form Edit Group: nama kosong, duplikat sibling, dan penanganan kegagalan simpan

## Prerequisites

- Login sebagai Role: Total Control
- Node target `"Region A"` dan sibling `"Region B"` pada parent yang sama

## Test Steps

### Validasi Nama Kosong saat Edit
1. Klik elipsis `[⋯]` pada baris `"Region A"` lalu pilih `[Edit]`
2. Kosongkan nilai field Group Name lalu klik `[Save]`
3. Verifikasi pesan error inline `"Group name must not be empty"` muncul di bawah input
### Validasi Duplikat Sibling (Exclude Self)
4. Ubah nama menjadi `"region b"` (nama milik sibling lain, huruf kecil)
5. Verifikasi muncul pesan error inline `"Group name already exists in this level"`
6. Ubah kembali nama menjadi `"Region A"` (nama dirinya sendiri)
7. Verifikasi pesan error duplikat TIDAK MUNCUL (sistem mengecualikan diri sendiri dari cek keunikan)
### Simulasi Server Down saat Save
8. Ubah nama menjadi `"Region A Modif"`
9. Pasang interceptor mock respons 500 Server Error pada request PATCH /groups/{id}
10. Klik tombol `[Save]`
11. Verifikasi toast error `"Error, failed to update group."` tampil
12. Verifikasi modal Edit tetap terbuka dan nilai `"Region A Modif"` tetap dipertahankan

## Notes

- Tombol konfirmasi pada modal Edit berlabel [Save] (prd-conventions.md §24.1).
