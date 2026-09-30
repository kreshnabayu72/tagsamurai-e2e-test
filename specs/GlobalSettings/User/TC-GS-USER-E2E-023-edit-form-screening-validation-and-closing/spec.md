---
id: TC-GS-USER-E2E-023-edit-form-screening-validation-and-closing
title: Validasi form Edit User dan menutup modal Edit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-254
  - TC-GS-USER-30
  - TC-GS-USER-422
  - TC-GS-USER-424
  - TC-GS-USER-464
  - TC-GS-USER-348
  - TC-GS-USER-432
  - TC-GS-USER-423
  - TC-GS-USER-488
coverage:
  web: automated
---

# Validasi form Edit User dan menutup modal Edit

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Budi Santoso" ada, status Activated, semua field terisi valid (First Name, Last Name, Email, Division "Finance", Access "Global Settings"). Nilai awalnya dicatat untuk dibandingkan di akhir spec
- User "Doni Pratama" ada dan emailnya diketahui
- Employee ID "EMP-001" sudah dipakai user lain di entity ini, dan bukan milik "Budi Santoso"
- Spec ini tidak menyimpan perubahan apa pun dan tidak membuat data, jadi tidak butuh cleanup

## Test Steps

### Screening

1. Klik row action `Edit` pada baris "Budi Santoso"
2. Verifikasi modal Edit terbuka dan semua field sudah terisi nilai user (pre-filled)
3. Verifikasi footer menampilkan `[Save]` dan `[Clear Field]`, dan tidak ada tombol `[Cancel]`

### Validasi

4. Untuk masing-masing First Name, Last Name, Email, dan Division: kosongkan hanya field itu (Access tetap terisi), klik `[Save]`, lalu verifikasi submit diblokir dan inline error "First Name must not be empty", "Last Name must not be empty", "Email must not be empty", atau "Division must not be empty" sesuai field-nya. Kembalikan nilai awal sebelum lanjut ke field berikutnya
5. Ganti Email dengan email milik "Doni Pratama"
6. Verifikasi inline error "Email already exists" muncul langsung saat mengetik (debounce sekitar 500 ms), lalu klik `[Save]` dan verifikasi submit diblokir serta data tidak tersimpan. Kembalikan Email ke nilai awal
7. Ganti Employee ID dengan "EMP-001"
8. Verifikasi inline error "Employee ID already exists" muncul langsung saat mengetik (debounce sekitar 500 ms), lalu klik `[Save]` dan verifikasi submit diblokir serta data tidak tersimpan. Kembalikan Employee ID ke nilai awal
9. Untuk masing-masing First Name, Last Name, dan Employee ID, isi 121 karakter sementara field lain tetap valid, lalu verifikasi inline error "Max. 120 characters" muncul langsung saat melebihi batas. Klik `[Save]` dan verifikasi submit diblokir. Kembalikan nilai awal
10. Ketik "😊" pada First Name dan Last Name, lalu verifikasi emoji tidak pernah masuk ke field dan field tetap bersih
11. Klik `[Clear Field]` tanpa mengubah apa pun sebelumnya
12. Verifikasi semua field dikosongkan (bukan dikembalikan ke nilai awal user) dan modal tetap terbuka

### Menutup modal

13. Klik `✕`
14. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" muncul dengan tombol `[Leave]` dan `[Cancel]`
15. Klik `[Cancel]` pada dialog, lalu verifikasi dialog tertutup, modal Edit tetap terbuka, dan field masih kosong
16. Klik `✕` lagi lalu klik `[Leave]` pada dialog
17. Verifikasi modal Edit tertutup dan baris "Budi Santoso" di User List tidak berubah dari nilai awal
18. Klik row action `Edit` pada baris "Budi Santoso" lagi tanpa mengubah field apa pun
19. Klik `✕`
20. Verifikasi modal langsung tertutup dan dialog "You have unsaved changes" tidak muncul

## Notes

- Spec ini adalah pasangan Edit dari `TC-GS-USER-E2E-001-create-form-screening-validation-and-closing` (Prinsip Simetri Create dan Edit). Dua sesi modal dipakai: langkah 1 sampai 16 di sesi pertama, langkah 18 sampai 20 di sesi kedua karena kasus tutup bersih butuh modal yang baru dibuka.
- Kasus "hapus semua Access" pada Edit (`TC-GS-USER-31`) dicakup `TC-GS-USER-E2E-009-remove-access-user`.
- Error kewajiban field ("... must not be empty") muncul setelah `[Save]`. Error duplikat Email dan Employee ID serta batas 120 karakter muncul langsung saat mengetik (PRD `user.md` bagian 6, kolom Timing).
- Aturan emoji mengikuti `prd-conventions.md` "Karakter yang Diizinkan (Name Fields)": hanya emoji yang diblokir. Fallback ketika emoji lolos block-input (`TC-GS-USER-465`) memakai DOM injection dan dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
- Modal Edit tidak punya tombol `[Cancel]` (`prd-conventions.md` bagian 24.1). `[Cancel]` hanya ada pada dialog unsaved changes. `Esc` juga menutup modal.
