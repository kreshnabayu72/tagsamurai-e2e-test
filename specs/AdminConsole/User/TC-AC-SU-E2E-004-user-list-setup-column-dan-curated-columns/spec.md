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

- Login sebagai Role: Principal Total Control
- Terdapat data pengguna dengan status Activation Status, Temporary User, Temporary Until, dan TAG

## Test Steps

### Screening Default Hidden Kolom Curated

1. Buka halaman User List
2. Verifikasi 4 kolom curated (`Activation Status`, `Temporary User`, `Temporary Until`, `TAG`) berstatus default Hidden pada tabel utama

### Aktivasi Visibilitas via Setup Column

1. Klik header kolom `⋯` lalu pilih `Column Visibility` / buka modal Setup Column
2. Centang checkbox untuk menampilkan kolom `Activation Status`, `Temporary User`, `Temporary Until`, dan `TAG`
3. Terapkan pengaturan Setup Column
4. Verifikasi keempat kolom kini tampil pada tabel User List

### Verifikasi Render Badge dan Sorting Kolom Curated

1. Amati render kolom `Activation Status`: verifikasi tampil sebagai Badge dengan warna severity sesuai state (`Activated` = success hijau, `Pending Activation` / `Pending Email Confirmation` = warning kuning)
2. Amati render kolom `Temporary User`: verifikasi tampil sebagai Badge `Yes` atau `No`
3. Amati render kolom `Temporary Until`: verifikasi menampilkan format tanggal terformat
4. Amati render kolom `TAG`: verifikasi menampilkan kode TAG atau `—` jika belum dipasangkan
5. Klik header kolom `Activation Status`, verifikasi data terurut secara alfabetis berdasarkan label badge
6. Klik header kolom `Temporary Until`, verifikasi data terurut berdasarkan tanggal (Newest / Oldest First)
7. Buka kembali Setup Column dan nonaktifkan keempat kolom tersebut, verifikasi tabel kembali ke tampilan awal tanpa kehilangan data

## Notes

- Fitur Setup Column memungkinkan admin menyesuaikan visibilitas kolom operasional tambahan.
