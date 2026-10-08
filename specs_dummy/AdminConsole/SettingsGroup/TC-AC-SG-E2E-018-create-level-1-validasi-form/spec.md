---
id: TC-AC-SG-E2E-018-create-level-1-validasi-form
title: "Validasi field Group Name form Create: kosong, batas panjang, reserved name, dan duplikat sibling"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-34
  - TC-AC-SG-35
  - TC-AC-SG-36
  - TC-AC-SG-37
  - TC-AC-SG-38
coverage:
  web: automated
---

# Validasi field Group Name form Create: kosong, batas panjang, reserved name, dan duplikat sibling

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat group level 1 eksisting bernama `"Region A"`

## Test Steps

### Validasi Wajib Isi (Empty)
1. Klik tombol `[+ New Group]` di sidebar untuk membuka modal Create
2. Kosongkan field Group Name (string hampa `""`) lalu klik `[Submit]`
3. Verifikasi pesan error inline `"Group name must not be empty"` muncul di bawah input
4. Ketik hanya karakter spasi `"   "` lalu klik `[Submit]`
5. Verifikasi pesan error `"Group name must not be empty"` tetap muncul
### Validasi Batas Panjang Maksimal (Max Length)
6. Ketik string sepanjang 121 karakter pada field Group Name
7. Verifikasi pesan peringatan inline `"Max. 120 characters"` muncul seketika saat mengetik
### Validasi Duplikat Sibling (Debounce)
8. Bersihkan input lalu ketik `"region a"` (huruf kecil semua, case-insensitive)
9. Hentikan pengetikan tanpa memindahkan kursor keluar field (tanpa blur)
10. Verifikasi setelah jeda debounce (~500ms) muncul pesan error `"Group name already exists in this level"`
### Validasi Reserved Name
11. Bersihkan input lalu ketik `"all groups"` (case-insensitive)
12. Klik `[Submit]`
13. Verifikasi muncul pesan error `"'All Groups' is a reserved name and cannot be used"`
### Validasi Sibling Beda Parent Diizinkan
14. Bersihkan input lalu tutup modal

## Notes

- Validasi duplikat sibling berjalan saat mengetik (debounce), sedangkan empty/reserved saat submit.
