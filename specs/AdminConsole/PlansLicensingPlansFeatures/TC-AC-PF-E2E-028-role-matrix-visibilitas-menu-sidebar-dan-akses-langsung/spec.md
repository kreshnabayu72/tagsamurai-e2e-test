---
id: TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung
title: Role Matrix - Visibilitas Menu Sidebar dan Akses Langsung ke URL Plans & Features
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-50
  - TC-AC-PF-51
  - TC-AC-PF-52
  - TC-AC-PF-53
  - TC-AC-PF-54
  - TC-AC-PF-55
  - TC-AC-PF-56
coverage:
  web: automated
---

# Role Matrix - Visibilitas Menu Sidebar dan Akses Langsung ke URL Plans & Features

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Tanpa Capability (Principal) | #7 noCapabilityPrincipal | `noCapabilityPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_NC_PASSWORD` | langkah 1 sampai 9 |
| Tanpa Capability (Distributor) | #15 noCapabilityDistributor | `noCapabilityDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_NC_PASSWORD` | langkah 10 sampai 18 |
| Client User | #20 clientUser | `clientUser_automated_{namaCompany}@qwertysystem.net` | `AC_PF_CLIENT_PASSWORD` | langkah 19 sampai 27 |
| Read Only (Principal) | #2 readOnlyPrincipal | `readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_RO_PASSWORD` | langkah 28 sampai 31 |
| Create-Only (Principal) | #3 createOnlyPrincipal | `createOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_PF_CO_PASSWORD` | langkah 32 sampai 35 |

- Login di hook `before` spec ini sebagai #7; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: tidak ada dataset khusus; item menu dan halaman Plans & Features dibaca sebagaimana adanya. Capability tiap akun sesuai Pre-setup #2, #3, #7, #15, dan #20.
- Kemampuan teknis: fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`; fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Blok Tanpa Capability (Principal): TC-AC-PF-50 dan TC-AC-PF-54

1. Buka halaman beranda Admin Console.
2. Buka sidebar.
3. Verifikasi item menu lain pada sidebar tampil.
4. Verifikasi item `Plans & Features` tidak ada di sidebar (Hidden).
5. Ketik URL halaman Plans & Features langsung di address bar lalu Enter.
6. Verifikasi muncul toast error: "You don't have permission to do this."
7. Verifikasi halaman Plans & Features tidak menampilkan data plan.
8. Verifikasi tidak ada redirect ke halaman unauthorized terpisah.
9. Verifikasi elemen tanpa hak tersembunyi.

### Blok Tanpa Capability (Distributor): TC-AC-PF-51 dan TC-AC-PF-55

10. Ganti akun: logout, lalu login sebagai Tanpa Capability (Distributor) (#15) sampai halaman beranda Admin Console tampil.
11. Buka sidebar.
12. Verifikasi item menu lain pada sidebar tampil.
13. Verifikasi item `Plans & Features` tidak ada di sidebar (Hidden).
14. Ketik URL halaman Plans & Features langsung di address bar lalu Enter.
15. Verifikasi muncul toast error: "You don't have permission to do this."
16. Verifikasi halaman Plans & Features tidak menampilkan data plan.
17. Verifikasi tidak ada redirect ke halaman unauthorized terpisah.
18. Verifikasi elemen tanpa hak tersembunyi.

### Blok Client User: TC-AC-PF-52 dan TC-AC-PF-56

19. Ganti akun: logout, lalu login sebagai Client User (#20) sampai halaman beranda tampil.
20. Buka sidebar.
21. Verifikasi menu Admin Console tidak tersedia sama sekali untuk Client.
22. Verifikasi item `Plans & Features` tidak ada.
23. Ketik URL halaman Plans & Features langsung di address bar lalu Enter.
24. Verifikasi muncul toast error: "You don't have permission to do this."
25. Verifikasi halaman Plans & Features tidak menampilkan data plan.
26. Verifikasi tidak ada redirect ke halaman unauthorized terpisah.
27. Verifikasi elemen tanpa hak tersembunyi.

### Blok Read Only (Principal) dan Create-Only (Principal): TC-AC-PF-53

28. Ganti akun: logout, lalu login sebagai Read Only (Principal) (#2).
29. Verifikasi item `Plans & Features` tampil di sidebar (Show).
30. Klik item `Plans & Features` di sidebar.
31. Verifikasi halaman Plans & Features terbuka.
32. Ganti akun: logout, lalu login sebagai Create-Only (Principal) (#3).
33. Verifikasi item `Plans & Features` tampil di sidebar (Show).
34. Klik item `Plans & Features` di sidebar.
35. Verifikasi halaman Plans & Features terbuka.

## Notes

- Spec ditulis per blok role karena tiap pergantian akun menuntut Step Ganti akun eksplisit (akun pertama login di hook `before`) dan langkah tiap blok berbeda (Hidden pada sidebar dan 403 untuk tiga role; Show untuk dua role).
- Langkah penghubung (S-03): langkah 1, 2, 11, 20, 30 dan 34 (membuka beranda, sidebar, dan item menu sebagai prasyarat langkah berikutnya). Langkah 10, 19, 28 dan 32 adalah Ganti akun eksplisit (S-07).
- Langkah 3 dan 12 adalah anchor positif untuk langkah 4 dan 13 (absence item menu; item menu lain pada sidebar yang sama sudah tampil).
- Untuk blok Read Only dan Create-Only, "dapat dibuka" (Expected TC-AC-PF-53) diasersi lewat langkah 30 dan 31 serta 34 dan 35.
- Temuan untuk QA:
  - TC-AC-PF-50, 51, dan 52 langkah 1 menulis "perluas grup Plans & Licensing (bila grup tampil)" sebagai langkah bersyarat; S-08 melarang langkah bersyarat dan TC tidak menyebut apakah grup tampil untuk role tanpa capability. Spec menulis "Buka sidebar" (langkah 2, 11, 20) dan memverifikasi item menu lain sebagai anchor.
  - TC-AC-PF-54 dan 55 Expected b menyebut "elemen tanpa hak tersembunyi" tanpa menyebut elemen yang diamati; spec menuliskannya apa adanya (langkah 9, 18, 27).
  - TC-AC-PF-52 dan 56 precondition "Client tidak memiliki akses Admin Console" tidak menyebut halaman beranda tempat Client User mendarat sesudah login; spec memakai "halaman beranda tampil".
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
