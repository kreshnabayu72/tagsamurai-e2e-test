---
id: TC-AC-SU-E2E-015-row-action-deactivate-user-dialog-konfirmasi-dan-focus-trap
title: "Deaktivasi user baris tunggal (ON ke OFF), dialog konfirmasi danger, focus trap a11y, Cancel path, dan toast sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-28
  - TC-AC-SU-29
  - TC-AC-SU-291
coverage:
  web: automated
---

# Deaktivasi user baris tunggal (ON ke OFF), dialog konfirmasi danger, focus trap a11y, Cancel path, dan toast sukses

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat target pengguna bernama `"User Active Target"` dengan switch Active berstatus ON (Active)

## Test Steps

### Trigger Dialog Konfirmasi Deaktivasi & Focus Trap A11y
1. Buka halaman `Settings > User`
2. Temukan baris `"User Active Target"` dengan switch Active posisi ON
3. Klik switch Active untuk mematikan akses (ON → OFF)
4. Verifikasi modal konfirmasi muncul dengan `severity="danger"`
5. Verifikasi judul dialog adalah `"Deactivate User"` dan body dialog memuat:
   - Bullet nama: `• User Active Target`
   - Teks peringatan: `"This user will lose portal access immediately. Any active sessions will be ended."`
   - Pertanyaan: `"Are you sure you want to deactivate it?"`
6. Uji fokus keyboard (Focus Trap): tekan tombol `Tab` berulang kali di dalam dialog
7. Verifikasi fokus keyboard terkunci hanya berputar di antara tombol `[Cancel]`, tombol `[Deactivate]`, dan tombol tutup `[×]` tanpa bocor ke halaman belakang
8. Tekan tombol `Esc` pada keyboard
9. Verifikasi dialog tertutup dan switch Active tetap pada posisi ON

### Eksekusi Deaktivasi Sukses
10. Klik kembali switch Active (ON → OFF)
11. Klik tombol konfirmasi destruktif `[Deactivate]`
12. Verifikasi switch beralih ke posisi OFF
13. Verifikasi muncul toast sukses: `"Success, User Active Target has been deactivated."`
14. Refresh halaman dan verifikasi status pengguna tetap Inactive

## Notes

- Dialog deaktivasi menerapkan focus trap dan severity danger untuk mencegah kesalahan aksi fatal.
