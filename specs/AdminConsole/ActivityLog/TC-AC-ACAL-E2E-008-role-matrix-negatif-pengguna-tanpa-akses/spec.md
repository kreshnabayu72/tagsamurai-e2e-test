---
id: TC-AC-ACAL-E2E-008-role-matrix-negatif-pengguna-tanpa-akses
title: "Role Matrix Negatif — Penolakan menu sidebar dan Direct URL 403 untuk Client dan Group Manager"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-26
  - TC-AC-ACAL-29
  - TC-AC-ACAL-30
  - TC-AC-ACAL-31
  - TC-AC-ACAL-32
coverage:
  web: automated
---

# Role Matrix Negatif — Penolakan menu sidebar dan Direct URL 403 untuk Client dan Group Manager

## Prerequisites

- Akun uji untuk role yang tidak memiliki akses:

| Role yang diuji | Entitas | Keterangan |
| :--- | :--- | :--- |
| Client | Client | Tidak memiliki menu Activity Log di Admin Console |
| Distributor Group Manager | Distributor | Group Manager diblokir dari Activity Log |
| Staff No Access Level | Distributor | Pengguna tanpa access_level |

## Test Steps

### Uji Sidebar Hidden

1. Login sebagai Role: Client
2. Amati sidebar Admin Console
3. Verifikasi menu `"Activity Log"` tersembunyi (Hidden sama sekali)
4. Logout dan login sebagai Role: Distributor Group Manager
5. Verifikasi menu `"Activity Log"` tersembunyi di sidebar
6. Logout dan login sebagai Role: Staff No Access Level
7. Verifikasi menu `"Activity Log"` tersembunyi di sidebar

### Uji Direct URL Access Guard

8. Saat login sebagai Staff No Access Level, masukkan URL direct Activity Log pada browser address bar
9. Verifikasi akses ditolak (halaman error 403 / redirect ke Dashboard) dan tidak ada bagian tabel yang ter-render
10. Logout dan login kembali sebagai Role: Client
11. Masukkan URL direct Activity Log pada address bar
12. Verifikasi akses ditolak dan halaman Activity Log tidak dapat dimuat

## Notes

- Penolakan akses direct URL diverifikasi baik pada level proteksi routing frontend maupun validasi otorisasi server.
