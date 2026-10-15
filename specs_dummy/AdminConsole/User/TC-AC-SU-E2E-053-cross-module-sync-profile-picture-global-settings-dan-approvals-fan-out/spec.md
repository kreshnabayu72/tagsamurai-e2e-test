---
id: TC-AC-SU-E2E-053-cross-module-sync-profile-picture-global-settings-dan-approvals-fan-out
title: "Sinkronisasi Lintas Modul: Pembaruan Foto Profil di Global Settings dan Fan-Out ke Approvals"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-56
  - TC-AC-SU-185
  - TC-AC-SU-186
coverage:
  web: automated
---

# Sinkronisasi Lintas Modul: Pembaruan Foto Profil di Global Settings dan Fan-Out ke Approvals

## Prerequisites

- Target user memiliki transaksi persetujuan aktif di modul Approvals
- Login sebagai Total Control

## Test Steps

### Pembaruan Identitas Pengguna di Global Settings
1. Buka aplikasi `Global Settings > Users`
2. Temukan user target dan unggah foto profil avatar baru
3. Perbarui informasi nomor kontak dan posisi pengguna
4. Simpan perubahan profil

### Verifikasi Sinkronisasi Seketika di Admin Console
5. Buka modul `Admin Console > Settings > User`
6. Cari user target pada tabel User List; verifikasi avatar baru langsung tampil pada baris tabel
7. Klik nama user untuk membuka `Detail User`
8. Verifikasi avatar baru dan nomor kontak yang diperbarui langsung ter-render di header dan general info

### Verifikasi Fan-Out Data ke Modul Approvals
9. Buka aplikasi `Approvals`
10. Cari transaksi persetujuan yang diajukan oleh user target
11. Verifikasi kartu requesters memuat foto profil baru dan identitas yang sinkron tanpa terjadi data stale

## Notes

Memastikan konsistensi identitas pengguna terdistribusi secara harmonis ke seluruh ekosistem TAG Samurai.
