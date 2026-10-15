---
id: TC-AC-PP-E2E-011-role-matrix-negatif-entity-gate
title: "Role Matrix Negatif: Entity Gate Distributor, Partner, dan Client Tidak Mengakses Privacy Policy"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-15
  - TC-AC-PP-16
coverage:
  web: automated
---

# Role Matrix Negatif: Entity Gate Distributor, Partner, dan Client Tidak Mengakses Privacy Policy

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (capability "Manage privacy policy" ter-assign keliru lewat Fixture BE, kondisi yang tidak mungkin lewat UI normal):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-AC-PP-15, TC-AC-PP-16 | Distributor User | `distributorUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_PASSWORD` |
| TC-AC-PP-15, TC-AC-PP-16 | Partner User | `partnerUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_PARTNER_PASSWORD` |
| TC-AC-PP-15, TC-AC-PP-16 | Client User | `clientUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_CLIENT_PASSWORD` |

- Hook `before` men-seed dataset Riwayat A (Version 3 Active) dan meng-assign capability "Manage privacy policy" ke ketiga user lewat Fixture BE, lalu login sebagai Distributor User (akun aktor pertama). Hook `after` mencabut capability yang di-assign, mengembalikan dataset ke Riwayat A, dan mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Password tidak ditulis di spec atau fixture; nama env `AC_DIST_PASSWORD`, `AC_PARTNER_PASSWORD`, `AC_CLIENT_PASSWORD`, `AC_TC_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`; selain `AC_TC_PASSWORD`, nama itu belum terdaftar.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat dan meng-assign capability lintas entity.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide dan capability di-assign sementara.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung halaman Settings > Privacy Policy | TC-AC-PP-16 (langkah URL) |

## Test Steps

### TC-AC-PP-15: Item sidebar Privacy Policy Hidden untuk user non-Principal walau capability keliru ter-assign

1. Amati sidebar sebagai Distributor User (login di hook `before`)
2. Verifikasi Distributor User: tidak ada item "Privacy Policy" di sidebar
3. Logout
4. Login sebagai Partner User
5. Amati sidebar
6. Verifikasi Partner User: tidak ada item "Privacy Policy" di sidebar
7. Logout
8. Login sebagai Client User
9. Amati sidebar
10. Verifikasi Client User: tidak ada item "Privacy Policy" di sidebar

### TC-AC-PP-16: Akses langsung ke URL halaman oleh user non-Principal ditolak dengan toast penolakan standar

11. Logout
12. Login sebagai Distributor User
13. Ketik URL halaman Settings > Privacy Policy (`urlHalamanPrivacyPolicy`) di address bar lalu tekan Enter
14. Verifikasi Distributor User: muncul toast error "You don't have permission to do this."
15. Verifikasi Distributor User: tidak ada baris Version History yang tampil
16. Logout
17. Login sebagai Partner User
18. Ketik URL halaman Settings > Privacy Policy (`urlHalamanPrivacyPolicy`) di address bar lalu tekan Enter
19. Verifikasi Partner User: muncul toast error "You don't have permission to do this."
20. Verifikasi Partner User: tidak ada baris Version History yang tampil
21. Logout
22. Login sebagai Client User
23. Ketik URL halaman Settings > Privacy Policy (`urlHalamanPrivacyPolicy`) di address bar lalu tekan Enter
24. Verifikasi Client User: muncul toast error "You don't have permission to do this."
25. Verifikasi Client User: tidak ada baris Version History yang tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix negatif (bagian 3a konvensi): langkah identik untuk tiga role, hanya akun login yang berbeda; tiap ganti akun punya langkah logout dan login eksplisit (S-07).
- Langkah 11-12 (logout lalu login ulang sebagai Distributor User) adalah langkah penghubung antar TC karena TC-AC-PP-16 menulis ulang login per role; tidak ada langkah penghubung lain.
- Tolak server langsung (HTTP 403 pada endpoint) untuk kondisi ini ada di TC-AC-PP-171 sampai 174 dan tidak termasuk spec ini (TC hanya-BE).
- Temuan untuk QA: TC-AC-PP-15 Post Condition dan TC-AC-PP-16 Post Condition ("Tidak ada perubahan data") tidak punya langkah observasi sehingga tidak diasersi. Teks toast pada TC-AC-PP-16 mengikuti `error-handling-convention.md` §2 dan sama persis dengan TC-AC-PP-14.
