---
id: TC-GS-USER-E2E-089-setup-column-screening-dan-live-preview
title: 'Setup Column User List: overlay, popup modal, dan Live Preview'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-259
  - TC-GS-USER-260
  - TC-GS-USER-129
  - TC-GS-USER-133
coverage:
  web: automated
---

# Setup Column User List: overlay, popup modal, dan Live Preview

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data User List mock dengan sedikitnya 15 baris supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom disimpan di browser per user, jadi setiap spec Setup Column dimulai dari konfigurasi default

## Test Steps

### Overlay

1. Klik header kolom `(⋯)` pada tabel User List
2. Verifikasi overlay berisi 13 kolom: `Active`, `Name`, `Email`, `Position`, `Division`, `Access`, `Employee ID`, `Modified By`, `Last Update` (Hideable, tercentang dan aktif) serta `Activation Status`, `Temporary User`, `Temporary Until`, `TAG` (Curated, tidak tercentang dan aktif)

### Popup modal

3. Buka popup modal Setup Column
4. Verifikasi header berjudul "Setup Column" dengan teks info dan tombol `✕`, body berisi 13 baris kolom dengan status Hideable atau Curated eksplisit beserta Live Preview, dan footer berisi `[Reset to Default]`, `[Cancel]`, dan `[Save]`

### Perubahan cepat lewat overlay

5. Hapus centang `Active` dan `Email` di overlay
6. Verifikasi kolom `Active` dan `Email` hilang dari tabel
7. Centang kolom Curated `Activation Status`
8. Verifikasi kolom `Activation Status` muncul dan konfigurasi tersimpan di browser (tetap ada setelah refresh)

### Popover di depan dialog

9. Klik row action `Delete` pada satu baris sehingga dialog konfirmasi terbuka, lalu buka popover Setup Column
10. Verifikasi popover Setup Column tampil di depan dialog, lalu tutup keduanya

## Notes

- Sumber `user.md` bagian 4.2a (User List Setup Column) dan `prd-conventions.md` bagian 9.3. Semua langkah dilakukan pada konfigurasi default, dan spec ini mengembalikan konfigurasi ke default di langkah akhir sesuai kebutuhan spec berikutnya.
- Detail per kolom dicakup spec 090 sampai 093.
