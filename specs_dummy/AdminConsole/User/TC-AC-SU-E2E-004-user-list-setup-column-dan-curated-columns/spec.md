---
id: TC-AC-SU-E2E-004-user-list-setup-column-dan-curated-columns
title: "Setup Column User List, toggle visibilitas 4 kolom curated, render badge format, dan sorting"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-260
coverage:
  web: automated
---

# Setup Column User List, toggle visibilitas 4 kolom curated, render badge format, dan sorting

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data pengguna dengan status variatif: Activation Status (Activated, Pending Activation, Pending Email Confirmation), Temporary User (Yes/No), Temporary Until, dan paired TAG

## Test Steps

### Toggle Visibilitas Kolom Curated
1. Buka halaman `Admin Console > Settings > User`
2. Verifikasi 4 kolom curated berikut dalam keadaan default Hidden: `Activation Status`, `Temporary User`, `Temporary Until`, dan `TAG`
3. Klik tombol `Column Visibility (⋯)` pada toolbar
4. Centang keempat kolom curated: `Activation Status`, `Temporary User`, `Temporary Until`, dan `TAG`
5. Verifikasi keempat kolom tersebut kini muncul di tabel User List

### Format Render Badge & Tanggal Kolom Curated
6. Amati render kolom `Activation Status`
7. Verifikasi kolom menampilkan badge: severity success untuk `"Activated"`, warning untuk `"Pending Activation"` dan `"Pending Email Confirmation"` (bukan teks polos)
8. Amati render kolom `Temporary User`
9. Verifikasi kolom menampilkan badge `Yes` atau `No`
10. Amati render kolom `Temporary Until`
11. Verifikasi kolom menampilkan tanggal berformat standar platform, atau placeholder `—` jika bukan temporary user
12. Amati render kolom `TAG`
13. Verifikasi menampilkan kode TAG yang ter-pair atau placeholder `—` jika belum ada TAG yang dipasangkan

### Sorting Kolom Curated & Re-hide
14. Klik header kolom `Activation Status` dan verifikasi pengurutan Alphabetical berdasarkan label badge
15. Klik header kolom `Temporary User` dan verifikasi pengurutan Alphabetical
16. Klik header kolom `Temporary Until` dan verifikasi pengurutan tanggal Newest/Oldest First
17. Klik header kolom `TAG` dan verifikasi pengurutan kode Alphabetical dengan data kosong selalu di posisi akhir
18. Buka kembali `Column Visibility (⋯)` dan uncheck keempat kolom curated
19. Verifikasi kolom curated kembali tersembunyi tanpa mengubah data pengguna di backend

## Notes

- Seluruh 16 kolom data User List bersifat hideable dengan batasan minimal 1 kolom tetap aktif.
