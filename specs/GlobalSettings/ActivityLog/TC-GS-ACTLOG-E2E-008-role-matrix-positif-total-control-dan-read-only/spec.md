---
id: TC-GS-ACTLOG-E2E-008-role-matrix-positif-total-control-dan-read-only
title: "Role Matrix Positif: Total Control dan Read Only memiliki akses baca penuh dan UI identik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-26
  - TC-GS-ACTLOG-27
coverage:
  web: automated
---

# Role Matrix Positif: Total Control dan Read Only memiliki akses baca penuh dan UI identik

## Prerequisites

- Role yang diuji:
  | Role | Akun | Expected Outcome |
  |---|---|---|
  | Total Control | Fixture.auth.totalControlUser | Akses penuh, menu show, semua table tools aktif |
  | Read Only | Fixture.auth.readOnlyUser | UI identik Total Control, menu show, semua table tools aktif |

## Test Steps

1. Lakukan langkah-langkah berikut untuk setiap role pada tabel Role yang diuji:
2. Login menggunakan akun role yang bersangkutan
3. Buka menu Global Settings
4. Verifikasi menu "Activity Log" tampil pada sidebar navigasi
5. Klik menu "Activity Log"
6. Verifikasi tab Session dan tab User Action tampil dan dapat diklik
7. Verifikasi table tools Search, Filter, Download, dan Setup Column tampil serta aktif
8. Verifikasi kolom data dan pagination tampil normal tanpa ada elemen kontrol yang disabled
9. Logout dari akun saat ini

## Notes

- Di modul Activity Log, role Total Control dan Read Only memiliki tampilan dan kapabilitas yang 100% identik.
