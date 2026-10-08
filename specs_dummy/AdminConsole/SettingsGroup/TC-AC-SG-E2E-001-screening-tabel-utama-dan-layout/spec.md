---
id: TC-AC-SG-E2E-001-screening-tabel-utama-dan-layout
title: "Screening tabel utama, toolbar, breadcrumb, dan hover baris Settings > Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-1
  - TC-AC-SG-3
  - TC-AC-SG-7
  - TC-AC-SG-173
  - TC-AC-SG-174
  - TC-AC-SG-175
  - TC-AC-SG-176
coverage:
  web: automated
---

# Screening tabel utama, toolbar, breadcrumb, dan hover baris Settings > Group

## Prerequisites

- Login sebagai Role: Total Control atau Default User
- Entitas memiliki ≥ 1 group dengan variasi nama panjang dan pengubah (modifier)

## Test Steps

### Screening Layout & Breadcrumb
1. Buka menu navigasi `Admin Console > Settings > Group`
2. Verifikasi breadcrumb page-level menampilkan `Settings > Group` di level chrome halaman dan segmen teks bersifat non-clickable
3. Verifikasi tidak ada Page Title Header terpisah di bawah breadcrumb
4. Verifikasi tata letak 2 zona utama: Tabel Utama di sisi kiri (dengan Group Context Header) dan Sidebar Group Tree di sisi kanan (right-docked)
### Screening Toolbar & Header Kolom
5. Verifikasi toolbar tabel memuat 4 kontrol: `[🔍 Search]`, `[Filter]`, `[⬇ Download]`, dan icon `[Changelog]`
6. Verifikasi tidak ada tombol `[+ New Group]` pada toolbar tabel (tombol create level-1 hanya berada di sidebar)
7. Verifikasi tabel memuat 7 kolom default: Checkbox, `Group`, `Total User`, `Total Member`, `Modified By`, `Last Updated`, dan `Actions (⋯)`
8. Verifikasi default sorting tabel adalah kolom `Group` ascending (A-Z)
### Interaktivitas Baris & Format Kolom
9. Klik di area tengah baris (di luar checkbox dan menu elipsis)
10. Verifikasi klik pada area baris bersifat non-interaktif (tidak memicu navigasi, modal detail, atau perubahan state)
11. Hover kursor mouse di atas salah satu baris tabel
12. Verifikasi baris yang di-hover mendapatkan highlight visual background dan kolom `Actions (⋯)` reveal terlihat
13. Jauhkan kursor dari baris dan verifikasi highlight hilang serta Actions kembali ke status default
14. Amati sel kolom `Group` pada baris dengan nama panjang
15. Verifikasi nama Group tampil utuh (hug content / wrap natural) tanpa pemotongan artifisial
16. Amati format teks pada kolom `Modified By`
17. Verifikasi format tampilan berupa teks plain `[First Name Lengkap] [Inisial Last Name]` (contoh: `Budi S`)
18. Hover kursor pada teks Modified By dan verifikasi kemunculan tooltip 🔖 yang menampilkan nama lengkap utuh (contoh: `Budi Santoso`)

## Notes

- Satu-satunya entry point create level-1 berada di sidebar kanan.
- Kolom Group adalah primary identifier dengan perilaku hug content.
