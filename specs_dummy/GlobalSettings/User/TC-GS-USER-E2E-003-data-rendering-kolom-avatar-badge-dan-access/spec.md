---
id: TC-GS-USER-E2E-003-data-rendering-kolom-avatar-badge-dan-access
title: "Data rendering kolom Name, Avatar, badge status, format tanggal, dan popup Access"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-12
  - TC-GS-USER-14
  - TC-GS-USER-15
  - TC-GS-USER-16
  - TC-GS-USER-17
  - TC-GS-USER-18
  - TC-GS-USER-19
  - TC-GS-USER-20
  - TC-GS-USER-21
  - TC-GS-USER-22
coverage:
  web: automated
---

# Data rendering kolom Name, Avatar, badge status, format tanggal, dan popup Access

## Prerequisites

- Login sebagai Role: Total Control
- Pre-setup User No. 10–22 tersedia di environment (memuat user Mike Tan, Rina Putri, Lilis Handayani, Dewi Lestari, Jane Smith, Joko Susilo, Hendra Gunawan)

## Test Steps

### Rendering Avatar, Badge, dan Nilai Kosong

1. Buka Global Settings > User > User List
2. Temukan baris Mike Tan, verifikasi sel Name menampilkan avatar inisial, teks 'Mike Tan', dan badge 'Pending Activation'
3. Temukan baris Rina Putri, verifikasi sel Name menampilkan badge 'Pending Email Confirmation' dan tidak menampilkan badge Pending Activation
4. Temukan baris Lilis Handayani, verifikasi sel Position dan Employee ID menampilkan karakter '—' karena kosong, sementara Division dan Access terisi
5. Hover sel Modified By pada baris Dewi Lestari, verifikasi format singkat 'Siti N' tampil dengan tooltip 'Siti Nurhaliza'
6. Verifikasi sel Last Update baris Dewi Lestari terformat sesuai pengaturan General Settings (DD/MM/YYYY HH:mm)

### Rendering Kolom Access dan Popup

7. Temukan baris Jane Smith, verifikasi sel Access menampilkan 1 badge 'Supply Asset' tanpa chip '+N more'
8. Temukan baris Joko Susilo, verifikasi sel Access menampilkan 2 badge 'Fixed Asset' dan 'Supply Asset' berurutan alfabetis tanpa chip
9. Temukan baris Hendra Gunawan, verifikasi sel Access menampilkan 2 badge produk dan chip '+1 more'
10. Klik chip '+1 more' pada baris Hendra Gunawan
11. Verifikasi popup Access terbuka dengan title 'Access' menampilkan seluruh produk terdaftar (Fixed Asset, Global Settings, Supply Asset) terurut A-Z
12. Verifikasi popup bersifat read-only tanpa tombol aksi, lalu klik ikon [✕] untuk menutup popup

### Navigasi Detail via Name

13. Klik teks Name 'Dewi Lestari'
14. Verifikasi aplikasi berpindah ke halaman User Detail Dewi Lestari dengan breadcrumb 'User > Detail'

## Notes

- Menggabungkan 10 test case granular (TC-GS-USER-12 s.d. TC-GS-USER-22).
