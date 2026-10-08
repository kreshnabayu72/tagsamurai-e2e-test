---
id: TC-AC-SU-E2E-033-tab-role-group-role-guards-modal-detail-assignment-dan-changelog
title: "Guard Sub-tab Group Role (Default User, Self-Edit), Modal Detail Assignment, dan Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-84
  - TC-AC-SU-162
  - TC-AC-SU-221
  - TC-AC-SU-261
coverage:
  web: automated
---

# Guard Sub-tab Group Role (Default User, Self-Edit), Modal Detail Assignment, dan Changelog

## Prerequisites

- Login sebagai Total Control
- Terdapat akun Default User, akun profil Self, dan user biasa dengan penugasan Group Role

## Test Steps

### Guard Default User dan Self-Edit pada Group Role
1. Buka Detail User `Default User` > tab `Role` > sub-tab `Group Role`
2. Verifikasi seluruh toggle switch peran grup disabled dengan tooltip: `"Default user group roles cannot be modified"`
3. Buka Detail User akun profil sendiri (`Self`)
4. Verifikasi kontrol mutasi peran grup disabled dengan tooltip: `"You cannot modify your own group roles"`

### Modal Detail Group Assignment dan Changelog
5. Buka Detail User akun biasa yang memiliki penugasan grup
6. Klik badge `Group Summary` (misal teks bergaris bawah `"3 Groups"`)
7. Verifikasi modal `Detail Group Assignment` terbuka dalam mode `Read-Only`, menampilkan daftar nama cabang grup dan tanggal penugasan
8. Tutup modal via tombol `[Close]`
9. Klik tombol `[Changelog]` pada toolbar sub-tab Group Role
10. Verifikasi modal `Changelog Group Role` terbuka menampilkan riwayat mutasi peran grup

## Notes

Menjaga kepatuhan akses dan menyediakan audit transparansi penugasan grup.
