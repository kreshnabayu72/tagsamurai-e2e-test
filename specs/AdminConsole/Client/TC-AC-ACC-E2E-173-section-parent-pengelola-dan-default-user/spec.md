---
id: TC-AC-ACC-E2E-173-section-parent-pengelola-dan-default-user
title: "Section Parent / Pengelola dan Section Default User pada Detail Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-798
  - TC-AC-ACC-799
coverage:
  web: automated
---

# Section Parent / Pengelola dan Section Default User pada Detail Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-01 "PT Sejahtera Abadi" (Partner CV Mitra Sejati), C-02 "PT Teknologi Maju" (Partner CV Mitra Sejati sebagai Anchor dan CV Mitra Lestari; Default User Dewi Lestari, `dewi.lestari@ptteknologimaju.test`, Division Finance, Position Finance Manager), C-11 "PT Sinar Distributor" (Distributor langsung PT Distribusi Nusantara), C-09 "PT Baru Daftar" (Direct, Group Cabang Menteng, Position Default User kosong). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-798: Section Parent / Pengelola menampilkan Partner, Distributor, dan Group sesuai relasi Client

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
3. Verifikasi Section "Parent / Pengelola" menampilkan Partner "CV Mitra Sejati"
4. Verifikasi Section "Parent / Pengelola" menampilkan Distributor "PT Distribusi Nusantara"
5. Verifikasi Section "Parent / Pengelola" menampilkan Group "Area Jakarta"
6. Verifikasi Partner, Distributor, dan Group tampil sebagai teks tanpa kontrol ubah
7. Kembali ke List lewat breadcrumb Client
8. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter
9. Klik Company Name "PT Teknologi Maju" untuk membuka Detail
10. Verifikasi Section "Parent / Pengelola" menampilkan Partner "CV Mitra Sejati" dan "CV Mitra Lestari"
11. Verifikasi Section "Parent / Pengelola" menampilkan Distributor "PT Distribusi Nusantara" (Distributor induk Anchor CV Mitra Sejati)
12. Verifikasi Section "Parent / Pengelola" menampilkan Group "Area Jakarta"
13. Verifikasi Partner, Distributor, dan Group tampil sebagai teks tanpa kontrol ubah
14. Kembali ke List lewat breadcrumb Client
15. Ganti isi Search dengan `PT Sinar Distributor`, tekan Enter
16. Klik Company Name "PT Sinar Distributor" untuk membuka Detail
17. Verifikasi Section "Parent / Pengelola" menampilkan Distributor "PT Distribusi Nusantara"
18. Verifikasi Section "Parent / Pengelola" menampilkan Group "Area Jakarta"
19. Verifikasi Partner, Distributor, dan Group tampil sebagai teks tanpa kontrol ubah
20. Kembali ke List lewat breadcrumb Client
21. Ganti isi Search dengan `PT Baru Daftar`, tekan Enter
22. Klik Company Name "PT Baru Daftar" untuk membuka Detail
23. Verifikasi Section "Parent / Pengelola" menampilkan Distributor `—`
24. Verifikasi Section "Parent / Pengelola" menampilkan Group "Cabang Menteng"
25. Verifikasi Partner, Distributor, dan Group tampil sebagai teks tanpa kontrol ubah

### TC-AC-ACC-799: Section Default User menampilkan Name, Email, Division, dan Position; Position kosong tampil —

26. Kembali ke List lewat breadcrumb Client
27. Klik ikon Search, ketik `PT Teknologi Maju`, tekan Enter
28. Klik Company Name "PT Teknologi Maju" untuk membuka Detail
29. Verifikasi Section "Default User" menampilkan Name "Dewi Lestari"
30. Verifikasi Section "Default User" menampilkan Email "dewi.lestari@ptteknologimaju.test"
31. Verifikasi Section "Default User" menampilkan Division "Finance"
32. Verifikasi Section "Default User" menampilkan Position "Finance Manager"
33. Kembali ke List lewat breadcrumb Client
34. Ganti isi Search dengan `PT Baru Daftar`, tekan Enter
35. Klik Company Name "PT Baru Daftar" untuk membuka Detail
36. Verifikasi Section "Default User" menampilkan Position `—`

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu role pada satu surface, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Kembali ke List lewat breadcrumb Client" dan Search adalah langkah penghubung (S-03). Verifikasi "tanpa kontrol ubah" pada TC-798 diasersi per Client sesuai Expected butir e (keempat Client).
- Temuan untuk QA (S-15): TC-798 tidak menyebut Partner untuk "PT Sinar Distributor" (C-11, relasi Distributor-Client langsung tanpa Partner) pada Expected sehingga Partner tidak diasersi; Post Condition kedua TC `-` sehingga tidak diasersi. Tabel A2 menyebut Default User "PT Baru Daftar" bernama Hadi Prasetyo tetapi TC-799 hanya mengasersi Position `—`.
