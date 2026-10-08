---
id: TC-AC-SU-E2E-005-user-list-search-toolbar-per-kolom-dan-guard
title: "Pencarian toolbar User List per kolom teks dan guard kolom non-searchable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-13
  - TC-AC-SU-14
  - TC-AC-SU-234
  - TC-AC-SU-235
  - TC-AC-SU-236
  - TC-AC-SU-237
  - TC-AC-SU-238
coverage:
  web: automated
---

# Pencarian toolbar User List per kolom teks dan guard kolom non-searchable

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat pengguna dengan variasi data unik pada kolom Full Name, Email, Position, Division, Role, dan Modified By

## Test Steps

### Pencarian Per Kolom Teks
1. Buka halaman `Settings > User`
2. Ketik sebagian nama pengguna unik pada kotak Search toolbar (contoh: `"Robert"`)
3. Verifikasi hanya baris pengguna dengan nama yang cocok yang tampil di tabel
4. Hapus input Search dan ketik sebagian alamat email unik (contoh: `"@wangs.id"`)
5. Verifikasi hanya pengguna dengan domain email tersebut yang tampil di tabel
6. Hapus input Search dan ketik sebagian nama Position (contoh: `"Manager"`)
7. Verifikasi pengguna dengan jabatan Manager tampil di tabel
8. Hapus input Search dan ketik sebagian nama Division (contoh: `"Operations"`)
9. Verifikasi pengguna dari divisi Operations tampil di tabel
10. Hapus input Search dan ketik nama role atau badge (contoh: `"Total Control"`)
11. Verifikasi pengguna pemegang badge Total Control tampil di tabel
12. Hapus input Search dan ketik nama admin pengubah pada kolom Modified By (contoh: `"Admin Super"`)
13. Verifikasi pengguna yang dimodifikasi oleh admin tersebut tampil di tabel

### Guard Kolom Non-Searchable
14. Ketik nilai status boolean switch Active (misal: `"true"` atau `"active"`) ke kotak Search
15. Verifikasi hasil pencarian tidak mencocokkan status switch melainkan hanya teks nama/email jika ada
16. Verifikasi kotak pencarian toolbar tidak mencari file gambar atau avatar foto pengguna

## Notes

- Toolbar Search mengevaluasi seluruh kolom teks visible dan menolak evaluasi kolom biner/switch.
