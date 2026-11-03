---
id: TC-AC-ACHA-E2E-013-scope-penerima-write-dropdown-client
title: "Scope Penerima WRITE: Opsi Dropdown Client pada Form Allocate per Tipe Entitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-76
  - TC-AC-ACHA-77
  - TC-AC-ACHA-78
  - TC-AC-ACHA-79
coverage:
  web: automated
---

# Scope Penerima WRITE: Opsi Dropdown Client pada Form Allocate per Tipe Entitas

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

| TC | Entitas | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-76 | Total Control Principal PT ABC | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| TC-77 | Total Control Distributor PT Global Distribusi | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| TC-78 | Total Control Partner CV Mitra Solusi | #43 | `totalControlPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P1_PASSWORD` |
| TC-79 | Total Control Partner CV Karya Mandiri | #46 | `totalControlPartner2_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P2_PASSWORD` |

- Login akun aktor pertama (Principal) di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): Client Pre-setup #7 sampai #13: `PT Sejahtera Logistik` (Active, binaan PT Global Distribusi), `PT Retail Makmur` (Active, binaan CV Mitra Solusi), `PT Cipta Kreasi` (Active, binaan CV Karya Mandiri), `PT Manufaktur Unggul` (Active, binaan PT ABC), `PT Bintang Timur` (Active, binaan PT Nusa Distribusi), `PT Agro Lestari` (Suspended, binaan PT Global Distribusi), `Toko Lama Abadi` (Archived, binaan PT Global Distribusi). Form dibuka dan ditutup tanpa Submit sehingga tidak ada data yang dibuat.
- Tabel opsi dropdown Client yang diharapkan per entitas:

| TC | Opsi yang tampil | Client yang tidak tampil (dicari di kotak pencarian dropdown) |
|---|---|---|
| TC-76 | `PT Sejahtera Logistik`, `PT Retail Makmur`, `PT Cipta Kreasi`, `PT Manufaktur Unggul`, `PT Bintang Timur` | `PT Agro Lestari`, `Toko Lama Abadi` |
| TC-77 | `PT Sejahtera Logistik` | `PT Retail Makmur`, `PT Agro Lestari`, `Toko Lama Abadi` |
| TC-78 | `PT Retail Makmur` | `PT Sejahtera Logistik` |
| TC-79 | `PT Cipta Kreasi` | - |

- General Settings Pre-setup #1 tidak diubah. State global: tidak ada yang diubah; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_DIST_PASSWORD`, `AC_DA_TC_P1_PASSWORD`, dan `AC_DA_TC_P2_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-76: Scope penerima WRITE Principal

1. Klik `[+ Allocation]`
2. Buka dropdown Client dan amati opsi
3. Verifikasi opsi dropdown Client hanya Client Active dalam scope WRITE: `PT Sejahtera Logistik`, `PT Retail Makmur`, `PT Cipta Kreasi`, `PT Manufaktur Unggul`, dan `PT Bintang Timur`
4. Ketik `PT Agro Lestari` pada kotak pencarian dropdown
5. Verifikasi `PT Agro Lestari` (Suspended) tidak muncul sebagai opsi maupun hasil pencarian
6. Ganti isi kotak pencarian dropdown dengan `Toko Lama Abadi`
7. Verifikasi `Toko Lama Abadi` (Archived) tidak muncul sebagai opsi maupun hasil pencarian
8. Tekan Esc untuk menutup dropdown
9. Klik `[×]` untuk menutup form Allocate Device

### Ganti akun ke Total Control Distributor

10. Logout dari akun Total Control Principal
11. Login sebagai Total Control Distributor (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
12. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-77: Scope penerima WRITE Distributor

13. Klik `[+ Allocation]`
14. Buka dropdown Client dan amati opsi
15. Verifikasi opsi dropdown Client hanya `PT Sejahtera Logistik` (Client binaan langsung, exact match)
16. Ketik `PT Retail Makmur` pada kotak pencarian dropdown
17. Verifikasi `PT Retail Makmur` (dipegang Partner di bawahnya) tidak muncul sebagai opsi maupun hasil pencarian
18. Ganti isi kotak pencarian dropdown dengan `PT Agro Lestari`
19. Verifikasi `PT Agro Lestari` (Suspended) tidak muncul sebagai opsi maupun hasil pencarian
20. Ganti isi kotak pencarian dropdown dengan `Toko Lama Abadi`
21. Verifikasi `Toko Lama Abadi` (Archived) tidak muncul sebagai opsi maupun hasil pencarian
22. Tekan Esc untuk menutup dropdown
23. Klik `[×]` untuk menutup form Allocate Device

### Ganti akun ke Total Control Partner CV Mitra Solusi

24. Logout dari akun Total Control Distributor
25. Login sebagai Total Control Partner CV Mitra Solusi (`totalControlPartner1_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_P1_PASSWORD`)
26. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-78: Scope penerima WRITE Partner CV Mitra Solusi

27. Klik `[+ Allocation]`
28. Buka dropdown Client dan amati opsi
29. Verifikasi opsi dropdown Client hanya `PT Retail Makmur` (Client binaan langsung)
30. Ketik `PT Sejahtera Logistik` pada kotak pencarian dropdown
31. Verifikasi `PT Sejahtera Logistik` tidak muncul sebagai opsi maupun hasil pencarian
32. Tekan Esc untuk menutup dropdown
33. Klik `[×]` untuk menutup form Allocate Device

### Ganti akun ke Total Control Partner CV Karya Mandiri

34. Logout dari akun Total Control Partner CV Mitra Solusi
35. Login sebagai Total Control Partner CV Karya Mandiri (`totalControlPartner2_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_P2_PASSWORD`)
36. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-79: Scope penerima WRITE Partner dengan dua kantong

37. Klik `[+ Allocation]`
38. Buka dropdown Client dan amati opsi
39. Verifikasi opsi dropdown Client hanya `PT Cipta Kreasi` (Client binaan langsung CV Karya Mandiri)
40. Tekan Esc untuk menutup dropdown
41. Klik `[×]` untuk menutup form Allocate Device

## Notes

- Ukuran spec (di atas 35 langkah): empat TC scope penerima memakai satu dataset dan satu urutan ganti akun; tiap opsi dropdown yang diharapkan menjadi `Verifikasi` sendiri (S-01).
- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec scope penerima WRITE (opsi dropdown Client); tanpa aksi tulis. Spec ditulis per blok entitas karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Anchor absence (bagian 8b butir 2): asersi Client tidak muncul sebagai opsi atau hasil pencarian didahului `Verifikasi` daftar opsi dropdown yang tampil (data pembanding pada surface yang sama).
- Langkah penghubung (S-03): langkah ganti akun (subjudul "Ganti akun ..."), `Esc` yang menutup dropdown, dan `[×]` yang menutup form dalam keadaan bersih (tidak ada field diisi; pengetikan di kotak pencarian dropdown bukan nilai field) sehingga dialog `Unsaved Changes` tidak diharapkan.
- Pembagian TC lintas spec: opsi Category, Pay From, dan isi form lain ada di spec 016; validasi di spec 017; blokir Client Suspended atau Archived oleh server di spec 015.
- Temuan untuk QA:
  - TC-78 Expected b menyebut "Client entitas lain" tanpa menyebut nama; spec hanya mencari `PT Sejahtera Logistik` (yang disebut eksplisit).
  - TC-76 Expected a memuat lima Client; TC-77 menulis "exact match" tanpa menjelaskan arti; spec memakai daftar yang disebut.
  - TC-79 tidak memuat Client yang dikecualikan; hanya opsi yang tampil yang diasersi.
  - Post Condition TC-76 sampai TC-79 bernilai `-`.
