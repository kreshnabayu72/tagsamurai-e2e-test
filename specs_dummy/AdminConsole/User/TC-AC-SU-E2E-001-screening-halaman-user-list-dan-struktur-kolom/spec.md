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
  - TC-AC-SU-163
  - TC-AC-SU-165
  - TC-AC-SU-264
  - TC-AC-SU-265
  - TC-AC-SU-266
coverage:
  web: automated
---

# Screening halaman User List, breadcrumb, header, struktur kolom tabel, baris Default User dan Self

## Prerequisites

- Login sebagai Role: Principal / Distributor / Partner Total Control
- Terdapat data pengguna aktif, Inactive, Total Control, Group Manager, Pending Activation, Pending Email Confirmation, dan Default User

## Test Steps

### Screening Halaman dan Toolbar
1. Buka sidebar menu `Admin Console > Settings > User`
2. Verifikasi breadcrumb menampilkan `"Settings > User"`
3. Verifikasi toolbar sisi kanan memuat: `Search 🔖 | Filter | Download | Changelog` tanpa tombol Add / Create User (manajemen identitas dikelola di Global Settings)
4. Verifikasi tabel User List memuat 11 kolom baku: `Checkbox`, `Active`, `[Avatar] Full Name`, `Email`, `Role`, `Position`, `Division`, `Employee ID`, `Modified By`, `Last Updated`, serta kolom `Actions (⋯)`

### Screening Kolom Role & Popup Active Roles
5. Amati kolom Role pada pengguna dengan 2 Global Role dan 1 Group Role aktif
6. Verifikasi kolom Role menampilkan angka gabungan `3`
7. Klik angka `3` pada kolom Role tersebut
8. Verifikasi popup terbuka dengan header literal `"Active Roles (3)"` yang memuat 2 bagian: `Global Role` dan `Group Role` dipisahkan oleh garis divider
9. Amati teks Group Role pada pengguna dengan role yang sama di 3 group berbeda
10. Verifikasi popup menampilkan konsolidasi `"Manage group — 3 groups"` tanpa enumerasi nama group atau tooltip hover
11. Amati kolom Role pada pengguna dengan tier Total Control
12. Verifikasi kolom Role menampilkan badge `"Total Control"` (bukan angka), dan klik badge tidak membuka popup role list
13. Amati kolom Role pada pengguna dengan status Group Manager tanpa access_level tier
14. Verifikasi kolom Role tetap menampilkan angka peran aktif biasa (bukan badge khusus)

### Screening Kolom Khusus, Guard Baris, dan Badge
15. Amati kolom Employee ID pada pengguna tanpa data Employee ID di Global Settings, verifikasi menampilkan placeholder `—`
16. Amati baris Default User dan baris akun yang sedang login (Self)
17. Verifikasi checkbox seleksi berstatus Disabled pada kedua baris tersebut, dan baris Self memuat tooltip `"You can't manage your own account from here."` sehingga dikecualikan dari bulk action
18. Verifikasi switch Active berstatus Disabled pada baris Default User, baris Self, entitas suspended, dan pengguna dengan status `isActiveGlobal=false` di Global Settings
19. Amati baris pengguna dengan status Pending Activation, verifikasi menampilkan badge `"Pending Activation"` di kolom Name
20. Amati baris pengguna berstatus Activated dengan perubahan email tertunda, verifikasi menampilkan badge `"Pending Email Confirmation"` di kolom Name
21. Verifikasi kedua badge status tersebut saling eksklusif dan tidak pernah muncul bersamaan pada satu baris nama pengguna
22. Amati kolom Group Summary Badge pada pengguna yang ter-assign ke 1 group, 2 group, dan seluruh master group
23. Verifikasi pengguna dengan 1 group menampilkan 1 badge nama group; 2 group menampilkan 2 badge terurut A-Z; seluruh group master menampilkan badge tunggal `"All Groups"`
24. Klik badge `"+N more"` pada baris pengguna dengan >2 group dan verifikasi popup menampilkan daftar group yang dapat di-scroll
25. Nonaktifkan role group pengguna tersebut dan verifikasi badge group tetap dipertahankan di tabel (retained)
26. Verifikasi baris Self tetap menampilkan tombol row action `Detail` yang aktif (Self tidak digate dari melihat detail profilnya sendiri)
27. Klik nama pengguna pada baris tabel dan verifikasi halaman Detail User terbuka
28. Kembali ke User List, klik tombol row action `Detail` pada baris lain dan verifikasi kedua jalur navigasi membuka halaman Detail User yang sama

## Notes

- Baris Default User dan Self dilindungi dari operasi bulk action dan perubahan status aktif.
- Kolom Group Summary menampilkan konsolidasi pintar nama grup.
