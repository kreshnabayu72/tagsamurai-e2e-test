---
id: TC-AC-SU-E2E-001-screening-halaman-user-list-dan-struktur-kolom
title: "Screening halaman User List, breadcrumb, header, struktur kolom tabel, baris Default User dan Self"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-1
  - TC-AC-SU-2
  - TC-AC-SU-3
  - TC-AC-SU-4
  - TC-AC-SU-5
  - TC-AC-SU-6
  - TC-AC-SU-7
  - TC-AC-SU-8
  - TC-AC-SU-9
  - TC-AC-SU-12
  - TC-AC-SU-264
  - TC-AC-SU-265
  - TC-AC-SU-266
coverage:
  web: automated
---

# Screening halaman User List, breadcrumb, header, struktur kolom tabel, baris Default User dan Self

## Prerequisites

- Login sebagai Role: Principal / Distributor / Partner Total Control
- Terdapat data pengguna aktif, Inactive, Total Control, Group Manager, dan Default User

## Test Steps

### Screening Halaman dan Toolbar

1. Buka sidebar menu `Admin Console > Settings > User`
2. Verifikasi breadcrumb menampilkan `"Settings > User"`
3. Verifikasi toolbar sisi kanan memuat: `Search 🔖 | Filter | Download | Changelog` tanpa tombol Add / Create User (manajemen identitas dikelola di Global Settings)
4. Verifikasi tabel User List memuat 11 kolom baku: `Checkbox`, `Active`, `[Avatar] Full Name`, `Email`, `Role`, `Position`, `Division`, `Employee ID`, `Modified By`, `Last Updated`, serta kolom `Actions (⋯)`

### Screening Kolom Role & Popup Active Roles

1. Amati kolom Role pada pengguna dengan 2 Global Role dan 1 Group Role aktif
2. Verifikasi kolom Role menampilkan angka gabungan `3`
3. Klik angka `3` pada kolom Role tersebut
4. Verifikasi popup terbuka dengan header literal `"Active Roles (3)"` yang memuat 2 bagian: `Global Role` dan `Group Role` dipisahkan oleh garis divider
5. Amati teks Group Role pada pengguna dengan role yang sama di 3 group berbeda
6. Verifikasi popup menampilkan konsolidasi `"Manage group — 3 groups"` tanpa enumerasi nama group atau tooltip hover
7. Amati kolom Role pada pengguna dengan tier Total Control
8. Verifikasi kolom Role menampilkan badge `"Total Control"` (bukan angka), dan klik badge tidak membuka popup role list
9. Amati kolom Role pada pengguna dengan status Group Manager tanpa access_level tier
10. Verifikasi kolom Role tetap menampilkan angka peran aktif biasa (bukan badge khusus)

### Screening Kolom Khusus, Guard Baris, dan Badge

1. Amati kolom Employee ID pada pengguna tanpa data Employee ID di Global Settings, verifikasi menampilkan placeholder `—`
2. Amati baris Default User dan baris akun yang sedang login (Self)
3. Verifikasi checkbox seleksi berstatus Disabled pada kedua baris tersebut, dan baris Self memuat tooltip `"You can't manage your own account from here."` sehingga dikecualikan dari bulk action
4. Verifikasi switch Active berstatus Disabled pada baris Default User, baris Self, entitas suspended, dan pengguna dengan status `isActiveGlobal=false` di Global Settings
5. Amati baris pengguna dengan status Pending Activation, verifikasi menampilkan badge `"Pending Activation"` di kolom Name
6. Amati baris pengguna Activated dengan `pendingEmail` terisi, verifikasi menampilkan badge `"Pending Email Confirmation"` di kolom Name
7. Verifikasi badge Pending Activation dan Pending Email Confirmation bersifat mutual exclusive (tidak pernah tampil bersamaan pada satu baris)
8. Amati kolom Group: verifikasi menampilkan 1 badge untuk 1 group, 2 badge urutan alfabetis A-Z untuk 2 group, badge tunggal `"All Groups"` untuk seluruh group master data, dan `"+N more"` untuk >2 group
9. Klik badge `"+N more"`, verifikasi popup scrollable daftar nama group terbuka dan tertutup saat klik di luar area popup

### Navigasi ke Detail User

1. Klik nama pengguna pada kolom Name, verifikasi halaman Detail User terbuka
2. Kembali ke halaman User List
3. Klik icon `[⋯]` pada kolom Actions baris lain lalu klik opsi `Detail`, verifikasi halaman Detail User terbuka

## Notes

- Modul Admin Console > Settings > User mengelola akses dan peran portal, bukan identitas pengguna.
- Identitas dan penambahan user dilakukan dari Global Settings > User.
